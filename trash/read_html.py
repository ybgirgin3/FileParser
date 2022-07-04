import lxml.html.html5parser as parse
from lxml.html import html5parser, clean
html_file = '../temp/index.html'


with open(html_file, "r") as f:
    ret = f.read()


html_p = html5parser.HTMLParser(ret)
cleaner = clean.Cleaner(html_p)
print(cleaner)
