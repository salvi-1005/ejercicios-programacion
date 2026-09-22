--3)

DROP TABLE IF EXISTS Estadistica CASCADE;
DROP TABLE IF EXISTS Compra CASCADE;
DROP TABLE IF EXISTS Alquiler CASCADE;
DROP TABLE IF EXISTS Peliculas CASCADE;
DROP TABLE IF EXISTS Genero CASCADE;
DROP TABLE IF EXISTS Director CASCADE;
DROP TABLE IF EXISTS Tipo CASCADE;
DROP TABLE IF EXISTS Socios CASCADE;
DROP TABLE IF EXISTS Transaccion CASCADE;
DROP TABLE IF EXISTS Auditoria_Transaccion CASCADE;
DROP TABLE IF EXISTS Pelicula_genero CASCADE;

CREATE TABLE IF NOT EXISTS Socios (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100)
        );

INSERT INTO Socios VALUES
(44816375, 'Salvador', 'Dangelo'),
(05607618, 'Roberto', 'Fernandez'),
(54897324, 'Nicolás', 'Sanchez'),
(10918724, 'Graciela', 'Ferrari');

CREATE TABLE IF NOT EXISTS Genero (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
);

INSERT INTO Genero VALUES
(1, 'Policial'),
(2, 'Navidad'),
(3, 'Infantil'),
(4, 'Terror'),
(5, 'Comedia');

CREATE TABLE IF NOT EXISTS Director (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
);

INSERT INTO Director VALUES
(24738026, 'George Lucas'),
(32617924, 'Daniel Szifron'),
(28903671, 'Steven Spielberg'),
(26902638, 'Vince Gilligan'),
(30982637, 'John Travolta'),
(25485092, 'Moby Dick');

CREATE TABLE IF NOT EXISTS Peliculas (
    ID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    Anio INT,
	Stock_vendido INT DEFAULT 0,
	Stock_alquilado INT DEFAULT 0,
    IdDirector INT,

    FOREIGN KEY (IdDirector)
        REFERENCES Director(ID)
);

INSERT INTO Peliculas (ID, Titulo, Anio, IdDirector) VALUES
(537, 'La Odisea De Los Giles', 2019, 32617924),
(638, 'Los Fantasmas De Scrooge', 2009, 24738026),
(846, 'El Secreto De Sus Ojos', 1996, 32617924),
(365, 'El Robo Del Siglo', 2020, 32617924),
(942, 'Toy Story 5', 2026, 26902638),
(457, 'El Exorcista', 2005, 28903671),
(777, 'Mi Pobre Angelito', NULL, 25485092);

CREATE TABLE IF NOT EXISTS Pelicula_genero (
    ID INT PRIMARY KEY,
	IdPelicula INT,
	IdGenero INT,

	FOREIGN KEY (IdPelicula)
	    REFERENCES Peliculas(ID),

	FOREIGN KEY (IdGenero)
	    REFERENCES Genero(ID)
    );

INSERT INTO Pelicula_genero VALUES
(1, 537, 1),
(2, 638, 2),
(3, 846, 1),
(4, 365, 1),
(5, 942, 3),
(6, 457, 4),
(7, 777, 2);

SELECT AVG(Anio), COUNT(*) FROM Peliculas;

CREATE TABLE IF NOT EXISTS Tipo (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
);

INSERT INTO Tipo VALUES
(1, 'Compra'),
(2, 'Alquiler');

CREATE TABLE IF NOT EXISTS Transaccion (
    ID INT PRIMARY KEY,
	Fecha TIMESTAMP,
	IdPelicula INT,
	IdSocio INT,
	IdTipo INT,

	FOREIGN KEY (IdPelicula)
	    REFERENCES Peliculas(ID),
		
	FOREIGN KEY (IdSocio)
	    REFERENCES Socios(ID),

	FOREIGN KEY (IdTipo)
	    REFERENCES Tipo(ID)
	
);

CREATE INDEX idx_titulo_pelicula ON Peliculas(Titulo);

SELECT * FROM Transaccion INNER JOIN Socios ON Socios.ID = Transaccion.IdSocio
WHERE Transaccion.IdTipo = 1;

SELECT * FROM Transaccion RIGHT JOIN Peliculas ON Peliculas.ID = Transaccion.IdPelicula
WHERE Transaccion.IdTipo = 1;

SELECT * FROM Transaccion FULL OUTER JOIN Peliculas ON Peliculas.ID = Transaccion.IdPelicula
WHERE Transaccion.IdTipo = 2 AND (Peliculas.ID IS NULL OR Transaccion.IdPelicula IS NULL);

SELECT P.Titulo, G.Nombre AS Género FROM Peliculas P INNER JOIN Pelicula_genero PG ON PG.IdPelicula = P.ID
INNER JOIN Genero G ON G.ID = PG.IdGenero;

SELECT P.Titulo, D.Nombre FROM Peliculas P INNER JOIN Director D ON D.ID = P.IdDirector;

SELECT P.Titulo, G.Nombre AS Genero, D.Nombre AS Director
FROM Peliculas P INNER JOIN Pelicula_genero PG ON PG.IdPelicula = P.ID
INNER JOIN Genero G ON G.ID = PG.IdGenero
INNER JOIN Director D ON D.ID = P.IdDirector;

CREATE OR REPLACE FUNCTION cantidad_total_movimientos(
    pelicula_id INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    cantidad INT;
BEGIN

    SELECT
        Stock_vendido + Stock_alquilado
    INTO cantidad
    FROM Peliculas
    WHERE Peliculas.ID = pelicula_id;

    RETURN cantidad;

END;
$$;

CREATE OR REPLACE PROCEDURE mostrar_peliculas_genero(
    gen_id INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    pelicula_actual RECORD;
BEGIN

    FOR pelicula_actual IN
        SELECT
            P.Titulo,
            G.Nombre AS Genero
        FROM Peliculas P
        INNER JOIN Pelicula_genero PG
            ON PG.IdPelicula = P.ID
		INNER JOIN Genero G
		    ON G.ID = PG.IdGenero
        WHERE G.ID = gen_id
    LOOP

        RAISE NOTICE
        'Pelicula: %, Genero: %',
        pelicula_actual.Titulo,
        pelicula_actual.Genero;

    END LOOP;

END;
$$;
CALL mostrar_peliculas_genero(1);

CREATE OR REPLACE FUNCTION actualizar_estadisticas()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    IF TG_OP = 'INSERT' THEN

        IF NEW.IdTipo = 1 THEN

            UPDATE Peliculas
            SET Stock_vendido = Stock_vendido + 1
            WHERE Peliculas.ID = NEW.IdPelicula;

        ELSIF NEW.IdTipo = 2 THEN

            UPDATE Peliculas
            SET Stock_alquilado = Stock_alquilado + 1
            WHERE Peliculas.ID = NEW.IdPelicula;

        END IF;

    END IF;

    IF TG_OP = 'DELETE' THEN

        IF OLD.IdTipo = 1 THEN

            UPDATE Peliculas
            SET Stock_vendido = Stock_vendido - 1
            WHERE Peliculas.ID = OLD.IdPelicula;

        ELSIF OLD.IdTipo = 2 THEN

            UPDATE Peliculas
            SET Stock_alquilado = Stock_alquilado - 1
            WHERE Peliculas.ID = OLD.IdPelicula;

        END IF;

    END IF;

    IF TG_OP = 'UPDATE'
       AND OLD.IdPelicula <> NEW.IdPelicula THEN

        IF OLD.IdTipo = 1 THEN

            UPDATE Peliculas
            SET Stock_vendido = Stock_vendido - 1
            WHERE Peliculas.ID = OLD.IdPelicula;
			
        ELSIF NEW.IdTipo = 1 THEN
		
            UPDATE Peliculas
            SET Stock_vendido = Stock_vendido + 1
            WHERE Peliculas.ID = NEW.IdPelicula;

        END IF;

        IF OLD.IdTipo = 2 THEN

            UPDATE Peliculas
            SET Stock_alquilado = Stock_alquilado - 1
            WHERE Peliculas.ID = OLD.IdPelicula;
			
        ELSIF NEW.IdTipo = 2 THEN
		
            UPDATE Peliculas
            SET Stock_alquilado = Stock_alquilado + 1
            WHERE Peliculas.ID = NEW.IdPelicula;

        END IF;

    END IF;

    RETURN NULL;

END;
$$;

CREATE TRIGGER trg_actualizar_compras_y_alquileres_pelicula
AFTER INSERT OR UPDATE OR DELETE
ON Transaccion
FOR EACH ROW
EXECUTE FUNCTION actualizar_estadisticas();

CREATE OR REPLACE FUNCTION validar_borrado_pelicula()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.anio IS NOT NULL THEN
        RAISE EXCEPTION 'Operación cancelada: La pelicula % posee un año que no es nulo $%', 
            OLD.ID, OLD.Titulo;
        -- Opción B (Silenciosa): Si simplemente retornamos NULL, Postgres no borra la fila
        -- RETURN NULL; 
    END IF;
   
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validar_año
BEFORE DELETE
ON Peliculas
FOR EACH ROW
EXECUTE FUNCTION validar_borrado_pelicula();

--DELETE FROM Transaccion WHERE IdPelicula = 638;
--DELETE FROM Peliculas WHERE ID = 638;

SELECT * FROM Peliculas AS p INNER JOIN Director AS d ON d.ID = p.IdDirector;

--extras:

--1)

SELECT D.Nombre, COUNT(*) AS CantidadPeliculas FROM Peliculas P INNER JOIN Director D ON D.ID = P.IdDirector
GROUP BY D.ID, D.Nombre HAVING COUNT(*) > 1;

--2)

SELECT G.Nombre FROM Genero G LEFT JOIN Pelicula_genero PG ON PG.IdGenero = G.ID
LEFT JOIN Peliculas P ON P.ID = PG.IdPelicula WHERE P.Titulo IS NULL;

--3)

SELECT S.Nombre, S.Apellido FROM Socios S LEFT JOIN Transaccion T ON T.IdSocio = S.ID
WHERE T.ID IS NULL;

--4)

SELECT MIN(anio) FROM Peliculas;

--5)

SELECT G.Nombre AS Género, COUNT(*) AS CantidadPeliculas FROM Peliculas P 
INNER JOIN Pelicula_genero PG ON PG.IdPelicula = P.ID
INNER JOIN Genero G ON G.ID = PG.IdGenero
GROUP BY G.ID, G.Nombre ORDER BY CantidadPeliculas DESC;

--6)

CREATE OR REPLACE FUNCTION promedio_anio_peliculas()
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    promedio DECIMAL;
BEGIN

    SELECT
        AVG(anio)
    INTO promedio
    FROM Peliculas;

    RETURN promedio;

END;
$$;

SELECT(promedio_anio_peliculas());

--7)

CREATE OR REPLACE FUNCTION cantidad_peliculas_genero(id_genero INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    cantidad INT;
BEGIN

    SELECT
        COUNT(*)
    INTO cantidad
    FROM Peliculas P INNER JOIN Pelicula_genero PG ON PG.IdPelicula = P.ID
	INNER JOIN Genero G ON G.ID = PG.IdGenero
    WHERE G.ID = id_genero;
    RETURN cantidad;

END;
$$;

SELECT(cantidad_peliculas_genero(1));

--8)

CREATE OR REPLACE FUNCTION cantidad_transacciones_socio(id_socio INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    cantidad INT;
BEGIN

    SELECT 
        COUNT(*)
    INTO cantidad
    FROM Socios S INNER JOIN Transaccion T ON T.IdSocio = S.ID
    WHERE S.ID = id_socio;
    RETURN cantidad;

END;
$$;

SELECT(cantidad_transacciones_socio(44816375));

--10)

CREATE OR REPLACE PROCEDURE mostrar_director(id_director INT)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '%',
    (
        SELECT CONCAT(
            'ID: ',
            ID,
            ' Nombre: ',
            Nombre
        )
        FROM Director
        WHERE ID = id_director
    );
END;
$$;

CALL mostrar_director(32617924);

--11)

CREATE OR REPLACE PROCEDURE mostrar_peliculas_director(id_director INT)
LANGUAGE plpgsql
AS $$
DECLARE
    pelicula_actual RECORD;
BEGIN

    FOR pelicula_actual IN
        SELECT
            P.Titulo,
            D.Nombre AS Director
        FROM Peliculas P
		INNER JOIN Director D
		    ON D.ID = P.IdDirector
        WHERE D.ID = id_director
    LOOP

        RAISE NOTICE
        'Pelicula: %, Genero: %',
        pelicula_actual.Titulo,
        pelicula_actual.Director;

    END LOOP;

END;
$$;
CALL mostrar_peliculas_director(32617924);

--14)

CREATE OR REPLACE FUNCTION validar_año_pelicula()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.anio > EXTRACT(YEAR FROM CURRENT_DATE) THEN
        RAISE EXCEPTION 'Operación cancelada: La película % posee un año que todavía no llegó', 
            NEW.Titulo; 
    END IF;
   
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validar_año_p
BEFORE INSERT
ON Peliculas
FOR EACH ROW
EXECUTE FUNCTION validar_año_pelicula();

--INSERT INTO Peliculas (ID, Titulo, Anio, IdDirector) VALUES (888, 'Mision Imposible', 2027, 28903671);

--20)

CREATE TABLE Auditoria_Transaccion(
    ID INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	Operacion VARCHAR(100),
	Fecha TIMESTAMP
);

CREATE OR REPLACE FUNCTION registrar_transaccion()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    tipo_transaccion VARCHAR(100);
BEGIN
    IF TG_OP = 'INSERT' THEN
            SELECT Nombre INTO tipo_transaccion FROM Tipo WHERE Tipo.ID = NEW.IdTipo;
            INSERT INTO Auditoria_Transaccion (ID, Operacion, Fecha) VALUES
			(NEW.ID, tipo_transaccion, NEW.Fecha);

    END IF;

    IF TG_OP = 'DELETE' THEN 
            DELETE FROM Auditoria_Transaccion WHERE Auditoria_Transaccion.ID = OLD.ID;

    END IF;

    IF TG_OP = 'UPDATE' THEN
	    IF OLD.IdTipo <> NEW.IdTipo THEN
		    SELECT Nombre INTO tipo_transaccion FROM Tipo WHERE Tipo.ID = NEW.IdTipo;
            UPDATE Auditoria_Transaccion
            SET Operacion = tipo_transaccion
            WHERE Auditoria_Transaccion.ID = NEW.ID;
			
		END IF;
		
		IF OLD.Fecha <> NEW.Fecha THEN
            UPDATE Auditoria_Transaccion
            SET Fecha = NEW.Fecha
            WHERE Auditoria_Transaccion.ID = NEW.ID;

        END IF;

    END IF;

    RETURN NULL;

END;
$$;

CREATE TRIGGER trg_registro_de_transaccion
AFTER INSERT OR UPDATE OR DELETE
ON Transaccion
FOR EACH ROW
EXECUTE FUNCTION registrar_transaccion();

INSERT INTO Transaccion VALUES
(1, '2026-04-24 16:30:00', 365, 44816375, 2),
(2, '2026-03-18 13:07:00', 537, 05607618, 2),
(3, '2026-02-09 08:24:00', 457, 54897324, 2),
(4, '2025-10-14 19:34:00', 638, 44816375, 1),
(5, '2025-08-29 15:57:00', 846, 05607618, 1),
(6, '2025-12-17 11:42:00', 942, 54897324, 1),
(7, '2024-12-28 11:42:00', 777, 44816375, 1),
(8, '2026-09-17 11:42:00', 365, 05607618, 2);

SELECT * FROM Peliculas AS p INNER JOIN Director AS d ON d.ID = p.IdDirector;

SELECT * FROM Auditoria_Transaccion;

--22)

CREATE OR REPLACE FUNCTION pelicula_mas_alquilada()
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE 
    id_maximo INT;
BEGIN

    SELECT ID
	INTO id_maximo
	FROM Peliculas
	ORDER BY Stock_alquilado DESC LIMIT 1;
	RETURN id_maximo;

END;
$$;

SELECT(pelicula_mas_alquilada());

--23)

CREATE OR REPLACE PROCEDURE informe_videoclub()
LANGUAGE plpgsql
AS $$
DECLARE
    cant_socios INT;
	cant_peliculas INT;
	cant_directores INT;
	cant_generos INT;
BEGIN
    SELECT COUNT(*) INTO cant_socios FROM Socios;
	SELECT COUNT(*) INTO cant_peliculas FROM Peliculas;
	SELECT COUNT(*) INTO cant_directores FROM Director;
	SELECT COUNT(*) INTO cant_generos FROM Genero;
    RAISE NOTICE 'Cantidad de socios: %, 
	 Cantidad de películas: %, 
	 Cantidad de directores: %,
	 Cantidad de generos: %',
				  cant_socios,
				  cant_peliculas,
				  cant_directores,
				  cant_generos;
 
END;
$$;

CALL informe_videoclub();

--24)

CREATE OR REPLACE FUNCTION verificar_eliminacion()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF OLD.Stock_vendido > 0 OR OLD.Stock_alquilado = 0 THEN
        RAISE EXCEPTION 'La película % ya tiene transacciones asociadas',
		OLD.Titulo;
    END IF;

    RETURN OLD;

END;
$$;

CREATE TRIGGER trg_ver_eliminacion
BEFORE DELETE
ON Peliculas
FOR EACH ROW
EXECUTE FUNCTION verificar_eliminacion();

--DELETE FROM Peliculas WHERE Peliculas.ID = 777;