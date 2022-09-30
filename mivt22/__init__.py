import os
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        files = os.listdir(app.static_folder)
        return render_template('index.html', files=files)

    return app
