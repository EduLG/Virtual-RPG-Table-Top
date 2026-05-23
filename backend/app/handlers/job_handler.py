from flask import jsonify, g
from flask_jwt_extended import jwt_required

from app.services.auth_service import ServiceError
from app.services.job_service import get_jobs


@jwt_required()
def get_jobs_handler():
    if g.get("is_demo"):
        from app.demo.demo_services import demo_get_jobs
        try:
            return jsonify(demo_get_jobs(g.demo_session_id)), 200
        except ServiceError as e:
            return jsonify({"error": str(e)}), e.status_code

    try:
        result = get_jobs()
        return jsonify(result), 200
    except ServiceError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception:
        return jsonify({"error": "Internal server error"}), 500
