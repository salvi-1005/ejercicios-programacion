from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(m):
    hay_filas_parecidas = False
    fila_a_analizar = 1
    while not hay_filas_parecidas and fila_a_analizar < len(m):
        hay_filas_parecidas = True
        columna_a_analizar = 1
        while columna_a_analizar < len(m[fila_a_analizar]) and hay_filas_parecidas:
            if m[fila_a_analizar][columna_a_analizar] - m[fila_a_analizar - 1][columna_a_analizar] != m[fila_a_analizar][0] - m[fila_a_analizar - 1][0]:
                hay_filas_parecidas = False
            else:
                columna_a_analizar += 1
        fila_a_analizar += 1
    return hay_filas_parecidas

def esMatriz(m):
    sí_es_matriz = True
    n_fila = 1
    while sí_es_matriz and n_fila < len(m):
        if len(m[n_fila]) != len(m[0]):
            sí_es_matriz = False
        else:
            n_fila += 1
    return sí_es_matriz

def filasParecidasAanterior(m, n):
    hay_una_fila_parecida_a_anterior = False
    fila_a_analizar = 1
    while fila_a_analizar < len(m) and not hay_una_fila_parecida_a_anterior:
        if filaAnteriorMasN(m, fila_a_analizar, n):
            hay_una_fila_parecida_a_anterior = True
        else:
            fila_a_analizar += 1
    return hay_una_fila_parecida_a_anterior

def filaAnteriorMasN(m, i, n):
    es_fila_anterior_más_n = True
    columna_a_analizar = 0
    while es_fila_anterior_más_n and columna_a_analizar < len(m[i]):
        if m[i][columna_a_analizar] != m[i - 1][columna_a_analizar] + n:
            es_fila_anterior_más_n = False
        else:
            columna_a_analizar += 1
    return es_fila_anterior_más_n

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))