# 1st Party Libraries
from app.models.ingrediente import Ingrediente

class Complemento(Ingrediente):
    
    # 1. Constructor
    def __init__(self, precio: float, calorias: int, nombre: str, es_vegetariano: bool, inventario: int = 0) -> None:
        super().__init__(precio, calorias, nombre, es_vegetariano, inventario)
    
    # 2. Función para abastecer el inventario del complemento
    def abastecer(self) -> None:
        """Cumple con el objetivo de abastecer en 10 el inventario a los complementos."""
        self._inventario += 10
    
    # 3. Función para reducir a cero el inventario para baja rotación
    def renovar_inventario(self) -> None:
        """Cumple con el objetivo de reducir a cero el inventario en casos de baja rotación."""
        self._inventario = 0