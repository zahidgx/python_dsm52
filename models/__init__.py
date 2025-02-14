from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .User import User  
from config import db