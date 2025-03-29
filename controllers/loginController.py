from models.User import User
from flask import jsonify
from config import db

# Lógica de login con email y password
def login_user(email, password):
    try:
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return user.to_dict()
        return None
    except Exception as e:
        print(f"ERROR {e}")
        return None
