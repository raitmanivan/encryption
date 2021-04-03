import app, json
from app.exceptions.exceptions import *
from flask import Blueprint, jsonify, request
from functools import wraps
import traceback

blueprint = Blueprint("blueprint", __name__)

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidCredentials:
            return jsonify({'Desc': 'Unauthorized'}),403
        except Exception as e:
            print(e)
            return jsonify({'Desc': "There was an error"}), 500
    return wrapper

@blueprint.route("/ping")
def main():
    return "pong"

@blueprint.route("/encrypt", methods=['POST'])
@exceptions_decorator
def encrypt():
    data = request.get_json(force=False)['data']
    encrypted_data = app.controller.encrypt(data)
    return jsonify({"data":encrypted_data}), 200

@blueprint.route("/decrypt", methods=['POST'])
@exceptions_decorator
def decrypt():
    data = request.get_json(force=False)['data']
    data_decrypted = app.controller.decrypt(data)
    return jsonify({"data":data_decrypted}), 200


