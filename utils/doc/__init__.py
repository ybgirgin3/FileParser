from docx import Document
import re
import os

def doc(fp: str):
  # assert isinstance(fp, os.PathLike)
  _doc = Document(fp)
  head1s = []
  for parag in _doc.paragraphs:
    #heading = re.match(r'^[A-Z]+[.]\s', parag.text)
    head1s.append(parag.text)
  return head1s

if __name__ == '__main__':
  import sys
  df = sys.argv[1]
  doc(df)