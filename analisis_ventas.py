import csv
import sys

#1)
def leer_ventas(nombre_archivo):
    lista_de_ventas = [] #Creo la lista
    with open(nombre_archivo, 'rt', encoding='utf-8') as f: #Abro el archivo
        rows = csv.reader(f)
        headers = next(rows) #Salteo la linea con los nombres de las columnas
        headers
        ['titulo', 'genero', 'precio', 'cantidad']
        try:
            for line in rows:
                #Creo diccionarios con la información que necesito y defino las claves con sus valores
                diccionario = {} 
                diccionario['titulo'] = line[0]
                diccionario['genero'] = line[1]
                diccionario['precio'] = float(line[2])
                diccionario['cantidad'] = int(line[3])
                lista_de_ventas.append(diccionario) #Actualizo la información
        except:
            print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    return lista_de_ventas

#Con línea de comandos:
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = r"C:\Users\SD\Downloads\ventas.csv"

ventas = leer_ventas(r"C:\Users\SD\Downloads\ventas.csv")
print(ventas[0])

#2)
def ingresos_por_genero(ventas):
    diccionario_ingresos = {} #Creo el diccionario
    #Inicializo un contador para el ingreso de cada género
    ingresos_clasico = 0
    ingresos_ficcion = 0
    ingresos_infantil = 0
    ingresos_historia = 0
    ingresos_fantasia = 0
    ingresos_ciencia_ficcion = 0
    ingresos_ciencia = 0
    for i in ventas:
        #Actualizo cada uno de los ingresos
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
        #Defino las claves del diccionario con sus valores
        diccionario_ingresos['Clásico'] = ingresos_clasico
        diccionario_ingresos['Ficción'] = ingresos_ficcion
        diccionario_ingresos['Infantil'] = ingresos_infantil
        diccionario_ingresos['Historia'] = ingresos_historia
        diccionario_ingresos['Fantasía'] = ingresos_fantasia
        diccionario_ingresos['Ciencia Ficción'] = ingresos_ciencia_ficcion
        diccionario_ingresos['Ciencia'] = ingresos_ciencia
    return diccionario_ingresos
       
ingresos_x_genero = print(ingresos_por_genero(ventas))

#3)
def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo) #Abro la lista de diccionarios de ventas
    ingresos = ingresos_por_genero(ventas) #Abro el diccionario con los ingresos de cada género
    ingreso_total = 0 #Inicializo un contador para el ingreso total
    try:
        for i in ingresos:
            ingreso_total += ingresos[i] #Actualizo el ingreso total
    except:
        print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    return ingreso_total

#Con línea de comandos:
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = r"C:\Users\SD\Downloads\ventas.csv"

informe = generar_informe(r"C:\Users\SD\Downloads\ventas.csv")
print('ingreso total:', informe)