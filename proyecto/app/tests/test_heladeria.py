# 1st Party Libraries
from app.models.base import Base
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.models.heladeria import Heladeria
from app.models.complemento import Complemento

# 3rd Party Libraries
import unittest

class test_funciones(unittest.TestCase):
    """Unittests that compare the output of methods in the Heladeria class against predefined expected values for each test case."""

    def test_producto_mas_rentable(self) -> None:  # Unittest #1
        """Unittest to compare the profitability value obtained from the .producto_mas_rentable() with the value defined in the test case."""

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

        # Instantiating Heladeria with Products Available
        heladeria = Heladeria([copa_caramelo, malteada_chocolate])

        # Confirming the profitable product
        self.assertEqual(heladeria.producto_mas_rentable(), 'Copa de Caramelo')

    def test_vender(self) -> None:  # Unittest #2
        """Unittest to compare if an item has been sold from the .vender() with the boolean value defined in the test case."""

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
        malteada_chocolate = Copa(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_4, ingrediente_2 = ingrediente_5, ingrediente_3 = ingrediente_6, tipo_vaso = 'Vidrio')

        # Instantiating Heladeria with Products Available
        heladeria = Heladeria([copa_caramelo, malteada_chocolate])

        # Proving if the sellout of the Caramel Cup was successful
        self.assertEqual(heladeria.vender('Copa de Caramelo'), True)

        # Proving as false of a non existing ice-cream in Heladeria
        self.assertFalse(heladeria.vender('Copa de Chocolate'))

        # Reducing Complemento Powder Milk to zero
        ingrediente_6.renovar_inventario()

        # Checking if Asset shows
        with self.assertRaises(ValueError):
            heladeria.vender("Malteada de Chocolate") 

    def test_ventas_del_dia(self) -> None:  # Unittest #3
        """Unittest to compare the sellings from the day, with the value defined in the test case."""

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
        malteada_chocolate = Copa(nombre = 'Malteada de Chocolate', precio_publico = 9000, ingrediente_1 = ingrediente_4, ingrediente_2 = ingrediente_5, ingrediente_3 = ingrediente_6, tipo_vaso = 'Vidrio')

        # Instantiating Heladeria with Products Available
        heladeria = Heladeria([copa_caramelo, malteada_chocolate])

        # Selling Caramel Cup
        heladeria.vender('Copa de Caramelo')

        # Proving if the earnings of the Caramel Cup are equivalent to its public price defined in the unittest
        self.assertEqual(heladeria.get_ventas_del_dia(), 12000.00)

    def test_get_productos(self) -> None: 

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

        # Instantiating Heladeria with Products Available
        heladeria = Heladeria([copa_caramelo, malteada_chocolate])
        
        # Determining there are two products
        self.assertEqual(len(heladeria.get_productos()), 2) 

        # Confirming Product Names
        self.assertEqual(heladeria.get_productos()[0].get_nombre(), "Copa de Caramelo")
        self.assertEqual(heladeria.get_productos()[1].get_nombre(), "Malteada de Chocolate")