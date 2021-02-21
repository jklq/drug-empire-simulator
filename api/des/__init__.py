from flask import Flask
from .user import user
from .common.database import db, migrate
from .common.jwt import jwt

app = Flask(__name__)
app.config.from_pyfile('../config.py')

db.init_app(app)
migrate.init_app(app, db) 
jwt.init_app(app)

# Blueprints
app.register_blueprint(user, url_prefix='/user')

app.config.from_pyfile('../config.py')
