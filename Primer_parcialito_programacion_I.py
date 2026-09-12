import csv

#1)
def leer_ventas(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['titulo', 'genero', 'precio', 'cantidad']
        for line in rows:
            diccionario = {}
            diccionario['titulo'] = line[0]
            diccionario['genero'] = line[1]
            diccionario['precio'] = float(line[2])
            diccionario['cantidad'] = int(line[3])
            lista.append(diccionario)
    return lista
            
ventas = leer_ventas(r"C:\Users\SD\Downloads\ventas.csv")
print(ventas[0])

#2)
def ingresos_por_genero(ventas):
    diccionario = {}
    ingresos_clasico = 0
    ingresos_ficcion = 0
    ingresos_infantil = 0
    ingresos_historia = 0
    ingresos_fantasia = 0
    ingresos_ciencia_ficcion = 0
    ingresos_ciencia = 0
    for i in ventas:
        if i['genero'] == 'Clásico':
            ingresos_clasico = ingresos_clasico + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Ficción':
            ingresos_ficcion = ingresos_ficcion + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Infantil':
            ingresos_infantil = ingresos_infantil + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Historia':
            ingresos_historia = ingresos_historia + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Fantasía':
            ingresos_fantasia = ingresos_fantasia + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Ciencia Ficción':
            ingresos_ciencia_ficcion = ingresos_ciencia_ficcion + (float(i['precio']) * float(i['cantidad']))
        elif i['genero'] == 'Ciencia':
            ingresos_ciencia = ingresos_ciencia + (float(i['precio']) * float(i['cantidad']))
        diccionario['Clásico'] = ingresos_clasico
        diccionario['Ficción'] = ingresos_ficcion
        diccionario['Infantil'] = ingresos_infantil
        diccionario['Historia'] = ingresos_historia
        diccionario['Fantasía'] = ingresos_fantasia
        diccionario['Ciencia Ficción'] = ingresos_ciencia_ficcion
        diccionario['Ciencia'] = ingresos_ciencia
    return diccionario
        
#3)
def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    ingresos = ingresos_por_genero(ventas)
    ingreso_total = 0
    for i in ingresos:
        ingreso_total += ingresos[i]
    return ingreso_total