import csv
import fileparse

def leer_camion_diccionario(nombre_archivo): #Me devuelve una lista de diccionarios
    camion = fileparse.parse_csv_tipos(nombre_archivo, select = None, types=[str, int, float])
    return camion

def leer_precios(nombre_archivo, debug): # Devuelve un diccionario
    precios = fileparse.parse_csv_sin_encabezados(nombre_archivo, types=[str, float], has_headers=False)
    return precios

camion = leer_camion_diccionario(r"C:\Users\SD\Downloads\camion.csv")
precios = dict(leer_precios(nombre_archivo = r"C:\Users\SD\Downloads\precios.csv", debug = True))


def hacer_informe(camion, precios):
    lote = []
    for fila in camion:
            lote.append((fila['nombre'], int(fila['cajones']), float(fila['precio']), float((precios[fila['nombre']] - fila['precio']))))
    return lote
    
informe = hacer_informe(camion, precios)

def encabezado():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')

def informe_camion(informe):
    for i in informe:
        nombre = i[0] 
        cajones = i[1]  
        precios = i[2] 
        cambio = i[3] 
        print(f'{nombre:>10s} {cajones:>10d} {("$"+f"{precios:0.2f}"):>10s} {cambio:>10.2f}')

def imprimir_informe(informe):
    encabezado() #Imprime encabezado
    informe_camion(informe) #Imprime informe

