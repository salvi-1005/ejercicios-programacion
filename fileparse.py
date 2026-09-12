import csv

#Seleccionar columnas
#7.4)
def parse_csv(nombre_archivo, select = None):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

#)Tipos
#7.5)
def parse_csv_tipos(nombre_archivo, select = None, types=[str, int, float]):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

#Sin encabezados:
#7.6)
def parse_csv_sin_encabezados(nombre_archivo, types=[str, float], has_headers=False):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue 
            if types:
                fila = tuple(func(val) for func, val in zip(types, fila))
            # Armar el diccionario
            registro = (fila)
            registros.append(registro)

    return registros
