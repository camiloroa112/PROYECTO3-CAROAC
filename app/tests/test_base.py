# 3rd Party Libraries
import unittest

# 1st Party Libraries
from app.models.base import Base

class test_base(unittest.TestCase):
    """Unittests that compare the output of methods in the Base class against predefined expected values for each test case."""

    def test_abastecer(self) -> None:  # Unittest #1
        """Unittest which identifies if the abastecer method has added five more units of inventory and compares the final inventory with the a default value set in the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Adding five more units of inventory
        helado_arequipe.abastecer()
        # Comparing units added with value defined in the unittest
        self.assertEqual(helado_arequipe.get_inventario(), 15)
    
    def test_get_sabor(self) -> None:  # Unittest #2
        """Unittest to compare the flavour from the Base class with the value defined within the test case."""

        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing flavor from method get_sabor() with value defined in the unittest
        self.assertEqual(helado_arequipe.get_sabor(), 'Arequipe')

    def test_set_sabor(self) -> None:  # Unittest #3
        """Unittest to compare the new flavour from the Base class with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Setting new flavour
        helado_arequipe.set_sabor(nuevo_sabor = 'Caramelo')
        # Comparing new flavor using the method get_sabor() with value defined in the unittest
        self.assertEqual(helado_arequipe.get_sabor(), 'Caramelo')
    
    def test_get_es_sano(self) -> None:  # Unittest #4
        """Unittest to compare if a product is healthy with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing if product is healthy with value defined in the unittest
        self.assertEqual(helado_arequipe.get_es_sano(), False)

    def test_set_es_sano(self) -> None:  # Unittest #5
        """Unittest to compare if a product new parameter value is healthy, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Defining new calories and a is healthy parameter
        helado_arequipe.set_es_sano(nuevas_calorias = 80, nuevo_es_vegetariano = True)
        # Comparing if product new healthy values with value defined in the unittest
        self.assertEqual(helado_arequipe.get_es_sano(), True)

    def test_get_calorias(self) -> None:  # Unittest #6
        """Unittest to retrieve the calories from the Base class, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing the calories from the get_calorias method with the values defined in the unittest
        self.assertEqual(helado_arequipe.get_calorias(), 350)

    def test_set_calorias(self) -> None:  # Unittest #7
        """Unittest to check the new calories from the Base class, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Defining new calories
        helado_arequipe.set_calorias(300)
        # Comparing the new calories from the get_calorias method with the values defined in the unittest
        self.assertEqual(helado_arequipe.get_calorias(), 300)

    def test_get_es_vegetariano(self) -> None:  # Unittest #8
        """Unittest to check if the Base is vegetarian, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing if product is vegetarian, with value defined within the unittest
        self.assertEqual(helado_arequipe.get_es_vegetariano(), False)

    def test_set_es_vegetariano(self) -> None:  # Unittest #9
        """Unittest to check if the Base new parameter value is vegetarian, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Defining a new vegetarian value in the constructor
        helado_arequipe.set_es_vegetariano(vegetariano = True)
        # Comparing if the new product parameter value with value defined in the unittest
        self.assertEqual(helado_arequipe.get_es_vegetariano(), True)

    def test_get_inventario(self) -> None:  # Unittest #10
        """Unittest to check the inventory, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing inventory from the get_inventario() with the value in the unittest
        self.assertEqual(helado_arequipe.get_inventario(), 10)

    def test_get_nombre(self) -> None:  # Unittest #11
        """Unittest to check the product name, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing product name from the get_nombre() with the value in the unittest
        self.assertEqual(helado_arequipe.get_nombre(), 'Helado de Arequipe')

    def test_set_nombre(self) -> None:  # Unittest #12
        """Unittest to check the new product name, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Defining a new product name
        helado_arequipe.set_nombre(nuevo_nombre = 'Helado de Caramelo')
        # Comparing product name from the get_nombre() with the value in the unittest
        self.assertEqual(helado_arequipe.get_nombre(), 'Helado de Caramelo')

    def test_get_precio(self) -> None:  # Unittest #13
        """Unittest to check the product price, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Comparing product price from the get_precio() with the value in the unittest
        self.assertEqual(helado_arequipe.get_precio(), 3300)

    def test_set_precio(self) -> None:  # Unittest #14
        """Unittest to check the new product price, with the value defined within the test case."""
        
        # Instantiating Helado de Arequipe
        helado_arequipe = Base(precio = 3300, calorias = 350, nombre = 'Helado de Arequipe', es_vegetariano = False, sabor = 'Arequipe', inventario = 10)
        # Setting new price
        helado_arequipe.set_precio(nuevo_precio = 3500)
        # Comparing new product price from the get_precio() with the value in the unittest
        self.assertEqual(helado_arequipe.get_precio(), 3500)