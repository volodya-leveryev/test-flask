import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    files = os.listdir("static")
    return render_template('index.html', files=files)
