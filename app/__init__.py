"""app/__init__.py"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.user_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type): # dev, test, or prod
    """create app method"""
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # e.g C:\\Users\\ogonk\\Desktop\\BookCatalog\\config\\dev.py

    app.config.from_pyfile(configuration) # config flask app through config file

    db.init_app(app) # binds database to flask app
    bootstrap.init_app(app) # initialize bootstrap
    login_manager.init_app(app) # initialize login mangaer
    bcrypt.init_app(app) # initialize bcrypt

    from app.catalog import main # import catalog blueprint
    app.register_blueprint(main) # register blueprint

    from app.auth import authentication # import auth blueprint
    app.register_blueprint(authentication) # register blueprint

    return app



