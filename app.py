# 1st Party Libraries
from app import create_app
from app.controllers.api import api
from app.config.config import Config

# Inicializar la configuracion de la app
app = create_app(Config)
app.register_blueprint(api)

# Ejecución del programa en Railway
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', threaded = True)

# Ejecución del programa en local
# if __name__ == '__main__':
#     app.run(debug = True, host = '127.0.0.1', port = 5500, threaded = True)