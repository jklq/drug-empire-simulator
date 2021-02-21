from flask import request, jsonify
from flask_classful import FlaskView
from ..db_actions import create_user
from ..handlers.validation_handler import registration_validation
from ..models import User

class RegisterView(FlaskView):
    excluded_methods = ['register_user']
    
    @registration_validation
    def post(self):
        return self.register_user()
    
    def register_user(self):
        user = {
            "email": request.args.get('email'),
            "username": request.args.get('username'),
            "password": request.args.get('password').encode('utf-8')
        }
        creation_response = create_user(user)
        return jsonify({'msg': creation_response[0]}), creation_response[1]
