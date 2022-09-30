from flask import Flask
from . import database
from . import views


def create_app():
    app = Flask(__name__)

    # TODO: put the database URI in config file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.db.init_app(app)

    app.add_url_rule("/", view_func=views.hello_world)

    return app
