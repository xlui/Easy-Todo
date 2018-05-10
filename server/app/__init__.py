from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    CORS(app, resources=r'/*')
    config[config_name].init_app(app=app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
