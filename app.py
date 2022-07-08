from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import tempfile
import os


# local
from utils.utils import _find_ext_n_run
from utils.logger import _log


app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = tempfile.gettempdir() 
#app.config['UPLOAD_FOLDER'] = '/tmp/' 
app.config['UPLOAD_FOLDER'] = 'uploads' 


@app.route('/', methods = ['GET', 'POST'])
def index():
  # save file
  if request.method == 'POST':
    if request.file:
      file = request.files['file']

      if file.filename == '':
        _log('Image MUST have a file name', 'danger')
        redirect(request.url)

      fn = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(fn)

      # give user the info
      _log('file uploaded successfully to tempdir', 'info')

      # extract from file
      return _find_ext_n_run(fn)
  return render_template('upload.html')



  
if __name__ == '__main__':
  app.run(debug=True)