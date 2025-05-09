from pypdf import PdfReader

def read_pdf(doc):
    pdf = PdfReader(doc)
    pdf_text = ""
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            pdf_text+=content
    return (pdf_text)