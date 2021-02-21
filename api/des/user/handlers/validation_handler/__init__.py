from cerberus import Validator
from .schemas import registration_schema, login_schema
from functools import wraps
from flask import request, flash, abort

def registration_validation(f):
    @wraps(f)
    def validate_registration_info(*args, **kwargs):
        user = {
            "username": request.args.get('username'),
            "email": request.args.get('email'),
            "password": request.args.get('password')
        }
        v = Validator(registration_schema)
        if (v.validate(user)):
           return f(*args, **kwargs)
        else:
            return 'Invalid Registration Details', 400
    return validate_registration_info

def login_validation(f):
    @wraps(f)
    def validate_login_info(*args, **kwargs):
        user = {
            "email": request.args.get('email'),
            "password": request.args.get('password')
        }
        v = Validator(login_schema)
        if (v.validate(user)):
            print("VALID")
            return f(*args, **kwargs)
        else:
            return 'Invalid Login Details', 400
    return validate_login_info
