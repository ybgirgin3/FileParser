from PIL import Image
from pytesseract import pytesseract as pts
import platform
from utils.extra.case_derivates import derivates
from utils.extra.yaml_data import yaml_parser 

# get system type
_os = platform.system()
_os = derivates(_os) # list 


def image(_arg: dict):
  fp, tess_path = _arg
  tess_path = yaml_parser(tess_path)
  "read image and extract text"
  for deriv in _os:
    if deriv in tess_path.keys():
      for p in tess_path[deriv]:
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
  