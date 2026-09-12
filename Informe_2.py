import csv
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
            records = dict(zip(headers,row))
            try:
                lote.append((records['nombre'], int(records['cajones']), float(records['precio'])))
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

