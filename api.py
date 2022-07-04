# *** coding: utf-8 ***
from flask import Flask
from utils import utils
import os

app = Flask(__name__)

TEMP_DIR = os.path.join(os.getcwd(), 'temp')


@app.route("/", methods=["GET"])
def home(filename=None):
    "user uploaded a file using api"
    # read file
    filename = os.path.join(TEMP_DIR, "text.txt")
    ret = utils.utils_main(filename=filename)  # counter
    # print(ret, type(ret))
    return ret


if __name__ == "__main__":
    app.run(debug=True)
