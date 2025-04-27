# 1st Party Libraries
from .settings import user, password

# 3rd Party Libraries
from pathlib import Path
from dotenv import load_dotenv, dotenv_values

# Cargar el .env
load_dotenv(override=True)

# Setting Path where the file is located
env_path = Path('.env').resolve()

# Reading .env file
env_vars = dotenv_values(dotenv_path=env_path)

# Placing info into a dictionary
env_credentials = {key: value for key, value in env_vars.items()}

class Config:
    """Colocación de las credenciales en variables para acceder a la base tablas."""

    SECRET_KEY = env_credentials['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = env_credentials['SQLALCHEMY_DATABASE_URI'] + f'{user}:{password}@localhost:3306/heladeria'