from ..extensions import db

class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    health = db.Column(db.Integer, default=100)
    power = db.Column(db.Integer, default=10)
    defense = db.Column(db.Integer, default=5)

    user_id = db.Column(db.Integer, db.ForeignKey('users'), nullable=False)