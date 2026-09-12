import csv

lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']

#8.7)
def parse_csv_flexible(lines, select=None, types=None, has_headers=True):
    rows = csv.reader(lines)
    registros = []
    if has_headers:
        encabezados = next(rows)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
               indices = list(range(len(encabezados)))
        for row in rows:
            if not row:
                continue
            if select:
               row = [row[index] for index in indices]
            if types:
               row = [func(val) for func, val in zip(types, row)]
            registro = dict(zip(encabezados, row))
            registros.append(registro)
    else:
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            registros.append(tuple(row))
    return registros

camion = parse_csv_flexible(lines, select=None, types=None, has_headers=True)
print(camion)