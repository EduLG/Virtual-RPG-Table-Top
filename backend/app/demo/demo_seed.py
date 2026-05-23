"""
Static demo data mirroring seed_db.py.
All items are plain dicts — no SQLAlchemy involved.
IDs match the 1-based insertion order used by the real seed.
"""

# ---------------------------------------------------------------------------
# Jobs (same order as seed_db.py — index determines job_index in loot formula)
# ---------------------------------------------------------------------------
# job_index: engineer=0, gunslinger=1, adventurer=2, alchemist=3,
#             warrior=4, fender=5, sage=6, thief=7, scholar=8, beastmaster=9

JOBS = [
    {"id": 1,  "name": "engineer",    "icon": "/character-templates/engineer_male.png"},
    {"id": 2,  "name": "gunslinger",  "icon": "/character-templates/gunslinger_male.png"},
    {"id": 3,  "name": "adventurer",  "icon": "/character-templates/adventurer_male.png"},
    {"id": 4,  "name": "alchemist",   "icon": "/character-templates/alchemist_male.png"},
    {"id": 5,  "name": "warrior",     "icon": "/character-templates/warrior_male.png"},
    {"id": 6,  "name": "fender",      "icon": "/character-templates/fender_male.png"},
    {"id": 7,  "name": "sage",        "icon": "/character-templates/sage_male.png"},
    {"id": 8,  "name": "thief",       "icon": "/character-templates/thief_male.png"},
    {"id": 9,  "name": "scholar",     "icon": "/character-templates/scholar_male.png"},
    {"id": 10, "name": "beastmaster", "icon": "/character-templates/beastmaster_male.png"},
]

# ---------------------------------------------------------------------------
# Equipment catalog — 500 items (5 slots × 10 jobs × 10 tiers)
# ID = 1-based index into this list (same as DB after seed)
# Slot bases: head=0  chest=100  primary_hand=200  secondary_hand=300  accesory=400
# ---------------------------------------------------------------------------

def _eq(idx, name, slot, rating, equipment_type):
    return {"id": idx + 1, "name": name, "slot": slot, "rating": rating, "equipment_type": equipment_type}


def _build_equipment_catalog():
    raw = [
        # ---- HEAD ----
        # T1 (rating 2)
        ("Apprentice Goggles",    "head", 2,  "cloth"),
        ("Rawhide Cap",           "head", 2,  "leather"),
        ("Cloth Cap",             "head", 2,  "leather"),
        ("Apprentice's Cap",      "head", 2,  "cloth"),
        ("Iron Coif",             "head", 2,  "plate"),
        ("Sentry Cap",            "head", 2,  "plate"),
        ("Apprentice Hood",       "head", 2,  "cloth"),
        ("Rogue's Wrap",          "head", 2,  "leather"),
        ("Student's Cap",         "head", 2,  "cloth"),
        ("Pelt Cap",              "head", 2,  "leather"),
        # T2 (rating 5)
        ("Workshop Goggles",      "head", 5,  "cloth"),
        ("Leather Cap",           "head", 5,  "leather"),
        ("Straw Hat",             "head", 5,  "leather"),
        ("Alchemist's Cap",       "head", 5,  "cloth"),
        ("Iron Helmet",           "head", 5,  "plate"),
        ("Guard's Helm",          "head", 5,  "plate"),
        ("Sage's Hood",           "head", 5,  "cloth"),
        ("Thief's Hood",          "head", 5,  "leather"),
        ("Researcher's Cap",      "head", 5,  "cloth"),
        ("Hunter's Cap",          "head", 5,  "leather"),
        # T3 (rating 9)
        ("Tinkerer's Helm",       "head", 9,  "cloth"),
        ("Frontier Hat",          "head", 9,  "leather"),
        ("Adventurer's Hat",      "head", 9,  "leather"),
        ("Alchemist Hood",        "head", 9,  "cloth"),
        ("Steel Helmet",          "head", 9,  "plate"),
        ("Sentinel's Helm",       "head", 9,  "plate"),
        ("Mage's Cap",            "head", 9,  "cloth"),
        ("Shadow Hood",           "head", 9,  "leather"),
        ("Academic Hood",         "head", 9,  "cloth"),
        ("Feral Mask",            "head", 9,  "leather"),
        # T4 (rating 14)
        ("Gear Cap",              "head", 14, "cloth"),
        ("Drifter's Brim",        "head", 14, "leather"),
        ("Traveler's Hood",       "head", 14, "leather"),
        ("Brew Master's Hat",     "head", 14, "cloth"),
        ("Knight's Visor",        "head", 14, "plate"),
        ("Vanguard's Helm",       "head", 14, "plate"),
        ("Arcanist's Hood",       "head", 14, "cloth"),
        ("Infiltrator's Mask",    "head", 14, "leather"),
        ("Scholar's Hat",         "head", 14, "cloth"),
        ("Wild Crown",            "head", 14, "leather"),
        # T5 (rating 20)
        ("Engineer Goggles",      "head", 20, "cloth"),
        ("Sharpshooter's Cap",    "head", 20, "leather"),
        ("Scout's Helm",          "head", 20, "leather"),
        ("Mystic Hood",           "head", 20, "cloth"),
        ("Battle Helm",           "head", 20, "plate"),
        ("Defender's Plate",      "head", 20, "plate"),
        ("Mystic Turban",         "head", 20, "cloth"),
        ("Shadow Mask",           "head", 20, "leather"),
        ("Analyst's Visor",       "head", 20, "cloth"),
        ("Beast Mask",            "head", 20, "leather"),
        # T6 (rating 28)
        ("Precision Visor",       "head", 28, "cloth"),
        ("Bounty Hunter's Hat",   "head", 28, "leather"),
        ("Pathfinder's Cap",      "head", 28, "leather"),
        ("Sage Veil",             "head", 28, "cloth"),
        ("Champion's Helm",       "head", 28, "plate"),
        ("Bulwark Helm",          "head", 28, "plate"),
        ("Elder's Hat",           "head", 28, "cloth"),
        ("Phantom Veil",          "head", 28, "leather"),
        ("Professor's Cap",       "head", 28, "cloth"),
        ("Alpha's Mark",          "head", 28, "leather"),
        # T7 (rating 38)
        ("Iron Goggle Mk.II",     "head", 38, "cloth"),
        ("Outlaw's Brim",         "head", 38, "leather"),
        ("Explorer's Visor",      "head", 38, "leather"),
        ("Arcane Hood",           "head", 38, "cloth"),
        ("Templar Helmet",        "head", 38, "plate"),
        ("Fortress Helm",         "head", 38, "plate"),
        ("Ethereal Hood",         "head", 38, "cloth"),
        ("Nightwalker's Hood",    "head", 38, "leather"),
        ("Mastermind's Hood",     "head", 38, "cloth"),
        ("Beast Crown",           "head", 38, "leather"),
        # T8 (rating 50)
        ("Mech Helm",             "head", 50, "cloth"),
        ("Marshal's Hat",         "head", 50, "leather"),
        ("Trailblazer's Helm",    "head", 50, "leather"),
        ("Arcane Circlet",        "head", 50, "cloth"),
        ("Warlord's Helm",        "head", 50, "plate"),
        ("Citadel Helm",          "head", 50, "plate"),
        ("Archmage's Cap",        "head", 50, "cloth"),
        ("Specter's Mask",        "head", 50, "leather"),
        ("Grand Scholar's Hat",   "head", 50, "cloth"),
        ("Warchief's Helm",       "head", 50, "leather"),
        # T9 (rating 65)
        ("Servo Cranium",         "head", 65, "cloth"),
        ("Desperado's Crown",     "head", 65, "leather"),
        ("Wayfarer's Crown",      "head", 65, "leather"),
        ("Philosopher's Hat",     "head", 65, "cloth"),
        ("Dragon Helm",           "head", 65, "plate"),
        ("Bastion Crown",         "head", 65, "plate"),
        ("Celestial Hood",        "head", 65, "cloth"),
        ("Void Mask",             "head", 65, "leather"),
        ("Sage's Laurel",         "head", 65, "cloth"),
        ("Elder Beast Crown",     "head", 65, "leather"),
        # T10 (rating 82)
        ("Neural Interface",      "head", 82, "cloth"),
        ("Legend's Hat",          "head", 82, "leather"),
        ("Explorer's Crown",      "head", 82, "leather"),
        ("Grand Alchemist's Crown","head",82, "cloth"),
        ("Legendary Helm",        "head", 82, "plate"),
        ("Aegis Helm",            "head", 82, "plate"),
        ("Divine Circlet",        "head", 82, "cloth"),
        ("Dark Assassin's Crown", "head", 82, "leather"),
        ("Omniscient's Crown",    "head", 82, "cloth"),
        ("Apex Predator's Crown", "head", 82, "leather"),

        # ---- CHEST ----
        # T1 (rating 2)
        ("Work Vest",             "chest", 2,  "cloth"),
        ("Canvas Shirt",          "chest", 2,  "leather"),
        ("Cloth Tunic",           "chest", 2,  "leather"),
        ("Apprentice's Robe",     "chest", 2,  "cloth"),
        ("Padded Armor",          "chest", 2,  "plate"),
        ("Guard's Tunic",         "chest", 2,  "plate"),
        ("Simple Robe",           "chest", 2,  "cloth"),
        ("Rogue's Shirt",         "chest", 2,  "leather"),
        ("Student's Coat",        "chest", 2,  "cloth"),
        ("Pelt Shirt",            "chest", 2,  "leather"),
        # T2
        ("Utility Vest",          "chest", 5,  "cloth"),
        ("Leather Vest",          "chest", 5,  "leather"),
        ("Work Tunic",            "chest", 5,  "leather"),
        ("Scholar's Coat",        "chest", 5,  "cloth"),
        ("Chain Mail",            "chest", 5,  "plate"),
        ("Scale Armor",           "chest", 5,  "plate"),
        ("Sage's Robe",           "chest", 5,  "cloth"),
        ("Shadow Garb",           "chest", 5,  "leather"),
        ("Lab Coat",              "chest", 5,  "cloth"),
        ("Hide Vest",             "chest", 5,  "leather"),
        # T3
        ("Tinkerer's Coat",       "chest", 9,  "cloth"),
        ("Drifter's Shirt",       "chest", 9,  "leather"),
        ("Traveler's Shirt",      "chest", 9,  "leather"),
        ("Mystic Robe",           "chest", 9,  "cloth"),
        ("Scale Mail",            "chest", 9,  "plate"),
        ("Mail Coat",             "chest", 9,  "plate"),
        ("Mage's Coat",           "chest", 9,  "cloth"),
        ("Thief's Coat",          "chest", 9,  "leather"),
        ("Researcher's Coat",     "chest", 9,  "cloth"),
        ("Hunter's Coat",         "chest", 9,  "leather"),
        # T4
        ("Steam Vest",            "chest", 14, "cloth"),
        ("Frontier Coat",         "chest", 14, "leather"),
        ("Explorer's Tunic",      "chest", 14, "leather"),
        ("Alchemist's Coat",      "chest", 14, "cloth"),
        ("Plate Vest",            "chest", 14, "plate"),
        ("Sentinel's Plate",      "chest", 14, "plate"),
        ("Arcanist's Robe",       "chest", 14, "cloth"),
        ("Infiltrator's Vest",    "chest", 14, "leather"),
        ("Academic Robe",         "chest", 14, "cloth"),
        ("Feral Vest",            "chest", 14, "leather"),
        # T5
        ("Engineer's Coat",       "chest", 20, "cloth"),
        ("Duster Coat",           "chest", 20, "leather"),
        ("Scout's Vest",          "chest", 20, "leather"),
        ("Brew Master's Robe",    "chest", 20, "cloth"),
        ("Battle Plate",          "chest", 20, "plate"),
        ("Vanguard's Armor",      "chest", 20, "plate"),
        ("Ethereal Robe",         "chest", 20, "cloth"),
        ("Nightweave Shirt",      "chest", 20, "leather"),
        ("Analyst's Coat",        "chest", 20, "cloth"),
        ("Beastkin Coat",         "chest", 20, "leather"),
        # T6
        ("Gear Plate",            "chest", 28, "cloth"),
        ("Bounty Coat",           "chest", 28, "leather"),
        ("Pathfinder's Coat",     "chest", 28, "leather"),
        ("Alchemist's Mantle",    "chest", 28, "cloth"),
        ("Knight's Plate",        "chest", 28, "plate"),
        ("Bulwark Coat",          "chest", 28, "plate"),
        ("Elder's Mantle",        "chest", 28, "cloth"),
        ("Shadow Suit",           "chest", 28, "leather"),
        ("Professor's Coat",      "chest", 28, "cloth"),
        ("Pack Leader's Vest",    "chest", 28, "leather"),
        # T7
        ("Steam Coat",            "chest", 38, "cloth"),
        ("Outlaw's Coat",         "chest", 38, "leather"),
        ("Traveler's Coat",       "chest", 38, "leather"),
        ("Arcane Robe",           "chest", 38, "cloth"),
        ("Dragon Scale Mail",     "chest", 38, "plate"),
        ("Fortress Plate",        "chest", 38, "plate"),
        ("Arcane Mantle",         "chest", 38, "cloth"),
        ("Phantom Garb",          "chest", 38, "leather"),
        ("Scholar's Mantle",      "chest", 38, "cloth"),
        ("Alpha's Hide",          "chest", 38, "leather"),
        # T8
        ("Mech Suit",             "chest", 50, "cloth"),
        ("Marshal's Coat",        "chest", 50, "leather"),
        ("Trailblazer's Vest",    "chest", 50, "leather"),
        ("Philosopher's Robe",    "chest", 50, "cloth"),
        ("Templar Plate",         "chest", 50, "plate"),
        ("Citadel Armor",         "chest", 50, "plate"),
        ("Archmage's Robe",       "chest", 50, "cloth"),
        ("Nightweave Suit",       "chest", 50, "leather"),
        ("Grand Scholar's Coat",  "chest", 50, "cloth"),
        ("Warchief's Coat",       "chest", 50, "leather"),
        # T9
        ("Power Armor",           "chest", 65, "cloth"),
        ("Desperado's Vest",      "chest", 65, "leather"),
        ("Wayfarer's Coat",       "chest", 65, "leather"),
        ("Grand Alchemist's Robe","chest", 65, "cloth"),
        ("Warlord's Plate",       "chest", 65, "plate"),
        ("Bastion Armor",         "chest", 65, "plate"),
        ("Celestial Mantle",      "chest", 65, "cloth"),
        ("Void Garb",             "chest", 65, "leather"),
        ("Master's Mantle",       "chest", 65, "cloth"),
        ("Elder Beast Hide",      "chest", 65, "leather"),
        # T10
        ("Power Suit",            "chest", 82, "cloth"),
        ("Legend's Coat",         "chest", 82, "leather"),
        ("Explorer's Plate",      "chest", 82, "leather"),
        ("Celestial Robe",        "chest", 82, "cloth"),
        ("Void Plate",            "chest", 82, "plate"),
        ("Aegis Plate",           "chest", 82, "plate"),
        ("Divine Robe",           "chest", 82, "cloth"),
        ("Dark Assassin's Suit",  "chest", 82, "leather"),
        ("Omniscient's Robe",     "chest", 82, "cloth"),
        ("Apex Predator's Coat",  "chest", 82, "leather"),

        # ---- PRIMARY HAND ----
        # T1
        ("Rusty Wrench",          "primary_hand", 2,  "cloth"),
        ("Broken Pistol",         "primary_hand", 2,  "leather"),
        ("Wooden Stick",          "primary_hand", 2,  "leather"),
        ("Apprentice's Wand",     "primary_hand", 2,  "cloth"),
        ("Training Sword",        "primary_hand", 2,  "plate"),
        ("Wooden Club",           "primary_hand", 2,  "plate"),
        ("Crooked Staff",         "primary_hand", 2,  "cloth"),
        ("Rusty Knife",           "primary_hand", 2,  "leather"),
        ("Field Notes",           "primary_hand", 2,  "cloth"),
        ("Rope Whip",             "primary_hand", 2,  "leather"),
        # T2
        ("Iron Wrench",           "primary_hand", 5,  "cloth"),
        ("Flintlock",             "primary_hand", 5,  "leather"),
        ("Short Sword",           "primary_hand", 5,  "leather"),
        ("Crystal Wand",          "primary_hand", 5,  "cloth"),
        ("Iron Sword",            "primary_hand", 5,  "plate"),
        ("Iron Club",             "primary_hand", 5,  "plate"),
        ("Wooden Staff",          "primary_hand", 5,  "cloth"),
        ("Boot Knife",            "primary_hand", 5,  "leather"),
        ("Research Tome",         "primary_hand", 5,  "cloth"),
        ("Taming Whip",           "primary_hand", 5,  "leather"),
        # T3
        ("Titan Wrench",          "primary_hand", 9,  "cloth"),
        ("Revolver",              "primary_hand", 9,  "leather"),
        ("Scout's Blade",         "primary_hand", 9,  "leather"),
        ("Crystal Staff",         "primary_hand", 9,  "cloth"),
        ("Steel Sword",           "primary_hand", 9,  "plate"),
        ("War Club",              "primary_hand", 9,  "plate"),
        ("Sage's Wand",           "primary_hand", 9,  "cloth"),
        ("Shadow Blade",          "primary_hand", 9,  "leather"),
        ("Analytical Lens",       "primary_hand", 9,  "cloth"),
        ("Beast Prod",            "primary_hand", 9,  "leather"),
        # T4
        ("Gear Hammer",           "primary_hand", 14, "cloth"),
        ("Double Barrel",         "primary_hand", 14, "leather"),
        ("Traveler's Blade",      "primary_hand", 14, "leather"),
        ("Runic Rod",             "primary_hand", 14, "cloth"),
        ("Broad Sword",           "primary_hand", 14, "plate"),
        ("Iron Mace",             "primary_hand", 14, "plate"),
        ("Sage's Staff",          "primary_hand", 14, "cloth"),
        ("Twin Blades",           "primary_hand", 14, "leather"),
        ("Scholar's Tome",        "primary_hand", 14, "cloth"),
        ("Alpha Whip",            "primary_hand", 14, "leather"),
        # T5
        ("Wrench Mk.II",          "primary_hand", 20, "cloth"),
        ("Revolver Mk.II",        "primary_hand", 20, "leather"),
        ("Adventurer's Blade",    "primary_hand", 20, "leather"),
        ("Golden Staff",          "primary_hand", 20, "cloth"),
        ("War Sword",             "primary_hand", 20, "plate"),
        ("War Axe",               "primary_hand", 20, "plate"),
        ("Elder Staff",           "primary_hand", 20, "cloth"),
        ("Shadow Daggers",        "primary_hand", 20, "leather"),
        ("Professor's Lens",      "primary_hand", 20, "cloth"),
        ("Feral Staff",           "primary_hand", 20, "leather"),
        # T6
        ("Power Wrench",          "primary_hand", 28, "cloth"),
        ("Marksman's Rifle",      "primary_hand", 28, "leather"),
        ("Pathfinder's Blade",    "primary_hand", 28, "leather"),
        ("Arcane Rod",            "primary_hand", 28, "cloth"),
        ("Knight's Blade",        "primary_hand", 28, "plate"),
        ("Battle Axe",            "primary_hand", 28, "plate"),
        ("Arcane Staff",          "primary_hand", 28, "cloth"),
        ("Twin Daggers",          "primary_hand", 28, "leather"),
        ("Grand Tome",            "primary_hand", 28, "cloth"),
        ("Taming Staff",          "primary_hand", 28, "leather"),
        # T7
        ("Plasma Wrench",         "primary_hand", 38, "cloth"),
        ("Repeating Rifle",       "primary_hand", 38, "leather"),
        ("Explorer's Blade",      "primary_hand", 38, "leather"),
        ("Staff of Mysteries",    "primary_hand", 38, "cloth"),
        ("Holy Sword",            "primary_hand", 38, "plate"),
        ("Great Axe",             "primary_hand", 38, "plate"),
        ("Ethereal Staff",        "primary_hand", 38, "cloth"),
        ("Phantom Blades",        "primary_hand", 38, "leather"),
        ("Mastermind's Lens",     "primary_hand", 38, "cloth"),
        ("Beast Caller Staff",    "primary_hand", 38, "leather"),
        # T8
        ("Gear Cannon",           "primary_hand", 50, "cloth"),
        ("Thunder Gun",           "primary_hand", 50, "leather"),
        ("Trailblazer's Blade",   "primary_hand", 50, "leather"),
        ("Staff of Elements",     "primary_hand", 50, "cloth"),
        ("Champion's Blade",      "primary_hand", 50, "plate"),
        ("Warlord's Axe",         "primary_hand", 50, "plate"),
        ("Archmage's Staff",      "primary_hand", 50, "cloth"),
        ("Void Daggers",          "primary_hand", 50, "leather"),
        ("Grand Scholar's Lens",  "primary_hand", 50, "cloth"),
        ("Alpha Staff",           "primary_hand", 50, "leather"),
        # T9
        ("Plasma Cutter",         "primary_hand", 65, "cloth"),
        ("Devastator",            "primary_hand", 65, "leather"),
        ("Wayfarer's Blade",      "primary_hand", 65, "leather"),
        ("Grand Staff",           "primary_hand", 65, "cloth"),
        ("Dragon Sword",          "primary_hand", 65, "plate"),
        ("Fortress Axe",          "primary_hand", 65, "plate"),
        ("Celestial Staff",       "primary_hand", 65, "cloth"),
        ("Specter's Blades",      "primary_hand", 65, "leather"),
        ("Omniscient Lens",       "primary_hand", 65, "cloth"),
        ("Elder Taming Staff",    "primary_hand", 65, "leather"),
        # T10
        ("Neural Cannon",         "primary_hand", 82, "cloth"),
        ("Legend's Rifle",        "primary_hand", 82, "leather"),
        ("Vorpal Blade",          "primary_hand", 82, "leather"),
        ("Staff of Creation",     "primary_hand", 82, "cloth"),
        ("Excalibur",             "primary_hand", 82, "plate"),
        ("Aegis Axe",             "primary_hand", 82, "plate"),
        ("Divine Staff",          "primary_hand", 82, "cloth"),
        ("Dark Assassin's Blades","primary_hand", 82, "leather"),
        ("Oracle's Lens",         "primary_hand", 82, "cloth"),
        ("Apex Predator's Staff", "primary_hand", 82, "leather"),

        # ---- SECONDARY HAND ----
        # T1
        ("Worn Bracer",           "secondary_hand", 2,  "cloth"),
        ("Powder Horn",           "secondary_hand", 2,  "leather"),
        ("Wooden Buckler",        "secondary_hand", 2,  "leather"),
        ("Focus Shard",           "secondary_hand", 2,  "cloth"),
        ("Wooden Shield",         "secondary_hand", 2,  "plate"),
        ("Cracked Shield",        "secondary_hand", 2,  "plate"),
        ("Dim Orb",               "secondary_hand", 2,  "cloth"),
        ("Smoke Pellet",          "secondary_hand", 2,  "leather"),
        ("Field Journal",         "secondary_hand", 2,  "cloth"),
        ("Beast Token",           "secondary_hand", 2,  "leather"),
        # T2
        ("Reinforced Bracer",     "secondary_hand", 5,  "cloth"),
        ("Ammo Pouch",            "secondary_hand", 5,  "leather"),
        ("Wooden Targe",          "secondary_hand", 5,  "leather"),
        ("Focus Orb",             "secondary_hand", 5,  "cloth"),
        ("Iron Shield",           "secondary_hand", 5,  "plate"),
        ("Recruit's Shield",      "secondary_hand", 5,  "plate"),
        ("Spell Tome",            "secondary_hand", 5,  "cloth"),
        ("Throwing Knife",        "secondary_hand", 5,  "leather"),
        ("Research Journal",      "secondary_hand", 5,  "cloth"),
        ("Feather Totem",         "secondary_hand", 5,  "leather"),
        # T3
        ("Tool Bracer",           "secondary_hand", 9,  "cloth"),
        ("Quick Draw Holster",    "secondary_hand", 9,  "leather"),
        ("Travel Shield",         "secondary_hand", 9,  "leather"),
        ("Mana Crystal",          "secondary_hand", 9,  "cloth"),
        ("Kite Shield",           "secondary_hand", 9,  "plate"),
        ("Sentinel Shield",       "secondary_hand", 9,  "plate"),
        ("Arcane Tome",           "secondary_hand", 9,  "cloth"),
        ("Smoke Bomb",            "secondary_hand", 9,  "leather"),
        ("Data Tablet",           "secondary_hand", 9,  "cloth"),
        ("Bone Totem",            "secondary_hand", 9,  "leather"),
        # T4
        ("Gear Bracer",           "secondary_hand", 14, "cloth"),
        ("Off-hand Pistol",       "secondary_hand", 14, "leather"),
        ("Scout's Buckler",       "secondary_hand", 14, "leather"),
        ("Runic Crystal",         "secondary_hand", 14, "cloth"),
        ("Battle Shield",         "secondary_hand", 14, "plate"),
        ("Tower Shield",          "secondary_hand", 14, "plate"),
        ("Elder's Tome",          "secondary_hand", 14, "cloth"),
        ("Flash Bomb",            "secondary_hand", 14, "leather"),
        ("Annotated Tome",        "secondary_hand", 14, "cloth"),
        ("Pack Totem",            "secondary_hand", 14, "leather"),
        # T5
        ("Steam Bracer",          "secondary_hand", 20, "cloth"),
        ("Bandolier",             "secondary_hand", 20, "leather"),
        ("Pathfinder's Shield",   "secondary_hand", 20, "leather"),
        ("Grand Crystal",         "secondary_hand", 20, "cloth"),
        ("Knight's Shield",       "secondary_hand", 20, "plate"),
        ("Bulwark Shield",        "secondary_hand", 20, "plate"),
        ("Mystic Orb",            "secondary_hand", 20, "cloth"),
        ("Poison Vial",           "secondary_hand", 20, "leather"),
        ("Professor's Journal",   "secondary_hand", 20, "cloth"),
        ("Alpha Totem",           "secondary_hand", 20, "leather"),
        # T6
        ("Hydraulic Bracer",      "secondary_hand", 28, "cloth"),
        ("Marksman's Scope",      "secondary_hand", 28, "leather"),
        ("Explorer's Buckler",    "secondary_hand", 28, "leather"),
        ("Arcane Crystal",        "secondary_hand", 28, "cloth"),
        ("Champion's Shield",     "secondary_hand", 28, "plate"),
        ("Fortress Shield",       "secondary_hand", 28, "plate"),
        ("Arcane Orb",            "secondary_hand", 28, "cloth"),
        ("Shadow Bomb",           "secondary_hand", 28, "leather"),
        ("Grand Journal",         "secondary_hand", 28, "cloth"),
        ("Elder Totem",           "secondary_hand", 28, "leather"),
        # T7
        ("Plasma Bracer",         "secondary_hand", 38, "cloth"),
        ("Eagle Eye Scope",       "secondary_hand", 38, "leather"),
        ("Trailblazer's Shield",  "secondary_hand", 38, "leather"),
        ("Ether Crystal",         "secondary_hand", 38, "cloth"),
        ("Templar Shield",        "secondary_hand", 38, "plate"),
        ("Citadel Shield",        "secondary_hand", 38, "plate"),
        ("Ethereal Orb",          "secondary_hand", 38, "cloth"),
        ("Void Bomb",             "secondary_hand", 38, "leather"),
        ("Mastermind's Journal",  "secondary_hand", 38, "cloth"),
        ("Spirit Totem",          "secondary_hand", 38, "leather"),
        # T8
        ("Mech Bracer",           "secondary_hand", 50, "cloth"),
        ("Rapid Fire Module",     "secondary_hand", 50, "leather"),
        ("Wayfarer's Shield",     "secondary_hand", 50, "leather"),
        ("Philosopher's Orb",     "secondary_hand", 50, "cloth"),
        ("Warlord's Shield",      "secondary_hand", 50, "plate"),
        ("Aegis Shield",          "secondary_hand", 50, "plate"),
        ("Archmage's Orb",        "secondary_hand", 50, "cloth"),
        ("Specter's Bomb",        "secondary_hand", 50, "leather"),
        ("Grand Scholar's Journal","secondary_hand", 50, "cloth"),
        ("Apex Totem",            "secondary_hand", 50, "leather"),
        # T9
        ("Neural Bracer",         "secondary_hand", 65, "cloth"),
        ("Targeting System",      "secondary_hand", 65, "leather"),
        ("Explorer's Shield",     "secondary_hand", 65, "leather"),
        ("Grand Orb",             "secondary_hand", 65, "cloth"),
        ("Dragon Shield",         "secondary_hand", 65, "plate"),
        ("Bastion Shield",        "secondary_hand", 65, "plate"),
        ("Celestial Orb",         "secondary_hand", 65, "cloth"),
        ("Dark Bomb",             "secondary_hand", 65, "leather"),
        ("Omniscient Journal",    "secondary_hand", 65, "cloth"),
        ("Elder Spirit Totem",    "secondary_hand", 65, "leather"),
        # T10
        ("Exo Bracer",            "secondary_hand", 82, "cloth"),
        ("Legend's Scope",        "secondary_hand", 82, "leather"),
        ("Legendary Buckler",     "secondary_hand", 82, "leather"),
        ("Cosmic Orb",            "secondary_hand", 82, "cloth"),
        ("Eternal Shield",        "secondary_hand", 82, "plate"),
        ("Divine Shield",         "secondary_hand", 82, "plate"),
        ("Divine Orb",            "secondary_hand", 82, "cloth"),
        ("Phantom Bomb",          "secondary_hand", 82, "leather"),
        ("Oracle's Journal",      "secondary_hand", 82, "cloth"),
        ("Apex Spirit Totem",     "secondary_hand", 82, "leather"),

        # ---- ACCESORY ----
        # T1
        ("Bent Cog",              "accesory", 2,  "cloth"),
        ("Copper Badge",          "accesory", 2,  "leather"),
        ("Lucky Pebble",          "accesory", 2,  "leather"),
        ("Empty Vial",            "accesory", 2,  "cloth"),
        ("Tin Ring",              "accesory", 2,  "plate"),
        ("Recruit's Insignia",    "accesory", 2,  "plate"),
        ("Dim Crystal",           "accesory", 2,  "cloth"),
        ("Shadow Token",          "accesory", 2,  "leather"),
        ("Student's Pin",         "accesory", 2,  "cloth"),
        ("Animal Claw",           "accesory", 2,  "leather"),
        # T2
        ("Pocket Compass",        "accesory", 5,  "cloth"),
        ("Sheriff's Badge",       "accesory", 5,  "leather"),
        ("Lucky Clover",          "accesory", 5,  "leather"),
        ("Elixir Vial",           "accesory", 5,  "cloth"),
        ("Iron Ring",             "accesory", 5,  "plate"),
        ("Guard's Insignia",      "accesory", 5,  "plate"),
        ("Spirit Pendant",        "accesory", 5,  "cloth"),
        ("Assassin's Mark",       "accesory", 5,  "leather"),
        ("Scholar's Pin",         "accesory", 5,  "cloth"),
        ("Beast Fang",            "accesory", 5,  "leather"),
        # T3
        ("Gear Token",            "accesory", 9,  "cloth"),
        ("Marksman's Badge",      "accesory", 9,  "leather"),
        ("Journey Stone",         "accesory", 9,  "leather"),
        ("Alchemist's Seal",      "accesory", 9,  "cloth"),
        ("Warrior's Band",        "accesory", 9,  "plate"),
        ("Sentinel's Medal",      "accesory", 9,  "plate"),
        ("Rune Pendant",          "accesory", 9,  "cloth"),
        ("Shadow Seal",           "accesory", 9,  "leather"),
        ("Research Medal",        "accesory", 9,  "cloth"),
        ("Pack Fang",             "accesory", 9,  "leather"),
        # T4
        ("Clockwork Charm",       "accesory", 14, "cloth"),
        ("Bounty Medal",          "accesory", 14, "leather"),
        ("Explorer's Charm",      "accesory", 14, "leather"),
        ("Mystic Vial",           "accesory", 14, "cloth"),
        ("Steel Ring",            "accesory", 14, "plate"),
        ("Vanguard's Medal",      "accesory", 14, "plate"),
        ("Mystic Pendant",        "accesory", 14, "cloth"),
        ("Phantom Seal",          "accesory", 14, "leather"),
        ("Academic Medal",        "accesory", 14, "cloth"),
        ("Alpha Fang",            "accesory", 14, "leather"),
        # T5
        ("Steam Cog",             "accesory", 20, "cloth"),
        ("Outlaw's Star",         "accesory", 20, "leather"),
        ("Pathfinder's Stone",    "accesory", 20, "leather"),
        ("Grand Vial",            "accesory", 20, "cloth"),
        ("Knight's Ring",         "accesory", 20, "plate"),
        ("Defender's Emblem",     "accesory", 20, "plate"),
        ("Arcane Pendant",        "accesory", 20, "cloth"),
        ("Night Seal",            "accesory", 20, "leather"),
        ("Professor's Medal",     "accesory", 20, "cloth"),
        ("Elder Fang",            "accesory", 20, "leather"),
        # T6
        ("Precision Cog",         "accesory", 28, "cloth"),
        ("Marshal's Star",        "accesory", 28, "leather"),
        ("Wayfarer's Charm",      "accesory", 28, "leather"),
        ("Arcane Vial",           "accesory", 28, "cloth"),
        ("Champion's Ring",       "accesory", 28, "plate"),
        ("Fortress Emblem",       "accesory", 28, "plate"),
        ("Elder Rune",            "accesory", 28, "cloth"),
        ("Void Seal",             "accesory", 28, "leather"),
        ("Grand Medal",           "accesory", 28, "cloth"),
        ("Alpha Claw",            "accesory", 28, "leather"),
        # T7
        ("Gear Core",             "accesory", 38, "cloth"),
        ("Desperado's Star",      "accesory", 38, "leather"),
        ("Trailblazer's Stone",   "accesory", 38, "leather"),
        ("Philosopher's Vial",    "accesory", 38, "cloth"),
        ("Templar's Ring",        "accesory", 38, "plate"),
        ("Citadel Emblem",        "accesory", 38, "plate"),
        ("Ethereal Rune",         "accesory", 38, "cloth"),
        ("Specter's Mark",        "accesory", 38, "leather"),
        ("Mastermind's Medal",    "accesory", 38, "cloth"),
        ("Spirit Claw",           "accesory", 38, "leather"),
        # T8
        ("Gravity Core",          "accesory", 50, "cloth"),
        ("Legend's Badge",        "accesory", 50, "leather"),
        ("Legendary Stone",       "accesory", 50, "leather"),
        ("Grand Alchemist's Vial","accesory", 50, "cloth"),
        ("Warlord's Ring",        "accesory", 50, "plate"),
        ("Bastion Emblem",        "accesory", 50, "plate"),
        ("Celestial Rune",        "accesory", 50, "cloth"),
        ("Dark Seal",             "accesory", 50, "leather"),
        ("Grand Scholar's Medal", "accesory", 50, "cloth"),
        ("Apex Claw",             "accesory", 50, "leather"),
        # T9
        ("Neural Core",           "accesory", 65, "cloth"),
        ("Myth Badge",            "accesory", 65, "leather"),
        ("Ancient Stone",         "accesory", 65, "leather"),
        ("Cosmic Vial",           "accesory", 65, "cloth"),
        ("Dragon Ring",           "accesory", 65, "plate"),
        ("Citadel Crest",         "accesory", 65, "plate"),
        ("Divine Rune",           "accesory", 65, "cloth"),
        ("Phantom Mark",          "accesory", 65, "leather"),
        ("Omniscient Medal",      "accesory", 65, "cloth"),
        ("Elder Spirit Claw",     "accesory", 65, "leather"),
        # T10
        ("Omega Core",            "accesory", 82, "cloth"),
        ("Legend's Medallion",    "accesory", 82, "leather"),
        ("Explorer's Relic",      "accesory", 82, "leather"),
        ("Philosopher's Stone",   "accesory", 82, "cloth"),
        ("Legendary Ring",        "accesory", 82, "plate"),
        ("Aegis Crest",           "accesory", 82, "plate"),
        ("Cosmic Pendant",        "accesory", 82, "cloth"),
        ("Dark Assassin's Seal",  "accesory", 82, "leather"),
        ("Oracle's Medal",        "accesory", 82, "cloth"),
        ("Apex Predator's Fang",  "accesory", 82, "leather"),
    ]
    return [_eq(i, name, slot, rating, eq_type) for i, (name, slot, rating, eq_type) in enumerate(raw)]


def _build_dungeons(equipment_catalog):
    # Slot bases match the 100-item blocks in the catalog
    H, C, P, S, A = 0, 100, 200, 300, 400

    def tier_loot(t):
        return [
            equipment_catalog[base + (t - 1) * 10 + job]["id"]
            for base in [H, C, P, S, A]
            for job in range(10)
        ]

    return [
        {
            "id": 1, "name": "Primeval Dense Forest",
            "description": "Vast woodland of ancient trees, narrow rivers and mist-covered clearings.",
            "image_path": "/localizations/forest_1.png",
            "rating": 0, "min_rating": 0, "visibility_rating": 0, "duration": 60,
            "loot": tier_loot(1),
        },
        {
            "id": 2, "name": "The Infinite Observation Tower",
            "description": "Colossal vertical structure that pierces the clouds and vanishes into the sky.",
            "image_path": "/localizations/tower_2.png",
            "rating": 50, "min_rating": 24, "visibility_rating": 0, "duration": 210,
            "loot": tier_loot(2),
        },
        {
            "id": 3, "name": "Canyon of Eternal Storms",
            "description": "Deep rocky rift with sheer walls and violent air currents.",
            "image_path": "/localizations/canyon_3.png",
            "rating": 125, "min_rating": 60, "visibility_rating": 24, "duration": 600,
            "loot": tier_loot(3),
        },
        {
            "id": 4, "name": "Archipelago of Wandering Clouds",
            "description": "Collection of floating islands suspended above a sea of clouds.",
            "image_path": "/localizations/archipelago_4.png",
            "rating": 225, "min_rating": 108, "visibility_rating": 60, "duration": 1500,
            "loot": tier_loot(4),
        },
        {
            "id": 5, "name": "Abyssal Steam Pit",
            "description": "Enormous geothermal rift descending into the earth's crust.",
            "image_path": "/localizations/pit_5.png",
            "rating": 350, "min_rating": 168, "visibility_rating": 108, "duration": 3000,
            "loot": tier_loot(5),
        },
        {
            "id": 6, "name": "Sunken Bronze City",
            "description": "Ruins of an ancient technological metropolis beneath dense, dark waters.",
            "image_path": "/localizations/sunken_6.png",
            "rating": 500, "min_rating": 240, "visibility_rating": 168, "duration": 5400,
            "loot": tier_loot(6),
        },
        {
            "id": 7, "name": "Isle of the Fallen Engineers",
            "description": "Rocky island overrun by abandoned factories and ruined laboratories.",
            "image_path": "/localizations/engineers_7.png",
            "rating": 700, "min_rating": 336, "visibility_rating": 240, "duration": 9900,
            "loot": tier_loot(7),
        },
        {
            "id": 8, "name": "Resonant Crystal Desert",
            "description": "Vast expanse of dunes formed by fragments of translucent crystal.",
            "image_path": "/localizations/desert_8.png",
            "rating": 950, "min_rating": 456, "visibility_rating": 336, "duration": 14400,
            "loot": tier_loot(8),
        },
        {
            "id": 9, "name": "Airship Graveyard",
            "description": "Plains covered by the wreckage of crashed zeppelins and airships.",
            "image_path": "/localizations/graveyard_9.png",
            "rating": 1250, "min_rating": 600, "visibility_rating": 456, "duration": 21600,
            "loot": tier_loot(9),
        },
        {
            "id": 10, "name": "Etherized Caldera Volcano",
            "description": "Active volcano with a wide caldera surrounded by lava flows.",
            "image_path": "/localizations/volcano_10.png",
            "rating": 1625, "min_rating": 780, "visibility_rating": 600, "duration": 32400,
            "loot": tier_loot(10),
        },
        {
            "id": 11, "name": "Ether Core",
            "description": "Colossal cavity at the planet's core where the world's energy converges.",
            "image_path": "/localizations/core_11.png",
            "rating": 2050, "min_rating": 984, "visibility_rating": 780, "duration": 43200,
            "loot": [],
        },
    ]


# ---------------------------------------------------------------------------
# Public: build_seed()
# ---------------------------------------------------------------------------

def build_seed() -> dict:
    """
    Returns a complete, isolated session state dict for a new demo session.
    The returned dict is the root state stored in DemoStore._sessions[sid].
    """
    import copy

    equipment_catalog = _build_equipment_catalog()
    dungeons = _build_dungeons(equipment_catalog)
    jobs = copy.deepcopy(JOBS)

    # Equipment IDs for each character (T1 tier, matching job armor type)
    # job_index order: eng=0, gun=1, adv=2, alc=3, war=4, fen=5, sag=6, thi=7, sch=8, bst=9
    # Slot offsets: head=0, chest=100, primary=200, secondary=300, accesory=400
    # Within slot+tier: items 0-9 map to jobs 0-9
    # Firion   = warrior  (job_index=4) → plate
    # Sabin    = alchemist(job_index=3) → cloth
    # Balthier = engineer (job_index=0) → cloth
    # Locke    = adventurer(job_index=2)→ leather

    char_job_indexes = {1: 4, 2: 3, 3: 0, 4: 2}  # char_id → job_index in T1

    inventory = []
    character_equipment = []
    inv_id = 1
    ce_id = 1

    SLOTS_OFFSETS = [0, 100, 200, 300, 400]
    SLOT_NAMES = ["head", "chest", "primary_hand", "secondary_hand", "accesory"]

    for char_id, job_idx in char_job_indexes.items():
        for slot_offset, slot_name in zip(SLOTS_OFFSETS, SLOT_NAMES):
            eq_index = slot_offset + job_idx  # 0-based index in catalog (tier 1)
            eq_id = equipment_catalog[eq_index]["id"]

            inventory.append({"id": inv_id, "equipment_id": eq_id})
            character_equipment.append({
                "id": ce_id,
                "character_id": char_id,
                "slot": slot_name,
                "inventory_id": inv_id,
            })
            inv_id += 1
            ce_id += 1

    # Extra unequipped T2 items in inventory (one per slot per character type)
    # So users can immediately try equipping better gear
    for job_idx in [4, 3, 0, 2]:  # warrior, alchemist, engineer, adventurer
        for slot_offset in SLOTS_OFFSETS:
            eq_index = slot_offset + 10 + job_idx  # tier 2 = offset + 10
            eq_id = equipment_catalog[eq_index]["id"]
            inventory.append({"id": inv_id, "equipment_id": eq_id})
            inv_id += 1

    return {
        "user": {
            "id": None,  # filled in by DemoStore.create_session
            "username": "demo_visitor",
            "email": "demo@demo.com",
        },
        "party": {
            "id": 1,
            "name": "Heroes Party",
            "level": 1,
            "experience": 0,
        },
        "characters": [
            {"id": 1, "name": "Firion",   "job_id": 5, "party_id": 1},
            {"id": 2, "name": "Sabin",    "job_id": 4, "party_id": 1},
            {"id": 3, "name": "Balthier", "job_id": 1, "party_id": 1},
            {"id": 4, "name": "Locke",    "job_id": 3, "party_id": 1},
        ],
        "jobs": jobs,
        "equipment_catalog": equipment_catalog,
        "dungeons": dungeons,
        "inventory": inventory,
        "character_equipment": character_equipment,
        "exploration": None,
        "_next_inventory_id": inv_id,
        "_next_ce_id": ce_id,
    }
