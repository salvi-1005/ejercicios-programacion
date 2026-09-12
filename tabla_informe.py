import csv

#4.11)
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

a = [s for s in camion if s['precios'] > 100 and s['cajones'] > 50]
costo = sum([s['cajones']*s['precios'] for s in camion])
valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
mas100 = [s for s in camion if s['cajones'] > 100]
myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
costo10k = [s for s in camion if s['cajones'] * s['precios'] > 10000]
nombre_cajones =[(s['nombre'], s['cajones']) for s in camion]

f = open(r"C:\Users\SD\Downloads\camion.csv")
rows = csv.reader(f)
headers = next(rows)
headers
['nombre', 'fecha', 'hora', 'cajones', 'precio']
select = ['nombre', 'cajones', 'precio']
indices = [headers.index(ncolumna) for ncolumna in select]
row = next(rows)
camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:<10s} {headers[1]:<10s} {headers[2]:<10s} {headers[3]:<10s}')
print('---------- ---------- ---------- ----------')
for i in informe:
    nombre = i[0] 
    cajones = i[1]  
    precios = i[2] 
    cambio = i[3] 
    print(f'{nombre:<10s} {cajones:<10d} {("$"+f"{precios:0.2f}"):<10s} {cambio:<10.2f}')
   
#Tabla de multiplicar:
#Con multiplicación:
tabla_de_multiplicar_1 = [[y*x for x in range(10)] for y in range(10)]

#Con suma:
tabla_de_multiplicar_2 = [[sum([x for _ in range(y)]) for x in range(10)]for y in range(10)]



