--5)
CREATE SCHEMA IF NOT EXISTS aerolinea;

SET search_path TO aerolinea;

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

CREATE INDEX IF NOT EXISTS idx_reserva_vuelo ON Reserva (NumeroVuelo, DocumentoPasajero);
CREATE INDEX IF NOT EXISTS idx_vuelo_aeropuerto_dest ON Vuelo (IdAeropuertoDestino);
CREATE INDEX IF NOT EXISTS idx_aeropuerto_ciudad ON Aeropuerto (IdCiudad);
CREATE INDEX IF NOT EXISTS idx_mostrador_tipo_aerolinea ON Mostrador (IdTipo, IdAerolinea);

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

CREATE OR REPLACE FUNCTION validar_cantidad_aviones()
RETURNS TRIGGER 
AS $$
BEGIN
    IF NEW.Cant_aviones < 10 THEN
        RAISE EXCEPTION 'Operación cancelada: Una aerolinea debe tener 10 aviones como mínimo $%', NEW.Cant_aviones;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validar_cant_av
BEFORE INSERT ON Aerolinea
FOR EACH ROW
EXECUTE FUNCTION validar_cantidad_aviones();

INSERT INTO Aerolinea VALUES
(4, 'Malasian Airlines', 11);

SELECT * FROM Aerolinea;

--SELECT AGE(NOW(), '2003-05-10');