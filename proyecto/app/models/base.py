# 1st Party Libraries
from app.models.ingrediente import Ingrediente

class Base(Ingrediente):
    
    #1. Constructor
    def __init__(self, precio: float, calorias: int, nombre: str, es_vegetariano: bool, sabor: str, inventario: int = 0) -> None:
        super().__init__(precio, calorias, nombre, es_vegetariano, inventario)
        self._sabor = sabor

    # 2. Función para abastecer el inventario de la base
    def abastecer(self) -> None:
        """Cumple con el objetivo de abastecer en 5 el inventario a las bases."""
        self._inventario += 5

    # 3. Función para obtener el sabor de la base
    def get_sabor(self) -> str:
        """Retorna el sabor de la base."""
        return self._sabor
    
    # 3. Función para obtener el sabor de la base
    def set_sabor(self, nuevo_sabor: str) -> None:
        """Retorna el nuevo sabor de la base."""
        self._sabor = nuevo_sabor