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

CREATE TABLE IF NOT EXISTS Socios (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100)
        );

INSERT INTO Socios VALUES
(44816375, 'Salvador', 'Dangelo'),
(05607618, 'Roberto', 'Fernandez'),
(54897324, 'Nicolás', 'Sanchez');

CREATE TABLE IF NOT EXISTS Genero (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100)
);

INSERT INTO Genero VALUES
(1, 'Policial'),
(2, 'Navidad'),
(3, 'Infantil'),
(4, 'Terror');

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

CREATE TRIGGER trg_actualizar_compras_pelicula
AFTER INSERT OR UPDATE OR DELETE
ON Transaccion
FOR EACH ROW
EXECUTE FUNCTION actualizar_estadisticas();

INSERT INTO Transaccion VALUES
(3927, '2026-04-24 16:30:00', 365, 44816375, 2),
(4586, '2026-03-18 13:07:00', 537, 05607618, 2),
(5824, '2026-02-09 08:24:00', 457, 54897324, 2),
(5742, '2025-10-14 19:34:00', 638, 44816375, 1),
(8637, '2025-08-29 15:57:00', 846, 05607618, 1),
(7265, '2025-12-17 11:42:00', 942, 54897324, 1),
(9247, '2024-12-28 11:42:00', 777, 44816375, 1);

SELECT * FROM Peliculas AS p INNER JOIN Director AS d ON d.ID = p.IdDirector;

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
