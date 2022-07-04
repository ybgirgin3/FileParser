from PyPDF2 import PdfReader
import sys

def _pdf_read(pdf_fn):
  reader = PdfReader(pdf_fn)
  page = reader.pages[0]
  return page.extract_text()
