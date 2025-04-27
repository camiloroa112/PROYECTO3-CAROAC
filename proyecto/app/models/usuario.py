# 1st Party Libraries
from app.config.db import db

# 3rd Party Libraries
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    """Especifica los atributos que conforman el modelo en SQLAlchemy de: Usuario para dar inicio de sesión."""

    # Nombre de la tabla en Heladeria
    __tablename__ = 'usuario'
    # Identificador unico del Usuario
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    # Nombre del usuario
    username = db.Column(db.String(255), nullable = False)
    # Contraseña
    password = db.Column(db.String(255), nullable = False)
    # Atributo que asocia si es admin o no
    is_admin = db.Column(db.Integer, nullable = False)
    # Atributo que da a conocer si es empleado o no
    is_employee = db.Column(db.Integer, nullable = False)