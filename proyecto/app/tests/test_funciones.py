# 1st Party Libraries
from app.models.base import Base
from app.models.copa import Copa
import app.models.funciones as funciones
from app.models.malteada import Malteada
from app.models.complemento import Complemento

# 3rd Party Libraries
import unittest

class test_funciones(unittest.TestCase):
    """Unittests that compare the output of functions from the funciones module against predefined expected values for each test case."""

    def test_es_sano(self) -> None:  # Unittest #1
        """Unittest to compare the value obtained from the .es_sano() method with the predefined value in the test case"""
        self.assertEqual(funciones.es_sano(calorias = 100, es_vegetariano = True), True)

    def test_calorias(self) -> None:  # Unittest #2
        """Unittest to compare the value obtained from the .calorias() method with the predefined value in the test case"""
        self.assertEqual(funciones.calorias(calorias_por_ingrediente = [100, 200, 300]), 570.00)

    def test_costos(self) -> None:  # Unittest #3
        """Unittest to compare the value obtained from the .calorias() method with the predefined value in the test case"""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
    
        # Cost comparison
        self.assertEqual(funciones.costos(ingrediente_1, ingrediente_2, ingrediente_3), 8300.00)

    def test_rentabilidad(self) -> None:  # Unittest #4
        """Unittest to compare the value obtained from the .rentabilidad() method with the predefined value in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Profitability comparison
        self.assertEqual(funciones.rentabilidad(precio_producto = copa_caramelo, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3), 3700.00)

    def test_producto_rentable(self) -> None:  # Unittest #5
        """Unittest to compare the value obtained from the .producto_rentable() method with the predefined value in the test case."""

        # Ingredients for preparing Copa de Caramelo
        ingrediente_1 = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        ingrediente_2 = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        ingrediente_3 = Complemento(precio = 2500, calorias = 200, nombre = 'Crema de Leche', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Copa de Caramelo
        copa_caramelo = Copa(nombre = 'Copa de Caramelo', precio_publico = 12000, ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3, tipo_vaso = 'Vidrio')

        # Ingredients for preparing Malteada de Chocolate
        ingrediente_4 = Base(precio = 3500, calorias = 160, nombre = 'Helado de Chocolate', es_vegetariano = False, sabor = 'Chocolate', inventario = 10)
        ingrediente_5 = Complemento(precio = 3000, calorias = 120, nombre = 'Leche Entera', es_vegetariano = False, inventario = 10)
        ingrediente_6 = Complemento(precio = 2000, calorias = 100, nombre = 'Leche en Polvo', es_vegetariano = True, inventario = 10)
        
        # Instantiating - Preparing Malteada de Chocolate
        malteada_chocolate = Malteada(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_4, ingrediente_2 = ingrediente_5, ingrediente_3 = ingrediente_6, volumen = '500mL')

        # Identifying the profitable product
        self.assertEqual(funciones.producto_rentable(producto_1 = copa_caramelo, producto_2 = malteada_chocolate), 'Copa de Caramelo')