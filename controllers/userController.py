from models.User import User
from config import db
from flask import jsonify

# Obtener todos los usuarios
def get_all_users():
    try:
        return [user.to_dict() for user in User.query.all()]
    except Exception as error:
        print(f"ERROR {error}")

# Crear un nuevo usuario
def create_user(name, email, last_name):
    try:
        new_user = User(name=name, email=email, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")

# Actualizar un usuario por ID
def update_user(id, name, email, last_name):
    try:
        user = User.query.get(id)
        if user:
            user.name = name
            user.email = email
            user.last_name = last_name
            db.session.commit()
            return user.to_dict()
        return None
    except Exception as e:
        print(f"ERROR {e}")

# Eliminar un usuario por ID
def delete_user(id):
    try:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    except Exception as e:
        print(f"ERROR {e}")
