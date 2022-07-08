
import os
from utils.html_parser.html import html
from utils.image_parser.image import image
from utils.pdf_parser.pdf import pdf
from utils.text_parser.text import text
from utils.logger import _log
from utils.count import counter

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
    _log(f"{ext} file found", 'info')
    _content = allowed_extensions[ext](fp).split()
    _count = counter(_content)

    ret = {
      'content': _content,
      'count': _count
    }

    return ret
    

# if __name__ == '__main__':
#  import sys
#  print(_find_ext_n_run(sys.argv[1]))