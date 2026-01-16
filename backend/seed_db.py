from app import create_app
from app.extensions import db
from werkzeug.security import generate_password_hash

from app.models.user import User
from app.models.character import Character
from app.models.equipment_type import EquipmentType
from app.models.equipment import Equipment
from app.models.character_equipment import CharacterEquipment

app = create_app()

with app.app_context():
    # Create user
    user = User(username="eduladron", email="edu@example.com", password=generate_password_hash("12345678"))
    db.session.add(user)
    db.session.commit()

    # Create characters
    character_types = ["adventurer", "engineer", "alchemist", "scholar"]
    characters = []
    for ctype in character_types:
        character = Character(user_id=user.user_id, character_type=ctype, name=f"{ctype}_char")
        db.session.add(character)
        characters.append(character)
    db.session.commit()

    # Create equipment-types
    equipment_type_names = ["head", "chest", "legs", "main_arm", "secondary_arm"]
    equipment_types = []
    for name in equipment_type_names:
        etype = EquipmentType(name=name)
        db.session.add(etype)
        equipment_types.append(etype)
    db.session.commit()

    # Create equipments
    equipments = []
    for etype in equipment_types:
        for ctype in character_types:
            eq = Equipment(
                name=f"{ctype}_{etype.name}",
                type_id=etype.type_id,
                rating=5,
                strength=10,
                defense=5,
                character_type=ctype
            )
            db.session.add(eq)
            equipments.append(eq)
    db.session.commit()

    # Assign equipment to characters
    for character in characters:
        for eq in equipments:
            if eq.character_type == character.character_type:
                char_eq = CharacterEquipment(
                    character_id=character.character_id,
                    equipment_id=eq.equipment_id,
                    type_id=eq.type_id
                )
                db.session.add(char_eq)
    db.session.commit()

    print("Seeding data inserted successfully")
