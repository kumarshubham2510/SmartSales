from spire.presentation import *

from CreateVectorData import results
from DataExtraction import slides

from DeepCloneSlide import add_slides_from_list

def generatePPT(OUTPUT_PATH):

    prs = Presentation()

    slides_to_copy=[slides[x].slide for x in results]

    prs =add_slides_from_list(slides_to_copy)

    prs.SaveToFile(OUTPUT_PATH, FileFormat.Pptx2016)
    prs.Dispose()

    print("New presentation 'new_presentation.pptx' created with added slides in the data outputs ppt")





