# Proyecto 3
Este es la siguiente parte del Proyecto 2, simula el funcionamiento de una heladería utilizando **Flask** como framework para la creación de la API y una serie de clases en Python que modelan los productos, ingredientes y ventas. La aplicación permite realizar ventas de productos como copas y malteadas, gestionando el inventario de los ingredientes (Bases y Complementos) y verificando la disponibilidad antes de cada venta. También contiene una API RESTful que permite la gestión de productos e ingredientes, que permite dar a conocer mensajes de error, de éxito y acceder a información organizada mediante un JSON.

## Descripción

La aplicación permite:
- Realizar ventas de productos.
- Ver la rentabilidad de los productos.
- Conocer el costo de elaboración de cada producto
- Atribuir roles y accesos a funciones y/o contenido.
- Ver el listado de ingredientes que conforman dicho producto.
- Verificar el inventario de los ingredientes (Bases y Complementos).
- Manejar los errores en caso de que falte algún ingrediente para la venta.

## Características

- **Gestión de Inventarios**: Se gestionan los inventarios sobre los ingredientes.
- **Venta de Productos**: Permite la venta de productos (copas, malteadas) siempre y cuando todos los ingredientes estén disponibles.
- **Manejo de Errores**: Presenta los errores específicos cuando falta un ingrediente mediante un mensaje personalizado.
- **Flask API**: Implementación de una API para interactuar con el sistema y realizar ventas, reabastecimiento del inventario, y renovación del mismo.
- **Gestión de Accesos**: Teniendo en cuenta los usuarios y los roles, tendrán acceso limitado a la utilización de funciones, interacción con las APIs y la visualización del contenido en la página. Como también usuarios indeseados no podrán acceder a contenido reservado para administradores, empleados y clientes.

## Requisitos

Se deben tener instaladas las siguientes dependencias:

- **Python 3.x**
- **Flask:** Visualización de front end.
- **pip:** Instalación y gestión de las dependencias.
- **SQL-Alchemy:** Manejo de bases de datos y interacción con frontend.

## Instalación

Sigue los siguientes pasos para instalar y ejecutar el proyecto:

1. Use el siguiente comando en la terminal de comandos desde C:\Usuarios:
   ```
   git clone https://github.com/camiloroa112/PROYECTO3-CAROAC.git
   ```

2. Crea un entorno virtual:

```
python3 -m venv venv
```

3. Activa el entorno virtual:

```
.venv\Scripts\activate
```

4. Instala las dependencias necesarias:

```
pip install -r requirements.txt
```

5. Ingrese a app/config/settings.py e ingrese sus credenciales de MySQL Workbench.

6. Ejecuta la aplicación Flask:

```
python app.py
```

> [!IMPORTANT]
> En caso de errores con MySQL, cerciorese de que en el administrador de tareas, especificamente en Servicios solo se este ejecutando el servicio MySQL80 y no MySQL83.
> Si dispone de otra base llamada heladeria, eliminela a fin de evitar cualquier conflicto con la visualización de la página.
> Toda la información de los endpoints y los outputs de los mismos solamente se verá reflejado en Postman. Recuerde que para comenzar a testear las APIs, primero debe iniciar sesión con http://127.0.0.1:5500/api/login, seleccione el método POST y presione Send para continuar.
> Si usted va a realizar algún ajuste en la API o en cualquiera, debe volver a iniciar sesión.
> El programa contiene la información necesaria, documentada y con el paso a paso sobre ¿Cómo se llego a cada solución?