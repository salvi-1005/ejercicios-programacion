import rebote
import hipoteca
import informe_funciones
import fileparse
import costo_camion
import csv

help(fileparse)
dir(fileparse)

camion = fileparse.parse_csv_tipos(r"C:\Users\SD\Downloads\camion.csv", select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
print(camion)

lista_precios = fileparse.parse_csv_sin_encabezados(r"C:\Users\SD\Downloads\precios.csv", types = [str, float], has_headers = False)
print(lista_precios)

precios = dict(lista_precios)
print(precios)

#7.9)
costo = costo_camion.costo_camion(r"C:\Users\SD\Downloads\camion.csv")

print(costo)

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion_diccionario(nombre_archivo)
    contador = 0
    for line in camion:
        contador = contador + float(float(line['cajones'])*float(line['precio']))      
    return float(contador)