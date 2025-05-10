from DataExtraction import extract_text_from_pptx

from GeneratePPT import generatePPT

OUTPUT_FILE="data/outputPPTs/new_presentation.pptx"

# Extract Text from PPTX and Create Slide Objects Add all your ppt files
extract_text_from_pptx("data/inputPPTs/Advantages-and-Disadvantages-of-AI.pptx")
extract_text_from_pptx("data/inputPPTs/AI.pptx.pptx")
extract_text_from_pptx("data/inputPPTs/Cyber-Security-Awarness-Slide-September-2022 (1).pptx")
extract_text_from_pptx("data/inputPPTs/cybersecurity.pptx")
extract_text_from_pptx("data/inputPPTs/IT-Security-20210426203847.pptx")

generatePPT(OUTPUT_FILE)

