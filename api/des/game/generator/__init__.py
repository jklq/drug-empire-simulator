from flask import jsonify
from flask_classful import FlaskView 
from .example_object import MenuDict

class GeneratorView(FlaskView):
    def index(self):
        return jsonify(MenuDict)
