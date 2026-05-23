from flask import request, jsonify, g
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.auth_service import ServiceError
from app.services.inventory_service import get_inventory, equip_from_inventory, delete_inventory_item


@jwt_required()
def get_inventory_handler():
    user_id = get_jwt_identity()

    if g.get("is_demo"):
        from app.demo.demo_services import demo_get_inventory
        try:
            return jsonify(demo_get_inventory(g.demo_session_id)), 200
        except ServiceError as e:
            return jsonify({"error": str(e)}), e.status_code

    try:
        result = get_inventory(user_id)
        return jsonify(result), 200
    except ServiceError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


@jwt_required()
def equip_from_inventory_handler(inventory_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    character_id = data.get("character_id")
    slot = data.get("slot")

    if not character_id or not slot:
        return jsonify({"error": "character_id and slot are required"}), 400

    if g.get("is_demo"):
        from app.demo.demo_services import demo_equip_from_inventory
        try:
            demo_equip_from_inventory(g.demo_session_id, inventory_id, character_id, slot)
            return jsonify({"message": "Item equipped from inventory"}), 200
        except ServiceError as e:
            return jsonify({"error": str(e)}), e.status_code

    try:
        equip_from_inventory(user_id, inventory_id, character_id, slot)
        return jsonify({"message": "Item equipped from inventory"}), 200
    except ServiceError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


@jwt_required()
def delete_inventory_handler(inventory_id):
    user_id = get_jwt_identity()
    data = request.get_json(silent=True) or {}
    force = bool(data.get("force", False))

    if g.get("is_demo"):
        from app.demo.demo_services import demo_delete_inventory_item
        try:
            demo_delete_inventory_item(g.demo_session_id, inventory_id, force=force)
            return jsonify({"message": "Item deleted"}), 200
        except ServiceError as e:
            return jsonify({"error": str(e)}), e.status_code

    try:
        delete_inventory_item(user_id, inventory_id, force=force)
        return jsonify({"message": "Item deleted"}), 200
    except ServiceError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception:
        return jsonify({"error": "Internal server error"}), 500
