"""Initialize Flask Application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from flask_login import LoginManager

db = SQLAlchemy()
patch_all()
login_manager = LoginManager()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    # app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm" #copied because i dont have one
    # app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        #from .assets import compile_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        db.create_all()  # Create database tables for our data model

        return app