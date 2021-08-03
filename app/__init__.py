from flask import Flask, make_response, request, jsonify


def createApp():
    # Create Flask's `app` object
    app = Flask(__name__, template_folder= "templates")

    with app.app_context():
        from . import routes

        return app
