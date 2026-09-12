# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:15:42 2024

@author: SD
"""

import numpy as np

def escalonar_filas(matriz):
    matriz = np.array(matriz, dtype=float)
    n_filas, n_columnas = matriz.shape
    fila_actual = 0
    for col in range(n_columnas):
        pivot = None
        for row in range(fila_actual, n_filas):
            if matriz[row, col] != 0:
                pivot = row
                break 
        if pivot is not None:
            if pivot != fila_actual:
                matriz[[fila_actual, pivot]] = matriz[[pivot, fila_actual]]
            for row in range(fila_actual + 1, n_filas):
                coeficiente = matriz[row, col] / matriz[fila_actual, col]
                matriz[row] -= coeficiente * matriz[fila_actual]
            fila_actual += 1
    return matriz

# Ejemplo de uso:
matriz = [
    [1, (-1), 0, 1],
    [0, 1, 4, 0],
    [2, (-1), 0, (-2)],
    [(-3), 3, 0, (-1)]
]

matriz_escalonada = escalonar_filas(matriz)
print("Matriz escalonada:\n", matriz_escalonada)