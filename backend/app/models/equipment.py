from ..extensions import db

class Equipment(db.Model):
    __tablename__ = 'equipments'

    equipment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('equipment_types.type_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, default=0)
    defense = db.Column(db.Integer, default=0)
    character_type = db.Column(db.String(20), nullable=False)

    # Relation with CharacterEquipment
    assignments = db.relationship('CharacterEquipments', backref='equipment', lazy=True)
