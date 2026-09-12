import csv

nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    print(i, nombres[i])
    
points = [(1, 4),(10, 40),(23, 14),(5, 6),(7, 8)]
for x, y in points:
    print(x,y)

columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)

for columna, valor in pares:
    print(columna, valor)
    
def costo_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(f)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, line in enumerate(rows):
            try: 
                _ = float(float(line[1])*float(line[2])) 
            except ValueError:
                print(f'line {i}: No pude interpretar: {line}')
    