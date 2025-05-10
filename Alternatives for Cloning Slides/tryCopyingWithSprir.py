from pptx.parts.chart import ChartPart
from pptx.parts.embeddedpackage import EmbeddedXlsxPart
from pptx import Presentation
import copy

from pptx import Presentation

from spire.presentation.common import *
from spire.presentation import *

inputFile_1 = "data/inputPPTs/AI.pptx.pptx"
# inputFile_2 = "Input2.pptx"
outputFile ="CloneSlidesToAnother.pptx"

# Load the first PowerPoint presentation
sourcePPT = Presentation()
sourcePPT.LoadFromFile(inputFile_1)

# Load the second PowerPoint presentation
destPPT = Presentation()
# destPPT.LoadFromFile(inputFile_2)

# Get two slides in the first presentation
slide1 =sourcePPT.Slides[3]
slide2 =sourcePPT.Slides[4]
slide3 =sourcePPT.Slides[5]
slide4 =sourcePPT.Slides[6]
slide5 =sourcePPT.Slides[7]

# Clone slide1 to the second position in the second presentation
destPPT.Slides.Insert(1, slide1)

# Clone slide2 to the end of the second presentation
destPPT.Slides.AppendBySlide(slide2)
destPPT.Slides.AppendBySlide(slide3)
destPPT.Slides.AppendBySlide(slide4)
destPPT.Slides.AppendBySlide(slide5)

# Save the second presentation
destPPT.SaveToFile(outputFile, FileFormat.Pptx2016)
destPPT.Dispose()