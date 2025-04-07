from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
from io import BytesIO


def add_slides_from_list(slide_objects):
    prs = Presentation()
    blank_slide_layout = None
    for layout in prs.slide_layouts:
        if not layout.placeholders:  # Check for truly blank layout
            blank_slide_layout = layout
            break
    if blank_slide_layout is None:
        blank_slide_layout = prs.slide_layouts[5] # Fallback if no truly blank layout


    for source_slide in slide_objects:
        slide = source_slide
        new_slide = prs.slides.add_slide(blank_slide_layout)
        # Clear Add to Title textbox from blank slides
        for shape in list(new_slide.shapes):
            new_slide.shapes._spTree.remove(shape._element)

        # Copy each shape from the source slide to the new slide
        for shape in slide.shapes:
            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height
            if shape.has_text_frame:
                new_shape = new_slide.shapes.add_textbox(left, top, width, height)
                new_text_frame = new_shape.text_frame
                new_text_frame.clear()
                new_text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
                new_text_frame.word_wrap = True

                for paragraph in shape.text_frame.paragraphs:
                    new_p = new_text_frame.add_paragraph()
                    new_p.alignment = paragraph.alignment
                    new_p.level = paragraph.level
                    new_p.space_before = paragraph.space_before
                    new_p.space_after = paragraph.space_after
                    new_p.line_spacing = paragraph.line_spacing

                    if hasattr(paragraph, 'first_line_indent'):
                        new_p.first_line_indent = paragraph.first_line_indent
                    if hasattr(paragraph, 'hanging_indent'):
                        new_p.hanging_indent = paragraph.hanging_indent
                    if hasattr(paragraph, 'tab_stops'):
                        new_p.tab_stops = paragraph.tab_stops

                    for run in paragraph.runs:
                        new_run = new_p.add_run()
                        new_run.text = run.text
                        new_run.font.name = getattr(run.font, 'name', None)
                        new_run.font.size = getattr(run.font, 'size', None)
                        new_run.font.bold = getattr(run.font, 'bold', None)
                        new_run.font.italic = getattr(run.font, 'italic', None)
                        new_run.font.underline = getattr(run.font, 'underline', None)
                        if run.font.color is not None:
                            if hasattr(run.font.color, 'rgb'):
                                new_run.font.color.rgb = run.font.color.rgb
            elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                image_stream = shape.image  # Get the Image object
                image_blob = image_stream.blob  # Get the raw image data
                image_io = BytesIO(image_blob)  # Wrap the bytes data in a BytesIO object
                new_slide.shapes.add_picture(image_io, left, top, width=width, height=height)

            elif shape.shape_type == MSO_SHAPE_TYPE.TABLE:
                table = shape.table
                num_rows = len(table.rows)
                num_cols = len(table.columns)
                new_table = new_slide.shapes.add_table(num_rows, num_cols, left, top, width, height).table
                for r_idx, row in enumerate(table.rows):
                    for c_idx, cell in enumerate(row.cells):
                        new_table.cell(r_idx, c_idx).text = cell.text

            # Add handling for other shape types if needed
        # Copy slide notes if they exist
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text
            new_notes_slide = new_slide.notes_slide
            new_notes_slide.notes_text_frame.text = notes
    return prs








