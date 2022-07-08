from PyPDF2 import PdfReader
from utils.count import counter

def pdf(fp):
  "parse pdf and return it's content"
  reader = PdfReader(fp)
  text = ""
  for page in reader.pages:
    text += page.extract_text() + "\n"
  return text