# 1st Party Libraries
from app.models.iProducto import iProducto
from app.models.ingrediente import Ingrediente
from app.models.funciones import calorias, costos, rentabilidad

class Copa(iProducto):
    
    # 1. Constructor
    def __init__(self, nombre: str, precio_publico: float, ingrediente_1: Ingrediente, ingrediente_2: Ingrediente, ingrediente_3: Ingrediente, tipo_vaso: str) -> None:
        self._nombre = nombre
        self._tipo_vaso = tipo_vaso
        self._ingrediente_1 = ingrediente_1
        self._ingrediente_2 = ingrediente_2
        self._ingrediente_3 = ingrediente_3
        self._precio_publico = precio_publico

    # 2. Función para calcular el costo de una copa
    def calcular_costo(self) -> float:
        """Calcular el costo de una copa."""
        return round(costos(ingrediente_1 = self._ingrediente_1, ingrediente_2 = self._ingrediente_2, ingrediente_3 = self._ingrediente_3), 2)
    
    # 3. Función para calcular las calorias de una copa
    def calcular_calorias(self) -> float:
        """Calcular las calorias de una copa."""
        
        # Obtener calorias de los ingredientes
        ingrediente_1 = self._ingrediente_1.get_calorias()
        ingrediente_2 = self._ingrediente_2.get_calorias()
        ingrediente_3 = self._ingrediente_3.get_calorias()

        # Almacenar en una lista
        ingredientes = [ingrediente_1, ingrediente_2, ingrediente_3]

        # Retornar las calorias redondeadas a dos cifras
        return round(calorias(ingredientes), 2)
    
    # 3. Función para calcular la rentabilidad de una copa
    def calcular_rentabilidad(self) -> float:
        """Calcular las calorías de una malteada, teniendo en cuenta cada uno de las calorias de los ingredientes."""
        return round(rentabilidad(precio_producto = self._precio_publico, ingrediente_1 = self._ingrediente_1, ingrediente_2 = self._ingrediente_2, ingrediente_3 = self._ingrediente_3), 2)
    
    # 4. Función para obtener el nombre de la copa
    def get_nombre(self) -> str:
        return self._nombre
    
    # 5. Función para obtener el precio al público de la copa
    def get_precio_publico(self) -> float:
        return self._precio_publico
    
    # 6. Función para obtener el tipo de vaso
    def get_tipo_vaso(self) -> str:
        return self._tipo_vaso
    
    # 7. Función para obtener el nuevo nombre de la copa
    def set_nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre
    
    # 8. Función para obtener el nuevo precio al público de la copa
    def set_precio_publico(self, nuevo_precio_publico: float) -> None:
        self._precio_publico = nuevo_precio_publico
    
    # 9. Función para obtener el tipo de vaso
    def set_tipo_vaso(self, nuevo_tipo: str) -> None:
        self._tipo_vaso = nuevo_tipo