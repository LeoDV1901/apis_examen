from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    """Obtenemos todos los usuarios."""
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/', methods=['POST'])
def user_store():
    """Creamos un nuevo usuario."""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')

    new_user = create_user(name, email, last_name)
    return jsonify(new_user)

@user_bp.route('/<int:id>', methods=['PUT'])
def user_update(id):
    """Actualizamos un usuario existente."""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')

    updated_user = update_user(id, name, email, last_name)
    if updated_user:
        return jsonify(updated_user), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/<int:id>', methods=['DELETE'])
def user_delete(id):
    """Eliminamos un usuario."""
    result = delete_user(id)
    if result:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404
