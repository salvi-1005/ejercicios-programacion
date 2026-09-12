#3)
#Importo las funciones
from segundo_parcial_programacion_I import crear_arreglo
from segundo_parcial_programacion_I import crear_histograma
from segundo_parcial_programacion_I import modulo

print(crear_arreglo)
print(crear_histograma)
print(modulo)

print("El módulo fue importado exitosamente.")

#Ejemplos de funcionamiento:
N = 10
gaussiana = crear_arreglo(N, select = 'Gaussiana', types = [str,int,float])
print(gaussiana)

histograma_gaussiana = crear_histograma(gaussiana)
