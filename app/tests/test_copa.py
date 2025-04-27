# 3rd Party Libraries
import unittest

# 1st Party Libraries
from app.models.base import Base
from app.models.copa import Copa
from app.models.complemento import Complemento

class test_copa(unittest.TestCase):
    """Unittests that compare the output of methods in the Copa class against predefined expected values for each test case."""
    
    def test_calcular_costo(self) -> None:  # Unittest #1
        """Unittest to compare the value obtained from the .calcular_costo() method with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Cost comparison
        self.assertEqual(copa_caramelo.calcular_costo(), 8300.00)

    def test_calcular_calorias(self) -> None:  # Unittest #2
        """Unittest to compare the value obtained from the .calcular_calorias() method with the value defined in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Calories comparison
        self.assertEqual(copa_caramelo.calcular_calorias(), 617.50)

    def test_calcular_rentabilidad(self) -> None:  # Unittest #3
        """Unittest to compare the profitability value obtained from the .calcular_rentabilidad() with the value defined in the test case."""
         
         # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Profitability comparison
        self.assertEqual(copa_caramelo.calcular_rentabilidad(), 3700.00)

    def test_get_nombre(self) -> None:  # Unittest #4
        """Unittest to compare the product name from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Product comparison
        self.assertEqual(copa_caramelo.get_nombre(), 'Copa de Caramelo')

    def test_get_precio_publico(self) -> None:  # Unittest #5
        """Unittest to compare the product public price from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Public price comparison
        self.assertEqual(copa_caramelo.get_precio_publico(), 12000)

    def test_get_tipo_vaso(self) -> None:  # Unittest #6
        """Unittest to compare the glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Glass type comparison
        self.assertEqual(copa_caramelo.get_tipo_vaso(), 'Vidrio')

    def test_set_nombre(self) -> None:  # Unittest #7
        """Unittest to compare the new glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Defining new product name
        copa_caramelo.set_nombre(nuevo_nombre = 'Copa de Caramel')

        # Glass type comparison
        self.assertEqual(copa_caramelo.get_nombre(), 'Copa de Caramel')

    def test_set_precio_publico(self) -> None:  # Unittest #8
        """Unittest to compare the new public price from the Copa class with the value defined in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Setting new public price
        copa_caramelo.set_precio_publico(nuevo_precio_publico = 14000)

        # Public price comparison
        self.assertEqual(copa_caramelo.get_precio_publico(), 14000)

    def test_set_tipo_vaso(self) -> None:  # Unittest #9
        """Unittest to compare the new glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Setting new glass type
        copa_caramelo.set_tipo_vaso('Plastico')
        
        # Glass type comparison
        self.assertEqual(copa_caramelo.get_tipo_vaso(), 'Plastico')