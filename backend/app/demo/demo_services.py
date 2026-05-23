"""
Demo service layer — operates on DemoStore, never touches the DB.
Each function returns the same dict/list structures that the real
Marshmallow schemas would produce, so handlers stay unchanged.
"""

import random
from datetime import datetime, timedelta, timezone

from app.demo.demo_store import demo_store
from app.services.auth_service import ServiceError
from app.models.equipment import JOB_ARMOR_TYPE


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _s(session_id: str) -> dict:
    """Fetch session or raise 401."""
    sess = demo_store.get_session(session_id)
    if sess is None:
        raise ServiceError("Demo session expired or not found", 401)
    return sess


def _by_id(lst: list, id_val: int):
    return next((x for x in lst if x["id"] == id_val), None)


def _eq_for_inventory(s: dict, inv_item: dict) -> dict | None:
    return _by_id(s["equipment_catalog"], inv_item["equipment_id"])


def _ce_for_inventory(s: dict, inventory_id: int) -> dict | None:
    return next((ce for ce in s["character_equipment"] if ce["inventory_id"] == inventory_id), None)


def _char_rating(s: dict, char: dict) -> int:
    total = 0
    for ce in s["character_equipment"]:
        if ce["character_id"] != char["id"]:
            continue
        inv = _by_id(s["inventory"], ce["inventory_id"])
        if not inv:
            continue
        eq = _eq_for_inventory(s, inv)
        if eq:
            total += eq["rating"]
    return total


def _serialize_eq(eq: dict) -> dict:
    return {
        "id": eq["id"],
        "name": eq["name"],
        "slot": eq["slot"],
        "rating": eq["rating"],
        "equipment_type": eq["equipment_type"],
    }


def _serialize_character(s: dict, char: dict) -> dict:
    job = _by_id(s["jobs"], char["job_id"])
    equipped_items = []
    for ce in s["character_equipment"]:
        if ce["character_id"] != char["id"]:
            continue
        inv = _by_id(s["inventory"], ce["inventory_id"])
        if not inv:
            continue
        eq = _eq_for_inventory(s, inv)
        if not eq:
            continue
        equipped_items.append({
            "slot": ce["slot"],
            "inventory_id": ce["inventory_id"],
            "equipment": _serialize_eq(eq),
        })
    return {
        "id": char["id"],
        "name": char["name"],
        "current_job": {"id": job["id"], "name": job["name"], "icon": job["icon"]} if job else None,
        "equipped_items": equipped_items,
        "rating": _char_rating(s, char),
    }


def _party_rating(s: dict) -> int:
    return sum(_char_rating(s, c) for c in s["characters"])


# ---------------------------------------------------------------------------
# User profile
# ---------------------------------------------------------------------------

def demo_get_user_profile(session_id: str) -> dict:
    s = _s(session_id)
    party = s["party"]
    characters = [c for c in s["characters"] if c["party_id"] == party["id"]]
    return {
        "id": s["user"]["id"],
        "username": s["user"]["username"],
        "email": s["user"]["email"],
        "party": {
            "id": party["id"],
            "name": party["name"],
            "level": party["level"],
            "experience": party["experience"],
            "rating": _party_rating(s),
            "characters": [_serialize_character(s, c) for c in characters],
        },
    }


# ---------------------------------------------------------------------------
# Jobs
# ---------------------------------------------------------------------------

def demo_get_jobs(session_id: str) -> list:
    s = _s(session_id)
    return [{"id": j["id"], "name": j["name"], "icon": j["icon"]} for j in s["jobs"]]


# ---------------------------------------------------------------------------
# Equipment catalog
# ---------------------------------------------------------------------------

def demo_get_equipment_by_type(session_id: str, equipment_type: str) -> list:
    if not equipment_type:
        raise ServiceError("equipment_type is required", 400)
    s = _s(session_id)
    return [_serialize_eq(e) for e in s["equipment_catalog"] if e["equipment_type"] == equipment_type]


# ---------------------------------------------------------------------------
# Inventory
# ---------------------------------------------------------------------------

def demo_get_inventory(session_id: str) -> list:
    s = _s(session_id)
    result = []
    for inv in s["inventory"]:
        eq = _eq_for_inventory(s, inv)
        ce = _ce_for_inventory(s, inv["id"])
        result.append({
            "id": inv["id"],
            "equipment": _serialize_eq(eq) if eq else None,
            "equipped": ce is not None,
        })
    return result


def demo_equip_from_inventory(session_id: str, inventory_id: int, character_id: int, slot: str) -> None:
    s = _s(session_id)

    inv = _by_id(s["inventory"], inventory_id)
    if not inv:
        raise ServiceError("Inventory item not found", 404)

    if _ce_for_inventory(s, inventory_id) is not None:
        raise ServiceError("Item is already equipped", 409)

    char = _by_id(s["characters"], character_id)
    if not char or char["party_id"] != s["party"]["id"]:
        raise ServiceError("Character not found", 404)

    eq = _eq_for_inventory(s, inv)
    if not eq:
        raise ServiceError("Equipment not found", 404)

    job = _by_id(s["jobs"], char["job_id"])
    if not job:
        raise ServiceError("Job not found", 404)

    expected_type = JOB_ARMOR_TYPE.get(job["name"])
    if eq["equipment_type"] != expected_type:
        raise ServiceError("Equipment is not compatible with this character's job", 400)

    # If slot already occupied, unequip the old item first
    existing = next(
        (ce for ce in s["character_equipment"] if ce["character_id"] == character_id and ce["slot"] == slot),
        None,
    )
    if existing:
        s["character_equipment"].remove(existing)

    new_id = s["_next_ce_id"]
    s["_next_ce_id"] += 1
    s["character_equipment"].append({
        "id": new_id,
        "character_id": character_id,
        "slot": slot,
        "inventory_id": inventory_id,
    })


def demo_delete_inventory_item(session_id: str, inventory_id: int, force: bool = False) -> None:
    s = _s(session_id)

    inv = _by_id(s["inventory"], inventory_id)
    if not inv:
        raise ServiceError("Inventory item not found", 404)

    ce = _ce_for_inventory(s, inventory_id)
    if ce is not None and not force:
        raise ServiceError("Item is equipped by a character", 409)
    if ce is not None:
        s["character_equipment"].remove(ce)

    s["inventory"].remove(inv)


# ---------------------------------------------------------------------------
# Dungeons & exploration
# ---------------------------------------------------------------------------

def demo_get_dungeons(session_id: str) -> list:
    s = _s(session_id)
    party_rating = _party_rating(s)
    visible = [d for d in s["dungeons"] if d["visibility_rating"] <= party_rating]
    return [
        {
            "id": d["id"], "name": d["name"], "description": d["description"],
            "image_path": d["image_path"], "rating": d["rating"],
            "min_rating": d["min_rating"], "visibility_rating": d["visibility_rating"],
            "duration": d["duration"],
        }
        for d in visible
    ]


def demo_explore_dungeon(session_id: str, dungeon_id: int) -> dict:
    s = _s(session_id)

    if s["exploration"] and s["exploration"]["status"] == "in_progress":
        raise ServiceError("Party is already on an exploration", 409)

    dungeon = _by_id(s["dungeons"], dungeon_id)
    if not dungeon:
        raise ServiceError("Dungeon not found", 404)

    party_rating = _party_rating(s)
    if party_rating < dungeon["visibility_rating"]:
        raise ServiceError("Dungeon not yet discovered", 403)

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    ends_at = now + timedelta(seconds=dungeon["duration"])

    s["exploration"] = {
        "dungeon_id": dungeon_id,
        "started_at": now,
        "ends_at": ends_at,
        "status": "in_progress",
        "result": None,
    }

    return {
        "status": "in_progress",
        "ends_at": ends_at.isoformat() + "Z",
        "dungeon_name": dungeon["name"],
    }


def demo_get_exploration_status(session_id: str) -> dict:
    s = _s(session_id)
    exploration = s["exploration"]

    if not exploration or exploration["status"] != "in_progress":
        return {"status": "idle"}

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    dungeon = _by_id(s["dungeons"], exploration["dungeon_id"])

    if now < exploration["ends_at"]:
        return {
            "status": "in_progress",
            "ends_at": exploration["ends_at"].isoformat() + "Z",
            "dungeon_name": dungeon["name"] if dungeon else "",
        }

    return _resolve_demo_exploration(s, exploration, dungeon)


def _resolve_demo_exploration(s: dict, exploration: dict, dungeon: dict) -> dict:
    party_rating = _party_rating(s)
    success, n_items = _resolve_outcome(party_rating, dungeon["min_rating"], dungeon["rating"])

    loot = []
    if success:
        loot_ids = dungeon.get("loot") or []
        sample_ids = random.sample(loot_ids, min(n_items, len(loot_ids)))
        for eq_id in sample_ids:
            eq = _by_id(s["equipment_catalog"], eq_id)
            if eq:
                new_inv_id = s["_next_inventory_id"]
                s["_next_inventory_id"] += 1
                s["inventory"].append({"id": new_inv_id, "equipment_id": eq_id})
                loot.append(_serialize_eq(eq))

    exploration["status"] = "completed"
    exploration["result"] = {"success": success, "loot": loot}

    return {
        "status": "completed",
        "dungeon_name": dungeon["name"],
        "success": success,
        "loot": loot,
    }


def _resolve_outcome(party_rating: int, min_rating: int, dungeon_rating: int) -> tuple[bool, int]:
    if min_rating == 0:
        if party_rating < 10:  return True, 2
        if party_rating < 24:  return True, 3
        if party_rating < 48:  return True, 4
        return True, 5
    if dungeon_rating == 0:
        return True, 1
    ratio = party_rating / dungeon_rating
    if ratio < 0.60: return False, 0
    if ratio < 1.00: return True, 1
    if ratio < 1.17: return True, 2
    if ratio < 1.34: return True, 3
    if ratio < 1.50: return True, 4
    return True, 5


# ---------------------------------------------------------------------------
# Party setup
# ---------------------------------------------------------------------------

def demo_setup_party(session_id: str, party_name: str, characters_data: list) -> None:
    s = _s(session_id)

    party_name = (party_name or "").strip()
    if not party_name:
        raise ServiceError("Party name is required", 400)
    if len(characters_data) != 4:
        raise ServiceError("Exactly 4 characters are required", 400)

    new_characters = []
    for i, char_data in enumerate(characters_data):
        name = (char_data.get("name") or "").strip()
        job_id = char_data.get("job_id")
        if not name:
            raise ServiceError("All characters must have a name", 400)
        if not job_id:
            raise ServiceError("All characters must have a job", 400)
        job = _by_id(s["jobs"], job_id)
        if not job:
            raise ServiceError(f"Job {job_id} not found", 404)
        new_characters.append({"id": i + 1, "name": name, "job_id": job_id, "party_id": 1})

    # Reset mutable state
    s["party"]["name"] = party_name
    s["characters"] = new_characters
    s["inventory"] = []
    s["character_equipment"] = []
    s["exploration"] = None
    s["_next_inventory_id"] = 1
    s["_next_ce_id"] = 1
