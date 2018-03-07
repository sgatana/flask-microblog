from config import app_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    # register blog blueprint
    from .blogs import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app