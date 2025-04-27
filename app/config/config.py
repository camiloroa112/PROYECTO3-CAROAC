# 1st Party Libraries
from .settings import user, password

# 3rd Party Libraries
import os
from dotenv import load_dotenv

# Cargar el .env
load_dotenv(override = True)

class Config:
    """Colocación de las credenciales en variables para acceder a la base tablas."""

    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')