from flask import request, jsonify
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..db_actions import update_user_role

class ProfileView(FlaskView):

    @jwt_required()
    def index(self):
        current_user = get_jwt_identity()
        return current_user
    
    @jwt_required()
    @route("/select-role/" ,methods=["POST"])
    def select_role(self):
        role = request.json.get('role')
        username = get_jwt_identity()
        response = update_user_role(username, role)
        resMsg = response['msg']
        status = response['status']
        return jsonify({'msg': resMsg}), status


