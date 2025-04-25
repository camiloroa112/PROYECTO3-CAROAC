# 1st Party Libraries
from app.config.db import db

# Class to create the Ingredientes Model
class ingredientes(db.Model):
    # ID Ingredient
    id = db.Column(db.Integer, primary_key = True)
    # Ingredient Name
    nombre = db.Column(db.String(50), nullable = False)
    # Ingredient Price
    precio = db.Column(db.Float, nullable = False)
    # Ingredient Calories
    calorias = db.Column(db.Integer, nullable = False)
    # Ingredient Inventory
    inventario = db.Column(db.Integer, nullable = False)
    # Ingredient Boolean Value if its Vegetarian or not
    es_vegetariano = db.Column(db.Boolean, nullable = False)
    # Flavour
    sabor = db.Column(db.String(10), nullable = True)