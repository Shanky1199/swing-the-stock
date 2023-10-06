from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        # Extract data from request
        # ...
        
        # Call the service function
        user, error_message = UserService.create_user(data)

        if user:
            return jsonify({"message": "User registered successfully"}), 201
        else:
            return jsonify({"message": error_message}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
