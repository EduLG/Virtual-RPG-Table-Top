from flask import request, jsonify, g
from flask_jwt_extended import jwt_required

from app.services.auth_service import ServiceError
from app.services.equipment_service import get_equipment_by_type


@jwt_required()
def get_equipment_by_type_handler():
    equipment_type = request.args.get("equipment_type")

    if g.get("is_demo"):
        from app.demo.demo_services import demo_get_equipment_by_type
        try:
            return jsonify(demo_get_equipment_by_type(g.demo_session_id, equipment_type)), 200
        except ServiceError as e:
            return jsonify({"error": str(e)}), e.status_code

    try:
        result = get_equipment_by_type(equipment_type)
        return jsonify(result), 200
    except ServiceError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception:
        return jsonify({"error": "Internal server error"}), 500
