import numpy as np
import matplotlib.pyplot as plt

#%%
#1)
def crear_arreglo(N, select = None, types=[str,int,float]):
    arreglo = np.array([]) #Creo nuevo arreglo
    if select == 'Gaussiana':
        gaussiana = np.random.normal(loc=0, scale=1, size=N) #Distribución Gaussiana
        nuevo_arreglo = np.append(arreglo, gaussiana) #lleno el arreglo con N números al azar
    if select == 'Uniforme':
        uniforme = np.random.uniform(0, 10, N) #Distribución Uniforme
        nuevo_arreglo = np.append(arreglo, uniforme)#lleno el arreglo con N números al azar
    if select == 'Poisson':
        poisson = np.random.poisson(1, N) #Distribución de Poisson
        nuevo_arreglo = np.append(arreglo, poisson)#lleno el arreglo con N números al azar
    return nuevo_arreglo
      
#Ejemplo:
N = 1000000
array_gaussiana = crear_arreglo(N, select = 'Gaussiana', types=[str,int,float])
array_uniforme = crear_arreglo(N, select = 'Uniforme', types=[str,int,float])
array_poisson = crear_arreglo(N, select = 'Poisson', types=[str,int,float])
  
#%%
#2)

def crear_histograma(array): #Probar con array_gaussiana, array_uniforme o array_poisson
    plt.hist(array,bins=25, density=True)
    plt.xlabel('Abundancia relativa')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de abundancia relativa de los números al azar generados')
    plot = plt.show() 
    return plot

#%%
#3)
def modulo(): #Creo un módulo que no ejecuta nada, pero que contiene a las funciones
    funcion = crear_arreglo(4, select = 'Gaussiana', types=[str,int,float])
    funcion
    grafico = crear_histograma(funcion)
    grafico
    pass

#%%
#4)
#Grafico con N = 20
A = 20
array_gaussiana_2 = crear_arreglo(A, select = 'Gaussiana', types=[str,int,float])
array_uniforme_2 = crear_arreglo(A, select = 'Uniforme', types=[str,int,float])
array_poisson_2 = crear_arreglo(A, select = 'Poisson', types=[str,int,float])
crear_histograma(array_gaussiana_2)
crear_histograma(array_uniforme_2)
crear_histograma(array_poisson_2)

#Con valores pequeños se observan pocas barras

#Gráfico con N = 2000
B = 2000
array_gaussiana_3 = crear_arreglo(B, select = 'Gaussiana', types=[str,int,float])
array_uniforme_3 = crear_arreglo(B, select = 'Uniforme', types=[str,int,float])
array_poisson_3 = crear_arreglo(B, select = 'Poisson', types=[str,int,float])
crear_histograma(array_gaussiana_3)
crear_histograma(array_uniforme_3)
crear_histograma(array_poisson_3)

#Con números más grandes se pueden observar las tendencias vistas en la teórica