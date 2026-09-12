import random
import numpy as np
import matplotlib.pyplot as plt

#7.19)
def busqueda_secuencial_comps(lista, x):
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria_comps(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 
    comps_promedio_secuencial = np.zeros(256)
    comps_promedio_binaria = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_binaria[i] = experimento_binario_promedio(lista, m, k)
    
    plt.figure(figsize=(8,5))
    plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_promedio_binaria,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Búsqueda Binaria vs Busqueda Secuencial")
    plt.legend()
    plt.show()