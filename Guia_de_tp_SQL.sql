--3)

DROP TABLE IF EXISTS Socios CASCADE;
DROP TABLE IF EXISTS Peliculas CASCADE;
DROP TABLE IF EXISTS Alquiler CASCADE;
DROP TABLE IF EXISTS Compra CASCADE;

CREATE TABLE IF NOT EXISTS Socios (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100)
        );

INSERT INTO Socios VALUES
(44816375, 'Salvador', 'Dangelo'),
(05607618, 'Roberto', 'Fernandez'),
(54897324, 'Nicolás', 'Sanchez');

CREATE TABLE IF NOT EXISTS Peliculas (
    ID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    Anio INT,
    Genero VARCHAR(100),
    StockVendido INT,
    StockAlquilado INT
        );

INSERT INTO Peliculas VALUES
(537, 'La Odisea De Los Giles', 2019, 'Policial', 4, 5),
(638, 'Los Fantasmas De Scrooge', 2009, 'Navidad', 3, 4),
(846, 'El Secreto De Sus Ojos', 1996, 'Policial', 6, 7),
(365, 'El Robo Del Siglo', 2020, 'Policial', 8, 9),
(942, 'Toy Story 5', 2026, 'Infantil', 4, 5),
(457, 'El Exorcista', 2005, 'Terror', 4, 5);

CREATE TABLE IF NOT EXISTS Alquiler (
    ID INT PRIMARY KEY,
    Inicio TIMESTAMP,
    Fin TIMESTAMP,
	ID_socio INT,
	ID_pelicula INT,

	FOREIGN KEY (ID_socio)
	    REFERENCES Socios(ID),

	FOREIGN KEY (ID_pelicula)
	    REFERENCES Peliculas(ID) 
        );

INSERT INTO Alquiler VALUES
(3927, '2026-04-24 16:30:00', '2026-04-27 16:30:00', 44816375, 365),
(4586, '2026-03-18 13:07:00', '2026-03-21 13:07:00', 05607618, 537),
(5824, '2026-02-09 08:24:00', '2026-02-12 08:24:00', 54897324, 457);

CREATE TABLE IF NOT EXISTS Compra (
    ID INT PRIMARY KEY,
    Fecha_compra TIMESTAMP,
	ID_socio INT,
	ID_pelicula INT,

	FOREIGN KEY (ID_socio)
	    REFERENCES Socios(ID),

	FOREIGN KEY (ID_pelicula)
	    REFERENCES Peliculas(ID)
        );

INSERT INTO Compra VALUES
(5742, '2025-10-14 19:34:00', 44816375, 638),
(8637, '2025-08-29 15:57:00', 05607618, 846),
(7265, '2025-12-17 11:42:00', 54897324, 942);

SELECT * FROM Compra INNER JOIN Socios
ON Socios.ID = Compra.ID_socio;

SELECT * FROM Compra RIGHT JOIN Peliculas
ON Peliculas.ID = Compra.ID_pelicula;

SELECT * FROM Alquiler FULL OUTER JOIN Peliculas
ON Peliculas.ID = Alquiler.ID_pelicula WHERE Peliculas.ID IS NULL OR Alquiler.ID_pelicula IS NULL;

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

--5)

DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Vuelo CASCADE;
DROP TABLE IF EXISTS Avion CASCADE;
DROP TABLE IF EXISTS Aerolinea CASCADE;
DROP TABLE IF EXISTS Aeropuerto CASCADE;
DROP TABLE IF EXISTS Ciudad CASCADE;
DROP TABLE IF EXISTS Mostrador CASCADE;
DROP TABLE IF EXISTS Aeropuerto_Aerolinea CASCADE;
DROP TABLE IF EXISTS Pista CASCADE;
DROP TABLE IF EXISTS UsoPista CASCADE;
DROP TABLE IF EXISTS Pasajero CASCADE;
DROP TABLE IF EXISTS TipoMostrador CASCADE;
DROP TABLE IF EXISTS TipoAvion CASCADE;
DROP TABLE IF EXISTS TipoVuelo CASCADE;
DROP TABLE IF EXISTS TipoPista CASCADE;
DROP TABLE IF EXISTS TipoDocumento CASCADE;

CREATE TABLE IF NOT EXISTS Ciudad(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO Ciudad VALUES 
(1, 'Buenos Aires'),
(2, 'Lima'),
(3, 'Cusco'),
(4, 'Madrid'),
(5, 'Shanghai');

CREATE TABLE IF NOT EXISTS Aeropuerto(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    IdCiudad INT,

    FOREIGN KEY (IdCiudad)
        REFERENCES Ciudad(ID)
        );

INSERT INTO Aeropuerto VALUES 
(1, 'Pistarini', 1),
(2, 'Jorge Chávez', 2),
(3, 'Alejandro Velasco', 3),
(4, 'Adolfo Suarez', 4),
(5, 'Manuel Belgrano', null);

CREATE INDEX IF NOT EXISTS idx_ciudad_nombre
ON Ciudad(Nombre);

SELECT Aeropuerto.ID AS ID_Aeropuerto, Ciudad.Nombre AS Nombre_Ciudad,
Aeropuerto.Nombre AS Nombre_Aeropuerto
FROM Ciudad INNER JOIN Aeropuerto ON Aeropuerto.IdCiudad = Ciudad.ID;

--Como Shanghai no tiene aeropuerto, me devuelve null en la columna de Nombre_Aeropuerto

SELECT Aeropuerto.ID AS ID_Aeropuerto, Ciudad.Nombre AS Nombre_Ciudad,
Aeropuerto.Nombre AS Nombre_Aeropuerto
FROM Ciudad LEFT JOIN Aeropuerto ON Aeropuerto.IdCiudad = Ciudad.ID;

--Como el aeropuerto Manuel Belgrano no tiene ciudad, me devuelve null en la columna de nombre_ciudad

SELECT Aeropuerto.ID AS ID_Aeropuerto, Ciudad.Nombre AS Nombre_Ciudad,
Aeropuerto.Nombre AS Nombre_Aeropuerto
FROM Ciudad FULL OUTER JOIN Aeropuerto ON Aeropuerto.IdCiudad = Ciudad.ID;

CREATE TABLE IF NOT EXISTS Aerolinea(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Cant_aviones INT
        );

INSERT INTO Aerolinea VALUES
(1, 'Aerolineas Argentinas', 10),
(2, 'LATAM', 15),
(3, 'American Airlines', 12);

CREATE TABLE IF NOT EXISTS TipoMostrador(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO TipoMostrador VALUES
(1, 'Turista'),
(2, 'Primera clase'),
(3, 'Business');

CREATE TABLE IF NOT EXISTS Mostrador(
    ID INT PRIMARY KEY,
    Ubicacion VARCHAR(100),
    IdTipo INT,
    IdAerolinea INT,
    
    FOREIGN KEY (IdTipo)
        REFERENCES TipoMostrador(ID),

    FOREIGN KEY (IdAerolinea)
        REFERENCES Aerolinea(ID)
        );

INSERT INTO Mostrador VALUES
(1, 'Terminal 1', 1, 2),
(2, 'Terminal 2', 2, 1),
(3, 'Terminal 3', 3, 3);
	
CREATE TABLE IF NOT EXISTS Aeropuerto_Aerolinea(
    IdAeropuerto INT,
    IdAerolinea INT,
    PRIMARY KEY(IdAeropuerto, IdAerolinea),
    
    FOREIGN KEY (IdAeropuerto)
        REFERENCES Aeropuerto(ID),
    
    FOREIGN KEY (IdAerolinea)
        REFERENCES Aerolinea(ID)
        );

INSERT INTO Aeropuerto_Aerolinea VALUES
(1,1),
(1,2),
(1,3),
(2,1),
(2,2),
(2,3),
(3,1),
(3,2),
(3,3),
(4,1),
(4,2),
(4,3);

CREATE TABLE IF NOT EXISTS TipoAvion(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO TipoAvion VALUES
(1, 'Avioneta'),
(2, 'Avion mediano'),
(3, 'Boeing');

CREATE TABLE IF NOT EXISTS Avion (
    ID INT PRIMARY KEY,
    IdTipo INT,
    Cant_asientos INT,
    IdAerolinea INT NOT NULL,

    FOREIGN KEY (IdTipo)
        REFERENCES TipoAvion(ID),

    FOREIGN KEY (IdAerolinea)
        REFERENCES Aerolinea(ID)
        );

INSERT INTO Avion VALUES
(1, 2, 180, 2),
(2, 2, 190, 2),
(3, 2, 170, 2),
(4, 1, 50, 1),
(5, 3, 200, 3),
(6, 3, 210, 1);

DELETE FROM Avion WHERE Avion.ID = 6;

SELECT * FROM Avion;
	
CREATE TABLE IF NOT EXISTS TipoVuelo(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO TipoVuelo VALUES
(1, 'De linea'),
(2, 'Charter');

CREATE TABLE IF NOT EXISTS Vuelo(
    Numero_de_vuelo INT PRIMARY KEY,
    IdTipo INT,
    Fecha_de_salida TIMESTAMP,
	Fecha_de_llegada TIMESTAMP,
    IdAvion INT,
    IdAeropuertoOrigen INT,
    IdAeropuertoDestino INT,
    
    FOREIGN KEY (IdTipo)
        REFERENCES TipoVuelo(ID),

    FOREIGN KEY (IdAvion)
        REFERENCES Avion(ID),

    FOREIGN KEY (IdAeropuertoOrigen)
        REFERENCES Aeropuerto(ID),

    FOREIGN KEY (IdAeropuertoDestino)
        REFERENCES Aeropuerto(ID)
        );

INSERT INTO Vuelo VALUES
(2464, 1, '2026-07-25 08:45:00', '2026-07-25 13:25:00', 1, 1, 2),
(2028, 1, '2026-07-25 13:55:00', '2026-07-25 15:15:00', 2, 2, 3),
(3196, 2, '2011-03-31 10:05:00', '2011-03-31 11:45:00', 4, 3, 2),
(5198, 2, '2018-12-09 06:30:00', '2018-12-09 18:30:00', 5, 1, 4),
(8374, 1, '2026-09-27 13:20:00', '2026-09-28 01:20:00', 3, 4, 2);

CREATE INDEX IF NOT EXISTS idx_vuelo_fecha
ON Vuelo(Fecha_de_salida);

SELECT V.Numero_de_vuelo, V.Fecha_de_salida, CO.Nombre AS Ciudad_Origen, CD.Nombre AS Ciudad_Destino
FROM Vuelo V
INNER JOIN Aeropuerto AO ON AO.ID = V.IdAeropuertoOrigen
INNER JOIN Ciudad CO ON CO.ID = AO.IdCiudad
INNER JOIN Aeropuerto AD ON AD.ID = V.IdAeropuertoDestino
INNER JOIN Ciudad CD ON CD.ID = AD.IdCiudad
WHERE EXTRACT(YEAR FROM V.Fecha_de_salida) = 2011;

SELECT * FROM Vuelo WHERE Numero_de_vuelo = 8374;

--Vuelos que salieron de Aerolineas Argentinas en marzo de 2011:

SELECT Numero_de_vuelo, Fecha_de_salida, Aerolinea.Nombre AS Aerolinea 
FROM Vuelo INNER JOIN Aeropuerto_Aerolinea 
ON Aeropuerto_Aerolinea.IdAeropuerto = Vuelo.IdAeropuertoOrigen 
INNER JOIN Aerolinea ON Aerolinea.ID = Aeropuerto_Aerolinea.IdAerolinea 
WHERE EXTRACT(MONTH FROM Fecha_de_salida) = 3 
AND EXTRACT(YEAR FROM Fecha_de_salida) = 2011
AND Aerolinea.Nombre = 'Aerolineas Argentinas';  

CREATE TABLE IF NOT EXISTS TipoPista(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO TipoPista VALUES
(1, 'Despegue'),
(2, 'Aterrizaje');

CREATE TABLE IF NOT EXISTS Pista (
    ID INT PRIMARY KEY,
    IdTipo INT,
    IdAeropuerto INT NOT NULL,

    FOREIGN KEY (IdTipo)
        REFERENCES TipoPista(ID),

    FOREIGN KEY (IdAeropuerto)
        REFERENCES Aeropuerto(ID)
        );

INSERT INTO Pista VALUES
(1, 1, 1),
(2, 2, 1),
(3, 1, 2),
(4, 2, 2),
(5, 1, 3),
(6, 2, 3),
(7, 1, 4),
(8, 2, 4);
	
CREATE TABLE IF NOT EXISTS UsoPista (
    IdAvion INT,
    IdPista INT,
    FechaHora TIMESTAMP,
    PRIMARY KEY (IdAvion, IdPista, FechaHora),

    FOREIGN KEY (IdAvion)
        REFERENCES Avion(ID),

    FOREIGN KEY (IdPista)
        REFERENCES Pista(ID)
);

INSERT INTO UsoPista VALUES
(1, 1, '2026-07-25 08:45:00'),
(1, 4, '2026-07-25 11:25:00'),
(2, 3, '2026-07-25 13:55:00'),
(2, 6, '2026-07-25 15:15:00'),
(3, 5, '2011-03-31 10:05:00'),
(3, 4, '2011-03-31 11:35:00'),
(4, 1, '2018-12-09 06:30:00'),
(4, 8, '2018-12-09 18:30:00');

CREATE TABLE IF NOT EXISTS TipoDocumento(
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
        );

INSERT INTO TipoDocumento VALUES
(1, 'DNI'),
(2, 'Libreta de enrolamiento'),
(3, 'Libreta civica');

CREATE TABLE IF NOT EXISTS Pasajero(
    NumeroDocumento INT PRIMARY KEY,
    Nombre VARCHAR(100),
    IdTipoDocumento INT,

    FOREIGN KEY (IdTipoDocumento)
        REFERENCES TipoDocumento(ID)
        );

INSERT INTO Pasajero VALUES
(44816375, 'Salvador', 1),
(22526104, 'Paula', 3),
(25673509, 'Sergio', 2),
(27908312, 'Natalia', 3),
(28546732, 'Natalia', 3),
(49674109, 'Santiago', 1),
(23809424, 'Hugo Lopez', 2);

CREATE TABLE IF NOT EXISTS Reserva (
    Codigo INT PRIMARY KEY,
    Fecha_de_vencimiento TIMESTAMP,
    DocumentoPasajero INT,
    NumeroVuelo INT,

    FOREIGN KEY (DocumentoPasajero)
        REFERENCES Pasajero(NumeroDocumento),

    FOREIGN KEY (NumeroVuelo)
        REFERENCES Vuelo(Numero_de_vuelo)
        );

INSERT INTO Reserva VALUES
(234, '2026-07-18 08:45:00', 44816375, 2464),
(459, '2026-07-18 08:45:00', 22526104, 2464),
(638, '2026-07-18 08:45:00', 25673509, 2464),
(983, '2026-07-18 08:45:00', 27908312, 2464),
(153, '2026-07-18 08:45:00', 28546732, 2464),
(375, '2026-07-18 08:45:00', 49674109, 2464),
(432, '2026-07-18 13:55:00', 44816375, 2028),
(954, '2026-07-18 13:55:00', 22526104, 2028),
(836, '2026-07-18 13:55:00', 25673509, 2028),
(389, '2026-07-18 13:55:00', 27908312, 2028),
(351, '2026-07-18 13:55:00', 28546732, 2028),
(573, '2026-07-18 13:55:00', 49674109, 2028),
(324, '2011-03-21 13:55:00', 44816375, 3196),
(549, '2011-03-21 13:55:00', 22526104, 3196),
(368, '2011-03-21 13:55:00', 25673509, 3196),
(893, '2011-03-21 13:55:00', 27908312, 3196),
(513, '2011-03-21 13:55:00', 28546732, 3196),
(735, '2011-03-21 13:55:00', 49674109, 3196),
(651, '2018-12-02 15:45:00', 44816375, 5198),
(159, '2018-12-02 15:45:00', 22526104, 5198),
(098, '2018-12-02 15:45:00', 25673509, 5198),
(692, '2018-12-02 15:45:00', 27908312, 5198),
(409, '2018-12-02 15:45:00', 28546732, 5198),
(327, '2018-12-02 15:45:00', 49674109, 5198),
(468, '2026-09-20 10:45:00', 23809424, 8374),
(555, '2027-04-17 07:25:00', 23809424, 8374);

SELECT
    DocumentoPasajero,
    COUNT(*) AS CantidadReservas
FROM Reserva WHERE NumeroVuelo = 2464
GROUP BY DocumentoPasajero
HAVING DocumentoPasajero < 30000000
ORDER BY CantidadReservas DESC;

CREATE INDEX IF NOT EXISTS idx_pasajero_nombre
ON Pasajero(Nombre);

SELECT *
FROM Pasajero INNER JOIN TipoDocumento ON TipoDocumento.ID = Pasajero.IdTipoDocumento
WHERE Pasajero.Nombre = 'Hugo Lopez';

--Pasajeros que viajaron en vuelos Business a Madrid 

CREATE VIEW Pasajeros_Vuelos_Business_a_Madrid AS
SELECT DISTINCT Pasajero.NumeroDocumento, Pasajero.Nombre AS NombrePasajero, 
TipoMostrador.Nombre AS TipoDeMostrador, Ciudad.Nombre AS NombreCiudad
FROM Pasajero 
INNER JOIN Reserva ON Reserva.DocumentoPasajero = Pasajero.NumeroDocumento
INNER JOIN Vuelo ON Reserva.NumeroVuelo = Vuelo.Numero_de_vuelo
INNER JOIN Aeropuerto ON Vuelo.IdAeropuertoDestino = Aeropuerto.ID
INNER JOIN Aeropuerto_Aerolinea ON Aeropuerto.ID = Aeropuerto_Aerolinea.IdAeropuerto
INNER JOIN Mostrador ON Mostrador.IdAerolinea = Aeropuerto_Aerolinea.IdAerolinea
INNER JOIN TipoMostrador ON TipoMostrador.ID = Mostrador.IdTipo
INNER JOIN Ciudad ON Ciudad.ID = Aeropuerto.IdCiudad
WHERE TipoMostrador.Nombre = 'Business' AND Ciudad.Nombre = 'Madrid';

SELECT * FROM Pasajeros_Vuelos_Business_a_Madrid;

--Reservas de Hugo López para el mes que viene

SELECT Pasajero.NumeroDocumento, Pasajero.Nombre, Reserva.Codigo, Vuelo.Fecha_de_salida
FROM Reserva
INNER JOIN Pasajero
    ON Pasajero.NumeroDocumento = Reserva.DocumentoPasajero
INNER JOIN Vuelo
    ON Reserva.NumeroVuelo = Vuelo.Numero_de_vuelo
WHERE Pasajero.Nombre = 'Hugo Lopez'
AND EXTRACT(YEAR FROM Vuelo.Fecha_de_salida) =
    EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
AND EXTRACT(MONTH FROM Vuelo.Fecha_de_salida) =
    EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month');

SELECT * FROM Aeropuerto;

SELECT * FROM Aerolinea;

SELECT * FROM Aeropuerto_Aerolinea;

SELECT * FROM Mostrador;

SELECT * FROM Vuelo;

SELECT * FROM Avion;

SELECT * FROM Pista;

SELECT * FROM UsoPista;

SELECT COUNT(*) FROM Pasajero;

SELECT * FROM Reserva GROUP BY Codigo, DocumentoPasajero;

SELECT *
FROM Cliente
WHERE EXISTS (
    SELECT *
    FROM Cliente
    WHERE Nombre = 'Salvador'
);

SELECT
    Numero_de_vuelo,
    Fecha_de_llegada - Fecha_de_salida AS Duracion
FROM Vuelo;

--Procedure

CREATE OR REPLACE PROCEDURE mostrar_vuelo(p_numero INT)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '%',
    (
        SELECT CONCAT(
            'Vuelo ',
            Numero_de_vuelo,
            ' sale ',
            Fecha_de_salida
        )
        FROM Vuelo
        WHERE Numero_de_vuelo = p_numero
    );

END;
$$;

CALL mostrar_vuelo(2464);

CREATE OR REPLACE PROCEDURE mostrar_pasajero(p_numero INT)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '%',
    (
        SELECT CONCAT(
            'Nombre: ',
            Nombre,
            ' Numero de documento: ',
            NumeroDocumento
        )
        FROM Pasajero
        WHERE NumeroDocumento = p_numero
    );
END;
$$;

CALL mostrar_pasajero(44816375);

--Function

CREATE OR REPLACE FUNCTION pasajeros_vuelo(p_vuelo INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE cantidad INT;
BEGIN
    SELECT COUNT(*)
    INTO cantidad
    FROM Reserva
    WHERE NumeroVuelo = p_vuelo;

    RETURN cantidad;
END;
$$;

SELECT pasajeros_vuelo(2464);

CREATE OR REPLACE FUNCTION reservas_pasajero(d_pasajero INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE cantidad INT;
BEGIN
    SELECT COUNT(*)
    INTO cantidad
    FROM Reserva
    WHERE DocumentoPasajero = d_pasajero;

    RETURN cantidad;
END;
$$;

SELECT reservas_pasajero(44816375);

--Trigger

CREATE OR REPLACE FUNCTION validar_fechas_vuelo()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    IF NEW.Fecha_de_llegada
       < NEW.Fecha_de_salida THEN

        RAISE EXCEPTION
        'La llegada no puede ser anterior a la salida';

    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_validar_fechas
BEFORE INSERT OR UPDATE
ON Vuelo
FOR EACH ROW
EXECUTE FUNCTION validar_fechas_vuelo();

CREATE OR REPLACE FUNCTION registrar_uso_pista()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO UsoPista
    VALUES(
        NEW.IdAvion,
        1,
        NEW.Fecha_de_salida
    );

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_uso_pista
AFTER INSERT
ON Vuelo
FOR EACH ROW
EXECUTE FUNCTION registrar_uso_pista();

CREATE OR REPLACE FUNCTION validar_fechas_reserva()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    Fecha_salida TIMESTAMP;
BEGIN
    SELECT Fecha_de_salida
	INTO Fecha_salida
	FROM Vuelo
	WHERE Numero_de_vuelo = NEW.NumeroVuelo;
	
    IF NEW.Fecha_de_vencimiento
       > Fecha_salida THEN

        RAISE EXCEPTION
        'La reserva no puede vencer después de la salida';

    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_validar_fechas_r
BEFORE INSERT OR UPDATE
ON Reserva
FOR EACH ROW
EXECUTE FUNCTION validar_fechas_reserva();

--INSERT INTO Reserva VALUES
--(555, '2027-04-17 07:25:00', 23809424, 8374);

CREATE OR REPLACE FUNCTION registrar_pasajero()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    RAISE NOTICE 'Se ejecutó el trigger. NEW.ID = %', NEW.ID;

    INSERT INTO Pasajero
    VALUES(
        22197809,
        'Alejandro',
        NEW.ID
    );

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_pasajero
AFTER INSERT
ON TipoDocumento
FOR EACH ROW
EXECUTE FUNCTION registrar_pasajero();

INSERT INTO TipoDocumento VALUES (4, 'Pasaporte');

SELECT * FROM Pasajero;

CREATE OR REPLACE FUNCTION modificar_nombre()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    RAISE NOTICE 'Nombre anterior: %, Nombre nuevo: %', OLD.Nombre, NEW.Nombre;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_mod_nombre
BEFORE UPDATE
ON Pasajero
FOR EACH ROW
EXECUTE FUNCTION modificar_nombre();

UPDATE Pasajero
SET Nombre = 'Salvador Dangelo'
WHERE NumeroDocumento = 44816375;

SELECT * FROM Pasajero;

--INNER JOIN
--LEFT JOIN
--GROUP BY
--HAVING
--EXISTS
--ANY
--ALL

--CREATE FUNCTION
--CREATE TRIGGER
--CREATE PROCEDURE

