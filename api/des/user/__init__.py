from flask import Blueprint
from flask_classful import FlaskView

from .login import LoginView
from .register import RegisterView
from .profile import ProfileView

user = Blueprint('user', __name__)

LoginView.register(user)
RegisterView.register(user)
ProfileView.register(user)

class UserView(FlaskView):
    route_base = "/"

    def index(self):
        return 'user'

UserView.register(user)
