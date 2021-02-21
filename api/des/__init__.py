from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from .common.database import db, migrate
    from .common.jwt import jwt
    db.init_app(app)
    migrate.init_app(app, db) 
    jwt.init_app(app)

    # Blueprints
    from .user import user
    app.register_blueprint(user, url_prefix='/user')

    return app
