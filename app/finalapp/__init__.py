"""Initialize Flask Application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all

db = SQLAlchemy()
patch_all()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    # app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm" #copied because i dont have one
    # app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}
    db.init_app(app)
    with app.app_context():
        from . import routes
        db.create_all()  # Create database tables for our data models
        return app