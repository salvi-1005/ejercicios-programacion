import csv
from collections import Counter

nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    print(i, nombres[i])
    
points = [(1, 4),(10, 40),(23, 14),(5, 6),(7, 8)]
for x, y in points:
    print(x,y)

#%%Zip:
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)

for columna, valor in pares:
    print(columna, valor)


#4.3)
def costo_camion_missing(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, line in enumerate(rows):
            try: 
                _ = float(float(line[1])*float(line[2])) 
            except ValueError:
                print(f'line {i}: No pude interpretar: {line}')

#4.4)
def costo_camion_zip(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        contador = 0
        for i, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try: 
                contador = contador + (int(record['cajones'])*float(record['precio'])) 
            except ValueError:
                print(f'line {i}: No pude interpretar: {line}')
    return contador

precios = {'Pera' : 490.1,'Lima' : 23.45,'Naranja' : 91.1,'Mandarina' : 34.23}
print(precios.items())

lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)

#%%Contadores:
camion = [('Pera', 100, 490.1),('Naranja', 50, 91.1),('Caqui', 150, 83.44),('Naranja', 100, 45.23),('Pera', 75, 572.45),('Lima', 50, 23.15)]

total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
print(total_cajones['Naranja'])
print(total_cajones['Pera'])

def leer_camion_diccionario(nombre_archivo): #Me devuelve una lista de diccionarios
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lista = []

    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        try:
           for i, row in enumerate(rows):
                lote = {}
                lote['nombre'] = row[0]
                lote['cajones'] = int(row[1])
                lote['precios'] = float(row[2])
                lista.append(lote)
        except ValueError:
            print('Faltan datos en la línea', i, 'del archivo.')
    return lista

camion = leer_camion_diccionario(r"C:\Users\SD\Downloads\camion.csv")
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']
print(tenencias)

frutas_mas_comunes = tenencias.most_common(3)

camion2 = leer_camion_diccionario(r"C:\Users\SD\Downloads\camion2.csv")
from collections import Counter
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']
print(tenencias2)

combinada = tenencias + tenencias2

#%%Formatos
nombre = 'Naranja'
cajones = 100
precio = 91.1
print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')


