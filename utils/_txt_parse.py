import os
from ._types import reading_types


def _txt_read(fn: str) -> dict:
  ext = os.path.splitext(fn)[-1]

  if ext in reading_types.keys():
    read_type = reading_types[ext]

  f_content = open(fn, read_type).read().split()

  return f_content, read_type, ext



