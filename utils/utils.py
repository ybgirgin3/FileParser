#from utils.html_parser import html
from utils.html import html
from utils.image import image
from utils.pdf import pdf
from utils.text import text
from utils.logger import log
from utils.count import counter
import os

tess_paths = os.path.join(os.getcwd(), 'utils/configs/tess_paths.yaml')

allowed_extensions = {
  'pdf': pdf,
  'jpeg': image, 'png': image, 'jpg': image,
  'html': html,
  'txt': text
}

extensions, vals = allowed_extensions.keys(), allowed_extensions.values()


def find_ext_n_run(fp):
  """
    find extension of file, calls the specific function, calls `counter` function
    gets count of word and returns as a dict
  """

  ext = fp.split(os.extsep)[-1]
  if ext in extensions:
    log(f"{ext} file found", 'info')
    if ext in ('jpeg', 'png', 'jpg'): _fp = fp, tess_paths
    else: _fp = fp
    _content = allowed_extensions[ext](_fp).split()
    _count = counter(_content)

    ret = {
      'content': _content,
      'count': _count
    }

    return ret

# if __name__ == '__main__':
#  import sys
#  print(_find_ext_n_run(sys.argv[1]))
