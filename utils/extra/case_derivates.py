from itertools import product

def derivates(istr):
  list_ = [(c, c.upper()) if not c.isdigit() else (c,) for c in istr.lower()]
  return ["".join(item) for item in product(*list_)]


#import sys
#print(randString(sys.argv[1]))
