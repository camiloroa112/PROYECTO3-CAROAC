# 1st Party Libraries
from app import views
from app.config.db import db
from app.models.usuario import Usuario
from app.models.productos import productos
from app.models.ingredientes import ingredientes

# 3rd Party Libraries
from sqlalchemy.orm import aliased
from app.config.auth import login_manager
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

# Instanciar Blueprint
home_blueprint = Blueprint('home', __name__)

@login_manager.user_loader
def load_user(user_id: str) -> Usuario:
    # Obtiene el ID de un Registro
    return Usuario.query.get(str(user_id))

@home_blueprint.route('/')
def home():
    # Renderiza como página principal del sitio a login.html
    return render_template('login.html')

@home_blueprint.route('/acceso-login', methods = ['GET', 'POST'])
def login():
    # En caso de un método GET, presenta en un inicio la página de login en HTML
    if request.method == 'GET':
        return render_template('login.html')
    
    # Extracción de datos recopilados del formulario
    elif request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']

        # Búsqueda de un usuario
        user = Usuario.query.filter_by(username = _username, password = _password).first()

        # En caso de que se encuentre el usuario
        if user: 

            # Se inicia sesión en la página
            login_user(user)

            # Inspecciona si este es admin o no
            if user.is_admin:
                return redirect(url_for('home.index')), 200
            
            # En caso de no ser admin pero si empleado
            elif user.is_employee:
                return redirect(url_for('home.comprador')), 200
            
            # Para un usuario sin credenciales validas
            else:
                return redirect(url_for('home.no_autorizado')), 401
            
        # Informe de credenciales incorrectas
        else:
            flash("Incorrect credentials!")
            return redirect(url_for('home.no_autorizado')), 401

@home_blueprint.route('/logout')
def logout():
    # Modulo para desloguear a un usuario
    logout_user()
    return redirect(url_for('home.login')), 200

@home_blueprint.route('/index')
@login_required
def index():
    
    # Trayendo resultados del controlador
    productos_ingredientes = obtener_productos(productos, ingredientes, db)
    
    # Displaying results in index.html
    return render_template('index.html', heladeria = productos_ingredientes, user = current_user)

@home_blueprint.route('/comprador')
@login_required
def comprador():
    # Trayendo resultados del controlador
    productos_ingredientes = obtener_productos(productos, ingredientes, db)

    # Redirección a usuarios no administradores del sitio web
    return render_template('comprador.html', heladeria = productos_ingredientes, user = current_user)

@home_blueprint.route('/no-autorizado')
def no_autorizado():
    # Redirigiendo un usuario a una pagina de: No Autorizado
    return render_template('no_autorizado.html'), 401


def obtener_productos(productos, ingredientes, db) -> list[tuple]:
    """Obtiene todos los productos con sus ingredientes de la base de datos."""

    # Crear alias para cada uno de los ingredientes
    ingrediente1 = aliased(ingredientes)
    ingrediente2 = aliased(ingredientes)
    ingrediente3 = aliased(ingredientes)

    # Query para obtener los productos y sus ingredientes con los alias correspondientes
    productos_ingredientes = db.session.query(
        productos.id,
        productos.nombre,
        productos.volumen,
        productos.precio_publico,
        productos.tipo_vaso,
        ingrediente1.inventario.label('inventario1'),
        ingrediente2.inventario.label('inventario2'),
        ingrediente3.inventario.label('inventario3'),
        ingrediente1.calorias.label('calorias1'),
        ingrediente2.calorias.label('calorias2'),
        ingrediente3.calorias.label('calorias3'),
        ingrediente1.precio.label('precio1'),
        ingrediente2.precio.label('precio2'),
        ingrediente3.precio.label('precio3'),
        ingrediente1.nombre.label('ingrediente1'),
        ingrediente2.nombre.label('ingrediente2'),
        ingrediente3.nombre.label('ingrediente3')
    ).join(ingrediente1, productos.ingrediente1_id == ingrediente1.id
    ).join(ingrediente2, productos.ingrediente2_id == ingrediente2.id
    ).join(ingrediente3, productos.ingrediente3_id == ingrediente3.id).all()

    # Retornando los ingredientes disponibles en inventario
    return productos_ingredientes
