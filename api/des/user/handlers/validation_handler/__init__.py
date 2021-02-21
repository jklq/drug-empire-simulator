from cerberus import Validator
from .schemas import registration_schema, login_schema
from functools import wraps
from flask import request, flash, abort, jsonify

def registration_validation(f):
    @wraps(f)
    def validate_registration_info(*args, **kwargs):
        if not request.is_json:
            return jsonify({'msg': 'Incorrect request format. Expected JSON.'}), 422
        else:
            print("JSON")
            user = {
                "username": request.json.get('username'),
                "email": request.json.get('email'),
                "password": request.json.get('password')
            }
            v = Validator(registration_schema)
            if (v.validate(user)):
               return f(*args, **kwargs)
            else:
                return jsonify({'msg': 'Invalid Registration Details'}), 400
    return validate_registration_info

def login_validation(f):
    @wraps(f)
    def validate_login_info(*args, **kwargs):
        if not request.is_json:
            return jsonify({'msg': 'Incorrect request format. Expected JSON.'}), 422
        else:
            user = {
                "email": request.json.get('email'),
                "password": request.json.get('password')
            }
            v = Validator(login_schema)
            if (v.validate(user)):
                print("VALID")
                return f(*args, **kwargs)
            else:
                return jsonify({'msg': 'Invalid Login Details'}), 400
    return validate_login_info
