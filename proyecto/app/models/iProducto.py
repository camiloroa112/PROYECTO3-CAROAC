from abc import ABC, abstractmethod
class iProducto(ABC):
    """Interfaz que brinda los métodos abstractos que serán utilizados en las clases malteada y copa."""
    
    @abstractmethod
    def calcular_costo(self) -> None: #1
        pass

    @abstractmethod
    def calcular_rentabilidad(self) -> None: #2
        pass

    @abstractmethod
    def calcular_calorias(self)-> None: #3
        pass