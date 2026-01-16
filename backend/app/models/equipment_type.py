from ..extensions import db

class EquipmentType(db.Model):
    __tablename__ = 'equipment_types'

    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    # Relation with Equipment
    equipment_items = db.relationship('Equipment', backref='type', lazy=True)
