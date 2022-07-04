from collections import Counter
from ._types import reading_types
import os


def _read(fn: str) -> dict:
    ext = os.path.splitext(fn)[-1]

    if ext in reading_types.keys():
        read_type = reading_types[ext]

    f_content = open(fn, read_type).read().split()

    return f_content, read_type, ext


def _count(data: list) -> Counter:
    c = Counter(data)
    return c


def utils_main(filename):
    fc, rt, ext = _read(filename)
    _ret = _count(fc)

    return {
        "content": _ret,
        "file_extension": ext,
        "read_type": rt
    }
