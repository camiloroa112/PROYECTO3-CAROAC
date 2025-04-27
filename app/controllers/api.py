# 1st Party Libraries
from app.config.db import db
from app.models.base import Base
from app.models.usuario import Usuario
from app.models.productos import productos
from app.models.heladeria import Heladeria
from app.models.complemento import Complemento
from app.models.ingrediente import Ingrediente
from app.models.ingredientes import ingredientes
from app.models.obtener_producto import obtener_producto

# 3rd Party Libraries
from sqlalchemy.orm import aliased
from flask import Blueprint, jsonify
from app.config.auth import login_manager
from flask_login import login_required, login_user

# Instanciando el Blueprint de la API
api = Blueprint('api', __name__)

@login_manager.user_loader
def load_user(user_id: str) -> Usuario:
    # Obtiene el ID de un Registro
    return Usuario.query.get(str(user_id))

# API para permitir el logeo y uso de las demás APIs
@api.route('/api/login', methods = ['POST'])
def login():
    
    # Colocación de un uusario admin
    _username = 'camilor123'
    _password = 'Camilor123'

    # Búsqueda de un usuario
    user = Usuario.query.filter_by(username = _username, password = _password).first()

    # En caso de que se encuentre el usuario
    if user: 

        # Se inicia sesión en la página
        login_user(user)

        # Inspecciona si este es admin o no
        if user.is_admin:
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})
        
        # Para un usuario sin credenciales validas
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

# Consultando todos los Productos
@api.route('/api/productos', methods = ['GET'])
@login_required
def obtener_productos():
    
    # Consulta de los productos disponibles en la base
    heladeria_productos = productos.query.all()    
    
    # Preparación de una lista para almacenar resultados
    resultado = []
    # Iterando en cada ino para ser guardado en una lista
    
    for producto in heladeria_productos:
        resultado.append({'id': producto.id, 'nombre': producto.nombre, 'volumen': producto.volumen, 'precio_publico': producto.precio_publico, 'tipo_vaso': producto.tipo_vaso})
    
    # Retorno de la lista en un JSON
    return jsonify(resultado), 200

# Consultar producto por su ID
@api.route('/api/productos/<int:producto_id>', methods = ['GET'])
@login_required
def obtener_producto_por_id(producto_id):
    
    # Obteniendo los productos por ID
    producto = productos.query.get_or_404(producto_id)
    
    # Retornando JSON del producto
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'precio_publico': producto.precio_publico, 'volumen': producto.volumen}), 200

# Consultando producto por nombre del producto
@api.route('/api/productos/nombre/<string:nombre>', methods = ['GET'])
@login_required
def obtener_producto_por_nombre(nombre):
    
    # Filtrando por el nombre
    producto = productos.query.filter_by(nombre = nombre).first()
    
    # En caso de que no hayan resultados
    if producto is None:
        return jsonify({'error: El producto no se encuentra.'}), 404
    
    # Retorno de los productos
    else:
        return jsonify({'id': producto.id, 'nombre': producto.nombre, 'precio_publico': producto.precio_publico}), 200
    
# Calcular calorias por ID Producto
@api.route('/api/productos/<int:producto_id>/calorias', methods = ['GET'])
@login_required
def obtener_calorias(producto_id):
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)

    # Calcular calorías
    calorias = producto.calcular_calorias()

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'calorias': calorias}), 200

# Calcular rentabilidad por ID Producto
@api.route('/api/productos/<int:producto_id>/rentabilidad', methods = ['GET'])
@login_required
def obtener_rentabilidad(producto_id):
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)

    # Calcular rentabilidad
    rentabilidad = producto.calcular_rentabilidad()

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'rentabilidad': rentabilidad}), 200

# Calcular costo por ID Producto
@api.route('/api/productos/<int:producto_id>/costo_produccion', methods = ['GET'])
@login_required
def obtener_costo(producto_id):
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)

    # Calcular costo del producto
    costo_produccion = producto.calcular_costo()

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'costo_produccion': costo_produccion}), 200

# Vender un producto por su ID
@api.route('/api/productos/vender/<int:producto_id>', methods = ['POST'])
@login_required
def vender_producto(producto_id):
    
    # Identificar producto por su ID
    producto = productos.query.get(producto_id)
    
    # En caso de no encontrarse
    if producto is None:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)
    
    # Instanciando Heladería
    heladeria = Heladeria([producto])
    
    # Confirmación de venta exitosa
    if heladeria.vender(producto_obtenido.nombre):
        return jsonify({'id': producto_obtenido.id, 'mensaje': 'Venta exitosa', 'producto': producto_obtenido.nombre}), 200
    
    # En caso de algún error en la venta
    else:
        return jsonify({'error': 'No se pudo realizar la venta'}), 400
    
# Obteniendo todos los ingredientes
@api.route('/api/ingredientes', methods = ['GET'])
@login_required
def obtener_todos_los_ingredientes():
    
    # Consultando todos los ingredientes disponibles en la base
    ingredientes_lista = ingredientes.query.all()

    # Introduciendo los ingredientes en una lista
    ingredientes_serializados = [{'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio, 'tipo_ingrediente': ingrediente.tipo} for ingrediente in ingredientes_lista]
    
    # Retornando la lista en un JSON
    return jsonify(ingredientes_serializados), 200

# Obteniendo Ingrediente por su ID
@api.route('/api/ingredientes/<int:ingrediente_id>', methods = ['GET'])
@login_required
def obtener_ingrediente_por_id(ingrediente_id):
    
    # Realizando búsqueda del ingrediente
    ingrediente = ingredientes.query.get(ingrediente_id)
    
    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    else:
        return jsonify({'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio, 'tipo_ingrediente': ingrediente.tipo}), 200

# Obteniendo Ingrediente por su nombre
@api.route('/api/ingredientes/nombre/<string:nombre>', methods = ['GET'])
@login_required
def obtener_ingrediente_por_nombre(nombre):
    
    # Obteniendo ingrediente por su nombre
    ingrediente = ingredientes.query.filter_by(nombre = nombre).first()
    
    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    return jsonify({'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio, 'tipo_ingrediente': ingrediente.tipo}), 200

# Consultar si un ingrediente es sano segun su ID
@api.route('/api/ingredientes/<int:ingrediente_id>/sano', methods = ['GET'])
@login_required
def obtener_sano_por_id(ingrediente_id):
    
    # Obteniendo ingrediente por su nombre
    ingrediente = ingredientes.query.get(ingrediente_id)
    
    # Instanciando la clase Ingrediente
    ingrediente_ = Ingrediente(precio = ingrediente.precio, calorias = ingrediente.calorias, nombre = ingrediente.nombre, es_vegetariano = ingrediente.es_vegetariano, inventario = ingrediente.inventario)

    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    return jsonify({'ingrediente': ingrediente.nombre, 'es_sano': ingrediente_.get_es_sano(), 'tipo_ingrediente': ingrediente.tipo}), 200

# Reabastecer inventario por ID Producto
@api.route('/api/productos/<int:producto_id>/reabastecer', methods = ['GET'])
@login_required
def reabastecer_producto(producto_id: int):
    
    try:
        # Crear alias para cada uno de los ingredientes
        ingrediente1 = aliased(ingredientes)
        ingrediente2 = aliased(ingredientes)
        ingrediente3 = aliased(ingredientes)

        # Query que obtiene el producto y sus 3 ingredientes
        resultado = db.session.query(
            productos,
            ingrediente1, 
            ingrediente2, 
            ingrediente3, 
        ).join(ingrediente1, productos.ingrediente1_id == ingrediente1.id
        ).join(ingrediente2, productos.ingrediente2_id == ingrediente2.id
        ).join(ingrediente3, productos.ingrediente3_id == ingrediente3.id
        ).filter(
            productos.id == producto_id
        ).first()

        # En caso de no encontrarse el producto
        if not resultado:
            return jsonify({'error': 'Producto no encontrado'}), 404

        # Extraer tupla de la consulta
        producto_obtenido, ingrediente1, ingrediente2, ingrediente3 = resultado

        # Lista para almacenar los resultados
        ingredientes_actualizados = []

        # Lista para almacenar los resultados
        listado_ingredientes = [ingrediente1, ingrediente2, ingrediente3]

        # Ingredientes que conforman al producto
        for ingrediente in listado_ingredientes:
            
            # Determinar si es Base o Complemento por si tiene un sabor
            if ingrediente.tipo == 'Base':
                ingrediente_ = Base(precio = ingrediente.precio, calorias = ingrediente.calorias, nombre = ingrediente.nombre, es_vegetariano = ingrediente.es_vegetariano, sabor = ingrediente.sabor, inventario = ingrediente.inventario)
                ingrediente_.abastecer()

            # En caso contrario
            else:  
                ingrediente_ = Complemento(precio = ingrediente.precio, calorias = ingrediente.calorias, nombre = ingrediente.nombre, es_vegetariano = ingrediente.es_vegetariano, inventario = ingrediente.inventario)
                ingrediente_.abastecer()
            
            # Actualizar el inventario en la base de datos
            ingrediente.inventario = ingrediente_.get_inventario()
            
            # Actualización del JSON
            ingredientes_actualizados.append({'nombre': ingrediente_.get_nombre(), 'inventario': ingrediente_.get_inventario(), 'tipo': ingrediente.tipo})

        # Aplicacion de cambios en la BD
        db.session.commit()

        # Retornando JSON
        return jsonify({'id': producto_obtenido.id, 
                        'producto': producto_obtenido.nombre, 
                        'ingredientes': ingredientes_actualizados, 
                        'mensaje': 'Inventario renovado con éxito'}), 200

    # Retorno de Error en caso de no exito
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al reabastecer: {str(e)}'}), 500

# Renovar inventario por ID Producto
@api.route('/api/productos/<int:producto_id>/renovar', methods = ['POST'])
@login_required
def renovar_inventario(producto_id):
    try:
        # Crear alias para cada uno de los ingredientes
        ingrediente1 = aliased(ingredientes)
        ingrediente2 = aliased(ingredientes)
        ingrediente3 = aliased(ingredientes)

        # Query que obtiene el producto y sus 3 ingredientes
        resultado = db.session.query(
            productos,
            ingrediente1, 
            ingrediente2, 
            ingrediente3, 
        ).join(ingrediente1, productos.ingrediente1_id == ingrediente1.id
        ).join(ingrediente2, productos.ingrediente2_id == ingrediente2.id
        ).join(ingrediente3, productos.ingrediente3_id == ingrediente3.id
        ).filter(
            productos.id == producto_id
        ).first()

        # En caso de no encontrarse el producto
        if not resultado:
            return jsonify({'error': 'Producto no encontrado'}), 404

        # Extraer tupla de la consulta
        producto_obtenido, ingrediente1, ingrediente2, ingrediente3 = resultado
        # Lista para almacenar los resultados
        ingredientes_actualizados = []
        # Lista para almacenar los resultados
        listado_ingredientes = [ingrediente1, ingrediente2, ingrediente3]

        # Ingredientes que conforman al producto
        for ingrediente in listado_ingredientes:
            # Almacenando inventario inicial
            inventario_anterior = ingrediente.inventario
            
            # Corroborando si el tipo de ingrediente corresponde a una base
            if ingrediente.tipo == 'Base':
                # No hay instancia ya que no se renueva en las bases
                accion = 'No requiere renovación'
                # Se obtiene el inventario actual
                inventario_actual = inventario_anterior
            
            # Para el caso de los complementos
            else:
                # Instanciando la clase complemento
                complemento = Complemento(precio = ingrediente.precio, calorias = ingrediente.calorias, nombre = ingrediente.nombre, es_vegetariano = ingrediente.es_vegetariano, inventario = ingrediente.inventario)
                # Renovación del inventario
                complemento.renovar_inventario()
                # Obtención del inventario después de su renovación
                ingrediente.inventario = complemento.get_inventario()
                # Comentario sobre la acción
                accion = 'Renovado (inventario a 0)'
                # Obteniendo inventario renovado
                inventario_actual = ingrediente.inventario

            # Comentario para ser colocado en un JSON
            ingredientes_actualizados.append({
                'nombre': ingrediente.nombre,
                'inventario_anterior': inventario_anterior,
                'inventario_actual': inventario_actual,
                'tipo': ingrediente.tipo,
                'accion': accion
            })

        # Guardar cambios
        db.session.commit()

        # Retornando JSON
        return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'ingredientes': ingredientes_actualizados, 'mensaje': 'Inventario de complementos renovado con éxito'}), 200
    
    # Mensaje de error al abastecer
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al reabastecer: {str(e)}'}), 500