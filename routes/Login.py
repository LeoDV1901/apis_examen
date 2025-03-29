from flask import Blueprint, request, jsonify
from controllers.loginController import login_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = login_user(email, password)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
