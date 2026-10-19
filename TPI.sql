DROP TABLE IF EXISTS Actividad CASCADE;
DROP TABLE IF EXISTS Auditoria_Ventas_Bar CASCADE;
DROP TABLE IF EXISTS Bar CASCADE;
DROP TABLE IF EXISTS Cancha CASCADE;
DROP TABLE IF EXISTS Categoria_Bar CASCADE;
DROP TABLE IF EXISTS Categoria_Socio CASCADE;
DROP TABLE IF EXISTS Compra_Proveedor CASCADE;
DROP TABLE IF EXISTS Control_Accesos CASCADE;
DROP TABLE IF EXISTS Cuota_Mensual CASCADE;
DROP TABLE IF EXISTS Deporte CASCADE;
DROP TABLE IF EXISTS Detalle_Compra_Proveedor CASCADE;
DROP TABLE IF EXISTS Detalle_Pedido CASCADE;
DROP TABLE IF EXISTS Estado_Cancha CASCADE;
DROP TABLE IF EXISTS Estado_Pedido CASCADE;
DROP TABLE IF EXISTS Especialidad CASCADE;
DROP TABLE IF EXISTS Horario_Actividad CASCADE;
DROP TABLE IF EXISTS Inscripcion_Actividad CASCADE;
DROP TABLE IF EXISTS Mozo_Empleado CASCADE;
DROP TABLE IF EXISTS Pago_Reserva CASCADE;
DROP TABLE IF EXISTS Pedido CASCADE;
DROP TABLE IF EXISTS Producto CASCADE;
DROP TABLE IF EXISTS Producto_Bar CASCADE;
DROP TABLE IF EXISTS Profesor CASCADE;
DROP TABLE IF EXISTS Profesor_Actividad CASCADE;
DROP TABLE IF EXISTS Proveedor_Bar CASCADE;
DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Socio CASCADE;
DROP TABLE IF EXISTS Telefonos_Profesor CASCADE;
DROP TABLE IF EXISTS Telefonos_Proveedor CASCADE;
DROP TABLE IF EXISTS Telefonos_Socio CASCADE;
DROP TABLE IF EXISTS Tipo_Cancha CASCADE;
DROP TABLE IF EXISTS Tipo_Movimiento CASCADE;
DROP TABLE IF EXISTS Tipo_Telefono CASCADE;
DROP TABLE IF EXISTS Turno_Disponible CASCADE;


CREATE TABLE Categoria_Socio (
    id_categoria_socio INT PRIMARY KEY,
	descripcion TEXT,
	precio_cuota DECIMAL
    );

CREATE TABLE Socio (
    id_socio INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    id_categoria_socio INT NOT NULL,
	
    FOREIGN KEY (id_categoria_socio) 
	    REFERENCES Categoria_Socio(id_categoria_socio)
);

CREATE TABLE Tipo_Telefono (
    id_tipo_telefono INT PRIMARY KEY,
	nombre_tipo_telefono VARCHAR(100)
);

CREATE TABLE Telefonos_Socio (
    id_telefono INT PRIMARY KEY,
    id_socio INT NOT NULL,
    numero VARCHAR(30) NOT NULL,
    id_tipo_telefono INT,
	
    FOREIGN KEY (id_socio) 
	    REFERENCES Socio(id_socio) ON DELETE CASCADE,

	FOREIGN KEY (id_tipo_telefono) 
	    REFERENCES Tipo_Telefono(id_tipo_telefono) ON DELETE CASCADE
);

CREATE TABLE Cuota_Mensual (
    id_cuota INT PRIMARY KEY,
	id_socio INT,
	mes INT,
	anio INT,
	fecha_pago TIMESTAMP,
	monto_pagado DECIMAL,
	pagado BOOLEAN,

	FOREIGN KEY (id_socio)
	    REFERENCES Socio(id_socio)
);

CREATE TABLE Tipo_Movimiento (
    id_tipo_movimiento INT PRIMARY KEY,
	nombre_tipo_movimiento VARCHAR(100)
);

CREATE TABLE Control_Accesos (
    id_acceso INT PRIMARY KEY,
	id_socio INT,
	fecha_hora TIMESTAMP,
	id_tipo_movimiento INT,
	
	FOREIGN KEY (id_socio)
	    REFERENCES Socio(id_socio),
		
	FOREIGN KEY (id_tipo_movimiento)
	    REFERENCES Tipo_Movimiento(id_tipo_movimiento)
);

CREATE TABLE Deporte (
    id_deporte INT PRIMARY KEY,
	nombre_deporte VARCHAR(100)
);

CREATE TABLE Tipo_Cancha (
    id_tipo_cancha INT PRIMARY KEY,
	id_deporte INT,
	precio_por_hora DECIMAL,

	FOREIGN KEY (id_deporte)
	    REFERENCES Deporte(id_deporte)
);

CREATE TABLE Estado_Cancha (
    id_estado_cancha INT PRIMARY KEY,
	nombre_estado_cancha VARCHAR(100)
);

CREATE TABLE Cancha (
    id_cancha INT PRIMARY KEY,
	nombre VARCHAR(100),
	id_tipo_cancha INT,
	id_estado_cancha INT,

    FOREIGN KEY (id_tipo_cancha)
	    REFERENCES Tipo_Cancha(id_tipo_cancha),

	FOREIGN KEY (id_estado_cancha)
	    REFERENCES Estado_Cancha(id_estado_cancha)
);

CREATE TABLE Turno_Disponible (
    id_turno INT PRIMARY KEY,
	hora_inicio TIME,
	hora_fin TIME
);

CREATE TABLE Reserva (
    id_reserva INT PRIMARY KEY,
	id_socio INT,
	id_cancha INT,
	fecha_reserva TIMESTAMP,
	id_turno INT,

	FOREIGN KEY (id_socio)
	    REFERENCES Socio(id_socio),

	FOREIGN KEY (id_cancha)
	    REFERENCES Cancha(id_cancha),

	FOREIGN KEY (id_turno)
	    REFERENCES Turno_Disponible(id_turno)
);

CREATE TABLE Pago_Reserva (
    id_pago_reserva INT PRIMARY KEY,
	id_reserva INT,
	monto DECIMAL,
	fecha_pago TIMESTAMP,

	FOREIGN KEY (id_reserva)
	    REFERENCES Reserva(id_reserva)
);

CREATE TABLE Especialidad (
    id_especialidad INT PRIMARY KEY,
	nombre_especialidad VARCHAR(100)
);

CREATE TABLE Profesor (
    id_profesor INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    id_especialidad INT,
	
    FOREIGN KEY (id_especialidad) 
	    REFERENCES Especialidad(id_especialidad)
);

CREATE TABLE Telefonos_Profesor (
    id_telefono INT PRIMARY KEY,
    id_profesor INT NOT NULL,
    numero VARCHAR(30) NOT NULL,
    id_tipo_telefono INT NOT NULL, 
	
    FOREIGN KEY (id_profesor) 
	    REFERENCES Profesor(id_profesor) ON DELETE CASCADE,

	FOREIGN KEY (id_tipo_telefono) 
	    REFERENCES Tipo_Telefono(id_tipo_telefono) ON DELETE CASCADE
);

CREATE TABLE Actividad (
    id_actividad INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    costo_extra DECIMAL(10,2) NOT NULL
);

CREATE TABLE Profesor_Actividad (
    id_profesor INT NOT NULL,
    id_actividad INT NOT NULL,
    PRIMARY KEY (id_profesor, id_actividad), -- Clave primaria compuesta
    FOREIGN KEY (id_profesor) REFERENCES Profesor(id_profesor) ON DELETE CASCADE,
    FOREIGN KEY (id_actividad) REFERENCES Actividad(id_actividad) ON DELETE CASCADE
);

CREATE TABLE Horario_Actividad (
    id_horario INT PRIMARY KEY,
	id_actividad INT,
	dia_semana INT,
	hora_inicio INT,

	FOREIGN KEY (id_actividad)
	    REFERENCES Actividad(id_actividad)
);

CREATE TABLE Inscripcion_Actividad (
    id_inscripcion INT PRIMARY KEY,
	id_socio INT,
	id_actividad INT,
	fecha_alta TIMESTAMP,

	FOREIGN KEY (id_socio)
	    REFERENCES Socio(id_socio),

	FOREIGN KEY (id_actividad)
	    REFERENCES Actividad(id_actividad)
);

CREATE TABLE Mozo_Empleado (
    id_empleado INT PRIMARY KEY,
	nombre VARCHAR(100),
	apellido VARCHAR(100),
	Legajo INT UNIQUE
);

CREATE TABLE Categoria_Bar (
    id_categoria_bar INT PRIMARY KEY,
	nombre VARCHAR(100)
);

-- 1. Nueva tabla para identificar los distintos bares/puntos de venta del club
CREATE TABLE Bar (
    id_bar INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL, -- Ej: 'Buffet Central', 'Kiosco Canchas'
    ubicacion VARCHAR(150)
);

-- 2. Tabla Productos_Bar (Limpia, sin datos de stock local ni de un bar fijo)
CREATE TABLE Producto (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio_venta DECIMAL(10,2) NOT NULL,
    id_categoria_bar INT NOT NULL,
	
    FOREIGN KEY (id_categoria_bar) 
	    REFERENCES Categoria_Bar(id_categoria_bar)
);

-- 3. Nueva Entidad Asociativa: Productos_Bares (Maneja el stock por cada punto de venta)
CREATE TABLE Producto_Bar (
    id_bar INT NOT NULL,
    id_producto INT NOT NULL,
    stock_actual INT NOT NULL DEFAULT 0,
    stock_minimo INT NOT NULL DEFAULT 5,
    PRIMARY KEY (id_bar, id_producto),
	
    FOREIGN KEY (id_bar) 
	    REFERENCES Bar(id_bar) ON DELETE CASCADE,
		
    FOREIGN KEY (id_producto)
	    REFERENCES Producto(id_producto) ON DELETE CASCADE
);

CREATE TABLE Estado_Pedido (
    id_estado_pedido INT PRIMARY KEY,
	nombre_estado_pedido VARCHAR(100)
);

CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY,
	id_socio INT,
	id_bar INT,
	id_empleado INT NOT NULL,
	fecha_hora_pedido TIMESTAMP NOT NULL,
	nro_mesa INT NOT NULL,
	id_estado_pedido INT NOT NULL,

	FOREIGN KEY (id_socio)
	    REFERENCES Socio(id_socio),

	FOREIGN KEY (id_bar)
	    REFERENCES Bar(id_bar),

	FOREIGN KEY (id_empleado)
	    REFERENCES Mozo_Empleado(id_empleado),

	FOREIGN KEY (id_estado_pedido)
	    REFERENCES Estado_Pedido(id_estado_pedido)
);

CREATE TABLE Detalle_Pedido (
    id_detalle INT PRIMARY KEY,
	id_pedido INT,
	id_producto INT,
	cantidad INT,
	precio_unitario_historico DECIMAL,

	FOREIGN KEY (id_pedido)
	    REFERENCES Pedido(id_pedido),

	FOREIGN KEY (id_producto)
	    REFERENCES Producto(id_producto)
);

CREATE TABLE Proveedor_Bar (
    id_proveedor INT PRIMARY KEY,
	razon_social VARCHAR(100),
	cuit VARCHAR(20)
);

CREATE TABLE Telefonos_Proveedor (
    id_telefono INT PRIMARY KEY,
    id_proveedor INT NOT NULL,
    numero VARCHAR(30) NOT NULL,
    id_tipo_telefono INT NOT NULL,
	
    FOREIGN KEY (id_proveedor) 
	    REFERENCES Proveedor_Bar(id_proveedor) ON DELETE CASCADE,

	FOREIGN KEY (id_tipo_telefono) 
	    REFERENCES Tipo_Telefono(id_tipo_telefono) ON DELETE CASCADE
);

CREATE TABLE Compra_Proveedor (
    id_compra INT PRIMARY KEY,
	id_proveedor INT,
	fecha TIMESTAMP,
	monto_total DECIMAL,

	FOREIGN KEY (id_proveedor)
	    REFERENCES Proveedor_Bar(id_proveedor)
);

CREATE TABLE Detalle_Compra_Proveedor (
    id_detalle_compra INT PRIMARY KEY,
	id_compra INT,
	id_producto INT,
	cantidad INT,
	precio_costo DECIMAL,

	FOREIGN KEY (id_compra)
	    REFERENCES Compra_Proveedor(id_compra),

	FOREIGN KEY (id_producto)
	    REFERENCES Producto(id_producto)
);

CREATE TABLE Auditoria_Ventas_Bar (
    id_auditoria INT PRIMARY KEY,
	id_pedido INT,
	monto_total DECIMAL,
	fecha_auditoria TIMESTAMP,
	usuario VARCHAR(100),

	FOREIGN KEY (id_pedido)
	    REFERENCES Pedido(id_pedido)
);

CREATE OR REPLACE FUNCTION total_ingresos_cancha(
    p_id_cancha INT,
    p_mes INT,
    p_anio INT
)
RETURNS DECIMAL(10,2)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total_recaudado DECIMAL(10,2) := 0.00;
BEGIN
    -- Sumamos los pagos asociados a las reservas de la cancha en el mes y año filtrado
    SELECT COALESCE(SUM(pr.monto), 0.00)
    INTO v_total_recaudado
    FROM Reserva r
    INNER JOIN Pago_Reserva pr ON r.id_reserva = pr.id_reserva
    WHERE r.id_cancha = p_id_cancha
      AND EXTRACT(MONTH FROM r.fecha_reserva) = p_mes
      AND EXTRACT(YEAR FROM r.fecha_reserva) = p_anio;

    RETURN v_total_recaudado;
END;
$$;

-- Ejemplo de uso permitido en un SELECT (Reporte mensual de canchas):
-- SELECT id_cancha, nombre, total_ingresos_cancha(id_cancha, 10, 2026) FROM Cancha;


-------------------------------------------------------------------------------
-- TRIGGER: Descuento Automatizado de Stock por Punto de Venta (AFTER INSERT)
-------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION descontar_stock_bar()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_bar INT;
BEGIN
    -- 1. Buscamos el id_bar al que pertenece el pedido que se está vendiendo
    SELECT id_bar INTO v_id_bar
    FROM Pedido
    WHERE id_pedido = NEW.id_pedido;

    -- 2. Restamos el stock actual en la tabla asociativa para ESE bar y ESE producto
    UPDATE Producto_Bar
    SET stock_actual = stock_actual - NEW.cantidad
    WHERE id_bar = v_id_bar AND id_producto = NEW.id_producto;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_descontar_stock_bar
AFTER INSERT ON Detalle_Pedido
FOR EACH ROW
EXECUTE FUNCTION descontar_stock_bar();

CREATE OR REPLACE FUNCTION auditoria_pedidos_bar_log()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_monto_total DECIMAL(10,2) := 0.00;
BEGIN
    -- 1. Calculamos el monto total acumulado de los detalles del pedido afectado
    SELECT COALESCE(SUM(precio_unitario_historico * cantidad), 0.00)
    INTO v_monto_total
    FROM Detalle_Pedido
    WHERE id_pedido = NEW.id_pedido;

    -- 2. Insertamos el registro de control inmutable utilizando las variables globales del motor
    INSERT INTO Auditoria_Ventas_Bar (id_auditoria, id_pedido, monto_total, fecha_auditoria, usuario)
    VALUES (
        NEXTVAL('secuencia_auditoria_bar'), -- Supone que usas una secuencia o SERIAL para la PK
        NEW.id_pedido, 
        v_monto_total, 
        NOW(), 
        current_user -- Descubre automáticamente la cuenta que disparó el cambio
    );

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_auditoria_ventas_bar
AFTER UPDATE ON Pedido
FOR EACH ROW
WHEN (OLD.id_estado_pedido <> NEW.id_estado_pedido) -- Solo audita si cambió el estado del pedido
EXECUTE FUNCTION auditoria_pedidos_bar_log();

CREATE OR REPLACE PROCEDURE generar_reserva(
    p_id_reserva INT,
    p_id_socio INT,
    p_id_cancha INT,
    p_fecha TIMESTAMP, -- Cambiado a TIMESTAMP para que coincida exactamente con tu tabla
    p_id_turno INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_ya_existe INT;
BEGIN
    -- 1. VALIDACIÓN: Contamos si ya existe una reserva para esa misma cancha, fecha y turno
    SELECT COUNT(*) INTO v_ya_existe
    FROM Reserva
    WHERE id_cancha = p_id_cancha 
      AND fecha_reserva = p_fecha 
      AND id_turno = p_id_turno;

    -- 2. CONTROL DE NEGOCIO: Si el conteo es mayor a 0, la cancha está ocupada en ese momento
    IF v_ya_existe > 0 THEN
        RAISE EXCEPTION 'Error de reserva: La cancha ya se encuentra ocupada en la fecha % y turno %.', p_fecha, p_id_turno;
    END IF;

    -- 3. OPERACIÓN: Si está libre, insertamos la nueva reserva de forma segura
    INSERT INTO Reserva (id_reserva, id_socio, id_cancha, fecha_reserva, id_turno)
    VALUES (p_id_reserva, p_id_socio, p_id_cancha, p_fecha, p_id_turno);

    -- Confirmamos los cambios en el disco duro de manera atómica
    

EXCEPTION
    WHEN OTHERS THEN
        -- Si ocurre una violación de FK o cualquier fallo, cancelamos la operación para evitar datos corruptos
       
        RAISE; -- Propaga el mensaje de error original para que pgAdmin lo muestre en pantalla
END;
$$;


CREATE OR REPLACE PROCEDURE generar_cuotas_mensuales(
    p_mes INT,
    p_anio INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_registro_socio RECORD;
    v_id_cuota_actual INT;
BEGIN
    -- Obtenemos el próximo ID secuencial base para las cuotas
    SELECT COALESCE(MAX(id_cuota), 0) INTO v_id_cuota_actual FROM Cuota_Mensual;

    -- Cursor/Bucle que recorre todos los socios e identifica el precio de su categoría
    FOR v_registro_socio IN 
        SELECT s.id_socio, cs.precio_cuota 
        FROM Socio s
        INNER JOIN Categoria_Socio cs ON s.id_categoria_socio = cs.id_categoria_socio
    LOOP
        v_id_cuota_actual := v_id_cuota_actual + 1;

        -- Insertamos el registro de deuda (fecha_pago nace en NULL y pagado en FALSE)
        INSERT INTO Cuota_Mensual (id_cuota, id_socio, mes, anio, fecha_pago, monto_pagado, pagado)
        VALUES (v_id_cuota_actual, v_registro_socio.id_socio, p_mes, p_anio, NULL, v_registro_socio.precio_cuota, FALSE);
    END LOOP;

    -- Confirmamos el bloque masivo de datos de forma atómica en el disco duro
    

EXCEPTION
    WHEN OTHERS THEN
        -- Si un solo socio falla o está corrupto, la transacción aborta al 100% por seguridad
   
        RAISE EXCEPTION 'Error crítico en la facturación masiva. Proceso revertido.';
END;
$$;

-- Para ejecutarlo cada primer día del mes:
-- CALL generar_cuotas_mensuales(10, 2026);

-- ============================================================================
-- SET DE DATOS DE PRUEBA (Módulos Socios, Canchas, Profesores y Bar)
-- ============================================================================

-- 1. MÓDULO SOCIOS (Tablas Maestras e Iniciales)
INSERT INTO Categoria_Socio (id_categoria_socio, descripcion, precio_cuota) VALUES
(1, 'Menor (Hasta 12 años)', 8000.00),
(2, 'Cadete (13 a 17 años)', 12000.00),
(3, 'Activo Pleno (Adulto)', 18000.00);

INSERT INTO Socio (id_socio, nombre, apellido, dni, fecha_nacimiento, id_categoria_socio) VALUES
(1, 'Esteban', 'Pérez', '45123456', '2003-05-14', 3),
(2, 'Alejandro', 'Gómez', '48987654', '2008-11-22', 2),
(3, 'Rodrigo', 'Rodríguez', '35441637', '1990-02-09', 3);

INSERT INTO Tipo_Telefono (id_tipo_telefono, nombre_tipo_telefono) VALUES 
(1, 'Fijo'),
(2, 'Movil');

INSERT INTO Telefonos_Socio (id_telefono, id_socio, numero, id_tipo_telefono) VALUES
(1, 1, '1123456789', 2),
(2, 1, '47551234', 1),
(3, 2, '1198765432', 2);

-- 2. MÓDULO CANCHAS Y INSTALACIONES
INSERT INTO Deporte (id_deporte, nombre_deporte) VALUES
(1, 'Fútbol 5'),
(2, 'Tenis');

INSERT INTO Tipo_Cancha (id_tipo_cancha, id_deporte, precio_por_hora) VALUES
(10, 1, 15000.00), -- Fútbol 5
(20, 2, 10000.00); -- Tenis

INSERT INTO Estado_Cancha (id_estado_cancha, nombre_estado_cancha) VALUES
(1, 'Disponible'),
(2, 'En Mantenimiento');

INSERT INTO Cancha (id_cancha, nombre, id_tipo_cancha, id_estado_cancha) VALUES
(1, 'Cancha de Fútbol 5 Techada', 10, 1),
(2, 'Cancha de Tenis Polvo de Ladrillo', 20, 1);

INSERT INTO Turno_Disponible (id_turno, hora_inicio, hora_fin) VALUES
(1, '18:00:00', '19:00:00'),
(2, '19:00:00', '20:00:00'),
(3, '20:00:00', '21:00:00');


-- 3. MÓDULO BAR / BUFFET MULTIPUNTO
INSERT INTO Categoria_Bar (id_categoria_bar, nombre) VALUES
(1, 'Cafetería y Desayunos'),
(2, 'Bebidas y Refrescos');

INSERT INTO Bar (id_bar, nombre, ubicacion) VALUES
(1, 'Buffet Central Sede Grande', 'Planta Baja Sector Gimnasio'),
(2, 'Kiosco de la Pileta', 'Sector Natatorio Exterior');

INSERT INTO Mozo_Empleado (id_empleado, nombre, Apellido, Legajo) VALUES
(100, 'Carlos', 'López', 4021),
(200, 'Lucía', 'Fernández', 5510);

INSERT INTO Estado_Pedido (id_estado_pedido, nombre_estado_pedido) VALUES
(1, 'Pendiente de Preparación'),
(2, 'Confirmado y Entregado');

-- Productos Base del Club
INSERT INTO Producto (id_producto, nombre, precio_venta, id_categoria_bar) VALUES
(1, 'Café en Jarrito', 2500.00, 1),
(2, 'Gaseosa Cola 500ml', 3000.00, 2),
(3, 'Agua Mineral 500ml', 2200.00, 2);

-- Distribución de Stock inicial por Bar (Tabla asociativa)
INSERT INTO Producto_Bar (id_bar, id_producto, stock_actual, stock_minimo) VALUES
(1, 1, 100, 10), -- En el Buffet Central hay 100 cafés
(1, 2, 50, 5),   -- En el Buffet Central hay 50 gaseosas
(2, 2, 12, 5),   -- En el Kiosco de la Pileta hay sólo 12 gaseosas
(2, 3, 80, 10);  -- En el Kiosco de la Pileta hay 80 aguas

-- Ejecución 1: Reservamos la cancha 1 para el socio 1 el 15 de Octubre en el Turno 2 (Debería dar ÉXITO)
CALL generar_reserva(10, 1, 1, '2026-10-15', 2);

-- Ejecución 2: El socio 3 intenta reservar la MISMA cancha 1 el MISMO día en el MISMO turno (Debería lanzar tu EXCEPCIÓN)
--CALL generar_reserva(11, 3, 1, '2026-10-15', 2);

-- Insertamos la cabecera de un pedido para el Buffet Central (id_bar = 1) tomado por Carlos
INSERT INTO Pedido (id_pedido, id_bar, id_socio, id_empleado, fecha_hora_pedido, nro_mesa, id_estado_pedido) VALUES
(50, 1, 1, 100, NOW(), 4, 1);

-- Antes de insertar los detalles, revisemos el stock actual de gaseosas (id_producto = 2) en el Buffet Central (Debería ser 50)
SELECT stock_actual FROM Producto_Bar WHERE id_bar = 1 AND id_producto = 2;

-- Insertamos un detalle del pedido vendiendo 3 gaseosas (El trigger se disparará automáticamente)
INSERT INTO Detalle_Pedido (id_detalle, id_pedido, id_producto, cantidad, precio_unitario_historico) VALUES
(1001, 50, 2, 3, 3000.00);

-- Volvemos a revisar el stock en Producto_Bar (Debería haber bajado automáticamente a 47)
SELECT stock_actual FROM Producto_Bar WHERE id_bar = 1 AND id_producto = 2;

-- Ejecutamos la facturación para todo el club para Octubre de 2026
CALL generar_cuotas_mensuales(10, 2026);

-- Verificamos la tabla (Deberían aparecer automáticamente 3 registros de cuotas calculados según la categoría de cada socio)
SELECT * FROM Cuota_Mensual;

-- ============================================================================
-- 1. CONFIGURACIÓN COMPLEMENTARIA PARA LA AUDITORÍA
-- ============================================================================
CREATE SEQUENCE IF NOT EXISTS secuencia_auditoria_bar START WITH 1;

-- ============================================================================
-- 2. DESARROLLO DEL COMPONENTE PROGRAMABLE (Punto 9)
-- ============================================================================
CREATE OR REPLACE FUNCTION auditoria_pedidos_bar_log()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_monto_total DECIMAL(10,2) := 0.00;
BEGIN
    -- 1. Calculamos el monto total acumulado de los detalles del pedido afectado
    SELECT COALESCE(SUM(precio_unitario_historico * cantidad), 0.00)
    INTO v_monto_total
    FROM Detalle_Pedido
    WHERE id_pedido = NEW.id_pedido;

    -- 2. Insertamos la bitácora utilizando las variables globales del motor (current_user)
    INSERT INTO Auditoria_Ventas_Bar (id_auditoria, id_pedido, monto_total, fecha_auditoria, usuario)
    VALUES (
        NEXTVAL('secuencia_auditoria_bar'), 
        NEW.id_pedido, 
        v_monto_total, 
        NOW(), 
        current_user -- Captura automáticamente la cuenta de pgAdmin que realiza el cambio
    );

    RETURN NEW;
END;
$$;

-- Creamos el Trigger sobre tu tabla Pedido
CREATE TRIGGER trg_auditoria_ventas_bar
AFTER UPDATE ON Pedido
FOR EACH ROW
WHEN (OLD.id_estado_pedido <> NEW.id_estado_pedido) -- Solo se activa si cambia el estado (ej: de Pendiente a Entregado)
EXECUTE FUNCTION auditoria_pedidos_bar_log();

