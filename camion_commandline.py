import csv
import sys

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
    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = r"C:\Users\SD\Downloads\camion.csv"
costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
