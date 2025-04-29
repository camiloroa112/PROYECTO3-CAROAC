# 1st Party Libraries
from app.models.usuario import Usuario

# 3rd Party libraries
import atexit
from flask import Flask
from app.config.db import db
from app.config.auth import login_manager
from app.config.routes import path_registration

def create_app(config) -> Flask:
    """Se crea un objeto de tipo Flask y se configuran sus distintos modulos, caracteristicas y conexiones."""
    
    # Instanciar Flask
    app = Flask(__name__, template_folder = 'views')
    app.config.from_object(config)

    # Inicialización de la App
    db.init_app(app)

    # Inicialización de Login
    login_manager.init_app(app)

    # Inicialización del registro de rutas
    path_registration(app)

    # Al momento de la activación de la app
    with app.app_context():

        # Creación de bases de datos
        db.create_all()

        # Limpiar tabla de usuarios
        db.session.query(Usuario).delete()
        db.session.commit()

        # # Instanciar usuarios
        # user1 = Usuario(username = 'camilor123', password = 'Camilor123', is_admin = 1, is_employee = 0)
        # user2 = Usuario(username = 'fulanitodetal1', password = 'Fulano123', is_admin = 0, is_employee = 1)
        # user3 = Usuario(username = 'david99', password = 'David99', is_admin = 1, is_employee = 0)
        # user4 = Usuario(username = 'humbert', password = 'Humbert71', is_admin = 0, is_employee = 0)
        
        # # Agregar usuarios a la base
        # db.session.add_all([user1, user2, user3, user4])

        # # Guardar cambios
        # db.session.commit()
    
    # Eliminación de registros al cierre de la aplicación
    def clean_tables():
        with app.app_context():
            db.session.query(Usuario).delete()
            db.session.commit()
    
    # Registro de funciones de limpieza
    atexit.register(clean_tables)

    # Utilizado para ser ejecutado en app.py
    return app