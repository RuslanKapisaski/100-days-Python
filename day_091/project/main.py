from pdf_extractor import pdf_extractor
from text_speaker import speak



print("Press 'e' to exit the program.")

while (True):
    pdf_path = input("Enter PDF file path: ")

    if pdf_path.lower() == "e":
        print("Program exited..")
        break

    text = pdf_extractor(pdf_path)

    if text.strip():
        speak(text)
        print("Audiobook created successfully: audiobook.mp3")
    else:
        print("No text found in this PDF.")
