
from flask import Blueprint
from flask_classful import FlaskView

from .generator import GeneratorView
from .broker import BrokerView

game = Blueprint('game', __name__)

GeneratorView.register(game)
BrokerView.register(game)
