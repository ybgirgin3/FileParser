import os
from flask import Flask, request, redirect, render_template
from flask_cors import CORS

from werkzeug.utils import secure_filename

from utils.utils import find_ext_n_run, extensions
from utils.logger import log

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    # if program has skill to upload file
    if 'file' not in request.files:
      msg = 'Not file part'
      log(msg, 'warning')
      return redirect(request.url)

    # get file
    file = request.files['file']

    # if user not select a file
    if file.filename == '':
      msg = 'No selected file'
      log(msg, 'warning')
      return redirect(request.url)

    # save file
    _f_ext = file.filename.split(os.extsep)[-1]

    # if file is valid
    if file and (_f_ext in extensions):
      log(f"{_f_ext} in {extensions}", 'info')
      filename = secure_filename(file.filename)
      fp = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(fp)
      log(f"file saved to {app.config['UPLOAD_FOLDER']} ", 'info')
      return find_ext_n_run(fp)
  return render_template('upload.html')


if __name__ == '__main__':
  app.run(debug=True)
