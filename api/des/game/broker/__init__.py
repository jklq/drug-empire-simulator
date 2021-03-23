from flask import jsonify
from flask_classful import FlaskView 
from ..shared.db import list_brokers

class BrokerView(FlaskView):
    def index(self):
        list_brokers()
        return "testfunction"
    def vessels(self):
        return "vessels"
