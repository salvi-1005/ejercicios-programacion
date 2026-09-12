import numpy as np
import random
import matplotlib.pyplot as plt

a = np.array([5,6,3,2,4,1])

np.empty(2)
np.arange(2, 9, 2)
np.linspace(0, 10, num=5)

#6.7)
impares = np.arange(1, 20, 2)
impares_2 = np.linspace(1, 19, num = 10)

print(impares)
print(impares_2)

x = np.ones(2, dtype=np.int64)

print(np.sort(a))

b = np.array([1, 2, 3, 4])
c = np.array([5, 6, 7, 8])

conc = np.concatenate((b, c))

array_ejemplo = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])

print(array_ejemplo.ndim) 
print(array_ejemplo.shape)  
print(array_ejemplo.size) 

d = a.reshape(3, 2)
print(d)

e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(e[e < 5])

five_up = (e >= 5)
print(e[five_up])

pares = e[e%2==0]
print(pares)

print(e[(e > 2) & (e < 11)])
print(five_up)

f = np.nonzero(e < 5)
print(f)

lista_de_coordenadas = list(zip(f[0], f[1]))

for coord in lista_de_coordenadas:
    print(coord)

#%%Guardar datos en disco
#)Formato de texto
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr)
np.loadtxt('new_file.csv')

#6.8)
def medir_temp(n):
    temperaturas = []
    for i in range(n):
        temperaturas.append(random.normalvariate(37.5,0.2))
    return temperaturas

#En forma compacta
n = 999
temperaturas = np.array(medir_temp(n))
np.save('temperaturas', temperaturas)
np.load('temperaturas.npy')

#6.9)
def plotear_temperaturas():
    temperaturas = np.load('temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.xlabel('Temperatura')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas simuladas')
    plot = plt.show() 
    return plot