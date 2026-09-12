import numpy as np
import random

#Calculo matriz de conectividad
def construir_matriz_conectividad(links):
    n = len(links)  
    W = [[0] * n for _ in range(n)]
    for j, enlaces in enumerate(links):
        for i in enlaces:
            W[i][j] = 1  
    return W

#Calculo "cj"
def calcular_cj(matriz):
    n = len(matriz)  
    m = len(matriz[0])  
    cj = [0] * m  
    for i in range(n):  
        for j in range(m): 
            cj[j] += matriz[i][j]  
    return cj
                
#Calculo "xi"

def calcular_xi(matriz, x, c):
    n = len(matriz)  
    m = len(matriz[0])  
    resultados = [0] * n  
    
    for i in range(n):  
        suma = 0
        for j in range(m): 
            suma += (x[j] / c[j]) * matriz[i][j] 
        
        resultados[i] = suma  
    
    return resultados

#Calculo matriz diagonal
def construir_matriz_diagonal(cj):
    n = len(cj)  
    D = []  
    for j in range(n): 
        if cj[j] != 0:
            D.append([1 / cj[j] if cj[j] != 0 else 0 for _ in range(n)])  
        else:
            D.append([0] * n)  
    return D

#Calculo matriz R
def calcular_matriz_R(W, D):
    n = len(W)
    m = len(W[0])
    if len(D) != n or len(D[0]) != n:
        raise ValueError("Las dimensiones de W y D no son compatibles")
    R = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(n):
                R[i][j] += W[i][k] * D[k][j]
    return R

#Calculo matriz A
def construir_matriz_A(W, c, p):
    n = len(W)
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if c[j] != 0:
                A[i][j] = ((1 - p) / n) + (p * W[i][j] / c[j])
            else:
                A[i][j] = 1 / n
    return A

#calculo p
def generar_probabilidad():
    return random.uniform(0, 1)

#Calculo "e"
def vector_de_unos(n):
    return np.ones(n)

#calculo "z"
def construir_vector_z(c, p):
    n = len(c)
    z = np.zeros(n)
    for j in range(n):
        if c[j] != 0:
            z[j] = (1 - p) / n
        else:
            z[j] = 1 / n
    return z


#Calculo A mediante la fórmula pWD + ez
def pwdez(n, links, cj, c):
    return generar_probabilidad()*(np.dot(construir_matriz_conectividad(links), construir_matriz_diagonal(cj))) + np.dot(vector_de_unos(n), construir_vector_z(c, generar_probabilidad())) 

#Calculo pageRank mediante la fórmula Ax = x
def pageRank(n, links, cj, c, matriz, x, W, p):
    F = construir_matriz_A(W, c, p)
    G = calcular_xi(matriz, x, c)
    return np.linalg.solve(F,G)

