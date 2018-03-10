from config import app_config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    from app import models

    # register blog blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html', title='Not Found'), 404

    return app

