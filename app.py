from flask import Flask
import os

# local


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(filename):
  # temp file 

  reading_type = find_reading_type(filename) #get reading type
  parsed = parse(filename, reading_type) #get word count
  inf = info(parsed)

  _return = {
    'parsed': parsed,
    'info': inf
  }
  return _return