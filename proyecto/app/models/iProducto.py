from abc import ABC, abstractmethod
class iProducto(ABC):
    """Interfaz que brinda los métodos abstractos que serán utilizados en las clases malteada y copa."""
    
    @abstractmethod
    def calcular_costo(self) -> None:
        pass

    @abstractmethod
    def calcular_rentabilidad(self) -> None:
        pass

    @abstractmethod
    def calcular_calorias(self)-> None:
        pass