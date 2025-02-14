from models.User import User
from flask import jsonify
from config import db

def get_all_users():
    try:
        return [ user.to_dict() for user in User.query.all()]    
    except Exception as error:
        print(f"ERROR {error}")

def create_user(name, email):
    try:
        new_user = User(name, email)
    
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict()

    except Exception as e:
        print(f"ERROR {e}")

def update_user(user_id, name=None, email=None):
    try:
        user = User.query.get(user_id)
        if not user:
            return None

        if name:
            user.name = name
        if email:
            user.email = email

        db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")

def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return None

        db.session.delete(user)
        db.session.commit()
        return {"message": "usuairo eliminado"}
    except Exception as e:
        print(f"ERROR {e}")