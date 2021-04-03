import app, requests, json
from functools import wraps
from app.exceptions.exceptions import *
import os
from app.resources import security

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise
    return wrapper

class Controller():

    def __init__(self):
        self.var = "test"
    
    @exceptions_decorator
    def encrypt(self, data):
        return security.encrypt(data)
    
    @exceptions_decorator
    def decrypt(self, data):
        return security.decrypt(data)        