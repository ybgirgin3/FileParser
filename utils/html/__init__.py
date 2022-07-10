from bs4 import BeautifulSoup

def html(fp):
  "read html and return it's content"
  with open(fp) as fp:
    soup = BeautifulSoup(fp, features="html.parser")

  # kill all script and style elements
  for script in soup(["script", "style"]):
    script.extract() 

  text = soup.get_text()

  # break into lines and remove leading and trailing space on each
  lines = (line.strip() for line in text.splitlines())
  # break multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)

  #print(text)
  return text



  


