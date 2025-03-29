from flask import Blueprint, jsonify, request
from models import db, User
from controllers.userController import get_all_users, create_user, update_user, delete_user, get_user_by_id,login_user

user_bp = Blueprint('users', __name__)

# Ruta para obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()
    if isinstance(users, tuple):
        return jsonify(users[0]), users[1]
    return jsonify(users)

# Ruta para crear un nuevo usuario
@user_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')
    password = data.get('password')
    
    if not name or not last_name or not email:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_user = create_user(name, email, last_name, password)
    return jsonify(new_user), 201

# Ruta para obtener un usuario por ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def user_show(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Ruta para actualizar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    last_name = data.get('last_name')
    password = data.get('password')
    
    updated_user = update_user(user_id, name, email, last_name, password)
    if updated_user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(updated_user)

# Ruta para eliminar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    deleted_user = delete_user(user_id)
    if deleted_user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 204

@user_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    return login_user(data['email'], data['password'])

