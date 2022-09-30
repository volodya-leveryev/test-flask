import os
from flask import current_app, render_template


def hello_world():
    files = os.listdir(current_app.static_folder)
    return render_template('index.html', files=files)
