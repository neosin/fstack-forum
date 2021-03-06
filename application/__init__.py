# application/__init__.py

import logging
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('application_error.log')
formatter = logging.Formatter('%(asctime)s: %(levelname)s: \
                              %(name)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login_route'
mail = Mail()
toolbar = DebugToolbarExtension()


def create_app():
    '''Get application set up'''

    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DEV_DATABASE_URI')
    app.config['DEBUG_TB_ENABLED'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = False
    app.config['MAIL_SERVER'] = environ.get('MAIL_SERVER')
    app.config['MAIL_PORT'] = environ.get('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_DEFAULT_SENDER'] = environ.get('MAIL_DEFAULT_SENDER')
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEBUG'] = True
    app.config['TESTING'] = False
    # app.config['MAIL_MAX_EMAILS'] = 1
    app.config['MAIL_SUPPRESS_SEND'] = True
    app.config['MAIL_ASCII_ATTACHMENTS'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    toolbar.init_app(app)

    from application.auth.routes import auth
    app.register_blueprint(auth)

    from application.admin.routes import admin
    app.register_blueprint(admin)

    from application.forum.routes import forum
    app.register_blueprint(forum)

    return app
