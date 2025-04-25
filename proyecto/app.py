# 1st Party Libraries
from app import create_app
from app.config.config import Config
from app.controllers.api import api

# Inicializar la configuracion de la app
app = create_app(Config)
app.register_blueprint(api)

# Ejecución del programa
if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5500, threaded = True)