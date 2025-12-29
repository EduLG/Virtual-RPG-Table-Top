from ..extensions import db

class Enemy(db.model):
    __tablename__ = 'Enemies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50), nullable=False)
    health = db.Column(db.Integer, default=10)
    power = db.Column(db.Integer, default=2)
    defense = db.Column(db.Integer, default=1)