# 1st Party Libraries
from app.controllers.home_controller import home_blueprint

# Registro de rutas
def path_registration(app):
    app.register_blueprint(home_blueprint)