import os
from flask import Flask, request, redirect, render_template
from flask_cors import CORS

from werkzeug.utils import secure_filename

from utils.utils import find_ext_n_run, extensions
from utils.logger import log

import tempfile

UPLOAD_FOLDER = tempfile.gettempdir()
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
  if not file:
    return {"message": "No upload file sent"}
  else:
    return {"filename": file.filename}

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)