from config import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, last_name, password):
        self.name = name
        self.email = email
        self.last_name = last_name
        self.password = generate_password_hash(password)  # Generamos el hash de la contraseña en el __init__

    def check_password(self, password):
        """Verifica si la contraseña proporcionada es correcta"""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Devuelve un diccionario con los campos del usuario, excluyendo la contraseña"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "last_name": self.last_name,
        }
