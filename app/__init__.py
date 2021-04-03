from flask import Flask, request, jsonify
from app.blueprint import blueprint
from app.modules import controller
import os

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(blueprint, url_prefix="/")
    return app
