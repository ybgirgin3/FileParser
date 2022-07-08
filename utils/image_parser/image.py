from PIL import Image
from pytesseract import pytesseract as pts
import platform

# default (?) tesseract paths
tess_path = {
  'darwin': '/opt/homebrew/bin/tesseract',
  'linux': 'usr/bin/tesseract',
  'windows': '..'
}

# get system type
_os = platform.system()

def image(fp):
  "read image and extract text"
  _pts_ocr = tess_path[_os]
  pts.tesseract_cmd = _pts_ocr

  img = Image.open(fp)
  text = pts.image_to_string(img)

  return text