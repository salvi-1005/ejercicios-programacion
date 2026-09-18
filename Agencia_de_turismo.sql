--4)

DROP TABLE IF EXISTS Cliente CASCADE;
DROP TABLE IF EXISTS Telefono CASCADE;
DROP TABLE IF EXISTS Familiar CASCADE;
DROP TABLE IF EXISTS Guia_de_turismo CASCADE;
DROP TABLE IF EXISTS Tour CASCADE;
DROP TABLE IF EXISTS Reservas CASCADE;
DROP TABLE IF EXISTS Escalas CASCADE;
DROP TABLE IF EXISTS Especializado CASCADE;
DROP TABLE IF EXISTS Pagos CASCADE;
DROP TABLE IF EXISTS Cuotas CASCADE;
DROP TABLE IF EXISTS Ocupacion CASCADE;
DROP TABLE IF EXISTS Direccion CASCADE;
DROP TABLE IF EXISTS Modalidad CASCADE;
DROP TABLE IF EXISTS Plaza CASCADE;
DROP TABLE IF EXISTS Tour_Plaza CASCADE;

CREATE TABLE IF NOT EXISTS Ocupacion (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO Ocupacion VALUES
(1, 'Estudiante'),
(2, 'Contador'),
(3, 'Verdulero'),
(4, 'Abogado'),
(5, 'Medico');

SELECT * FROM Ocupacion WHERE Nombre = 'Abogado';
DELETE FROM Ocupacion WHERE Nombre = 'Medico';
SELECT * FROM Ocupacion;

CREATE TABLE IF NOT EXISTS Cliente (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    IdOcupacion INT,

	FOREIGN KEY (IdOcupacion)
	    REFERENCES Ocupacion(ID)
        );

INSERT INTO Cliente VALUES
(44816375, 'Salvador', 1),
(34691592, 'Roberto', 2),
(51897324, 'Nicolás', 3),
(23809424, 'Hugo Lopez', 2),
(59426835, 'Aurelio', null);

SELECT Ocupacion.Nombre, Cliente.ID, Cliente.Nombre 
FROM Ocupacion 
INNER JOIN Cliente ON Cliente.IdOcupacion = Ocupacion.ID;

--Como no hay ningun abogado, el left join me devuelve null en la columna de abogado

SELECT Ocupacion.Nombre, Cliente.ID, Cliente.Nombre 
FROM Ocupacion 
LEFT JOIN Cliente ON Cliente.IdOcupacion = Ocupacion.ID;

--Como Aurelio no tiene ocupación, el full outer join me devuelve null en la columna de abogado y también en la de Aurelio

SELECT Ocupacion.Nombre, Cliente.ID, Cliente.Nombre   
FROM Ocupacion 
FULL OUTER JOIN Cliente ON Cliente.IdOcupacion = Ocupacion.ID;

CREATE TABLE IF NOT EXISTS Direccion (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
	IdCliente INT,

	FOREIGN KEY (IdCliente)
	    REFERENCES Cliente(ID)
        );

INSERT INTO Direccion VALUES
(1, 'Nazarre 4711', 44816375),
(2, 'Bogotá 912', 34691592),
(3, 'Asunción 2453', 51897324),
(4, 'Riglos 824', 23809424);

CREATE TABLE IF NOT EXISTS Telefono (
    ID_telefono INT PRIMARY KEY,
    Codigo_cliente INT,
    Numero INT,
    
    FOREIGN KEY (Codigo_cliente)
        REFERENCES Cliente(ID)
        );

INSERT INTO Telefono VALUES
(1, 44816375, 41877247),
(2, 34691592, 33967824),
(3, 51897324, 65280631),
(4, 23809424, 25895642);
    
CREATE TABLE IF NOT EXISTS Familiar(
    ID INT PRIMARY KEY,
    ID_Cliente INT,
    Nombre VARCHAR(100),

    FOREIGN KEY (ID_Cliente)
        REFERENCES Cliente(ID)
    );

INSERT INTO Familiar VALUES
(1, 44816375, 'Paula'),
(2, 34691592, 'Hector'),
(3, 51897324, 'Agustin'),
(4, 23809424, 'Emiliano');

CREATE INDEX IF NOT EXISTS idx_nombre_cliente
ON Cliente(Nombre);

SELECT Cliente.ID, Cliente.Nombre, Ocupacion.Nombre AS ocupacion, Direccion.Nombre AS Direccion, 
Telefono.Numero AS Telefono, Familiar.Nombre AS Familiar_Cercano FROM Cliente 
INNER JOIN Ocupacion ON Ocupacion.ID = Cliente.IdOcupacion
INNER JOIN Direccion ON Direccion.IdCliente = Cliente.ID
INNER JOIN Telefono ON Telefono.Codigo_cliente = Cliente.ID
INNER JOIN Familiar ON Familiar.ID_Cliente = Cliente.ID
WHERE Cliente.Nombre = 'Nicolás';
	
CREATE TABLE Guia_de_turismo(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    SueldoBasico DOUBLE PRECISION,
    Importe_por_antiguedad DOUBLE PRECISION,
    Adicional_por_cada_tour DOUBLE PRECISION
);

INSERT INTO Guia_de_turismo VALUES
(26739083, 'Fabian', 30000.00, 10000.00, 20000.00),
(27803589, 'Rodrigo', 40000.00, 20000.00, 30000.00),
(28745629, 'Santiago', 50000.00, 30000.00, 40000.00);

--Guías que más cobraron:

SELECT ID, Nombre, SueldoBasico + Importe_por_antiguedad + Adicional_por_cada_tour AS Sueldo
FROM Guia_de_turismo ORDER BY Sueldo DESC LIMIT 1;

CREATE INDEX IF NOT EXISTS idx_nombre_guia
ON Guia_de_turismo(Nombre);

SELECT * FROM Guia_de_turismo WHERE Nombre = 'Fabian';

SELECT Nombre
FROM Guia_de_turismo
WHERE SueldoBasico > ALL (
    SELECT SueldoBasico
    FROM Guia_de_turismo
    WHERE ID = 26739083
);

SELECT Nombre
FROM Guia_de_turismo
WHERE SueldoBasico > ANY (
    SELECT SueldoBasico
    FROM Guia_de_turismo
);

CREATE TABLE IF NOT EXISTS Tour (
    Codigo INT PRIMARY KEY,
    Fecha_hora_salida TIMESTAMP,
    Fecha_hora_llegada TIMESTAMP,
    ID_Guia INT,
    
    FOREIGN KEY (ID_Guia)
        REFERENCES Guia_de_turismo(ID)
        );

INSERT INTO Tour VALUES
(1, '2026-09-07 15:30:00', '2026-09-07 17:30:00', 26739083),
(2, '2025-05-10 16:30:00', '2025-05-10 18:30:00', 27803589),
(3, '2024-03-20 17:30:00', '2024-03-20 19:30:00', 28745629),
(4, '2023-08-09 10:30:00', '2023-08-09 12:30:00', 28745629),
(5, '2022-10-19 11:30:00', '2022-10-19 13:30:00', 27803589),
(6, '2021-12-27 12:30:00', '2021-12-27 14:30:00', 28745629);

--Guías que más trabajaron

SELECT Guia_de_turismo.ID, Guia_de_turismo.Nombre, COUNT(*) AS Cantidad_de_tours_por_guia
FROM Tour INNER JOIN Guia_de_turismo ON Guia_de_turismo.ID = Tour.ID_Guia
GROUP BY Guia_de_turismo.ID, Guia_de_turismo.Nombre ORDER BY Cantidad_de_tours_por_guia DESC LIMIT 1;

CREATE TABLE IF NOT EXISTS Plaza (
    ID INT PRIMARY KEY,
	Nombre VARCHAR(100)
        );

INSERT INTO Plaza VALUES
(1, 'Plaza de Armas'),
(2, 'Plaza San Francisco'),
(3, 'Plaza Tupac Amaru'),
(4, 'Plaza San Pedro'),
(5, 'Plaza San Blas'),
(6, 'Plaza Arenales'),
(7, 'Plaza Richieri');

CREATE TABLE IF NOT EXISTS Tour_Plaza (
    IdTour INT, 
	IdPlaza INT,
	PRIMARY KEY (IdTour, IdPlaza),

	FOREIGN KEY (IdTour)
	    REFERENCES Tour(Codigo),

	FOREIGN KEY (IdPlaza)
	    REFERENCES Plaza(ID)
        );

INSERT INTO Tour_Plaza VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 2),
(4, 4),
(5, 1),
(5, 5),
(6, 4),
(6, 6),
(6, 7),
(6, 3);

--Cantidad de plazas visitadas por tour en orden descendente

SELECT IdTour, COUNT(*) AS Plazas_Visitadas_por_tour 
FROM Tour_Plaza
GROUP BY IdTour ORDER BY Plazas_Visitadas_por_tour DESC;

CREATE TABLE IF NOT EXISTS Reservas (
    Codigo INT PRIMARY KEY,
	Fecha_vencimiento TIMESTAMP,
    IdCliente INT,
    IdTour INT,
    
    FOREIGN KEY (IdCliente)
        REFERENCES Cliente(ID),
        
    FOREIGN KEY (IdTour)
        REFERENCES Tour(Codigo)
        ); 

INSERT INTO Reservas VALUES
(2658, '09-02-2026 15:30:00', 44816375, 1),
(4545, '05-03-2025 16:30:00', 34691592, 2),
(1745, '03-13-2024 17:30:00', 51897324, 3),
(3385, '08-02-2023 10:30:00', 44816375, 4),
(0936, '10-19-2022 11:30:00', 44816375, 5),
(4586, '12-27-2026 15:30:00', 34691592, 6),
(7936, '09-02-2026 15:30:00', 23809424, 1);

	
CREATE TABLE IF NOT EXISTS Escalas (
    ID INT PRIMARY KEY,
    ID_Tour INT,
    Dia_y_hora_de_llegada TIMESTAMP,
    Tiempo_de_estadia INT,

    FOREIGN KEY (ID_Tour)
        REFERENCES Tour(Codigo)
        );

INSERT INTO Escalas VALUES
(465, 1, '2026-09-07 16:30:00', 30),
(638, 2, '2025-05-10 17:30:00', 30),
(897, 3, '2024-03-20 18:30:00', 30),
(989, 4, '2023-08-09 11:30:00', 30),
(254, 5, '2022-10-19 12:30:00', 30),
(563, 6, '2021-12-27 13:30:00', 30);
    
CREATE TABLE IF NOT EXISTS Especializado (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
	ID_escala INT,

	FOREIGN KEY (ID_escala)
	    REFERENCES Escalas(ID)
        );

INSERT INTO Especializado VALUES
(24785308, 'Gustavo', 465),
(27198367, 'Fernando', 638),
(30765298, 'Alejandro', 897),
(21694765, 'Jorge', 989),
(25935728, 'Eladio', 254),
(23890154, 'Simon', 563);

CREATE TABLE IF NOT EXISTS Modalidad (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        ); 

INSERT INTO Modalidad VALUES
(1, 'Efectivo'),
(2, 'Transferencia'),
(3, 'Tarjeta');

CREATE TABLE IF NOT EXISTS Pagos (
    Codigo INT PRIMARY KEY,
    IdModalidad INT,
	IdCliente INT NOT NULL,
	IdTour INT,

	FOREIGN KEY (IdModalidad)
	    REFERENCES Modalidad(ID),

	FOREIGN KEY (IdCliente)
	    REFERENCES Cliente(ID),

	FOREIGN KEY (IdTour)
	    REFERENCES Tour(Codigo)
        ); 

INSERT INTO Pagos VALUES
(751, 2, 44816375, 1),
(454, 1, 34691592, 2),
(693, 2, 51897324, 3),
(898, 3, 44816375, 4),
(638, 1, 44816375, 5),
(741, 3, 34691592, 6),
(378, 1, 23809424, 1);
    
CREATE TABLE IF NOT EXISTS Cuotas (
    ID INT PRIMARY KEY,
    Valor INT,
	IdPago INT,
    
    FOREIGN KEY (IdPago)
        REFERENCES Pagos(Codigo)
        );

INSERT INTO Cuotas VALUES
(1, 400, 751),
(2, 600, 454),
(3, 800, 693),
(4, 400, 751),
(5, 600, 454),
(6, 800, 693),
(7, 800, 693),
(8, 400, 751),
(9, 600, 454),
(10, 800, 693),
(11, 400, 751);

--Personas que más viajaron

SELECT Cliente.ID, Cliente.Nombre, COUNT(*) AS Cantidad_Tours_Realizados FROM Cliente
INNER JOIN Pagos ON Pagos.IdCliente = Cliente.ID
GROUP BY Cliente.ID, Cliente.Nombre ORDER BY Cantidad_Tours_Realizados DESC LIMIT 1;

--Viajes de Hugo López para el mes que viene

SELECT Cliente.ID, Cliente.Nombre, Tour.Codigo AS CodigoTour, Tour.Fecha_hora_salida
FROM Cliente
INNER JOIN Pagos ON Pagos.IdCliente = Cliente.ID
INNER JOIN Tour ON Tour.Codigo = Pagos.IdTour
WHERE Cliente.Nombre = 'Hugo Lopez'
AND EXTRACT(YEAR FROM Tour.Fecha_hora_salida) =
    EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
AND EXTRACT(MONTH FROM Tour.Fecha_hora_salida) =
    EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month');

--Reservas de Hugo López para el mes que viene

SELECT Cliente.ID, Cliente.Nombre, Reservas.Codigo AS Codigo_Reserva, Reservas.Fecha_vencimiento
FROM Cliente
INNER JOIN Reservas ON Reservas.IdCliente = Cliente.ID
WHERE Cliente.Nombre = 'Hugo Lopez'
AND EXTRACT(YEAR FROM Reservas.Fecha_vencimiento) =
    EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
AND EXTRACT(MONTH FROM Reservas.Fecha_vencimiento) =
    EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month');

--ALTER TABLE Tours DROP COLUMN ID_Escala;

SELECT * FROM Cliente;

SELECT * FROM Telefono;

SELECT * FROM Familiar;

SELECT * FROM Tour;

SELECT Nombre,
    SueldoBasico +
    Importe_por_antiguedad +
    Adicional_por_cada_tour AS Sueldo
        FROM Guia_de_turismo;

SELECT * FROM Guia_de_turismo;

SELECT * FROM Escalas;

SELECT * FROM Especializado;

SELECT * FROM Pagos;

--Sueldo DOUBLE PRECISION 
	--GENERATED ALWAYS AS (
        --SueldoBasico +
        --Importe_por_antiguedad +
        --Adicional_por_cada_tour
    --) STORED

--Procedure

CREATE OR REPLACE PROCEDURE mostrar_tour(
    p_codigo INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '%',
    (
        SELECT CONCAT(
            'Tour: ',
            Codigo,
            ' Salida: ',
            Fecha_hora_salida
        )
        FROM Tour
        WHERE Codigo = p_codigo
    );
END;
$$;

CALL mostrar_tour(1);

CREATE OR REPLACE PROCEDURE mostrar_guia(
    guia_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '%',
    (
        SELECT CONCAT(
            'Guia: ',
            Nombre,
            ' DNI: ',
            ID
        )
        FROM Guia_de_turismo
        WHERE ID = guia_id
    );
END;
$$;

CALL mostrar_guia(27803589);

--Function

CREATE OR REPLACE FUNCTION calcular_sueldo(
    p_id_guia INT
)
RETURNS DOUBLE PRECISION
LANGUAGE plpgsql
AS $$
DECLARE
    sueldo_total DOUBLE PRECISION;
BEGIN
    SELECT
        SueldoBasico +
        Importe_por_antiguedad +
        Adicional_por_cada_tour
    INTO sueldo_total
    FROM Guia_de_turismo
    WHERE ID = p_id_guia;

    RETURN sueldo_total;
END;
$$;

 SELECT calcular_sueldo(28745629);

CREATE OR REPLACE FUNCTION cantidad_plazas_tour(
    id_tour INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    cant_plazas INT;
BEGIN
    SELECT
        COUNT(*)
    INTO cant_plazas
    FROM Tour_Plaza
    WHERE IdTour = id_tour;

    RETURN cant_plazas;
END;
$$;

SELECT cantidad_plazas_tour(1);

--Trigger

CREATE OR REPLACE FUNCTION crear_cuota()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO Cuotas(
        ID,
        Valor,
        IdPago
    )
    VALUES(
        (SELECT COALESCE(MAX(ID),0)+1
         FROM Cuotas),
        500,
        NEW.Codigo
    );

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_crear_cuota
AFTER INSERT
ON Pagos
FOR EACH ROW
EXECUTE FUNCTION crear_cuota();

INSERT INTO Pagos
VALUES (999,1,44816375,1);

SELECT * FROM Pagos;
SELECT * FROM Cuotas;

CREATE OR REPLACE FUNCTION validar_cuota()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    IF NEW.Valor < 0 THEN
        RAISE EXCEPTION
        'La cuota no puede ser negativa';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_validar_cuota
BEFORE INSERT OR UPDATE
ON Cuotas
FOR EACH ROW
EXECUTE FUNCTION validar_cuota();

--INSERT INTO Cuotas VALUES
--(13, -400, 999);

CREATE OR REPLACE FUNCTION validar_fechas()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    Fecha_salida TIMESTAMP;
    Fecha_llegada TIMESTAMP;
BEGIN

    SELECT
    Fecha_hora_salida,
    Fecha_hora_llegada
    INTO
    Fecha_salida,
    Fecha_llegada
    FROM Tour
    WHERE Codigo = NEW.ID_Tour;
	
    IF NEW.Dia_y_hora_de_llegada < Fecha_salida OR NEW.Dia_y_hora_de_llegada > Fecha_llegada THEN
        RAISE EXCEPTION
        'La escala tiene que ser dentro del horario del tour';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_validar_fecha
BEFORE INSERT OR UPDATE
ON Escalas
FOR EACH ROW
EXECUTE FUNCTION validar_fechas();

--INSERT INTO Escalas VALUES
--(333, 1, '2026-09-07 22:30:00', 30);

CREATE OR REPLACE FUNCTION validar_aumento_salario()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.SueldoBasico > OLD.SueldoBasico * 1.10 THEN
        RAISE EXCEPTION 'Operación cancelada: El aumento del salario no puede superar el 10%% del salario actual ($%)', OLD.SueldoBasico;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validar_aumento
BEFORE UPDATE ON Guia_de_turismo
FOR EACH ROW
EXECUTE FUNCTION validar_aumento_salario();

--UPDATE Guia_de_turismo SET SueldoBasico = 150000 WHERE ID = 26739083;

CREATE OR REPLACE FUNCTION actualizar_fecha_salida()
RETURNS TRIGGER AS $$
BEGIN
    NEW.Fecha_hora_salida := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_fecha_salida
BEFORE UPDATE ON Tour
FOR EACH ROW
EXECUTE FUNCTION actualizar_fecha_salida();

UPDATE Tour SET Fecha_hora_llegada = '2026-10-01 17:30:00' WHERE Codigo = 1;

SELECT * FROM Tour;

--extras

CREATE OR REPLACE PROCEDURE mostrar_reservas_cliente(numero_cliente INT)
LANGUAGE plpgsql
AS $$
DECLARE
    reserva_actual RECORD;
BEGIN

    FOR reserva_actual IN
        SELECT
            C.Nombre AS Cliente,
            R.Codigo 
        FROM ReservaS R 
		INNER JOIN Cliente C ON C.ID = R.IdCliente
        WHERE C.ID = numero_cliente
    LOOP

        RAISE NOTICE
        'Reserva: %, Nombre: %',
        reserva_actual.Codigo,
        reserva_actual.Cliente;

    END LOOP;

END;
$$;
CALL mostrar_reservas_cliente(44816375);

