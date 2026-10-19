-- ============================================================================
-- 1. LIMPIEZA DE ESTRUCTURAS PREVIAS (En orden inverso por claves foráneas)
-- ============================================================================
DROP TRIGGER IF EXISTS trg_validar_cantidad_detalle ON Detalle_Pedido;
DROP FUNCTION IF EXISTS validar_cantidad_detalle();
DROP FUNCTION IF EXISTS total_pedido(INT);
DROP PROCEDURE IF EXISTS cancelar_pedido(INT);

DROP TABLE IF EXISTS Detalle_Pedido CASCADE;
DROP TABLE IF EXISTS Pedido CASCADE;
DROP TABLE IF EXISTS Cliente CASCADE;
DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Producto CASCADE;


-- ============================================================================
-- 2. CREACIÓN DE TABLAS (Estructura lógica en Tercera Forma Normal - 3FN)
-- ============================================================================

-- Tabla A: Clientes
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla B: Pedidos (Depende de Cliente)
CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabla C: Detalle de los Pedidos (Depende de Pedido)
CREATE TABLE Detalle_Pedido (
    id_detalle INT PRIMARY KEY,
    id_pedido INT NOT NULL,
    producto VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

-- ============================================================================
-- 3. CREACIÓN DE ÍNDICES (Optimización de búsquedas y JOINs - Punto 6.e)
-- ============================================================================

-- Optimización de la Clave Foránea en la tabla hija (Acelera drásticamente el INNER JOIN)
CREATE INDEX idx_detalle_pedido_fk ON Detalle_Pedido (id_pedido);

-- Optimización para búsquedas frecuentes por cliente e historial
CREATE INDEX idx_pedido_cliente ON Pedido (id_cliente);

-- Optimización para búsquedas de texto por productos específicos (Búsqueda de una clave)
CREATE INDEX idx_detalle_producto ON Detalle_Pedido (producto);


-- ============================================================================
-- 4. DESARROLLO DE COMPONENTES PROGRAMABLES (Punto 9)
-- ============================================================================

-------------------------------------------------------------------------------
-- A. TRIGGER: Validación de datos de inserción (BEFORE INSERT)
-------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION validar_cantidad_detalle()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    -- Regla de negocio: No se permiten ventas con cantidades menores o iguales a cero
    IF NEW.cantidad <= 0 THEN
        RAISE EXCEPTION 'Error de negocio: La cantidad del producto debe ser mayor a 0. Valor ingresado: %', NEW.cantidad;
    END IF;

    RETURN NEW; -- Permite continuar con la inserción segura de la fila
END;
$$;

CREATE TRIGGER trg_validar_cantidad_detalle
BEFORE INSERT ON Detalle_Pedido
FOR EACH ROW
EXECUTE FUNCTION validar_cantidad_detalle();


-------------------------------------------------------------------------------
-- B. FUNCIÓN: Cálculo acumulado (Uso permitido dentro de cláusulas SELECT)
-------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION total_pedido(p_id_pedido INT)
RETURNS DECIMAL(10,2)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total DECIMAL(10,2) := 0.00;
BEGIN
    -- Calcula el monto total neto del pedido multiplicando precio por cantidad
    SELECT COALESCE(SUM(precio * cantidad), 0.00)
    INTO v_total
    FROM Detalle_Pedido
    WHERE id_pedido = p_id_pedido;

    RETURN v_total;
END;
$$;


-------------------------------------------------------------------------------
-- C. STORED PROCEDURE: Operación comercial y control de transacciones (CALL)
-------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE cancelar_pedido(p_id_pedido INT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- 1. Eliminamos los detalles primero para evitar violaciones de clave foránea (FK)
    DELETE FROM Detalle_Pedido 
    WHERE id_pedido = p_id_pedido;

    -- 2. Eliminamos el pedido principal una vez liberada la integridad referencial
    DELETE FROM Pedido 
    WHERE id_pedido = p_id_pedido;

    -- 3. Confirmamos la persistencia atómica en el disco duro
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        -- Si ocurre cualquier error, revertimos todas las eliminaciones para mitigar corrupción de datos
        ROLLBACK;
        RAISE EXCEPTION 'Error crítico: No se pudo procesar la cancelación del pedido %. Operación abortada de forma segura.', p_id_pedido;
END;
$$;


-- ============================================================================
-- 5. SET DE DATOS DE PRUEBA (Para verificar el correcto funcionamiento)
-- ============================================================================
INSERT INTO Cliente VALUES (1, 'Esteban'), (2, 'Alejandro'), (3, 'Rodrigo');
INSERT INTO Pedido VALUES (10, 1, '2026-10-01 14:30:00'), (20, 2, '2026-10-02 09:15:00');

-- Inserciones válidas (Pasan el trigger con éxito)
INSERT INTO Detalle_Pedido VALUES (100, 10, 'Teclado Mecánico', 45000.00, 2);
INSERT INTO Detalle_Pedido VALUES (200, 20, 'Monitor 24', 120000.00, 1);


-- ============================================================================
-- EJERCICIOS DEL PUNTO 8 (Búsquedas en cadena de 3 tablas)
-- ============================================================================

-- 8.a. A partir de un dato de A (Nombre), conseguir uno de C (Producto)
SELECT c.producto 
FROM Cliente a 
INNER JOIN Pedido b ON a.id_cliente = b.id_cliente
INNER JOIN Detalle_Pedido c ON b.id_pedido = c.id_pedido
WHERE a.nombre = 'Esteban';

-- 8.b. A partir de un dato de C (Producto), conseguir uno de B (Fecha del Pedido)
SELECT b.fecha 
FROM Detalle_Pedido c
INNER JOIN Pedido b ON c.id_pedido = b.id_pedido
WHERE c.producto = 'Monitor 24';

-- 8.c. A partir de un dato de C (Producto), conseguir uno de A (Nombre del Cliente)
SELECT a.nombre 
FROM Detalle_Pedido c
INNER JOIN Pedido b ON c.id_pedido = b.id_pedido
INNER JOIN Cliente a ON b.id_cliente = a.id_cliente
WHERE c.producto = 'Teclado Mecánico';


-- ============================================================================
-- CONSULTAS AVANZADAS / PREGUNTAS DEL COLOQUIO
-- ============================================================================

-- Ejercicio 1: Clientes con más de 1 unidad comprada en total (Filtro con Agregación)
SELECT a.nombre, SUM(c.cantidad) AS Total_Gastado
FROM Cliente a 
INNER JOIN Pedido b ON a.id_cliente = b.id_cliente
INNER JOIN Detalle_Pedido c ON b.id_pedido = c.id_pedido
GROUP BY a.id_cliente, a.nombre 
HAVING SUM(c.cantidad) > 1;

-- Ejercicio 2: TODOS los clientes y sus cantidades (Uso de LEFT JOINs encadenados y COALESCE)
SELECT a.nombre, COALESCE(c.cantidad, 0) AS Cantidad_Productos
FROM Cliente a 
LEFT JOIN Pedido b ON a.id_cliente = b.id_cliente
LEFT JOIN Detalle_Pedido c ON b.id_pedido = c.id_pedido;

-- Ejercicio 3: Cliente con el pedido más caro de todos (Ordenamiento calculado con límite)
SELECT a.nombre, (c.precio * c.cantidad) AS Total_gastado
FROM Cliente a 
INNER JOIN Pedido b ON a.id_cliente = b.id_cliente
INNER JOIN Detalle_Pedido c ON b.id_pedido = c.id_pedido
ORDER BY (c.precio * c.cantidad) DESC 
LIMIT 1;