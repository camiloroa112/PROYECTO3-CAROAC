# 3rd Party Libraries
from typing import Union

# 1. Función para determinar si un ingrediente es saludable o no
def es_sano(calorias: int, es_vegetariano: bool) -> bool: 
    """
    Introducción
    ------------
        - Función que retorna un valor booleano al determinar si un ingrediente es saludable o no.
    
    Parametros
    ----------
        - num_calorias: Int, sin valores por defecto.
        - es_vegetariano: Booleano, sin valores por defecto.
    
    Retorna
    -------
        - True/False: bool."""
    
    # Anidacion que determinar si cumple con el numero de calorias o es vegetariano
    if calorias < 100 or es_vegetariano == True:
        return True
    
    # Retorna Falso si las dos condiciones no se cumplen
    else:
        return False
    
# 2. Función para retornar la suma de calorias
def calorias(calorias_por_ingrediente: list[int]) -> float:
    """
    Introducción
    ------------
        - Función para obtener la suma de las calorias por ingrediente y se multiplica por 0.95 redondeado a dos cifras significativas. 

    Parametros
    ----------
        - calorias_por_ingrediente: List, sin valores por defecto.
    
    Retorna
    -------
        - Valor sumado, redondeado a dos cifras significativas."""

    # Suma y aproximación a dos cifras significativas de los ingredientes de la lista
    return round(sum(calorias_por_ingrediente) * 0.95, 2)

# 3. Función para obtener los costos de productos
def costos(ingrediente_1: Union[dict, object] = None, ingrediente_2: Union[dict, object] = None, ingrediente_3: Union[dict, object] = None) -> float:
    """
    Introduccion
    ------------
        - Función para obtener los costos de elaborar un producto en particular.

    Parametros:
    -----------
        - ingrediente_1: Dict, sin valores por defecto.
        - ingrediente_2: Dict, sin valores por defecto.
        - ingrediente_3: Dict, sin valores por defecto.
    
    Retorna
    -------
        - costo_total: float."""

    # Inicializar suma de precios
    costo_total = 0

    # Incluir diccionarios en una lista
    new_list = [ingrediente_1, ingrediente_2, ingrediente_3]

    # Inicializando variables para confirmar tipos de datos
    is_dict = False
    is_none = False
    is_object = False
    is_number = False

    # Evaluando si todos los parámetros son de tipo diccionarios, objetos o None
    for element in new_list:
        if isinstance(element, dict):
            is_dict = True
        elif hasattr(element, 'get_precio'):
            is_object = True
        elif isinstance(element, int) or isinstance(element, float):
            is_number = True
        else:
            is_none = True

    # Todos los parámetros de la función tienen un tipo de dato dict
    if is_dict == True:

        # Modificar las llaves a minusculas mediante un for loop
        for i in range(0, len(new_list)):
            new_list[i] = {k.lower(): v for k, v in new_list[i].items() if new_list[i] != None and type(new_list[i]) == dict}
            globals()[f'ingrediente_{i + 1}'] = new_list[i]
        
        # Almacenar diccionarios con llaves en minusculas
        new_list = [ingrediente_1, ingrediente_2, ingrediente_3]
        
        # Obtener el costo de producir un producto en particular
        for i in range(0, len(new_list)):
            if 'precio' in new_list[i].keys():
                costo_total += new_list[i]['precio']

        # Retornar la suma de los costos para producir un producto
        return round(costo_total, 2)
    
    # Todos los parámetros de la función tienen un tipo de dato number
    elif is_number == True:
        return ingrediente_1 + ingrediente_2 + ingrediente_3
    
    # Todos los parámetros de la función tienen un tipo de dato Object
    elif is_object == True:
        return ingrediente_1.get_precio() + ingrediente_2.get_precio() + ingrediente_3.get_precio()

    # Todos los parámetros de la función tienenun tipo de dato None
    elif is_none == True:
        print('Todos los valores de los paramétros son de tipo None')
        pass

    # En cualquier otro tipo o combinaciones
    else:
        print('No aplica')
        pass
    
    # Todos los parámetros de la función tienen un tipo de dato dict

# 4. Función para obtener la rentabilidad de un producto
def rentabilidad(precio_producto: Union[float, object] = None, ingrediente_1: Union[dict, object] = None, ingrediente_2: Union[dict, object] = None, ingrediente_3: Union[dict, object] = None) -> float:
    """
    Introducción
    ------------
        - Función para obtener la rentabilidad de un producto, teniendo en cuenta su precio de venta versus los precios de los ingredientes.

    Parámetros
    ----------
        - precio_producto: Float, sin valores por defecto.
        - ingrediente_1: Dict, sin valores por defecto.
        - ingrediente_2: Dict, sin valores por defecto.
        - ingrediente_3: Dict, sin valores por defecto.
    
    Retorna
    -------
        - Rentabilidad: float."""
    
    # Confirmacion del tipo de dato tipo float
    if isinstance(precio_producto, float) or isinstance(precio_producto, int):
        # Retornar la suma de los costos para producir un producto siempre y cuando sean un diccionario
        return round(precio_producto - costos(ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3), 2)
    
    # En caso de que el primer parametro sea un objeto
    else:
        # Retornar la suma de los costos para producir un producto siempre y cuando sean un diccionario
        return round(precio_producto.get_precio_publico() - costos(ingrediente_1 = ingrediente_1, ingrediente_2 = ingrediente_2, ingrediente_3 = ingrediente_3), 2)

# 5. Función que calcula el producto más rentable
def producto_rentable(producto_1: Union[dict, object] = None, producto_2: Union[dict, object] = None, producto_3: Union[dict, object] = None, producto_4: Union[dict, object] = None) -> str:
    """
    Introducción
    ------------
        - Función que permite identificar el producto más rentable.
    
    Parámetros
    ----------
        - producto_1: Dict o Object, None.
        - producto_2: Dict o Object, None.
        - producto_3: Dict o Object, None.
        - producto_4: Dict o Object, None.

    Retorna
    -------
        - Producto más rentable: str."""

    # Incluyendo los productos en una lista
    new_list = [producto_1, producto_2, producto_3, producto_4]
    
    # Excluyendo los None
    new_list = [new for new in new_list if new != None]

    # Inicializando variables para confirmar tipos de datos
    is_dict = False
    is_none = False
    is_object = False

    # Evaluando si todos los parámetros son de tipo diccionarios, objetos o None
    for element in new_list:
        if isinstance(element, dict):
            is_dict = True
        elif isinstance(element, object):
            is_object = True
        else:
            is_none = True

    # Todos los parámetros de la función tienen un tipo de dato dict
    if is_dict == True:

        # Encontrando la rentabilidad máxima
        rentabilidad_maxima = max([[new_list[i]['rentabilidad']] for i in range(0, len(new_list)) if new_list[i] != None])[0]

        # Retorna el nombre del producto más rentable
        return ''.join([new_list[i]['nombre'] for i in range(0, len(new_list)) if new_list[i]['rentabilidad'] == rentabilidad_maxima])
    
    # Todos los parámetros de la función tienen un tipo de dato object
    elif is_object == True:
        producto_mas_rentable = max(new_list, key = lambda producto: producto.calcular_rentabilidad())
        return producto_mas_rentable.get_nombre()
    
    # Todos los parámetros de la función tienenun tipo de dato None
    elif is_none == True:
        print('Todos los valores de los paramétros son de tipo None')
        pass

    # En cualquier otro tipo o combinaciones
    else:
        print('No aplica')
        pass