
import os
from html_parser.html import html
from image_parser.image import image
from pdf_parser.pdf import pdf
from text_parser.text import text



allowed_extensions = {
  'pdf': pdf,
  'jpeg': image, 'png': image, 'jpg': image,
  'html': html,
  'txt': text
}

exts, vals = allowed_extensions.keys(), allowed_extensions.values()

def _find_ext_n_run(fp): 
  ext = fp.split(os.extsep)[-1]
  if ext in exts:
    return allowed_extensions[ext](fp)
    


# if __name__ == '__main__':
#  import sys
#  print(_find_ext_n_run(sys.argv[1]))