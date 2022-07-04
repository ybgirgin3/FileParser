from collections import Counter
import os
from ._types import reading_types
from ._txt_parse import _txt_read
from ._pdf_parse import _pdf_read


def _find_type(fn: str) -> str:
  ext = os.path.splitext(fn)[-1]

  if ext in reading_types.keys():
    read_type = reading_types[ext]

  return read_type, ext


def utils_main(filename):
  # find file ext
  rt, ext = _find_type(filename)
  print("rt: ", rt, "ext: ", ext)

  _ret = lambda x: Counter(x)(open(filename, rt))
  print("ret:", _ret)

  return {
      "content": _ret,
      "file_extension": ext,
      "read_type": rt
  }
