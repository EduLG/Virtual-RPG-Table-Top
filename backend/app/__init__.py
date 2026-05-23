import os
from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.equipment_routes import equipment_bp
from app.routes.inventory_routes import inventory_bp
from app.routes.dungeon_routes import dungeon_bp
from app.routes.job_routes import job_bp
from app.routes.party_routes import party_bp
from app.routes.character_routes import character_bp
from flask_cors import CORS
from flask_migrate import Migrate
from .extensions import db
from config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_demo_session_valid(jwt_header, jwt_payload):
        """
        Invalidate demo tokens whose session has been destroyed.
        Returns True (blocked) if the demo session no longer exists.
        """
        if not jwt_payload.get("is_demo"):
            return False
        from app.demo.demo_store import demo_store
        session_id = jwt_payload.get("demo_session_id")
        return not demo_store.session_exists(session_id)

    from flask_jwt_extended import get_jwt
    from flask import g

    @app.after_request
    def _inject_demo_context(response):
        return response

    # Inject demo context into Flask g on every verified JWT request
    from flask_jwt_extended import verify_jwt_in_request
    from flask import request as flask_request

    @app.before_request
    def _set_demo_context():
        auth_header = flask_request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return
        try:
            verify_jwt_in_request(optional=True)
            claims = get_jwt()
            if claims.get("is_demo"):
                g.is_demo = True
                g.demo_session_id = claims.get("demo_session_id")
            else:
                g.is_demo = False
                g.demo_session_id = None
        except Exception:
            g.is_demo = False
            g.demo_session_id = None

    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    CORS(app, origins=[frontend_url], allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"])
    db.init_app(app)
    Migrate(app, db)

    from app.models.user import User
    from app.models.party import Party
    from app.models.character import Character
    from app.models.job import Job
    from app.models.equipment import Equipment
    from app.models.character_equipment import CharacterEquipment
    from app.models.party_inventory import PartyInventory
    from app.models.dungeon import Dungeon
    from app.models.exploration import Exploration

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(user_bp, url_prefix="/api/v1/users")
    app.register_blueprint(equipment_bp, url_prefix="/api/v1/equipment")
    app.register_blueprint(inventory_bp, url_prefix="/api/v1/inventory")
    app.register_blueprint(dungeon_bp, url_prefix="/api/v1/dungeons")
    app.register_blueprint(job_bp, url_prefix="/api/v1/jobs")
    app.register_blueprint(party_bp, url_prefix="/api/v1/party")
    app.register_blueprint(character_bp, url_prefix="/api/v1/characters")

    return app
