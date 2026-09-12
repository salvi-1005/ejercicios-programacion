import random
import numpy as np

def medir_temp(n):
    temperaturas = []
    for i in range(n):
        temperaturas.append(random.normalvariate(37.5,0.2))
    return temperaturas

def resumen_temp(n):
    temp = medir_temp(n)
    promedio = sum(valor for valor in temp)/n
    ordenado = sorted(temp)
    if len(ordenado) % 2 == 0:
        mediana = (ordenado[len(ordenado)//2] + ordenado[len(ordenado)//2-1])/2
    else:
        mediana = ordenado[((len(ordenado)-1)//2)]
    return (max(temp), min(temp), promedio, mediana)  

n = 999
temperaturas = np.array(medir_temp(n))
np.save('temperaturas', temperaturas)