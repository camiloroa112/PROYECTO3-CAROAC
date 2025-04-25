# 3rd Party Libraries
import unittest

# 1st Party Libraries
from app.models.base import Base
from app.models.malteada import Malteada
from app.models.complemento import Complemento

class test_malteada(unittest.TestCase):
    """Unittests that compare the output of methods in the Copa class against predefined expected values for each test case."""
    
    def test_calcular_costo(self) -> None:  # Unittest #1
        """Unittest to compare the value obtained from the .calcular_costo() method with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Cost comparison
        self.assertEqual(malteada_chocolate.calcular_costo(), 9000.00)

    def test_calcular_calorias(self) -> None:  # Unittest #2
        """Unittest to compare the value obtained from the .calcular_calorias() method with the value defined in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Calories comparison
        self.assertEqual(malteada_chocolate.calcular_calorias(), 580.00)

    def test_calcular_rentabilidad(self) -> None:  # Unittest #3
        """Unittest to compare the profitability value obtained from the .calcular_rentabilidad() with the value defined in the test case."""
         
         # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Profitability comparison
        self.assertEqual(malteada_chocolate.calcular_rentabilidad(), 500.00)

    def test_get_nombre(self) -> None:  # Unittest #4
        """Unittest to compare the product name from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Product comparison
        self.assertEqual(malteada_chocolate.get_nombre(), 'Malteada de Chocolate')

    def test_get_precio_publico(self) -> None:  # Unittest #5
        """Unittest to compare the product public price from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Public price comparison
        self.assertEqual(malteada_chocolate.get_precio_publico(), 9000)

    def test_get_volumen(self) -> None:  # Unittest #6
        """Unittest to compare the glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Glass type comparison
        self.assertEqual(malteada_chocolate.get_volumen(), '500mL')

    def test_set_nombre(self) -> None:  # Unittest #7
        """Unittest to compare the new glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Defining new product name
        malteada_chocolate.set_nombre(nuevo_nombre = 'Chocomalteada')

        # Glass type comparison
        self.assertEqual(malteada_chocolate.get_nombre(), 'Chocomalteada')

    def test_set_precio_publico(self) -> None:  # Unittest #8
        """Unittest to compare the new public price from the Copa class with the value defined in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Setting new public price
        malteada_chocolate.set_precio_publico(nuevo_precio_publico = 10000)

        # Public price comparison
        self.assertEqual(malteada_chocolate.get_precio_publico(), 10000)

    def test_set_volumen(self) -> None:  # Unittest #6
        """Unittest to compare the new glass type from the Copa class with the value defined in the test case."""
        
        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_2 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, volumen = '500mL')

        # Setting new glass type
        malteada_chocolate.set_volumen('600mL')
        
        # Glass type comparison
        self.assertEqual(malteada_chocolate.get_volumen(), '600mL')