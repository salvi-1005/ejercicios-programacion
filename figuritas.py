import random
import numpy as np
import matplotlib.pyplot as plt

figus_total = 670
album_vacio = np.zeros(figus_total, dtype=np.int64)

def completo(album):
    completo = True
    for figurita in album:
        if figurita == 0:
            return False
    return completo

contador = 0
while not completo(album_vacio):
    figurita = random.randint(0,figus_total-1)
    album_vacio[figurita] = 1
    contador += 1
print(contador)

#6.13)
def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

#6.14)
def album_incompleto(A):
    completo = False
    for figurita in A:
        if figurita == 0:
            return True
    return completo

#6.15)
def comprar_figu(figus_total):
    figurita = random.randint(0,figus_total-1)
    return figurita

#6.16)
def cuantas_figus(figus_total):
    contador = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1
        contador += 1
    return contador

#6.17)
n_repeticiones = 1000
figus_total = 6

lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
figus_promedio = int(np.mean(lista))

#6.18)
def experimento_figus(n_repeticiones, figus_total):
    lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    figus_promedio = int(np.mean(lista))
    return figus_promedio

#)Con paquetes

figus_total = 670
figus_paquete = 5

#6.19)
e = list(np.arange(0, 670))
random.choices(e, k=5)

#6.20)
def comprar_paquete(figus_total, figus_paquete):
    todas_las_figuritas = list(np.arange(0, figus_total))
    paquete = random.choices(todas_las_figuritas, k=5)
    return paquete

#6.21)
def cuantos_paquetes(figus_total, figus_paquete):
    contador = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figurita in paquete:
            album[figurita] += 1
        contador += 1
    return contador
    
#6.22)
n_repeticiones = 100
lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
paquetes_promedio = int(np.mean(lista))

#Gráfico
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#6.23)
n_paquetes_hasta_llenar = np.array(lista)
prob = ((n_paquetes_hasta_llenar <= 850).sum())/len(lista)
np.save('n_paquetes_hasta_llenar', n_paquetes_hasta_llenar)

#6.24)
def plotear_paquetes():
    temperaturas = np.load('n_paquetes_hasta_llenar.npy')
    plt.hist(temperaturas,bins=25)
    plt.xlabel('Paquetes')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de paquetes simulados')
    plot = plt.show() 
    return plot