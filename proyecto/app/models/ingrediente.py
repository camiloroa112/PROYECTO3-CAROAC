# 1st Party Libraries
from app.models.funciones import es_sano

# 3rd Party Libraries
from abc import ABC, abstractmethod

class Ingrediente(ABC):

    # 1. Constructor
    def __init__(self, precio: float, calorias: int, nombre: str, es_vegetariano: bool, inventario: int = 0) -> None:
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
   
    # 3. Función que retorna el inventario de un ingrediente
    def get_inventario(self) -> int:
        return self._inventario

    # 4. Función que retorna el precio de un ingrediente
    def get_precio(self) -> float:
        return self._precio
    
    # 5. Función que retorna el nombre de un ingrediente
    def get_nombre(self) -> str:
        return self._nombre

    # 6. Función que indica si un ingrediente es vegetariano
    def get_es_vegetariano(self) -> bool:
        return self._es_vegetariano
    
    # 7. Función que retorna el número de calorías
    def get_calorias(self) -> int:
        return self._calorias

    # 8. Función que retrorna si el ingrediente es sano bajo los valores indicados en el constructor
    def get_es_sano(self) -> bool:
        return es_sano(calorias = self._calorias, es_vegetariano = self._es_vegetariano)
    
    # 9. Configurar nuevo precio
    def set_precio(self, nuevo_precio: float) -> float:
        self._precio = nuevo_precio

    # 10. Configurar nuevo nombre
    def set_nombre(self, nuevo_nombre: str) -> str:
        self._nombre = nuevo_nombre

    # 11. Configurar nuevo valor para es vegetariano
    def set_es_vegetariano(self, vegetariano: bool) -> None:
        self._es_vegetariano = vegetariano

    # 12. Configurar nuevas calorías
    def set_calorias(self, nuevas_calorias: int) -> None:
        self._calorias = nuevas_calorias

    # 13. Configurar nuevos valores para es sano
    def set_es_sano(self, nuevas_calorias: int, nuevo_es_vegetariano: bool) -> None:
        self._calorias = nuevas_calorias
        self._es_vegetariano = nuevo_es_vegetariano