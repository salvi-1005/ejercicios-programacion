import random
import numpy as np
import matplotlib.pyplot as plt

def medir_temp(n):
    temperaturas = []
    for i in range(n):
        temperaturas.append(random.normalvariate(37.5,0.2))
    return temperaturas

#6.9)
def plotear_temperaturas():
    temperaturas = np.load('temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.xlabel('Temperatura')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas simuladas')
    plot = plt.show() 
    return plot

