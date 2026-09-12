import random
import matplotlib.pyplot as plt
import numpy as np

#7.10)
def busqueda_lineal_ordenada(lista,e):
    encontrado = False
    for elem in lista:
        if elem == e:
            return True
        if elem > e:
            return False
    return encontrado

#7.11)
def indice(lista, e):
    for i, valor in enumerate(lista):
        if lista[i] == e:
            return i
    return -1

def donde_insertar(lista, x):
    izquierda = 0
    derecha = len(lista)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda

#7.12)
def insertar(lista, x):
    izquierda = 0
    derecha = len(lista)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

#7.15)
def no_es_ultima_secuencia(s):
    for elem in s:
        if elem == 0:
            return True
    return False

def listar_secuencias(n):
    lista = []
    s = [0]*n
    lista.append(s.copy()) #Agrego el [0]*n
    while no_es_ultima_secuencia(s):
        nueva_secuencia = incrementar(s)
        s = nueva_secuencia
        lista.append(s.copy())
    return lista

def busqueda_secuencial_comps(lista, x):
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria(lista, x, verbose = False):
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

#7.16)
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

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

m = 10000
k = 1000

largos = np.arange(256) + 1 
comps_promedio = np.zeros(256) 

def grafico_secuencial(m,k):
    largos = np.arange(256) + 1 
    comps_promedio = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
    
    plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()

#7.17)
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def grafico_binaria(m, k):
    largos = np.arange(256) + 1 
    comps_promedio = np.zeros(256)
    for i, n in enumerate(largos):
        lista_2 = generar_lista(n, m) 
        comps_promedio[i] = experimento_binario_promedio(lista_2, m, k)
    
    plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()

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