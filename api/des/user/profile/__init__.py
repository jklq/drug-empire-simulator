from flask import request, jsonify
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..db_actions import update_user_role, user_exists

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

    @jwt_required()
    @route("/can-play/" ,methods=["GET"])
    def can_play(self):
        username = get_jwt_identity()
        response = user_exists(username=username)
        if response['result']:
            userRecord = response['matching_user']
            if userRecord.role == None:
                return jsonify({'msg': 'No role set', 'result': False, 'redirectUrl': '/game/select-role'}), 200
            else:
                return jsonify({'msg': 'Can play', 'result': True}), 200
        else:
            return jsonify({'msg': 'User not found'}), 404 


