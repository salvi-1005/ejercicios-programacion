import numpy as np

#Ejercicio 3 práctica 1

a = 7
b = a + 1

v = np.array([1,2,3,(-1)])
w = np.array([2,3,0,5])
print('v + w =', v + w)
print('2*v=' , 2*v )
print('v**2=', v ** 2)
A = np.array([[1,2,3,4,5],[0,1,2,3,4],[2,3,4,5,6],[0,0,1,2,3],[0,0,0,0,1]])
F = A[0:2,3:5]
G = A[:2,3:]
H = A[[0,2,4],:]
I = ind = np.array([0,2,4])
J = A[ind,ind]
K = A[ind,ind[:,None]]

1j*1j
(1+2j)*1j

#Ejercicio 21 práctica 1

#a)
def esCuadrada(A):
    nlin, ncol = A.shape
    return nlin == ncol

def traza(A):
    lista = []
    if esCuadrada(A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i == j):
                    lista.append(A[i,j])
    res = sum(lista)
    return res  

#b)
def sumamodulo(A):
    lista = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            lista.append(A[i,j])
    resp = sum(lista)
    return resp

#c)
def comparar_sumas_positivos_negativos(A):
    suma_positivos = np.sum(A[A > 0])
    suma_negativos = np.sum(np.abs(A[A < 0]))
    
    return suma_positivos > suma_negativos
 
#Ejercicio 4 practica 1

xx = np.array([[1,1,1],[4,2,1],[9,3,1]])
yy = np.array([1,2,0])
L = np.linalg.solve(xx, yy)

f = np.array([[0.001,2],[1,1]])
g = np.array([8,2])
h = np.linalg.solve(f, g)


