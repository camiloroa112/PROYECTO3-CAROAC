# 1st Party Libraries
from flask import jsonify
from app.models.base import Base
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.models.complemento import Complemento
from app.models.funciones import producto_rentable

# 3rd Party Libraries
from typing import List, Union

class Heladeria():
    
    # 1. Constructor
    def __init__(self, productos: List[Union[Copa, Malteada]]) -> None:
        self._ventas_del_dia = 0
        self._productos = productos
        
    # 2. Función que verifica las existencias de un producto
    def existencias(self, index: int) -> dict | None:
        """
        Introducción
        ------------
            - Función para determinar si hay elementos disponibles en ciertos índices de una lista, en caso de no encontrarse, retorna None.
        
        Parametros
        ----------
            - index: int, sin valores por defecto.
        
        Retorna
        -------
            - Producto | None.
        """
        
        return self._productos[index] if index < len(self._productos) else None
    
    # 3. Función para obtener el producto más rentable
    def producto_mas_rentable(self) -> float:
        """Función que permite identificar el nombre del producto más rentable."""
        
        # Obteniendo las existencias por Index
        producto_1 = self.existencias(index = 0)
        producto_2 = self.existencias(index = 1)
        producto_3 = self.existencias(index = 2)
        producto_4 = self.existencias(index = 3)

        # Retorno de la rentabilidad
        return producto_rentable(producto_1 = producto_1, producto_2 = producto_2, producto_3 = producto_3, producto_4 = producto_4)
    
    # 4. Función para obtener un valor booleano de la venta de un producto
    def vender(self, nombre_producto: str) -> bool:
        """
        Introduccion
        ------------
            - Función que permite vender un producto.
        Parámetros
        ----------
            - nombre_producto: str, sin valores por defecto.
        Retorna
        -------
            - True/False: bool."""
        
        # Inicialización de la variable producto_a_vender
        producto_a_vender = None
        
        # Busqueda del nombre del producto en productos.
        for producto in self._productos:
            if producto.get_nombre() == nombre_producto:
                producto_a_vender = producto
                break
        
        # Si el producto no está disponible, retorna False
        if producto_a_vender is None:
            return jsonify({'error': 'Producto no encontrado o inventario insuficiente'}), 404

        
        # Verificar si los ingredientes están disponibles
        ingredientes = [producto_a_vender._ingrediente_1, producto_a_vender._ingrediente_2, producto_a_vender._ingrediente_3]
        
        # Búsqueda de ingrediente en ingredientes
        for ingrediente in ingredientes:

            # # Comprobación de existencias para ingredientes complemento
            # if isinstance(ingrediente, Complemento):
            #     if ingrediente.get_inventario() < 1:
            #         raise ValueError(f"¡Oh no! Nos hemos quedado sin {ingrediente.get_nombre()}")
                
            # # Comprobación de existencias para ingredientes Base
            # elif isinstance(ingrediente, Base):
            #     if ingrediente.get_inventario() < 0.2:
            #         raise ValueError(f"¡Oh no! Nos hemos quedado sin {ingrediente.get_nombre()}")
            for ingrediente in ingredientes:
                if isinstance(ingrediente, Complemento):
                    if ingrediente.get_inventario() < 1:
                        return jsonify({'error': f"Nos hemos quedado sin {ingrediente.get_nombre()}"})
                elif isinstance(ingrediente, Base):
                    if ingrediente.get_inventario() < 0.2:
                        return jsonify({'error': f"Nos hemos quedado sin {ingrediente.get_nombre()}"})

        
        # Si todos los ingredientes están disponibles, restamos las cantidades de inventario
        for ingrediente in ingredientes:

            # Restamos 1 unidad de cada complemento
            if isinstance(ingrediente, Complemento):
                ingrediente._inventario -= 1

            # Restamos 0.2 unidades de cada base
            elif isinstance(ingrediente, Base):
                ingrediente._inventario -= 0.2

        # Si todo está en orden, agregamos el precio del producto a las ventas del día
        self._ventas_del_dia += producto_a_vender.get_precio_publico()

        # Retorna True si la venta fue exitosa
        return True
    
    # 5. Funcion para obtener las ventas del día.
    def get_ventas_del_dia(self) -> float:
        return self._ventas_del_dia

    # 6. Función para obtener los productos
    def get_productos(self) -> list:
        return self._productos