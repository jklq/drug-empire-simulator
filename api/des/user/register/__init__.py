from flask import request, jsonify
from flask_classful import FlaskView
from ..db_actions import create_user
from ..handlers.validation_handler import registration_validation
from ..models import User

class RegisterView(FlaskView):
    excluded_methods = ['register_user']
    
    @registration_validation
    def post(self):
        user = {
            "email": request.json.get('email'),
            "username": request.json.get('username'),
            "password": request.json.get('password').encode('utf-8')
        }
        return self.register_user(user)
    
    def register_user(self, user):
        creation_response = create_user(**user)
        resMsg = creation_response['msg']
        status = creation_response['status']
        return jsonify({'msg': resMsg}), status
