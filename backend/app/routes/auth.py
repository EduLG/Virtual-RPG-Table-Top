from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", method=["post"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing data"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"error", "The user already exists"}), 409
    
    hasked_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hasked_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message", "User created succesfully."}), 201