-- Creacion BD
CREATE DATABASE HELADERIA;
USE HELADERIA;

-- Creacion Tabla Ingredientes
CREATE TABLE HELADERIA.INGREDIENTES
(
	ID INT PRIMARY KEY,
    NOMBRE CHAR(50) NOT NULL,
    PRECIO FLOAT NOT NULL,
    CALORIAS INT NOT NULL,
    INVENTARIO  INT NOT NULL,
    ES_VEGETARIANO BOOLEAN NOT NULL,
    SABOR CHAR(10) NULL, 
    TIPO CHAR(11) NOT NULL
);

-- Creacion Tabla Productos
CREATE TABLE HELADERIA.PRODUCTOS
(
	ID INT PRIMARY KEY,
    NOMBRE CHAR(50),
    VOLUMEN VARCHAR(10) NULL,
    INGREDIENTE1_ID INT,
    INGREDIENTE2_ID INT,
    INGREDIENTE3_ID INT,
    FOREIGN KEY(INGREDIENTE1_ID) REFERENCES INGREDIENTES(ID),
    FOREIGN KEY(INGREDIENTE2_ID) REFERENCES INGREDIENTES(ID),
    FOREIGN KEY(INGREDIENTE3_ID) REFERENCES INGREDIENTES(ID),
    PRECIO_PUBLICO FLOAT,
    TIPO_VASO CHAR(10) NULL
);

-- Introduciedo Valores en Ingredientes
INSERT INTO HELADERIA.INGREDIENTES(ID, NOMBRE, PRECIO, CALORIAS, INVENTARIO, ES_VEGETARIANO, SABOR, TIPO)
VALUES 
	-- Copa de Caramelo
	(1, 'Helado de Arequipe', 3300, 350, 10, FALSE, 'Arequipe', 'Base'),
    (2, 'Caramelo', 2500, 100, 10, FALSE, FALSE, 'Complemento'),
    (3, 'Crema de Leche', 2500, 200, 10, TRUE, FALSE, 'Complemento'),
    -- Malteada de Vainilla
    (4, 'Helado de Vainilla', 3000, 150, 10, FALSE, 'Vainilla', 'Base'),
    (5, 'Extracto de Vainilla', 1800, 100, 10, FALSE, FALSE, 'Complemento'),
    (6, 'Salsa de Chocolate', 2500, 120, 10, FALSE, FALSE, 'Complemento'),
    -- Copa de Fresa
    (7, 'Helado de Fresa', 3200, 120, 10, FALSE, 'Fresa', 'Base'),
    (8, 'Fresas', 2700, 100, 10, FALSE, FALSE, 'Complemento'),
    (9, 'Leche Condensada', 2000, 150, 10, FALSE, FALSE, 'Complemento'),
    -- Malteada de Chocolate
    (10, 'Helado de Chocolate', 3500, 160, 10, FALSE, 'Chocolate', 'Base'),
    (11, 'Leche Entera', 3000, 120, 10, TRUE, FALSE, 'Complemento'),
    (12, 'Leche en Polvo', 2000, 100, 10, TRUE, FALSE, 'Complemento')
;

-- Introduciendo Valores en Productos
INSERT INTO HELADERIA.PRODUCTOS(ID, NOMBRE, VOLUMEN, INGREDIENTE1_ID, INGREDIENTE2_ID, INGREDIENTE3_ID, PRECIO_PUBLICO, TIPO_VASO)
VALUES
	(1, 'Copa de Caramelo', FALSE, 1, 2, 3, 12000, 'Vidrio'),
    (2, 'Malteada de Vainilla', '500mL', 4, 5, 6, 9000, FALSE),
    (3, 'Copa de Fresa', FALSE, 7, 8, 9, 11000, 'Vidrio'),
    (4, 'Malteada de Chocolate', '500mL', 10, 11, 12, 9000, FALSE)
;

-- Ingredientes y Productos
CREATE TABLE INGREDIENTES_PRODUCTOS AS
SELECT 
	a.ID,
	a.NOMBRE,
    a.VOLUMEN,
    a.PRECIO_PUBLICO,
    a.TIPO_VASO,
    b.NOMBRE AS INGREDIENTE1,
    c.NOMBRE AS INGREDIENTE2,
    d.NOMBRE AS INGREDIENTE3
FROM 
	HELADERIA.PRODUCTOS a
INNER JOIN 
	HELADERIA.INGREDIENTES b ON a.INGREDIENTE1_ID = b.ID
INNER JOIN 
	HELADERIA.INGREDIENTES C ON a.INGREDIENTE2_ID = c.ID
INNER JOIN 
	HELADERIA.INGREDIENTES d ON a.INGREDIENTE3_ID = d.ID;
    
-- Visualizacion
SELECT * FROM INGREDIENTES_PRODUCTOS;