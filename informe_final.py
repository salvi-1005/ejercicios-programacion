import csv

lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
precios = ['Lima,150','Naranja,125','Mandarina,100']

#8.8)
def leer_camion(lines): 
    rows = csv.reader(lines)
    headers = next(rows)
    lista = []
    for i, row in enumerate(rows, start=1):
        if not row:
            continue
        try:
            record = dict(zip(headers, row))
            lote = {
                'nombre': record['nombre'],
                'cajones': int(record['cajones']),
                'precio': float(record['precio'])
            }
            lista.append(lote)
        except ValueError:
            print('Faltan datos en la línea', i, 'del archivo.')
    return lista

def leer_precios(lines): 
    rows = csv.reader(lines)
        
    precios = {}
    for i, row in enumerate(rows):
        if not row:
            continue
        try:
            precios[row[0]] = float(row[1])
        except ValueError:
            print('Faltan datos en la línea', i, 'del archivo.')
    return precios

camion = leer_camion(lines)
precios = leer_precios(precios)

print('camion:',camion)
print('precios:',precios)
