from PyPDF2 import PdfReader
from utils.count import counter

def pdf(fp):
  reader = PdfReader(fp)
  text = ""
  for page in reader.pages:
    text += page.extract_text() + "\n"
  return text