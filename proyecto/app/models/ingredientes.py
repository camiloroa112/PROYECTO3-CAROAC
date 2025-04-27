# 1st Party Libraries
from app.config.db import db

# Class para crear el modelo de ingrediente
class ingredientes(db.Model):
    """Especifican los atributos que conforman el modelo en SQLAlchemy de: ingredientes."""
    
    # Nombre de la tabla en Heladeria
    __tablename__ = 'ingredientes'
    # ID Ingrediente
    id = db.Column(db.Integer, primary_key = True)
    # Nombre del ingrediente
    nombre = db.Column(db.String(50), nullable = False)
    # Precio del ingrediente
    precio = db.Column(db.Float, nullable = False)
    # Calorias ingrediente
    calorias = db.Column(db.Integer, nullable = False)
    # Inventario ingrediente
    inventario = db.Column(db.Integer, nullable = False)
    # Valor booleano de un ingrediente conociendo si es vegetariano o no
    es_vegetariano = db.Column(db.Boolean, nullable = False)
    # Sabor
    sabor = db.Column(db.String(10), nullable = True)
    # Tipo
    tipo = db.Column(db.String(11), nullable = False)