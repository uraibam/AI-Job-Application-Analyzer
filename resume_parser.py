import fitz  # PyMuPDF for PDF extraction
import docx

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file"""
    text = ""
    with fitz.open(pdf_file) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    """Extract text from a DOCX file"""
    doc = docx.Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_resume_text(file_path):
    """Extract text from resume (PDF or DOCX)"""
    if file_path.name.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.name.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format!"
