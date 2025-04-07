from CreateVectorData import results
from main import slides
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
from io import BytesIO
from DeepCloneSlide import add_slides_from_list


OUTPUT_PATH= "data/outputPPTs/new_presentation.pptx"

prs = Presentation()

slides_to_copy=[slides[x].slide for x in results]

prs =add_slides_from_list(slides_to_copy)

prs.save(OUTPUT_PATH)
print("New presentation 'new_presentation.pptx' created with added slides in the data outputs ppt")





