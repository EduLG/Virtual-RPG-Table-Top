from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from app.repositories.auth_repository import (
    get_user_by_username,
    get_user_by_email,
    create_user,
)


class ServiceError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code


def _validate_password(password):
    import re
    if len(password) < 8:
        raise ServiceError("Password must be at least 8 characters.", 400)
    if not re.search(r"[A-Z]", password):
        raise ServiceError("Password must contain at least one uppercase letter.", 400)
    if not re.search(r"[a-z]", password):
        raise ServiceError("Password must contain at least one lowercase letter.", 400)


def register_user(username, email, password):
    if not username or not email or not password:
        raise ServiceError("Missing data", 400)

    username = username.strip().lower()
    email = email.strip().lower()

    _validate_password(password)

    if get_user_by_username(username):
        raise ServiceError("The user already exists", 409)

    if get_user_by_email(email):
        raise ServiceError("The email already exists", 409)

    hashed = generate_password_hash(password)
    user = create_user(username, email, hashed)
    return user


def authenticate_user(username, password):
    if not username or not password:
        raise ServiceError("Missing data", 400)

    username = username.strip().lower()
    user = get_user_by_username(username)
    if not user:
        raise ServiceError("Invalid user", 401)

    if not check_password_hash(user.password, password):
        raise ServiceError("Invalid pass", 401)

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user_id": user.id,
        "username": user.username,
    }
