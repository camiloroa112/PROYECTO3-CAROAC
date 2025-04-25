# 1st Party Libraries
from app.config.db import db
from app.models.base import Base
from app.models.productos import productos
from app.models.heladeria import Heladeria
from app.models.complemento import Complemento
from app.models.ingrediente import Ingrediente
from app.models.ingredientes import ingredientes
from app.models.obtener_producto import obtener_producto

# 3rd Party Libraries
from sqlalchemy.orm import aliased
from flask import Blueprint, jsonify
from flask_login import login_required

# Instanciando el Blueprint de la API
api = Blueprint('api', __name__)

# Consultando todos los Productos
@api.route('/api/productos', methods = ['GET'])
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
def obtener_rentabilidad(producto_id):
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)

    # Calcular rentabilidad
    rentabilidad = producto.calcular_rentabilidad()

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'rentabilidad': rentabilidad}), 200

# Calcular costo por ID Producto
@api.route('/api/productos/<int:producto_id>/costo_produccion', methods = ['GET'])
def obtener_costo(producto_id):
    
    # Obteniendo producto
    producto, producto_obtenido = obtener_producto(producto_id)

    # Calcular costo del producto
    costo_produccion = producto.calcular_costo()

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 'producto': producto_obtenido.nombre, 'costo_produccion': costo_produccion}), 200

# Vender un producto por su ID
@api.route('/api/productos/vender/<int:producto_id>', methods = ['POST'])
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
def obtener_todos_los_ingredientes():
    
    # Consultando todos los ingredientes disponibles en la base
    ingredientes_lista = ingredientes.query.all()

    # Introduciendo los ingredientes en una lista
    ingredientes_serializados = [{'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio} for ingrediente in ingredientes_lista]
    
    # Retornando la lista en un JSON
    return jsonify(ingredientes_serializados), 200

# Obteniendo Ingrediente por su ID
@api.route('/api/ingredientes/<int:ingrediente_id>', methods = ['GET'])
def obtener_ingrediente_por_id(ingrediente_id):
    
    # Realizando búsqueda del ingrediente
    ingrediente = ingredientes.query.get(ingrediente_id)
    
    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    else:
        return jsonify({'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio}), 200

# Obteniendo Ingrediente por su nombre
@api.route('/api/ingredientes/nombre/<string:nombre>', methods = ['GET'])
def obtener_ingrediente_por_nombre(nombre):
    
    # Obteniendo ingrediente por su nombre
    ingrediente = ingredientes.query.filter_by(nombre = nombre).first()
    
    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    return jsonify({'id': ingrediente.id, 'nombre': ingrediente.nombre, 'calorias': ingrediente.calorias, 'precio': ingrediente.precio}), 200

# Consultar si un ingrediente es sano segun su ID
@api.route('/api/ingredientes/<int:ingrediente_id>/sano', methods = ['GET'])
def obtener_sano_por_id(ingrediente_id):
    
    # Obteniendo ingrediente por su nombre
    ingrediente = ingredientes.query.get(ingrediente_id)
    
    # Retornando mensaje de error en caso de busqueda no exitosa
    if ingrediente is None:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
    # Retornando JSON sobre el ingrediente
    return jsonify({'ingrediente': ingrediente.nombre, 'es_sano': ingrediente.get_es_sano()}), 200

# Calcular rentabilidad por ID Producto
@api.route('/api/productos/<int:producto_id>/reabastecer', methods = ['GET'])
def reabastecer_producto(producto_id):
    
    # Creando alias para los tres diferentes ingredientes que conforman a un producto
    i1_alias = aliased(ingredientes)
    i2_alias = aliased(ingredientes)
    i3_alias = aliased(ingredientes)

    # JOIN producto con ingredientes
    resultado = db.session.query(productos, i1_alias, i2_alias, i3_alias
    ).join(i1_alias, productos.ingrediente1_id == i1_alias.id).join(i2_alias, productos.ingrediente2_id == i2_alias.id
    ).join(i3_alias, productos.ingrediente3_id == i3_alias.id).filter(productos.id == producto_id).first()

    # En caso de que no se encuentre el resultado
    if resultado is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    # Extraer tupla de la consulta
    producto_obtenido, ingrediente__1, ingrediente__2, ingrediente__3 = resultado

    # Instanciar Ingredientes
    ingrediente1 = Ingrediente(precio = ingrediente__1.precio, calorias = ingrediente__1.calorias, nombre = ingrediente__1.nombre, es_vegetariano = ingrediente__1.es_vegetariano, inventario = ingrediente__1.inventario)
    ingrediente2 = Ingrediente(precio = ingrediente__2.precio, calorias = ingrediente__2.calorias, nombre = ingrediente__2.nombre, es_vegetariano = ingrediente__2.es_vegetariano, inventario = ingrediente__2.inventario)
    ingrediente3 = Ingrediente(precio = ingrediente__3.precio, calorias = ingrediente__3.calorias, nombre = ingrediente__3.nombre, es_vegetariano = ingrediente__3.es_vegetariano, inventario = ingrediente__3.inventario)

    # Reabastecer los ingredientes de la copa o malteada
    ingredientes = [ingrediente1, ingrediente2, ingrediente3]
    
    # Llamamos al método abastecer según sea un complemento o una base
    for ingrediente in ingredientes:
        if isinstance(ingrediente, Complemento):
            ingrediente.abastecer()  # Reabastecer el complemento
        elif isinstance(ingrediente, Base):
            ingrediente.abastecer()  # Reabastecer la base

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 
                    'producto': producto_obtenido.nombre, 
                    'ingredientes': [
                                    {
                                        'nombre': ingrediente1.get_nombre(),
                                        'inventario': ingrediente1.get_inventario()
                                    },
                                    {
                                        'nombre': ingrediente2.get_nombre(),
                                        'inventario': ingrediente2.get_inventario()
                                    },
                                    {
                                        'nombre': ingrediente3.get_nombre(),
                                        'inventario': ingrediente3.get_inventario()
                                    }
                                    ],
                    'mensaje': 'Producto reabastecido con éxito'}), 200

# Calcular rentabilidad por ID Producto
@api.route('/api/productos/<int:producto_id>/renovar', methods = ['GET'])
def renovar_inventario(producto_id):
    
    # Creando alias para los tres diferentes ingredientes que conforman a un producto
    i1_alias = aliased(ingredientes)
    i2_alias = aliased(ingredientes)
    i3_alias = aliased(ingredientes)

    # JOIN producto con ingredientes
    resultado = db.session.query(productos, i1_alias, i2_alias, i3_alias
    ).join(i1_alias, productos.ingrediente1_id == i1_alias.id).join(i2_alias, productos.ingrediente2_id == i2_alias.id
    ).join(i3_alias, productos.ingrediente3_id == i3_alias.id).filter(productos.id == producto_id).first()

    # En caso de que no se encuentre el resultado
    if resultado is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    # Extraer tupla de la consulta
    producto_obtenido, ingrediente__1, ingrediente__2, ingrediente__3 = resultado

    # Instanciar Ingredientes
    ingrediente1 = Ingrediente(precio = ingrediente__1.precio, calorias = ingrediente__1.calorias, nombre = ingrediente__1.nombre, es_vegetariano = ingrediente__1.es_vegetariano, inventario = ingrediente__1.inventario)
    ingrediente2 = Ingrediente(precio = ingrediente__2.precio, calorias = ingrediente__2.calorias, nombre = ingrediente__2.nombre, es_vegetariano = ingrediente__2.es_vegetariano, inventario = ingrediente__2.inventario)
    ingrediente3 = Ingrediente(precio = ingrediente__3.precio, calorias = ingrediente__3.calorias, nombre = ingrediente__3.nombre, es_vegetariano = ingrediente__3.es_vegetariano, inventario = ingrediente__3.inventario)

    # Reabastecer los ingredientes de la copa o malteada
    ingredientes = [ingrediente1, ingrediente2, ingrediente3]
    
    # Llamamos al método renovar según sea un complemento o una base
    for ingrediente in ingredientes:
        # Comprobando si el ingrediente es un Complemento
        if isinstance(ingrediente, Complemento):
            ingrediente.renovar_inventario()
        # En caso de ser una base, esta seria no renovada
        elif isinstance(ingrediente, Base):
            continue

    # Retornando JSON
    return jsonify({'id': producto_obtenido.id, 
                    'producto': producto_obtenido.nombre, 
                    'ingredientes': [
                                    {
                                        'nombre': ingrediente1.get_nombre(),
                                        'inventario': ingrediente1.get_inventario()
                                    },
                                    {
                                        'nombre': ingrediente2.get_nombre(),
                                        'inventario': ingrediente2.get_inventario()
                                    },
                                    {
                                        'nombre': ingrediente3.get_nombre(),
                                        'inventario': ingrediente3.get_inventario()
                                    }
                                    ],
                    'mensaje': 'Inventario renovado con éxito'}), 200