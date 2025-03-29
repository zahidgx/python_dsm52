from models.User import User
from flask import jsonify
from config import db
from flask_jwt_extended import create_access_token

# Función para obtener todos los usuarios
def get_all_users():
    users = User.query.all()
    return [{"id": user.id, "name": user.name, "email": user.email, "last_name": user.last_name, "password":user.password} for user in users]

# Función para obtener un usuario por ID
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return {"id": user.id, "name": user.name, "email": user.email, "last_name": user.last_name, "password":user.password}
    return None

# Función para crear un nuevo usuario
def create_user(name, email, last_name, password):
    new_user = User(name=name, email=email, last_name=last_name, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email, "last_name": new_user.last_name, "password":new_user.password}

# Función para actualizar un usuario
def update_user(user_id, name, email, last_name, password):
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.email = email
        user.last_name = last_name
        user.password = password
        db.session.commit()
        return {"id": user.id, "name": user.name, "email": user.email, "last_name": user.last_name, "password":user.password}
    return None

# Función para eliminar un usuario
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}
    return None

def login_user(email, password):
    user = User.query.filter_by(email = email).first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user' : {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "last_name" : user.last_name,
            }
        })
    return jsonify ({ "msg" : "Credenciales invalidas"}), 401


        

