from flask import jsonify
from flask_classful import FlaskView 
from .example_object import get_menu_dict
from des.user.db_actions import user_exists
from flask_jwt_extended import jwt_required, get_jwt_identity

class GeneratorView(FlaskView):
    @jwt_required()
    def index(self):
        return jsonify(get_menu_dict(get_jwt_identity()))
