from ..extensions import db
from sqlalchemy import UniqueConstraint

class CharacterEquipment(db.Model):
    __tablename__ = 'character_equipment'

    char_eq_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.equipment_id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('equipment_types.type_id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('character_id', 'type_id', name='uix_character_type'),
    )
