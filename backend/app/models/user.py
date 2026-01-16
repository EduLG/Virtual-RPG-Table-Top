from ..extensions import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=False)
    password = db.Column(db.String(255), nullable=False)

    # Relation with Character
    characters = db.relationship('Character', backref='owner', lazy=True)