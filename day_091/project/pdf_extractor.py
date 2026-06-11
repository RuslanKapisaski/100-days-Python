import PyPDF2
import os

def pdf_extractor(pdf_path):
    if not os.path.isfile(pdf_path):
        print("Error: Please provide a valid PDF file path.")
        return ""

    if not pdf_path.lower().endswith(".pdf"):
        print("Error: Please select a PDF file.")
        return ""

    text = ""

    try:
        print("Reading PDF...")
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text