from flask import Blueprint, request
from flask_classful import FlaskView
from flask_jwt_extended import jwt_required, get_jwt_identity

profile = Blueprint('profile', __name__)

class ProfileView(FlaskView):
    route_base = '/'
    excluded_methods = ['login_user']
    
    @jwt_required()
    def index(self):
        current_user = get_jwt_identity()
        return current_user
