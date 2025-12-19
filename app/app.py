from flask import Flask, url_for
from app.auth import auth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)

    return app