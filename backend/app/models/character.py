from ..extensions import db

class Character(db.Model):
    __tablename__ = 'characters'

    character_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    character_type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    # Relation with CharacterEquipment
    equipment_assignments = db.relationship('CharacterEquipment', backref='character', lazy=True)
