from flask import Flask
from app.routes.auth import auth_bp
from flask_cors import CORS
from .extensions import db
from config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["JWT_SECRET_KEY"] = "super_secret_key"
    jwt = JWTManager(app)

    CORS(app)
    db.init_app(app)

    from .models.user import User
    from .models.character import Character
    from .models.enemy import Enemy

    app.register_blueprint(auth_bp)

    return app
