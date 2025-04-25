# 1st Party Libraries
from app.config.db import db
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.models.productos import productos
from app.models.ingrediente import Ingrediente
from app.models.ingredientes import ingredientes

# 3rd Party Libraries
from sqlalchemy.orm import aliased

def obtener_producto(producto_id: int):
    """Método utilizado para obtener el producto y su nombre a traves del inner join entre dos tablas."""
    
    # Aliases para ingredientes
    i1_alias = aliased(ingredientes)
    i2_alias = aliased(ingredientes)
    i3_alias = aliased(ingredientes)

    # JOIN producto con ingredientes
    resultado = db.session.query(productos, i1_alias, i2_alias, i3_alias
    ).join(i1_alias, productos.ingrediente1_id == i1_alias.id
    ).join(i2_alias, productos.ingrediente2_id == i2_alias.id
    ).join(i3_alias, productos.ingrediente3_id == i3_alias.id
    ).filter(productos.id == producto_id).first()

    # En caso de que no se encuentre el resultado
    if resultado is None:
        return None, 'Producto no encontrado'

    # Extraer tupla de la consulta
    producto_obtenido, ingrediente__1, ingrediente__2, ingrediente__3 = resultado

    # Instanciar ingredientes
    ingrediente1 = Ingrediente(precio = ingrediente__1.precio, calorias = ingrediente__1.calorias, nombre = ingrediente__1.nombre, es_vegetariano = ingrediente__1.es_vegetariano, inventario = ingrediente__1.inventario)
    ingrediente2 = Ingrediente(precio = ingrediente__2.precio, calorias = ingrediente__2.calorias, nombre = ingrediente__2.nombre, es_vegetariano = ingrediente__2.es_vegetariano, inventario = ingrediente__2.inventario)
    ingrediente3 = Ingrediente(precio = ingrediente__3.precio, calorias = ingrediente__3.calorias, nombre = ingrediente__3.nombre, es_vegetariano = ingrediente__3.es_vegetariano, inventario = ingrediente__3.inventario)

    # Determinar el producto por si tiene un vaso para las copas
    if producto_obtenido.tipo_vaso:
        producto = Copa(nombre = producto_obtenido.nombre, precio_publico = producto_obtenido.precio_publico, ingrediente_1=ingrediente1, ingrediente_2=ingrediente2, ingrediente_3 = ingrediente3, tipo_vaso = producto_obtenido.tipo_vaso)
    
    # Determinar el producto por si tiene un volumen para las malteadas
    elif producto_obtenido.volumen:
        producto = Malteada(nombre = producto_obtenido.nombre, precio_publico = producto_obtenido.precio_publico, ingrediente_1=ingrediente1, ingrediente_2=ingrediente2, ingrediente_3 = ingrediente3, volumen = producto_obtenido.volumen)
    
    # Para algún producto diferente
    else:
        return None, 'Tipo de producto no reconocido'

    # Retorno del producto instanciado
    return producto, producto_obtenido
