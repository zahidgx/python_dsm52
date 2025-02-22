from flask import Blueprint, jsonify, request
from models import db, User
from controllers.userController import get_all_users, create_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()
    if isinstance(users, tuple):
        return jsonify(users[0]), users[1] 
    return jsonify(users) 

@user_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')
    
    if not name or not last_name or not email:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_user = create_user(name, email, last_name)
    return jsonify(new_user)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')
    
    updated_user = update_user(user_id, name, email, last_name)
    return jsonify(updated_user)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    deleted_user = delete_user(user_id)
    return jsonify(deleted_user)
