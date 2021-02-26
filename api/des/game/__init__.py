
from flask import Blueprint
from flask_classful import FlaskView

from .generator import GeneratorView

game = Blueprint('game', __name__)

GeneratorView.register(game)
