# 3rd Party Libraries
import unittest

# 1st Party Libraries
from app.models.complemento import Complemento

class test_complemento(unittest.TestCase):
    """Unittests that compare the output of methods in the Complemento class against predefined expected values for each test case."""

    def test_abastecer(self) -> None:  # Unittest #1
        """Unittest which identifies if the abastecer method has added ten more units of inventory and compares the final inventory with the a default value set in the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Adding ten more units of inventory
        caramelo.abastecer()
        # Comparing units added with value defined in the unittest
        self.assertEqual(caramelo.get_inventario(), 20)

    def test_get_es_sano(self) -> None:  # Unittest #2
        """Unittest to compare if a product is healthy with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing if product is healthy with value defined in the unittest
        self.assertEqual(caramelo.get_es_sano(), False)

    def test_set_es_sano(self) -> None:  # Unittest #3
        """Unittest to compare if a product new parameter value is healthy, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Defining new calories and a is healthy parameter
        caramelo.set_es_sano(nuevas_calorias = 99, nuevo_es_vegetariano = True)
        # Comparing if product new healthy values with value defined in the unittest
        self.assertEqual(caramelo.get_es_sano(), True)

    def test_get_calorias(self) -> None:  # Unittest #4
        """Unittest to retrieve the calories from the Complemento class, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing the calories from the get_calorias method with the values defined in the unittest
        self.assertEqual(caramelo.get_calorias(), 100)

    def test_set_calorias(self) -> None:  # Unittest #5
        """Unittest to check the new calories from the Complemento class, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Defining new calories
        caramelo.set_calorias(90)
        # Comparing the new calories from the get_calorias method with the values defined in the unittest
        self.assertEqual(caramelo.get_calorias(), 90)

    def test_get_es_vegetariano(self) -> None:  # Unittest #6
        """Unittest to check if the Complemento class is vegetarian, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing if product is vegetarian, with value defined within the unittest
        self.assertEqual(caramelo.get_es_vegetariano(), False)

    def test_set_es_vegetariano(self) -> None:  # Unittest #7
        """Unittest to check if the Complemento class new parameter value is vegetarian, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Defining a new vegetarian value in the constructor
        caramelo.set_es_vegetariano(vegetariano = True)
        # Comparing if the new product parameter value with value defined in the unittest
        self.assertEqual(caramelo.get_es_vegetariano(), True)

    def test_get_inventario(self) -> None:  # Unittest #8
        """Unittest to check the inventory, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing inventory from the get_inventario() with the value in the unittest
        self.assertEqual(caramelo.get_inventario(), 10)

    def test_get_nombre(self) -> None:  # Unittest #9
        """Unittest to check the product name, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing product name from the get_nombre() with the value in the unittest
        self.assertEqual(caramelo.get_nombre(), 'Caramelo')

    def test_set_nombre(self) -> None:  # Unittest #10
        """Unittest to check the new product name, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Defining a new product name
        caramelo.set_nombre(nuevo_nombre = 'Caramel')
        # Comparing product name from the get_nombre() with the value in the unittest
        self.assertEqual(caramelo.get_nombre(), 'Caramel')

    def test_get_precio(self) -> None:  # Unittest #11
        """Unittest to check the product price, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing product price from the get_precio() with the value in the unittest
        self.assertEqual(caramelo.get_precio(), 2500)

    def test_set_precio(self) -> None:  # Unittest #12
        """Unittest to check the new product price, with the value defined within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Setting new price
        caramelo.set_precio(nuevo_precio = 2300)
        # Comparing new product price from the get_precio() with the value in the unittest
        self.assertEqual(caramelo.get_precio(), 2300)

    def test_renovar_inventario(self) -> None:  # Unittest #13
        """Unittest to check if the inventory has been reduced to zero, with the value compared within the test case."""
        
        # Instantiating Caramelo
        caramelo = Complemento(precio = 2500, calorias = 100, nombre = 'Caramelo', es_vegetariano = False, inventario = 10)
        # Comparing inventory from the get_inventario() with the value in the unittest
        self.assertEqual(caramelo.get_inventario(), 10)
        # Reducing inventory to zero
        caramelo.renovar_inventario()
        # Comparing inventory reduced to zero from the get_inventario() with the value in the unittest
        self.assertEqual(caramelo.get_inventario(), 0)