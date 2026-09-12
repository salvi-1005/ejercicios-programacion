# ej 3 guia 3 

import numpy as np
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


def resolver_Ly_b(L, b):
    return sustitucion_hacia_adelante(L, b)

def resolver_Ux_y(U, y):
    return sustitucion_hacia_atras(U, y)

# ej 4 guia 3
#a)

def descomposicion_LU_sin_pivoteos(A): #sin pivoteos
    n = A.shape[0]
    L = np.eye(n)  
    U = A.copy()   
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]
    return L, U

def descomposicion_LU(A): #con pivoteos
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            suma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - suma
        for j in range(i+1, n):
            suma = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - suma) / U[i][i]
    return L, U

#b)
def resolver_sistema_LU(A, b):
    L, U = descomposicion_LU(A)
    y = resolver_Ly_b(L, b)
    x = resolver_Ux_y(U, y)
    return x

A = np.array([[1,(-1),0,1],[0,1,4,0],[2,(-1),0,(-2)],[(-3),3,0,(-1)]])
L = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[(-3),0,0,1]])
U = np.array([[1,(-1),0,1],[0,1,4,0],[0,0,(-4),(-4)],[0,0,0,2]])
b = np.array([1, (-7), (-5), 1], dtype=float)

np.dot(L,U)

S = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
I = np.array([[1,0,0],[0,1,0],[0,0,1]])

norma_infinito = np.linalg.norm(I, ord=np.inf)

inversa_norma_infinito = 1 / norma_infinito

condicion_infinito = np.linalg.norm(I, ord=np.inf) * np.linalg.norm(np.linalg.inv(I), ord=np.inf)

Q = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

U, S, V = np.linalg.svd(Q)

def es_admisible_LU(I):
    if len(I.shape) != 2 or I.shape[0] != I.shape[1]:
        return False  
    try:
        np.linalg.cholesky(I)
        return True
    except np.linalg.LinAlgError:
        return False  

np.random.seed(0)
A = (np.random.rand(5, 3) * 10).astype(np.int32)

def gram_schmidt_qr(A):
    m, n = A.shape
    Q = np.zeros((m, n)).astype(np.int32)
    R = np.zeros((n, n)).astype(np.int32)

    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R

def householder_qr(A):
    m, n = A.shape
    Q = np.eye(m).astype(np.int32)
    R = A.copy().astype(np.int32)

    for k in range(n):
        x = R[k:, k].astype(np.int32)
        e = np.zeros_like(x).astype(np.int32)
        e[0] = np.linalg.norm(x).astype(np.int32)
        v = (np.sign(x[0]) * e + x).astype(np.int32)
        v = v / np.linalg.norm(v).astype(np.int32)

        R[k:, k:] -= 2 * np.outer(v, np.dot(v, R[k:, k:])).astype(np.int32)
        Q[k:] -= 2 * np.outer(v, np.dot(v, Q[k:])).astype(np.int32)

    return Q.T, np.triu(R[:n, :])

Q_gs, R_gs = gram_schmidt_qr(A)
Q_hh, R_hh = householder_qr(A)
Q_np, R_np = np.linalg.qr(A)

def qr_solver(A, b):
    Q, R = np.linalg.qr(A)
    y = np.dot(Q.T, b)
    x = np.linalg.solve(R, y)

    return x

A = np.array([[1, -1, 2],
              [0, -1, 1],
              [2, 1, -1]])
b = np.array([5, -1, 2])
x = qr_solver(A, b)
