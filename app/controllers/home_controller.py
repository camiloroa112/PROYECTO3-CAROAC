# 1st Party Libraries
from app import views
from app.config.db import db
from app.models.usuario import Usuario
from app.models.heladeria import Heladeria
from app.models.productos import productos
from app.models.ingredientes import ingredientes
from app.models.obtener_producto import obtener_producto

# 3rd Party Libraries
from sqlalchemy import func, case
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
                return redirect(url_for('home.admin'))
            
            # En caso de no ser admin pero si empleado
            elif user.is_employee:
                return redirect(url_for('home.empleado'))
            
            # Para un usuario sin credenciales validas
            else:
                return redirect(url_for('home.cliente'))
            
        # Informe de credenciales incorrectas
        else:
            flash("Incorrect credentials!")
            return redirect(url_for('home.no_autorizado'))

@home_blueprint.route('/logout')
@login_required
def logout():
    # Modulo para desloguear a un usuario
    logout_user()
    return redirect(url_for('home.login'))

@home_blueprint.route('/admin')
@login_required
def admin():
    # En caso de que el usuario no sea administrador
    if not current_user.is_admin:
        return redirect(url_for('home.no_autorizado'))
    
    # De lo contrario
    else:
        # Trayendo resultados del controlador
        productos_ingredientes = obtener_productos(productos, ingredientes, db)
        # Displaying results in index.html
        return render_template('admin.html', heladeria = productos_ingredientes, user = current_user)

@home_blueprint.route('/empleado')
@login_required
def empleado():
    # En caso de que el usuario no sea administrador
    if not current_user.is_employee:
        return redirect(url_for('home.no_autorizado'))
    
    # De lo contrario
    else:
        # Trayendo resultados del controlador
        productos_ingredientes = obtener_productos(productos, ingredientes, db)

        # Redirección a usuarios no administradores del sitio web
        return render_template('empleado.html', heladeria = productos_ingredientes, user = current_user)

@home_blueprint.route('/cliente')
@login_required
def cliente():
    # Trayendo resultados del controlador
    productos_ingredientes = obtener_productos(productos, ingredientes, db)

    # Redirección a usuarios no administradores del sitio web
    return render_template('cliente.html', heladeria = productos_ingredientes, user = current_user)

@home_blueprint.route('/no-autorizado')
def no_autorizado():
    # Redirigiendo un usuario a la pagina de: No Autorizado
    return render_template('no_autorizado.html'), 401

@home_blueprint.route('/invitado')
def invitado():
    # Trayendo resultados del controlador
    productos_ingredientes = obtener_productos(productos, ingredientes, db)

    # Redirigiendo un usuario a la pagina de: No Autorizado
    return render_template('invitado.html', heladeria = productos_ingredientes)

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
        ingrediente3.nombre.label('ingrediente3'),
        func.round(productos.precio_publico - (ingrediente1.precio + ingrediente2.precio + ingrediente3.precio), 2).label('rentabilidad'),
        func.round(ingrediente1.precio + ingrediente2.precio + ingrediente3.precio, 2).label('costo_total'),
        case(
            (func.substring_index(productos.nombre, ' ', 1) == 'Malteada', 
             func.round(ingrediente1.calorias + ingrediente2.calorias + ingrediente3.calorias + 200, 2)),
            (func.substring_index(productos.nombre, ' ', 1) == 'Copa', 
             func.round((ingrediente1.calorias + ingrediente2.calorias + ingrediente3.calorias) * 0.95, 2)),
            else_ = func.round(ingrediente1.calorias + ingrediente2.calorias + ingrediente3.calorias, 2)
        ).label('calorias_totales')
    ).join(ingrediente1, productos.ingrediente1_id == ingrediente1.id
    ).join(ingrediente2, productos.ingrediente2_id == ingrediente2.id
    ).join(ingrediente3, productos.ingrediente3_id == ingrediente3.id).all()

    # Retornando los ingredientes disponibles en inventario
    return productos_ingredientes

@home_blueprint.route('/vender/<int:producto_id>', methods = ['POST'])
@login_required
def vender_producto(producto_id):
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)
    if current_user.is_admin or current_user.is_employee:
        try:
            heladeria = Heladeria([producto])
            if heladeria.vender(producto_obtenido.nombre):
                mensaje = f"¡{producto_obtenido.nombre} vendido con éxito!"
                tipo_mensaje = 'success'
            else:
                mensaje = "No se pudo completar la venta"
                tipo_mensaje = 'warning'
        except ValueError as e:
            mensaje = f"¡Oh no! {str(e)}"
            tipo_mensaje = 'danger'
        
        # Redirección con parámetros de mensaje
        redirect_url = url_for('home.admin' if current_user.is_admin else 'home.empleado' if current_user.is_employee else 'home.cliente')
        
        return redirect(f"{redirect_url}?mensaje={mensaje}&tipo={tipo_mensaje}&producto_id={producto_id}")

    else:
        try:
            heladeria = Heladeria([producto])
            if heladeria.vender(producto_obtenido.nombre):
                mensaje = f"¡{producto_obtenido.nombre} comprado con éxito!"
                tipo_mensaje = 'success'
            else:
                mensaje = "No se pudo completar la compra :("
                tipo_mensaje = 'warning'
        except ValueError as e:
            mensaje = f"¡Oh no! {str(e)}"
            tipo_mensaje = 'danger'
        
        # Redirección con parámetros de mensaje
        redirect_url = url_for('home.admin' if current_user.is_admin else 'home.empleado' if current_user.is_employee else 'home.cliente')
        
        return redirect(f"{redirect_url}?mensaje={mensaje}&tipo={tipo_mensaje}&producto_id={producto_id}")