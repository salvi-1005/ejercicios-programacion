-- ============================================================================
-- LIMPIEZA DE TABLAS RESTRUCTURADAS (Ecosistema de 13 Tablas Definitivas)
-- ============================================================================
DROP TABLE IF EXISTS Detalle_Pedido CASCADE;
DROP TABLE IF EXISTS Pedido CASCADE;
DROP TABLE IF EXISTS Producto CASCADE;
DROP TABLE IF EXISTS Marca CASCADE;
DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Cancha CASCADE;
DROP TABLE IF EXISTS Tipo_Cancha CASCADE;
DROP TABLE IF EXISTS Control_Accesos CASCADE;
DROP TABLE IF EXISTS Profesor CASCADE;
DROP TABLE IF EXISTS Cuota_Mensual CASCADE;
DROP TABLE IF EXISTS Socio CASCADE;
DROP TABLE IF EXISTS Categoria_Socio CASCADE;
DROP TABLE IF EXISTS Especialidad CASCADE;

-- Eliminación de tipos ENUM previos por si se recarga el script
DROP TYPE IF EXISTS tipo_estado_cancha CASCADE;
DROP TYPE IF EXISTS tipo_estado_reserva CASCADE;
DROP TYPE IF EXISTS tipo_estado_pedido CASCADE;
DROP TYPE IF EXISTS tipo_estado_profesor CASCADE;

-- ============================================================================
-- 1. CREACIÓN DE TIPOS PERSONALIZADOS (ENUMs)
-- ============================================================================
CREATE TYPE tipo_estado_cancha AS ENUM ('Disponible', 'En Mantenimiento');
CREATE TYPE tipo_estado_reserva AS ENUM ('Pendiente', 'Confirmado', 'Rechazado');
CREATE TYPE tipo_estado_pedido AS ENUM ('Pendiente', 'Entregado', 'Cancelado');
CREATE TYPE tipo_estado_profesor AS ENUM ('Disponible', 'Ocupado', 'Baja');

-- ============================================================================
-- 2. MÓDULO PERSONAS Y DEUDAS (5 Tablas)
-- ============================================================================

-- Tabla 1: Categorías de los Socios
CREATE TABLE Categoria_Socio (
    id_categoria_socio INT PRIMARY KEY,
    descripcion TEXT,
    precio_cuota DECIMAL NOT NULL
);

-- Tabla 2: Padrón Unificado de Socios (Campos históricos migrados a Control_Accesos)
CREATE TABLE Socio (
    id_socio INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(100) UNIQUE NOT NULL,
    fecha_nacimiento TIMESTAMP NOT NULL,
    email VARCHAR(100) NOT NULL,
    id_categoria_socio INT NOT NULL,
    FOREIGN KEY (id_categoria_socio) REFERENCES Categoria_Socio(id_categoria_socio)
);

-- Tabla 3: Cuenta Corriente y Deudores del Club
CREATE TABLE Cuota_Mensual (
    id_cuota INT PRIMARY KEY,
    id_socio INT NOT NULL,
    mes INT NOT NULL CHECK (mes BETWEEN 1 AND 12),
    anio INT NOT NULL CHECK (anio >= 2000),
    fecha_pago TIMESTAMP, 
    monto_pagado DECIMAL, 
    pagado BOOLEAN NOT NULL, 
    FOREIGN KEY (id_socio) REFERENCES Socio(id_socio)
);

-- Tabla 4: Especialidad de los Profesores
CREATE TABLE Especialidad (
    id_especialidad INT PRIMARY KEY,
    descripcion TEXT,
    nombre_especialidad VARCHAR(100) NOT NULL
);

-- Tabla 5: Profesores / Docentes del Club
CREATE TABLE Profesor (
    id_profesor INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(100) UNIQUE NOT NULL,
    id_especialidad INT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100),
    estado tipo_estado_profesor NOT NULL DEFAULT 'Disponible',
    FOREIGN KEY (id_especialidad) REFERENCES Especialidad(id_especialidad)
);

-- Tabla 6: Historial de Molinetes Unificado (Maneja Socios y Profesores de forma flexible)
CREATE TABLE Control_Accesos (
    id_acceso INT PRIMARY KEY,
    id_socio INT,      -- Nullable si accede un profesor
    id_profesor INT,   -- Nullable si accede un socio
    fecha_hora_entrada TIMESTAMP NOT NULL,
    fecha_hora_salida TIMESTAMP,
    FOREIGN KEY (id_socio) REFERENCES Socio(id_socio),
    FOREIGN KEY (id_profesor) REFERENCES Profesor(id_profesor),
    -- CONTROL DE INTEGRIDAD: Bloquea registros fantasmas en el molinete
    CONSTRAINT chk_persona_acceso CHECK (id_socio IS NOT NULL OR id_profesor IS NOT NULL)
);

-- ============================================================================
-- 3. MÓDULO INSTALACIONES Y RESERVAS (3 Tablas)
-- ============================================================================

-- Tabla 7: Catálogo de Configuraciones de Infraestructura y Costos
CREATE TABLE Tipo_Cancha (
    id_tipo_cancha INT PRIMARY KEY,
    nombre_tipo_cancha VARCHAR(100) NOT NULL,
    precio_por_hora DECIMAL NOT NULL
);

-- Tabla 8: Canchas Físicas del Club
CREATE TABLE Cancha (
    id_cancha INT PRIMARY KEY,
    nombre_cancha VARCHAR(100) NOT NULL,
    id_tipo_cancha INT NOT NULL,
    estado_cancha tipo_estado_cancha NOT NULL DEFAULT 'Disponible',
    FOREIGN KEY (id_tipo_cancha) REFERENCES Tipo_Cancha(id_tipo_cancha)
);

-- Tabla 9: Registro Transaccional de Alquileres, Clases y Pagos Congelados
CREATE TABLE Reserva (
    id_reserva INT PRIMARY KEY,
    fecha_reserva DATE NOT NULL,
    id_socio INT,       -- NULLABLE para permitir entrenamientos de profesores solos
    id_cancha INT NOT NULL,
    id_profesor INT,    -- NULLABLE para partidos comunes entre amigos
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    estado tipo_estado_reserva NOT NULL DEFAULT 'Pendiente',
    monto_total DECIMAL(10,2) NOT NULL, -- Preserva el precio histórico calculado de la reserva
    fecha_pago TIMESTAMP,
    pagado BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_socio) REFERENCES Socio(id_socio),
    FOREIGN KEY (id_cancha) REFERENCES Cancha(id_cancha),
    FOREIGN KEY (id_profesor) REFERENCES Profesor(id_profesor),
    -- CONTROL DE INTEGRIDAD: Asegura que el turno pertenezca a alguien
    CONSTRAINT chk_dueno_reserva CHECK (id_socio IS NOT NULL OR id_profesor IS NOT NULL)
);

-- ============================================================================
-- 4. MÓDULO BUFFET / BAR UNIFICADO (3 Tablas)
-- ============================================================================

-- Tabla 10: Insertamos las marcas en su tabla independiente
CREATE TABLE Marca (
    id_marca INT PRIMARY KEY,
    nombre_marca VARCHAR(100) NOT NULL 
);

-- Tabla 11. Insertamos los productos apuntando a sus respectivas marcas
CREATE TABLE Producto (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio_venta DECIMAL NOT NULL,
    id_marca INT NOT NULL, 
    stock_actual INT NOT NULL DEFAULT 0 CHECK (stock_actual >= 0),
    FOREIGN KEY (id_marca) REFERENCES Marca(id_marca)
);

-- Tabla 12: Comandas del Bar (Soporta Clientes Cruzados y Externos)
CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY,
    fecha_hora_pedido TIMESTAMP NOT NULL DEFAULT NOW(),
    nro_mesa INT NOT NULL,
    estado_pedido tipo_estado_pedido NOT NULL DEFAULT 'Pendiente',
    id_socio INT,
    id_profesor INT,
    FOREIGN KEY (id_socio) REFERENCES Socio(id_socio),
    FOREIGN KEY (id_profesor) REFERENCES Profesor(id_profesor)
);

-- Tabla 13: Renglones del Ticket de Venta
CREATE TABLE Detalle_Pedido (
    id_detalle INT PRIMARY KEY,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario_historico DECIMAL NOT NULL, -- Resguardo histórico de caja
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

-- ============================================================================
-- INSERCIÓN DE DATOS DE PRUEBA (Consistencia entre las 13 Tablas)
-- ============================================================================

-- 1. TABLAS MAESTRAS DE CONFIGURACIÓN
INSERT INTO Categoria_Socio (id_categoria_socio, descripcion, precio_cuota) VALUES
(1, 'Menor (Hasta 12 años)', 8000.00),
(2, 'Activo Pleno (Adulto)', 18000.00),
(3, 'Vitalicio', 0.00);

INSERT INTO Especialidad (id_especialidad, descripcion, nombre_especialidad) VALUES
(10, 'Instrucción en Superficies lentas', 'Tenis de Campo'),
(20, 'Entrenamiento de Alto Rendimiento', 'Natación y Rescate'),
(30, 'Acondicionamiento Físico', 'Preparación Física General');

-- 2. REGISTROS DE PADRONES
INSERT INTO Socio (id_socio, nombre, apellido, dni, fecha_nacimiento, email, id_categoria_socio) VALUES
(1, 'Esteban', 'Pérez', '45123456', '2003-05-14 00:00:00', 'esteban.perez@email.com', 2),
(2, 'Alejandro', 'Gómez', '48987654', '2008-11-22 00:00:00', 'ale.gomez@email.com', 1),
(3, 'Rodrigo', 'Rodríguez', '35441637', '1990-02-09 00:00:00', 'rodrigo.rod@email.com', 3);

INSERT INTO Profesor (id_profesor, nombre, apellido, dni, id_especialidad, fecha_nacimiento, email, estado) VALUES
(100, 'Carlos', 'López', '25111222', 10, '1978-04-12', 'carlos.lopez@polideportivo.com', 'Disponible'),
(200, 'Lucía', 'Fernández', '30444555', 20, '1985-09-23', 'lucia.f@polideportivo.com', 'Disponible');

-- 3. HISTORIAL DE MOLINETES (Manejo histórico independiente de la tabla maestra)
INSERT INTO Control_Accesos (id_acceso, id_socio, id_profesor, fecha_hora_entrada, fecha_hora_salida) VALUES
(1, 1, NULL, '2026-10-18 08:00:00', '2026-10-18 10:00:00'), -- Entrada de un Socio
(2, NULL, 100, '2026-10-18 07:45:00', NULL);                  -- Entrada activa de un Profesor (Fichada)

-- 4. CUENTAS CORRIENTES (Octubre 2026)
INSERT INTO Cuota_Mensual (id_cuota, id_socio, mes, anio, fecha_pago, monto_pagado, pagado) VALUES
(1001, 1, 9, 2026, NULL, NULL, FALSE), -- Esteban arrastra deuda de Septiembre
(1002, 2, 10, 2026, '2026-10-05 14:22:10', 8000.00, TRUE),
(1003, 3, 10, 2026, NULL, 0.00, TRUE); -- Vitalicio exento

-- 5. INFRAESTRUCTURA Y CRONOGRAMA DE TURNOS
INSERT INTO Tipo_Cancha (id_tipo_cancha, nombre_tipo_cancha, precio_por_hora) VALUES
(1, 'Fútbol 5 Techado', 15000.00),
(2, 'Tenis Polvo de Ladrillo', 10000.00);

INSERT INTO Cancha (id_cancha, nombre_cancha, id_tipo_cancha, estado_cancha) VALUES
(1, 'Cancha de Fútbol nro 1', 1, 'Disponible'),
(2, 'Cancha de Tenis Central', 2, 'Disponible'),
(3, 'Cancha de Tenis Auxiliar', 2, 'En Mantenimiento');

-- Carga transaccional de reservas (Casos: Socio Solo, Clase Particular y Profesor Solo)
INSERT INTO Reserva (id_reserva, fecha_reserva, id_socio, id_cancha, id_profesor, hora_inicio, hora_fin, estado, monto_total, fecha_pago, pagado) VALUES
-- Caso 1: Turno de fútbol de amigos del Socio 1 (Profesor en NULL)
(5001, '2026-10-19', 1, 1, NULL, '19:00:00', '20:00:00', 'Confirmado', 15000.00, '2026-10-18 12:00:00', TRUE),
-- Caso 2: Alumno Gómez toma clase con el Profesor López ($10.000 la hora x 1.5 horas = $15.000)
(5002, '2026-10-19', 2, 2, 100, '18:00:00', '19:30:00', 'Confirmado', 15000.00, NULL, FALSE),
-- Caso 3: El Profesor López reserva la pista sola para su práctica personal (Socio en NULL y precio bonificado)
(5003, '2026-10-20', NULL, 2, 100, '09:00:00', '10:30:00', 'Confirmado', 0.00, NULL, TRUE);
-- 6. CATÁLOGO CON MARCAS Y TICKETS DEL BUFFET CENTRAL
INSERT INTO Marca (id_marca, nombre_marca) VALUES
(1, 'Bonafide'),
(2, 'Coca-Cola'),
(3, 'Kin');

INSERT INTO Producto (id_producto, nombre, precio_venta, id_marca, stock_actual) VALUES
(1, 'Café en Jarrito', 2500.00, 1, 120),
(2, 'Gaseosa Cola 500ml', 3000.00, 2, 45),
(3, 'Agua Mineral 500ml', 2200.00, 3, 8);
-- Comandas cruzadas con enums de cocina unificados
INSERT INTO Pedido (id_pedido, fecha_hora_pedido, nro_mesa, estado_pedido, id_socio, id_profesor) VALUES
(10, '2026-10-18 13:05:00', 3, 'Pendiente', 1, NULL),
(20, '2026-10-18 13:12:00', 5, 'Entregado', NULL, 100),
(30, '2026-10-18 13:25:00', 1, 'Pendiente', NULL, NULL);
INSERT INTO Detalle_Pedido (id_detalle, cantidad, precio_unitario_historico, id_pedido, id_producto) VALUES
(9001, 2, 3000.00, 10, 2),
(9002, 1, 2500.00, 10, 1),
(9003, 2, 2500.00, 20, 1),
(9004, 1, 2200.00, 30, 3);
-- ============================================================================
-- 3 CONSULTAS DE UNIÓN SOLICITADAS POR EL PUNTO 8 (INNER JOINs Puros)
-- ============================================================================
-- 8.a. A partir de un dato de A (Socio), conseguir uno de C (ID Detalle de Pedido)
SELECT d.id_detalle
FROM Socio s
INNER JOIN Pedido p ON p.id_socio = s.id_socio
INNER JOIN Detalle_Pedido d ON d.id_pedido = p.id_pedido;
-- 8.b. A partir de un dato de C (Detalle), conseguir uno de B (Pedido) con conteo de renglones
SELECT p.id_pedido, COALESCE(COUNT(d.id_detalle), 0) AS cantidad_lineas_pedido
FROM Detalle_Pedido d
INNER JOIN Pedido p ON p.id_pedido = d.id_pedido
GROUP BY p.id_pedido;
-- 8.c. A partir de un dato de C (Precio Histórico en el Detalle), conseguir uno de A (Datos del Socio)
SELECT DISTINCT s.id_socio, s.nombre, s.apellido
FROM Detalle_Pedido d
INNER JOIN Pedido p ON p.id_pedido = d.id_pedido
INNER JOIN Socio s ON s.id_socio = p.id_socio
WHERE d.precio_unitario_historico = 3000.00;
-- ============================================================================
-- 4. COMPONENTES PROGRAMABLES AVANZADOS (Punto 9)
-- ============================================================================
-- Stored Procedure: Agenda administrativa de clases particulares en el club
CREATE OR REPLACE PROCEDURE mostrar_reservas_con_profesor()
LANGUAGE plpgsql
AS $$
DECLARE
v_fila RECORD;
v_contador INT := 0;
BEGIN
RAISE NOTICE '======================================================================';
RAISE NOTICE '       REPORTE DE CLASES PARTICULARES Y RESERVAS CON INSTRUCTOR        ';
RAISE NOTICE '======================================================================';
FOR v_fila IN
SELECT r.id_reserva,
s.nombre AS socio_nom, s.apellido AS socio_ape,
c.nombre_cancha AS cancha_nom,
p.nombre AS prof_nom, p.apellido AS prof_ape,
r.fecha_reserva, r.hora_inicio, r.hora_fin
FROM Reserva r
INNER JOIN Socio s ON r.id_socio = s.id_socio
INNER JOIN Cancha c ON r.id_cancha = c.id_cancha
INNER JOIN Profesor p ON r.id_profesor = p.id_profesor
ORDER BY r.fecha_reserva, r.hora_inicio
LOOP
v_contador := v_contador + 1;
RAISE NOTICE 'Reserva Nro: % | Fecha: % (% a %)',
v_fila.id_reserva, v_fila.fecha_reserva, v_fila.hora_inicio, v_fila.hora_fin;
RAISE NOTICE '   - Cancha: %', v_fila.cancha_nom;
RAISE NOTICE '   - Socio Alumno: % %', v_fila.socio_nom, v_fila.socio_ape;
RAISE NOTICE '   - Profesor Instructor: % %', v_fila.prof_nom, v_fila.prof_ape;
RAISE NOTICE '----------------------------------------------------------------------';
END LOOP;
IF v_contador = 0 THEN
RAISE NOTICE 'No se registran reservas con profesor asignado en el sistema.';
ELSE
RAISE NOTICE 'Fin del reporte. Total de clases particulares encontradas: %', v_contador;
END IF;
RAISE NOTICE '======================================================================';
END;
$$;

CREATE OR REPLACE PROCEDURE cancelar_pedido(p_id_pedido INT)
LANGUAGE plpgsql
AS $$
DECLARE
    v_fila RECORD;
    v_existe_pedido BOOLEAN;
    v_estado_actual VARCHAR(50);
BEGIN
    -- 1. Verificamos si el pedido existe y cuál es su estado actual
    SELECT EXISTS(SELECT 1 FROM Pedido WHERE id_pedido = p_id_pedido) INTO v_existe_pedido;
    
    IF NOT v_existe_pedido THEN
        RAISE EXCEPTION 'Error: El Pedido Nro % no existe en el sistema.', p_id_pedido;
    END IF;

    SELECT estado_pedido::VARCHAR INTO v_estado_actual FROM Pedido WHERE id_pedido = p_id_pedido;

    -- 2. Si el pedido ya estaba cancelado, no hacemos nada
    IF v_estado_actual = 'Cancelado' THEN
        RAISE NOTICE 'El Pedido Nro % ya se encuentra cancelado.', p_id_pedido;
        RETURN;
    END IF;

    -- 3. Recorremos los renglones del detalle para DEVOLVER el stock al buffet
    FOR v_fila IN 
        SELECT id_producto, cantidad 
        FROM Detalle_Pedido 
        WHERE id_pedido = p_id_pedido
    LOOP
        UPDATE Producto
        SET stock_actual = stock_actual + v_fila.cantidad
        WHERE id_producto = v_fila.id_producto;
    END LOOP;

    -- 4. Modificamos el estado del pedido a 'Cancelado'
    UPDATE Pedido
    SET estado_pedido = 'Cancelado'
    WHERE id_pedido = p_id_pedido;

    RAISE NOTICE '¡Éxito! El Pedido Nro % ha sido cancelado y su mercadería fue reincorporada al stock.', p_id_pedido;
END;
$$;

SELECT nombre, stock_actual FROM Producto WHERE id_producto = 3; -- Devuelve 8 unidades

CALL cancelar_pedido(30);
-- Verás el mensaje: NOTICE: ¡Éxito! El Pedido Nro 30 ha sido cancelado...

SELECT estado_pedido FROM Pedido WHERE id_pedido = 30; -- Ahora figura 'Cancelado'
SELECT nombre, stock_actual FROM Producto WHERE id_producto = 3; -- ¡Ahora figura 9 unidades!

-- Función Escalar: Calcula el aforo presencial de socios en tiempo real desde el historial
CREATE OR REPLACE FUNCTION socios_actuales_en_club()
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
v_cantidad_presentes INT := 0;
BEGIN
-- Contamos las filas del historial donde se registró entrada pero aún no se marcó la salida
SELECT COUNT(DISTINCT id_socio)
INTO v_cantidad_presentes
FROM Control_Accesos
WHERE id_socio IS NOT NULL AND fecha_hora_salida IS NULL;
RETURN v_cantidad_presentes;
END;
$$;

CREATE OR REPLACE FUNCTION canchas_libres_actualmente()
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    v_cantidad_libres INT := 0;
    v_fecha_hoy DATE;
    v_hora_hoy TIME;
BEGIN
    -- 1. Capturamos el momento exacto del reloj del servidor
    v_fecha_hoy := NOW()::DATE;
    v_hora_hoy := NOW()::TIME;

    -- 2. Contamos usando LEFT JOIN puro para evitar subconsultas
    SELECT COUNT(c.id_cancha) 
    INTO v_cantidad_libres
    FROM Cancha c
    LEFT JOIN Reserva r ON c.id_cancha = r.id_cancha 
                       AND r.fecha_reserva = v_fecha_hoy
                       AND r.estado = 'Confirmado'
                       AND v_hora_hoy BETWEEN r.hora_inicio AND r.hora_fin
    WHERE c.estado_cancha = 'Disponible'
      AND r.id_reserva IS NULL; -- Si el ID de reserva es NULL, significa que la cancha está LIBRE ahora

    RETURN v_cantidad_libres;
END;
$$;

SELECT canchas_libres_actualmente() AS total_canchas_libres_hoy;


-- Trigger Function: Valida deudas financieras del socio en la base de datos antes de destrabar el molinete
CREATE OR REPLACE FUNCTION validar_ingreso_molinete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
v_debe_cuotas BOOLEAN;
BEGIN
-- Ejecuta la validación solo si el registro corresponde al ingreso de un Socio
IF NEW.id_socio IS NOT NULL THEN
SELECT EXISTS (
SELECT 1
FROM Cuota_Mensual
WHERE id_socio = NEW.id_socio AND pagado = FALSE
) INTO v_debe_cuotas;
IF v_debe_cuotas THEN
RAISE EXCEPTION 'Acceso denegado: El socio ID % registra cuotas impagas vencidas en su cuenta corriente.',
NEW.id_socio;
END IF;
END IF;
RETURN NEW;
END;
$$;
CREATE TRIGGER trg_control_acceso_molinete
BEFORE INSERT ON Control_Accesos
FOR EACH ROW
EXECUTE FUNCTION validar_ingreso_molinete();

-- 1. Función del Trigger que valida que el precio no cambie
CREATE OR REPLACE FUNCTION proteger_precio_historico_pedido()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    -- Comparamos el valor que se intenta guardar (NEW) con el que ya existía (OLD)
    IF NEW.precio_unitario_historico <> OLD.precio_unitario_historico THEN
        -- Si son distintos, lanzamos un error crítico y abortamos el UPDATE
        RAISE EXCEPTION 'Error de Integridad: No está permitido modificar el precio unitario histórico de un pedido cerrado (Detalle ID %).', 
                        OLD.id_detalle;
    END IF;

    RETURN NEW; -- Si no cambió el precio, permite guardar otros campos (como la cantidad)
END;
$$;

-- 2. El disparador asociado a tu tabla Detalle_Pedido
CREATE TRIGGER trg_bloquear_cambio_precio_historico
BEFORE UPDATE OF precio_unitario_historico ON Detalle_Pedido
FOR EACH ROW
EXECUTE FUNCTION proteger_precio_historico_pedido();

-- Intentemos "dibujar" el ticket 9001 (que era de $3000) para decir que se cobró $1000
--UPDATE Detalle_Pedido 
--SET precio_unitario_historico = 1000.00 
--WHERE id_detalle = 9001;


CREATE OR REPLACE FUNCTION proteger_monto_total_reserva()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    -- Comparamos el valor que se intenta guardar (NEW) con el que ya existía (OLD)
    IF NEW.monto_total <> OLD.monto_total THEN
        -- Si son distintos, lanzamos un error crítico y abortamos el UPDATE
        RAISE EXCEPTION 'Error de Integridad: No está permitido modificar el monto total histórico de una reserva cerrada (Reserva ID %).', 
                        OLD.id_reserva;
    END IF;

    RETURN NEW; -- Si no cambió el precio, permite guardar otros campos (como la cantidad)
END;
$$;

-- 2. El disparador asociado a tu tabla Reserva
CREATE TRIGGER trg_bloquear_cambio_monto_total
BEFORE UPDATE OF monto_total ON Reserva
FOR EACH ROW
EXECUTE FUNCTION proteger_monto_total_reserva();

-- Intentemos "dibujar" el ticket 9001 (que era de $3000) para decir que se cobró $1000
--UPDATE Reserva 
--SET monto_total = 100000.00 
--WHERE id_reserva = 5001;

CREATE OR REPLACE FUNCTION proteger_monto_pagado_cuota()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    -- Comparamos el valor que se intenta guardar (NEW) con el que ya existía (OLD)
    IF NEW.monto_pagado <> OLD.monto_pagado THEN
        -- Si son distintos, lanzamos un error crítico y abortamos el UPDATE
        RAISE EXCEPTION 'Error de Integridad: No está permitido modificar el monto pagado histórico de una cuota cerrada (Cuota ID %).', 
                        OLD.id_cuota;
    END IF;

    RETURN NEW; -- Si no cambió el precio, permite guardar otros campos (como la cantidad)
END;
$$;

-- 2. El disparador asociado a tu tabla Cuota_Mensual
CREATE TRIGGER trg_bloquear_cambio_monto_pagado
BEFORE UPDATE OF monto_pagado ON Cuota_Mensual
FOR EACH ROW
EXECUTE FUNCTION proteger_monto_pagado_cuota();

-- Intentemos "dibujar" el ticket 9001 (que era de $3000) para decir que se cobró $1000
--UPDATE Cuota_Mensual
--SET monto_pagado = 10000.00 
--WHERE id_cuota = 1002;

-- ============================================================================
-- EJECUCIÓN DE PRUEBAS DE COMPONENTES
-- ============================================================================
CALL mostrar_reservas_con_profesor();
SELECT socios_actuales_en_club() AS total_socios_adentro;
-- Prueba del Trigger (Simulación del Socio 1 intentando ingresar arrastrando deuda de Septiembre):
-- UNCOMMENT PARA PROBAR EL ERROR EN CONSOLA:
-- INSERT INTO Control_Accesos (id_acceso, id_socio, id_profesor, fecha_hora_entrada, fecha_hora_salida) VALUES (3, 1, NULL, NOW(), NULL);

-- ============================================================================
-- SIMULACIÓN EN VIVO: CONTROL DE PRECIOS HISTÓRICOS VS ACTUALES
-- ============================================================================

-- 1. El club aplica un aumento de tarifa al Café en la tabla maestra
UPDATE Producto 
SET precio_venta = 3500.00 
WHERE id_producto = 1; -- El café ahora pasa a costar $3500 en lista

-- 2. El Profesor Carlos (ID 100) va hoy al buffet y pide 1 café al nuevo precio
-- Creamos una nueva comanda (Pedido 40)
INSERT INTO Pedido (id_pedido, fecha_hora_pedido, nro_mesa, estado_pedido, id_socio, id_profesor) VALUES
(40, NOW(), 4, 'Entregado', NULL, 100);

-- Se registra el renglón congelando el nuevo precio de venta actual ($3500)
INSERT INTO Detalle_Pedido (id_detalle, cantidad, precio_unitario_historico, id_pedido, id_producto) VALUES
(9005, 1, 3500.00, 40, 1);

-- ============================================================================
-- 3. AUDITORÍA FINAL: LA CONSULTA QUE DEMUESTRA LA 3FN
-- ============================================================================
SELECT 
    p.id_pedido,
    p.fecha_hora_pedido::DATE AS fecha_venta,
    COALESCE(s.apellido, pr.apellido, 'Cliente Externo') AS cliente,
    prod.nombre AS articulo,
    prod.precio_venta AS precio_lista_HOY,               -- Lo que vale el café hoy
    d.precio_unitario_historico AS precio_PAGADO_MOMENTO -- Lo que realmente pagó el cliente
FROM Detalle_Pedido d
INNER JOIN Pedido p ON d.id_pedido = p.id_pedido
INNER JOIN Producto prod ON d.id_producto = prod.id_producto
LEFT JOIN Socio s ON p.id_socio = s.id_socio
LEFT JOIN Profesor pr ON p.id_profesor = pr.id_profesor
WHERE prod.id_producto = 1 -- Filtramos solo para ver el historial del Café
ORDER BY p.id_pedido;

-- ============================================================================
-- SIMULACIÓN EN VIVO: CONTROL HISTÓRICO DE RESERVAS Y CUOTAS
-- ============================================================================

-- ----------------------------------------------------------------------------
-- PARTE 1: ESCENARIO DE LA CANCHA (Aumento de tarifa de Tenis)
-- ----------------------------------------------------------------------------

-- 1. El club aumenta la tarifa de la hora de 'Tenis Polvo de Ladrillo' de $10.000 a $14.000
UPDATE Tipo_Cancha 
SET precio_por_hora = 14000.00 
WHERE id_tipo_cancha = 2;

-- 2. El Profesor López (ID 100) reserva HOY una cancha para dar otra clase de 1 hora y media
-- Al nuevo precio, el costo total debería ser: 1.5 horas x $14.000 = $21.000
INSERT INTO Reserva (id_reserva, fecha_reserva, id_socio, id_cancha, id_profesor, hora_inicio, hora_fin, estado, monto_total, fecha_pago, pagado) VALUES
(5004, NOW()::DATE, 3, 2, 100, '15:00:00', '16:30:00', 'Confirmado', 21000.00, NOW(), TRUE);


-- ----------------------------------------------------------------------------
-- PARTE 2: ESCENARIO DE LA CUOTA MENSUAL (Aumento de la Cuota Social)
-- ----------------------------------------------------------------------------

-- 1. El club aumenta la cuota de la categoría 'Activo Pleno (Adulto)' de $18.000 a $25.000
UPDATE Categoria_Socio 
SET precio_cuota = 25000.00 
WHERE id_categoria_socio = 2;

-- 2. Se genera la nueva cuota del mes de Octubre para el Socio 1 (Esteban), quien pertenece a esta categoría
INSERT INTO Cuota_Mensual (id_cuota, id_socio, mes, anio, fecha_pago, monto_pagado, pagado) VALUES
(1004, 1, 10, 2026, NOW(), 25000.00, TRUE);


-- ============================================================================
-- AUDITORÍA: LAS CONSULTAS DE COMPROBACIÓN (DEMOSTRACIÓN DE LA 3FN)
-- ============================================================================

-- REPORTE A: Muestra que la Reserva 5002 mantiene sus $15.000 originales de Octubre
SELECT 
    r.id_reserva,
    r.fecha_reserva,
    tc.nombre_tipo_cancha AS tipo_de_cancha,
    tc.precio_por_hora AS precio_lista_HOY, -- Nueva tarifa de lista ($14.000)
    r.monto_total AS precio_COBRADO_MOMENTO    -- Precio histórico congelado ($15.000)
FROM Reserva r
INNER JOIN Cancha c ON r.id_cancha = c.id_cancha
INNER JOIN Tipo_Cancha tc ON c.id_tipo_cancha = tc.id_tipo_cancha
WHERE tc.id_tipo_cancha = 2
ORDER BY r.id_reserva;

-- REPORTE B: Muestra que la Cuota de Septiembre de Esteban se mantiene inmutable a pesar del aumento
SELECT 
    cm.id_cuota,
    cm.mes AS mes_periodo,
    cat.descripcion AS categoria,
    cat.precio_cuota AS cuota_lista_HOY,    -- Nueva tarifa de cuota ($25.000)
    cm.monto_pagado AS monto_PAGADO_HISTORICO -- Mantendrá NULL o el valor antiguo ($8000/$0) según el insert
FROM Cuota_Mensual cm
INNER JOIN Socio s ON cm.id_socio = s.id_socio
INNER JOIN Categoria_Socio cat ON s.id_categoria_socio = cat.id_categoria_socio
WHERE s.id_socio = 2 -- Evaluamos al Socio 2 para ver su cuota de Septiembre ($8000) vs el HOY ($25000)
ORDER BY cm.id_cuota;
