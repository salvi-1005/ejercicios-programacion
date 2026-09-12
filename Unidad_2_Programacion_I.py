import gzip
import urllib.request
import csv
c = open(r"C:\Users\SD\Downloads\camion.csv", 'rt', encoding='utf-8')
headers = next(c).split(',')
headers
['nombre', 'cajones', 'precio\n']
contador = 0
for line in c:
    row = line.split(',')
    contador = contador + float(float(row[1])*float(row[2]))
print(contador)

['"Lima"', '100', '32.20\n']
['"Naranja"', '50', '91.10\n']
c.close()

d = open(r"C:\Users\SD\Downloads\precios.csv", 'rt', encoding='utf-8')
fruta = 'Naranja'
headers = next(d).split(',')
headers
for line in d:
    row = line.split(',')
    nombre = row[0].strip('"')
    precio_naranja = float(row[1])
    if nombre == fruta:
        print(precio_naranja)
d.close()

u = urllib.request.urlopen('http://www.python.org/')
data_u = u.read()

def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)
        
def costo_camion(nombre_archivo):
    c = open(nombre_archivo)
    headers = next(c).split(',')
    headers
    ['nombre', 'cajones', 'precio\n']
    contador = 0
    for line in c:
        row = line.split(',')
        contador = contador + float(float(row[1])*float(row[2]))      
    return contador
    
def buscar_precio(nombre_archivo, fruta):
    d = open(nombre_archivo)
    headers = next(d).split(',')
    headers
    for line in d:
        row = line.split(',')
        nombre = row[0].strip('"')
        precio_fruta = float(row[1])
        if nombre == fruta:
            return precio_fruta
        
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

t = {'fruta': 'Manzana','cajones': 100,'precio': 490.1}
for k in t:
        print('k =', t[k])
    
def geringoso(cadena:str):
    capadepenapa =''
    for c in cadena:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c 
    return capadepenapa
        
def diccionario_geringoso(lista:list):
    d = {}
    for palabra in lista:
        d[palabra] = geringoso(palabra)
    return d