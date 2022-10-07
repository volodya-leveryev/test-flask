import os
from flask import current_app, redirect, render_template, request


def hello_world():
    error = request.args.get('error')
    files = os.listdir(current_app.static_folder)
    return render_template('index.html', files=files, error=error)


def upload_file():
    new_file = request.files.get('new_file')
    if new_file:
        filename = current_app.static_folder + '/' + new_file.filename
        new_file.save(filename)
    else:
        return redirect('/?error=1')
    return redirect('/')
