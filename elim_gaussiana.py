#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,1,2,3],[4,3,3,4],[(-2),2,(-4),(-12)],[4,1,8,(-3)]])

#1 & 2)
def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
    else:
        for k in range(len(Ac)-1):
            for i in range(k+1, len(Ac)):
                factor = Ac[i, k] / Ac[k, k]
                Ac[i, k] = factor
                cant_op += 1
                for j in range(k+1, len(Ac)):
                    Ac[i, j] -= factor * Ac[k, j]
                    cant_op += 1
    return Ac, cant_op


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    for i in range(len(B)):
        for j in range(len(B[0])):
            if i == j:
                return 1
            if i > j:
                return (-1)
    return 0
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()

#3)
def num_operaciones(n):
    return n**3 / 3 + n**2 / 2 - n / 6

# Tamaños de la matriz
tamanios = np.arange(2, 101)  # Considerando matrices de tamaño de 2 a 100

# Calcular el número de operaciones para cada tamaño de matriz
operaciones = [num_operaciones(n) for n in tamanios]

# Graficar
plt.plot(tamanios, operaciones)
plt.xlabel('Tamaño de la matriz (n)')
plt.ylabel('Número de operaciones')
plt.title('Número de operaciones en función del tamaño de la matriz')
plt.grid(True)
plt.show()
    
#4)
def sustitucion_hacia_adelante(L, b):
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y

def sustitucion_hacia_atras(U, y):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x