from models.User import User
from flask import jsonify
from config import db

def get_all_users():
    try:
        users = [user.to_dict() for user in User.query.all()]
        return users  
    except Exception as error:
        print(f"ERROR al obtener usuarios: {error}")
        return {"error": "Error al obtener los usuarios"}, 500


def create_user(name, email, last_name):
    try:
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "El correo electrónico ya está en uso"}), 400
        new_user = User(name, email, last_name)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        print(f"ERROR al crear usuario: {e}")
        return jsonify({"error": "Error al crear usuario"}), 500


def update_user(user_id, name=None, email=None, last_name=None): 
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        if name:
            user.name = name
        if email:
            user.email = email
        if last_name: 
            user.last_name = last_name

        db.session.commit()
        return jsonify(user.to_dict())
    except Exception as e:
        
        print(f"ERROR al actualizar usuario: {e}")
        return jsonify({"error": "Error al actualizar usuario"}), 500


def delete_user(user_id):
    try:
        
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "Usuario eliminado"}), 200
    except Exception as e:
        print(f"ERROR al eliminar usuario: {e}")
        return jsonify({"error": "Error al eliminar usuario"}), 500
