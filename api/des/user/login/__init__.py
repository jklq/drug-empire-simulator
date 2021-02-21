from flask import Blueprint, request, jsonify
from flask_classful import FlaskView
from ..handlers.validation_handler import login_validation
from ..db_actions import user_exists 
from ..helpers.hash_helper import hash_compare 
from flask_jwt_extended import create_access_token

login = Blueprint('login', __name__)

class LoginView(FlaskView):
    excluded_methods = ['login_user']

    @login_validation
    def post(self):
        user = {
            "email": request.json.get('email'),
            "password": request.json.get('password').encode('utf-8')
        }
        return self.login_user(user)

    def login_user(self, user):
        user_match = user_exists(**user)
        if user_match['result']:
            user_record = user_match['matching_user']
            user_record.password = user_record.password
            if hash_compare(user['password'], user_record.password):
                access_token = create_access_token(identity=user_record.username)
                return jsonify({'msg': access_token})

            response = jsonify({'msg': 'Wrong Password'})
            return response, 401
        else:
            response = jsonify({'msg': 'Wrong Email'}) 
            return response, 401
