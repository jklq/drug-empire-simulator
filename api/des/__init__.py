from flask import Flask
from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from .common.database import db, migrate
    from .common.jwt import jwt
    db.init_app(app)
    migrate.init_app(app, db) 
    jwt.init_app(app)
    CORS(app)

    # Blueprints
    from .user import user
    from .game import game
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(game, url_prefix='/game')

    return app
