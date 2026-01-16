from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.character import Character
from app.models.equipment_type import EquipmentType
from app.models.equipment import Equipment
from app.models.character_equipment import CharacterEquipment

app = create_app()

with app.app_context():
    # User
    user = User(
        username="edu",
        email="eduladron@gmail.com",
        password="12345678"
    )
    db.session.add(user)
    db.session.commit()

    # Character
    character = Character(
        user_id=user.user_id,
        character_type="adventurer",
        name="Arthos"
    )
    db.session.add(character)
    db.session.commit()

    # Equipment types
    head = EquipmentType(name="Head")
    weapon = EquipmentType(name="main_weapon")
    db.session.add_all([head, weapon])
    db.session.commit()

    # Equipments
    helmet = Equipment(
        name="Iron Helmet",
        type_id=head.type_id,
        rating=1,
        defense=5,
        strength=0,
        character_type="adventurer"
    )
    sword = Equipment(
        name="Short Sword",
        type_id=weapon.type_id,
        rating=1,
        defense=0,
        strength=7,
        character_type="adventurer"
    )
    db.session.add_all([helmet, sword])
    db.session.commit()

    # Assign equipment to character
    char_helmet = CharacterEquipment(
        character_id=character.character_id,
        equipment_id=helmet.equipment_id,
        type_id=head.type_id
    )
    char_sword = CharacterEquipment(
        character_id=character.character_id,
        equipment_id=sword.equipment_id,
        type_id=weapon.type_id
    )
    db.session.add_all([char_helmet, char_sword])
    db.session.commit()

    print("Seeding data inserted successfully")
