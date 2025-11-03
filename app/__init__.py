from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():

    app = Flask(__name__)

    app.config.from_pyfile(filename='config.py')

    csrf.init_app(app=app)

    db.init_app(app=app)

    login_manager.init_app(app=app)
    login_manager.login_view = 'auth.login'


    from app.routes import main_bp
    from app.auth.routes import auth_bp
    from app.lists.routes import list_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(list_bp)

    return app