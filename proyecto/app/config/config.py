# 1st Party Libraries
from .settings import user, password

# 3rd Party Libraries
from pathlib import Path
from dotenv import load_dotenv
from dotenv import dotenv_values

# Obtención valores de las variables en el archivo .env
load_dotenv(override = True)

# Setting Path where the file is located
env_path = Path(__file__).resolve().parents[2] / ".env"

# Reading .env file
env_vars = dotenv_values(dotenv_path = env_path)

# Placing info into a dictionary
env_credentials = {key:value for key, value in env_vars.items()}

class Config:
    """Colocación de las credenciales en variables para acceder a la base tablas."""
    
    # Obtaining Secret_Key
    SECRET_KEY = env_credentials['SECRET_KEY']

    # Reading DB
    SQLALCHEMY_DATABASE_URI = env_credentials['SQLALCHEMY_DATABASE_URI'] + f'{user}:{password}@localhost:3306/heladeria'