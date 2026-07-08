from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from the uploaded PDF resume.
    """

    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("PDF Error :", e)

    return text