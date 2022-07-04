from utils._pdf_parse import _pdf_read
import sys

ret = _pdf_read(sys.argv[1])
print(ret)

