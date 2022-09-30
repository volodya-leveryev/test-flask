from flask import Flask
from . import views


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.hello_world)

    return app
