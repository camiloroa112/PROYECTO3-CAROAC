# 1st Party Libraries
from app.config.db import db

# 3rd Party Libraries
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    """Especifica los atributos que conforman el modelo de Usuario para dar inicio de sesión."""
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    is_admin = db.Column(db.Integer, nullable = False)
    is_employee = db.Column(db.Integer, nullable = False)