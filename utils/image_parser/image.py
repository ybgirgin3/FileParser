from PIL import Image
from pytesseract import pytesseract as pts
from subprocess import check_output

def image(fp):
  #_pts_ocr = check_output(['which', 'tesseract'])
  _pts_ocr = "/opt/homebrew/bin/tesseract"
  pts.tesseract_cmd = _pts_ocr

  img = Image.open(fp)
  text = pts.image_to_string(fp)

  return text