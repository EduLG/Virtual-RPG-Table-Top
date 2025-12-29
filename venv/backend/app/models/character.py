from ..extensions import db

class Character(db.model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50), nullable=False)
    health = db.Column(db.Integer, default=100)
    power = db.Column(db.Integer, default=10)
    defense = db.Column(db.Integer, default=5)

    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)