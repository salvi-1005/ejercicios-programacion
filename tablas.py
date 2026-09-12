import csv
from pprint import pprint

def leer_camion_diccionario(nombre_archivo): #Me devuelve una lista de diccionarios
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lista = []

    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, row in enumerate(rows):
            records = dict(zip(headers,row))
            try:
                lote = {}
                lote['nombre'] = records['nombre']
                lote['cajones'] = int(records['cajones'])
                lote['precios'] = float(records['precio'])
                lista.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return lista

def leer_precios(nombre_archivo): # Devuelve un diccionario
    precios = {}
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1])
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return precios

camion = leer_camion_diccionario(r"C:\Users\SD\Downloads\camion.csv")
precios = leer_precios(r"C:\Users\SD\Downloads\precios.csv")

def hacer_informe(camion, precios):
    lote = []
    for fila in camion:
            lote.append((fila['nombre'], int(fila['cajones']), float(fila['precios']), float((precios[fila['nombre']] - fila['precios']))))
    return lote
    
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for i in informe:
    nombre = i[0] 
    cajones = i[1]  
    precios = i[2] 
    cambio = i[3] 
    print(f'{nombre:>10s} {cajones:>10d} {("$"+f"{precios:0.2f}"):>10s} {cambio:>10.2f}')
    
encabezado = ('', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
numeros = range(10)
print(f'{encabezado[0]:>3s} {encabezado[1]:>4d} {encabezado[2]:>4d} {encabezado[3]:>4d} {encabezado[4]:>4d} {encabezado[5]:>4d} {encabezado[6]:>4d} {encabezado[7]:>4d} {encabezado[8]:>4d} {encabezado[9]:>4d} {encabezado[10]:>4d}')
print('-'*53)

for i in numeros:
    fila = [i * j for j in numeros]
    print(f"{i:>2d}: ", end="")
    for valor in fila:
        print(f"{valor:>4d}", end=" ")
    print()

    