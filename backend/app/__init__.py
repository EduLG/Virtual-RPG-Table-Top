from flask import Flask
from app.routes.auth import auth_bp
from flask_cors import CORS
from .extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    from .models.user import User
    from .models.character import Character
    from .models.enemy import Enemy

    app.register_blueprint(auth_bp)

    return app
