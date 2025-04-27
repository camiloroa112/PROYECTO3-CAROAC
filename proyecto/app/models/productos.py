
from app.config.db import db

# Class to create the Productos Model
class productos(db.Model):
    """Especifican los atributos que conforman el modelo en SQLAlchemy de: productos."""
    
    # Nombre de la tabla en Heladeria
    __tablename__ = 'productos'
    # ID Product
    id = db.Column(db.Integer, primary_key = True) 
    # Product Name
    nombre = db.Column(db.String(50), nullable = False)
    # Volume of the product
    volumen = db.Column(db.String(8), nullable = True)
    # Ingredient ID #1
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient ID #2
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient ID #3
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient #1
    ingrediente1 = db.relationship('ingredientes', foreign_keys = [ingrediente1_id])
    # Ingredient #2
    ingrediente2 = db.relationship('ingredientes', foreign_keys = [ingrediente2_id])
    # Ingredient #3
    ingrediente3 = db.relationship('ingredientes', foreign_keys = [ingrediente3_id])
    # Public Price
    precio_publico = db.Column(db.Float, nullable = False)
    # Glass type
    tipo_vaso = db.Column(db.String(8), nullable = True)