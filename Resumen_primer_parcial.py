import numpy as np
import keyword
import math
keyword.kwlist

#%% 
#Unidad 1
altura_obelisco = 102
dia = 1
pila_billetes = 1
while (pila_billetes < altura_obelisco):
    pila_billetes = pila_billetes*2
    dia = dia + 1
    print(dia, pila_billetes)
    
altura_pelota = 100
i = 0
while i < 10:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 1))
    
def saludo(nombre):
    print('hola', nombre)

a = 2.1 + 4.2

#1.8)
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

adelanto = 1000
mes = 0
 
while saldo > 0:
    mes = mes + 1
    if mes <= 12:
        pago = pago_mensual + adelanto
    else:
       pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago 
    total_pagado = total_pagado + pago 
    
print('Total pagado', round(total_pagado, 2), mes)

#1.9)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= 60) and (mes <= 108):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    mes = mes + 1
    
print('Total pagado', round(total_pagado, 2), mes)

#1.10)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= 61) and (mes <= 108):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    print(mes, round(total_pagado, 2), round(saldo, 2))
    mes = mes + 1
    
#1.11)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    if pago > saldo * (1+tasa/12):
        pago = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    print(mes, round(total_pagado, 2), round(saldo, 2))
    mes = mes + 1    
        
#1.13)
def esfera(r):
    return (4/3)*(math.pi)*(r**3)

a = 'basavareddy'
b = a [-1:]
a.strip()
c = a.replace('basavareddy','monfils')

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

cadena = "Ejemplo con for"
for c in cadena:
    print('caracter:', c)
# Mirá el output.

cadena = "Ejemplo con for"

def contar_letras(cadenas:str):
    contador = 0
    for c in cadenas:
        if c == "o":
            contador += 1 
    print(contador)
    
tenistas = ['alcaraz', 'sinner']

frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera,Banana'
lista_frutas = frutas.split(',')
compra = []

for s in lista_frutas:
    print('s =', s)

frase = 'todos somos programadores'
palabras = frase.split()
nuevas_palabras = []

for palabra in palabras:
    if palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e'
    elif palabra[-2:-1] == 'o':   # chequeo anteúltima
        palabra = palabra[:-2] + 'e' + palabra[-1]
    nuevas_palabras.append(palabra)

frase_t = ' '.join(nuevas_palabras)
print(frase_t)
#'todes somes programadores'

#%%
#Unidad 2
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
html = data_u.decode('utf-8')

def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)
        
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
    
def costo_camion_with(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(f).split(',')
        headers
        ['nombre', 'cajones', 'precio\n']
        contador = 0
        for line in rows:
            contador = contador + float(float(line[1])*float(line[2]))      
    return float(contador)

def buscar_precio(fruta):
    d = open(r"C:\Users\SD\Downloads\precios.csv", 'rt', encoding='utf-8')
    headers = next(d).split(',')
    headers
    encontrado = False
    for line in d:
        row = line.split(',')
        nombre = row[0].strip('"')
        precio_fruta = float(row[1])
        if nombre == fruta:
            print('El precio de un cajón de', fruta, 'es:', precio_fruta)
            encontrado = True
            break
    if not encontrado:
        print(fruta, 'no figura en el listado de precios')
        
def buscar_precio_with(fruta):
    with open(r"C:\Users\SD\Downloads\precios.csv", 'rt', encoding='utf-8') as f:
        headers = next(f).split(',')
        headers
        encontrado = False
        for line in f:
            row = line.split(',')
            nombre = row[0].strip('"')
            precio_fruta = float(row[1])
            if nombre == fruta:
                print('El precio de un cajón de', fruta, 'es:', precio_fruta)
                encontrado = True
                break
        if not encontrado:
            print(fruta, 'no figura en el listado de precios')        
        
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

#%%
#Unidad 3
from pprint import pprint

def leer_camion_tuplas(nombre_archivo): #Me devuelve una lista de tuplas
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lote = []

    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, row in enumerate(rows):
            try:
                lote.append((row[0], int(row[1]), float(row[2])))
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return lote

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

def balance(camion, precios):
    dic = {}
    total_ganado = 0.0
    total_perdido = 0.0
    ganancia = leer_precios(precios)
    perdida = leer_camion_diccionario(camion)
    for i in perdida:
        total_perdido = total_perdido + float(i['cajones']*i['precios'])
        fruta = i['nombre'].strip()
        if fruta in ganancia:
            total_ganado += int(i['cajones']) * float(ganancia[fruta])
    dic['perdi'] = total_perdido
    dic['gane'] = total_ganado
    dic['balance'] = total_ganado - total_perdido
    return dic

import sys

altura_pelota = 100
i = 0
if len(sys.argv) == 2:
    altura_pelota = float(sys.argv[1])
while i < 10:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 1))

def costo_camion_sys(nombre_archivo):
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
costo = costo_camion_sys(nombre_archivo)
print('Costo total:', costo)

#%%
#Linea de comandos:
    
#Add-Type -AssemblyName System.IO.Compression.FileSystem
#[System.IO.Compression.ZipFile]::OpenRead("Downloads\Ejercicios.zip").Entries | Select-Object FullName

#mkdir Ejercicios

#Expand-Archive -Path .\Downloads\Ejercicios.zip -DestinationPath .\Ejercicios
