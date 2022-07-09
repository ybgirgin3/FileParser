from PIL import Image
from pytesseract import pytesseract as pts
import platform

# default (?) tesseract paths
tess_path = {
  'Darwin': ['/opt/homebrew/bin/tesseract', 'usr/bin/tesseract'],
  'Linux': ['usr/bin/tesseract'],
  'Windows': ['..']
}

# get system type
_os = platform.system()

def image(fp):
  "read image and extract text"
  if _os in tess_path.keys():
    for p in tess_path[_os]:
      try:
        pts.tesseract_cmd = p

        img = Image.open(fp)
        text = pts.image_to_string(img)
        return text

      except Exception as e:
        print(e)
  
  
  
  # if _os in tess_path.keys():
    # vals = tess_path[_os]
    # try:
    #   for p in vals:
    #     _pts_ocr = p
    #   pts.tesseract_cmd = _pts_ocr

    #   img = Image.open(fp)
    #   text = pts.image_to_string(img)

    #   return text
    # except Exception as e:
    #   raise(e)
  