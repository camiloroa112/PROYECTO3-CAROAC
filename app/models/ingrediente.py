# 1st Party Libraries
from app.models.funciones import es_sano

# 3rd Party Libraries
from abc import ABC

class Ingrediente(ABC):
    """Clase que crea las características que conforman a un ingrediente y brinda métodos de cálculo de calorias, costos, con sus respectivos setters y getters del objeto."""

    # 1. Constructor
    def __init__(self, precio: float, calorias: int, nombre: str, es_vegetariano: bool, inventario: int = 0) -> None:
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
   
    # 2. Función que retorna el inventario de un ingrediente
    def get_inventario(self) -> int:
        """Retorna el inventario que posee el ingrediente."""
        return self._inventario

    # 3. Función que retorna el precio de un ingrediente
    def get_precio(self) -> float:
        """Retorna el precio que posee el ingrediente."""
        return self._precio
    
    # 4. Función que retorna el nombre de un ingrediente
    def get_nombre(self) -> str:
        """Retorna el nombre del ingrediente"""
        return self._nombre

    # 5. Función que indica si un ingrediente es vegetariano
    def get_es_vegetariano(self) -> bool:
        """Indica si el ingrediente es vegetariano a partir de un Booleano: True/False"""
        return self._es_vegetariano
    
    # 6. Función que retorna el número de calorías
    def get_calorias(self) -> int:
        """Retorna el numero de calorias que posee un ingrediente."""
        return self._calorias

    # 7. Función que retorna si el ingrediente es sano bajo los valores indicados en el constructor
    def get_es_sano(self) -> bool:
        """Retorna a partir de un Booleano: True/False si un ingrediente es sano."""
        return es_sano(calorias = self._calorias, es_vegetariano = self._es_vegetariano)
    
    # 8. Configurar nuevo precio
    def set_precio(self, nuevo_precio: float) -> float:
        """Establece un precio nuevo a un ingrediente."""
        self._precio = nuevo_precio

    # 9. Configurar nuevo nombre
    def set_nombre(self, nuevo_nombre: str) -> str:
        """Establece un nombre nuevo a un ingrediente."""
        self._nombre = nuevo_nombre

    # 10. Configurar nuevo valor para es vegetariano
    def set_es_vegetariano(self, vegetariano: bool) -> None:
        """Establece un nuevo valor booleano a un ingrediente: True/False. Conociendo si es vegetariano o no."""
        self._es_vegetariano = vegetariano

    # 11. Configurar nuevas calorías
    def set_calorias(self, nuevas_calorias: int) -> None:
        """Establece un nuevo numero de calorias a un ingrediente."""
        self._calorias = nuevas_calorias

    # 12. Configurar nuevos valores para es sano
    def set_es_sano(self, nuevas_calorias: int, nuevo_es_vegetariano: bool) -> None:
        """Establece nuevos valores a las calorias y a si es vegetariano a un ingrediente."""
        self._calorias = nuevas_calorias
        self._es_vegetariano = nuevo_es_vegetariano