from flask import jsonify
from flask_classful import FlaskView 

class BrokerView(FlaskView):
    def index(self):
        return "test"
    def vessels(self):
        return "vessels"
