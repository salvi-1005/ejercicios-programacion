import csv

def costo_camion(nombre_archivo):
    c = open(nombre_archivo)
    rows = csv.reader(c)
    headers = next(c).split(',')
    headers
    ['nombre', 'cajones', 'precio\n']
    contador = 0
    for line in rows:
        contador = contador + float(float(line[1])*float(line[2]))      
    return float(contador)

