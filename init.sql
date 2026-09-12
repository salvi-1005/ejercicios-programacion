-- =========================
-- SCHEMA GOLD
-- =========================
CREATE SCHEMA IF NOT EXISTS gold;

-- =========================
-- DIMENSIONES
-- =========================

CREATE TABLE IF NOT EXISTS gold.dim_ciudad (
    ciudad_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100),
    latitud NUMERIC,
    longitud NUMERIC,
    UNIQUE (nombre, pais)
);

CREATE TABLE IF NOT EXISTS gold.dim_tiempo (
    fecha DATE PRIMARY KEY,
    anio INTEGER,
    mes INTEGER,
    dia INTEGER,
    dia_semana VARCHAR(20)
);

-- =========================
-- FACT TABLE
-- =========================

CREATE TABLE IF NOT EXISTS gold.fact_clima_diario (
    fecha DATE,
    ciudad_id INTEGER,
    
    temp_promedio NUMERIC,
    temp_max NUMERIC,
    temp_min NUMERIC,
    
    lluvia_acumulada NUMERIC,
    humedad_promedio NUMERIC,
    viento_promedio NUMERIC,

    PRIMARY KEY (fecha, ciudad_id),

    FOREIGN KEY (ciudad_id) REFERENCES gold.dim_ciudad(ciudad_id),
    FOREIGN KEY (fecha) REFERENCES gold.dim_tiempo(fecha)
);