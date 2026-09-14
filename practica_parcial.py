def suma_impares(n):
    if n == 1:
        return 1
    return n + suma_impares(n - 2)

n = 7
print(f"Suma impares de {n}: {suma_impares(n)}")

def cantidad_ceros(n):
    if n < 10:
        if n == 0:
            return 1
        return 0
    if n % 10 == 0:
        return 1 + cantidad_ceros(n // 10)
    return cantidad_ceros(n // 10)

n = 10090
print(f"Cantidad de ceros de {n}: {cantidad_ceros(n)}")

def es_potencia_de_2(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return es_potencia_de_2(n // 2)

n = 64
print(f"{n} es potencia de 2? {es_potencia_de_2(n)}")

def maximo_digito(n):
    if n < 10:
        return n
    max_resto = maximo_digito(n // 10)
    if n % 10 > max_resto:
        return n % 10
    return max_resto

n = 478639
print(f"El máximo dígito de {n} es: {maximo_digito(n)}")

def rotar_derecha(lista, i=0):
    if i >= len(lista):
        return []
    return [lista[i-1]] + rotar_derecha(lista, i+1)

lista = [1,2,3,4]
print(f"Lista {lista} rotada: {rotar_derecha(lista)}")

def rotar_derecha_cola(lista, resultado=None, i=0):
    if resultado is None:
        resultado = []
    if i >= len(lista):
        return resultado
    resultado.append(lista[i-1])
    return rotar_derecha_cola(lista, resultado, i+1)

lista = [1,2,3,4]
print(f"Lista {lista} rotada: {rotar_derecha_cola(lista)}")

def rotar_derecha_iterativo(lista):
    resultado = []
    for i in range(len(lista)):
        resultado.append(lista[i-1])
    return resultado

lista = [1,2,3,4]
print(f"Lista {lista} rotada: {rotar_derecha_iterativo(lista)}")

def interseccion(lista1, lista2):
    if not lista1:
        return []
    if lista1[0] in lista2:
        return [lista1[0]] + interseccion(lista1[1:], lista2)
    return interseccion(lista1[1:], lista2)

lista1 = [1,2,3,4]
lista2 = [3,4,5,6]
print(f"Intersección entre {lista1} y {lista2}: {interseccion(lista1, lista2)}")

def interseccion_cola(lista1, lista2, resultado=None, i=0):
    if resultado is None:
        resultado = []
    if i >= len(lista1):
        return resultado
    if lista1[i] in lista2:
        resultado.append(lista1[i])
    return interseccion_cola(lista1, lista2, resultado, i+1)

lista1 = [1,2,3,4]
lista2 = [3,4,5,6]
print(f"Intersección entre {lista1} y {lista2}: {interseccion_cola(lista1, lista2)}")

def interseccion_iterativo(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            resultado.append(lista1[i])
    return resultado

lista1 = [1,2,3,4]
lista2 = [3,4,5,6]
print(f"Intersección entre {lista1} y {lista2}: {interseccion_iterativo(lista1, lista2)}")

def aux_cantidad_apariciones(lista, n):
    if not lista:
        return 0
    if lista[0] == n:
        return 1 + aux_cantidad_apariciones(lista[1:], n)
    return aux_cantidad_apariciones(lista[1:], n)

def eliminar_repetidos(lista):
    if not lista:
        return []
    if aux_cantidad_apariciones(lista, lista[0]) > 1:
        return eliminar_repetidos(lista[1:])
    return [lista[0]] + eliminar_repetidos(lista[1:])

lista = [1,2,2,3,3,3]
print(f"Lista {lista} sin repetidos: {eliminar_repetidos(lista)}")

def eliminar_repetidos_cola(lista, resultado=None):
    if resultado is None:
        resultado = []
    if not lista:
        return resultado
    if aux_cantidad_apariciones(lista, lista[0]) > 1:
        return eliminar_repetidos_cola(lista[1:], resultado)
    resultado.append(lista[0])
    return eliminar_repetidos_cola(lista[1:], resultado)

lista = [1,2,2,3,3,3]
print(f"Lista {lista} sin repetidos: {eliminar_repetidos_cola(lista)}")

def eliminar_repetidos_iterativo(lista):
    resultado = []
    for i in range(len(lista)):
        if aux_cantidad_apariciones(lista, lista[i]) == 1 \
            or (aux_cantidad_apariciones(lista, lista[i]) > 1 \
                and lista[i] not in resultado):
            resultado.append(lista[i])
    return resultado

lista = [1,2,2,3,3,3]
print(f"Lista {lista} sin repetidos: {eliminar_repetidos_iterativo(lista)}")

def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    return (lista[0] <= lista[1] and esta_ordenada(lista[1:]))

lista = [1,2,3,4,5]
print(f"Está ordenada la lista {lista}? {esta_ordenada(lista)}")

def esta_ordenada_cola(lista):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False
    return esta_ordenada_cola(lista[1:])

lista = [1,2,3,4,5]
print(f"Está ordenada la lista {lista}? {esta_ordenada_cola(lista)}")

def esta_ordenada_iterativo(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

lista = [1,2,3,4,5]
print(f"Está ordenada la lista {lista}? {esta_ordenada_iterativo(lista)}")

def quicksort(lista):
  if len(lista) <= 1:
    return lista
  pivote = lista[len(lista) // 2]

  menores = [x for x in lista if x < pivote]
  iguales = [x for x in lista if x == pivote]
  mayores = [x for x in lista if x > pivote]

  return quicksort(menores) + iguales + quicksort(mayores)

def fusionar_ordenadas(lista1, lista2):
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    if lista1[0] <= lista2[0]:
        return [lista1[0]] + fusionar_ordenadas(lista1[1:], lista2)
    return [lista2[0]] + fusionar_ordenadas(lista1,lista2[1:])
    
lista1 = [1,5,7]
lista2 = [2,3,4,6]
print(f"Fusion de listas ordenadas: {fusionar_ordenadas(lista1, lista2)}")

def fusionar_ordenadas_cola(lista1, lista2, resultado=None):
    if resultado is None:
        resultado = []
    if not lista1:
        resultado.extend(lista2)
        return resultado
    if not lista2:
        resultado.extend(lista1)
        return resultado
    if lista1[0] <= lista2[0]:
        resultado.append(lista1[0])
        return fusionar_ordenadas_cola(lista1[1:], lista2, resultado)
    resultado.append(lista2[0])
    return fusionar_ordenadas_cola(lista1,lista2[1:],resultado)
    
lista1 = [1,5,7]
lista2 = [2,3,4,6]
print(f"Fusion de listas ordenadas: {fusionar_ordenadas_cola(lista1, lista2)}")

def fusionar_ordenadas_iterativo(lista1, lista2):
    resultado = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        if lista1[i] > lista2[j]:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado
    
lista1 = [1,5,7]
lista2 = [2,3,4,6]
print(f"Fusion de listas ordenadas: {fusionar_ordenadas_iterativo(lista1, lista2)}")

def subsecuencias_contiguas(lista, nivel=None):
    if nivel is None:
        nivel = len(lista)
    if nivel == 0:
        return []
    resultado_actual = [lista[i:nivel] for i in range(nivel)]
    return (resultado_actual + subsecuencias_contiguas(lista, nivel - 1))

lista = [1,2,3,4,5]
print(f"Subsecuencias contiguas de {lista}: {subsecuencias_contiguas(lista)}")

def subsecuencias_contiguas_cola(lista, nivel=None, resultado=None):
    if resultado is None:
        resultado = []
    if nivel is None:
        nivel = len(lista)
    if nivel == 0:
        return resultado
    for i in range(nivel):
        resultado.append(lista[i:nivel])
    return subsecuencias_contiguas_cola(lista,nivel - 1,resultado)
        
lista = [1,2,3,4,5]
print(f"Subsecuencias contiguas de {lista}: {subsecuencias_contiguas_cola(lista)}")

def subsecuencias_contiguas_iterativa(lista):
    resultado = []
    for nivel in range(len(lista), 0, -1):
        for i in range(nivel):
            resultado.append(lista[i:nivel])
    return resultado
        
lista = [1,2,3,4,5]
print(f"Subsecuencias contiguas de {lista}: {subsecuencias_contiguas_cola(lista)}")

def subsecuencias_no_contiguas(lista):
    if not lista:
        return [list()]
    primero = lista[0]
    nueva_lista = []
    for elem in subsecuencias_no_contiguas(lista[1:]):
        nueva_lista.append([primero] + elem)
    return subsecuencias_no_contiguas(lista[1:]) + nueva_lista

lista = ['A','B','C','D','E']
print(f"Subsecuencias no contiguas de {lista}: {subsecuencias_no_contiguas(lista)}")

def subsecuencias_no_contiguas_cola(lista, resultado=None):
    if resultado is None:
        resultado = [[]]
    if not lista:
        return resultado
    nuevos = []
    for subconjunto in resultado:
        nuevos.append(subconjunto + [lista[0]])
    resultado.extend(nuevos)
    return subsecuencias_no_contiguas_cola(lista[1:], resultado)

lista = ['A','B','C','D','E']
print(f"Subsecuencias no contiguas de {lista}: {subsecuencias_no_contiguas_cola(lista)}")

def subsecuencias_no_contiguas_iterativo(lista):
  resultado = [list()]
  for elemento in lista:
    nuevos = [sub + [elemento] for sub in resultado]
    resultado.extend(nuevos)
  return resultado

lista = ['A','B','C','D','E']
print(f"Subsecuencias no contiguas de {lista}: {subsecuencias_no_contiguas_iterativo(lista)}")

def mochila(objetos, capacidad, combinaciones=None):
    if combinaciones is None:
        combinaciones = subsecuencias_no_contiguas(objetos)
    if not combinaciones:
        return []
    if sum(combinaciones[0]) <= capacidad and len(combinaciones[0]) > 0:
        return [combinaciones[0]] + mochila(objetos, capacidad, combinaciones[1:])
    return mochila(objetos, capacidad, combinaciones[1:])
    
objetos = [2,4,7,5]
capacidad = 9
print(f"Posibles combinaciones de {objetos} con peso {capacidad}: {mochila(objetos, capacidad)}")

def mochila_cola(objetos, capacidad, combinaciones=None, resultado = None):
    if resultado is None:
        resultado = []
    if combinaciones is None:
        combinaciones = subsecuencias_no_contiguas(objetos)
    if not combinaciones:
        return resultado
    if sum(combinaciones[0]) <= capacidad and len(combinaciones[0]) > 0:
        resultado.append(combinaciones[0])
        return mochila_cola(objetos, capacidad, combinaciones[1:], resultado)
    return mochila_cola(objetos, capacidad, combinaciones[1:], resultado)
    
objetos = [2,4,7,5]
capacidad = 9
print(f"Posibles combinaciones de {objetos} con peso {capacidad}: {mochila_cola(objetos, capacidad)}")

def mochila_iterativo(objetos, capacidad):
    resultado = []
    combinaciones = subsecuencias_no_contiguas(objetos)
    for i in range(len(combinaciones)):
        if sum(combinaciones[i]) <= capacidad and len(combinaciones[i]) > 0:
            resultado.append(combinaciones[i])
    return resultado
    
objetos = [2,4,7,5]
capacidad = 9
print(f"Posibles combinaciones de {objetos} con peso {capacidad}: {mochila_iterativo(objetos, capacidad)}")

def particionar_pila(lista, pivote):
    if not lista:
        return ([],[])
    izquierda, derecha = particionar_pila(lista[1:], pivote)
    if lista[0] < pivote:
        return ([lista[0]] + izquierda, derecha)
    if lista[0] >= pivote:
        return (izquierda, [lista[0]] + derecha)
    
lista = [7,2,9,4,1,8]
pivote = 5
print(f"Particiones (pila): {particionar_pila(lista, pivote)}")

def particionar_cola(lista, pivote, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda = []
    if derecha is None:
        derecha = []
    if not lista:
        return (izquierda, derecha)
    if lista[0] < pivote:
        izquierda.append(lista[0])
        return particionar_cola(lista[1:], pivote, izquierda, derecha)
    if lista[0] >= pivote:
        derecha.append(lista[0])
        return particionar_cola(lista[1:], pivote, izquierda, derecha)
    
lista = [7,2,9,4,1,8]
pivote = 5
print(f"Particiones (cola): {particionar_cola(lista, pivote)}")
    
def particionar_iterativo(lista, pivote):
    izquierda = []
    derecha = []
    for elem in lista:
        if elem < pivote:
            izquierda.append(elem)
        if elem >= pivote:
            derecha.append(elem)
    return (izquierda, derecha)
    
lista = [7,2,9,4,1,8]
pivote = 5
print(f"Particiones (iterativo): {particionar_iterativo(lista, pivote)}")

def agrupar_por_paridad(lista):
    if not lista:
        return ([],[])
    izquierda, derecha = agrupar_por_paridad(lista[1:])
    if lista[0] % 2 == 0:
        return ([lista[0]] + izquierda, derecha)
    if lista[0] % 2 != 0:
        return (izquierda, [lista[0]] + derecha)
    
lista = [7,2,9,4,1,8]
print(f"Agrupar por paridad: {agrupar_por_paridad(lista)}")

def agrupar_por_paridad_cola(lista, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda = []
    if derecha is None:
        derecha = []
    if not lista:
        return (izquierda, derecha)
    if lista[0] % 2 == 0:
        izquierda.append(lista[0])
        return agrupar_por_paridad_cola(lista[1:], izquierda, derecha)
    if lista[0] % 2 != 0:
        derecha.append(lista[0])
        return agrupar_por_paridad_cola(lista[1:], izquierda, derecha)
    
lista = [7,2,9,4,1,8]
print(f"Agrupar por paridad: {agrupar_por_paridad_cola(lista)}")
    
def agrupar_por_paridad_iterativo(lista):
    izquierda = []
    derecha = []
    for elem in lista:
        if elem % 2 == 0:
            izquierda.append(elem)
        if elem % 2 != 0:
            derecha.append(elem)
    return (izquierda, derecha)
    
lista = [7,2,9,4,1,8]
print(f"Agrupar por paridad: {agrupar_por_paridad_iterativo(lista)}")

def separar_positivos_negativos(lista):
    if not lista:
        return ([],[])
    izquierda, derecha = separar_positivos_negativos(lista[1:])
    if lista[0] >= 0:
        return ([lista[0]] + izquierda, derecha)
    if lista[0] < 0:
        return (izquierda, [lista[0]] + derecha)
    
lista = [3,-2,7,-5,0,-1,4]
print(f"Separar positivos de negativos: {separar_positivos_negativos(lista)}")

def separar_positivos_negativos_cola(lista, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda = []
    if derecha is None:
        derecha = []
    if not lista:
        return (izquierda, derecha)
    if lista[0] >= 0:
        izquierda.append(lista[0])
        return separar_positivos_negativos_cola(lista[1:], izquierda, derecha)
    if lista[0] < 0:
        derecha.append(lista[0])
        return separar_positivos_negativos_cola(lista[1:], izquierda, derecha)
    
lista = [3,-2,7,-5,0,-1,4]
print(f"Separar positivos de negativos: {separar_positivos_negativos_cola(lista)}")
    
def separar_positivos_negativos_iterativo(lista):
    izquierda = []
    derecha = []
    for elem in lista:
        if elem >= 0:
            izquierda.append(elem)
        if elem < 0:
            derecha.append(elem)
    return (izquierda, derecha)
    
lista = [3,-2,7,-5,0,-1,4]
print(f"Separar positivos de negativos: {separar_positivos_negativos_iterativo(lista)}")

def separar_multiplos_de_3(lista):
    if not lista:
        return ([],[])
    izquierda, derecha = separar_multiplos_de_3(lista[1:])
    if lista[0] % 3 == 0:
        return ([lista[0]] + izquierda, derecha)
    return (izquierda, [lista[0]] + derecha)

lista = [1,3,4,6,7,9,10,12]
print(f"Separar múltiplos de 3: {separar_multiplos_de_3(lista)}")

def separar_multiplos_de_3_cola(lista, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda = []
    if derecha is None:
        derecha = []
    if not lista:
        return izquierda, derecha
    if lista[0] % 3 == 0:
        izquierda.append(lista[0])
        return separar_multiplos_de_3_cola(lista[1:], izquierda, derecha)
    if lista[0] % 3 != 0:
        derecha.append(lista[0])
        return separar_multiplos_de_3_cola(lista[1:], izquierda, derecha)
        
lista = [1,3,4,6,7,9,10,12]
print(f"Separar múltiplos de 3: {separar_multiplos_de_3_cola(lista)}")

def separar_multiplos_de_3_iterativo(lista):
    izquierda = []
    derecha = []
    for elem in lista:
        if elem % 3 == 0:
            izquierda.append(elem)
        if elem % 3 != 0:
            derecha.append(elem)
    return (izquierda, derecha)

lista = [1,3,4,6,7,9,10,12]
print(f"Separar múltiplos de 3: {separar_multiplos_de_3_iterativo(lista)}")

def separar_vocales_consonantes(palabra):
    if not palabra:
        return ([],[])
    izquierda, derecha = separar_vocales_consonantes(palabra[1:])
    if palabra[0] in 'aeiou':
        return ([palabra[0]] + izquierda, derecha)
    return (izquierda, [palabra[0]] + derecha)

palabra = 'algoritmos'
print(f"Separar vocales de consonantes: {separar_vocales_consonantes(palabra)}")

def separar_vocales_consonantes_cola(palabra, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda = []
    if derecha is None:
        derecha = []
    if not palabra:
        return izquierda, derecha
    if palabra[0] in 'aeiou':
        izquierda.append(palabra[0])
        return separar_vocales_consonantes_cola(palabra[1:], izquierda, derecha)
    if palabra[0] not in 'aeiou':
        derecha.append(palabra[0])
        return separar_vocales_consonantes_cola(palabra[1:], izquierda, derecha)
        
palabra = 'algoritmos'
print(f"Separar vocales de consonantes: {separar_vocales_consonantes_cola(palabra)}")

def separar_vocales_consonantes_iterativo(palabra):
    izquierda = []
    derecha = []
    for elem in palabra:
        if elem in 'aeiou':
            izquierda.append(elem)
        if elem not in 'aeiou':
            derecha.append(elem)
    return (izquierda, derecha)

palabra = 'algoritmos'
print(f"Separar vocales de consonantes: {separar_vocales_consonantes_iterativo(palabra)}")

def agrupar_palabras(palabras):
    if not palabras:
        return ([],[],[],[])
    if len(palabras[0]) < 3:
        raise ValueError("Las palabras deben tener como mínimo 3 letras")
    grupo1,grupo2,grupo3,grupo4 = agrupar_palabras(palabras[1:])
    if len(palabras[0]) == 3:
        return ([palabras[0]] + grupo1, grupo2, grupo3, grupo4)
    if len(palabras[0]) == 4:
        return (grupo1, [palabras[0]] +  grupo2, grupo3, grupo4)
    if len(palabras[0]) >= 5 and len(palabras[0]) <= 7:
        return (grupo1, grupo2, [palabras[0]] + grupo3, grupo4)
    if len(palabras[0]) > 7:
        return (grupo1, grupo2, grupo3, [palabras[0]] + grupo4)
    
palabras = ["sol", "luna", "mar", "estrella", "cielo"]
print(f"palabras agrupadas por longitud: {agrupar_palabras(palabras)}")

def agrupar_palabras_cola(palabras, grupo1=None, grupo2=None, grupo3=None, grupo4=None):
    if grupo1 is None:
        grupo1 = []
    if grupo2 is None:
        grupo2 = []
    if grupo3 is None:
        grupo3 = []
    if grupo4 is None:
        grupo4 = []
    if not palabras:
        return (grupo1, grupo2, grupo3, grupo4)
    if len(palabras[0]) < 3:
        raise ValueError("Las palabras deben tener como mínimo 3 letras")
    if len(palabras[0]) == 3:
        grupo1.append(palabras[0])
        return agrupar_palabras_cola(palabras[1:], grupo1, grupo2, grupo3, grupo4)
    if len(palabras[0]) == 4:
        grupo2.append(palabras[0])
        return agrupar_palabras_cola(palabras[1:], grupo1, grupo2, grupo3, grupo4)
    if len(palabras[0]) >= 5 and len(palabras[0]) <= 7:
        grupo3.append(palabras[0])
        return agrupar_palabras_cola(palabras[1:], grupo1, grupo2, grupo3, grupo4)
    if len(palabras[0]) > 7:
        grupo4.append(palabras[0])
        return agrupar_palabras_cola(palabras[1:], grupo1, grupo2, grupo3, grupo4)
    
palabras = ["sol", "luna", "mar", "estrella", "cielo"]
print(f"palabras agrupadas por longitud: {agrupar_palabras_cola(palabras)}")

def agrupar_palabras_iterativo(palabras):
    if len(palabras[0]) < 3:
        raise ValueError("Las palabras deben tener como mínimo 3 letras")
    grupo1 = []
    grupo2 = []
    grupo3 = []
    grupo4 = []
    for palabra in palabras:
        if len(palabra) == 3:
            grupo1.append(palabra)
        if len(palabra) == 4:
            grupo2.append(palabra)
        if len(palabra) >= 5 and len(palabra) <= 7:
            grupo3.append(palabra)
        if len(palabra) > 7:
            grupo4.append(palabra)
    return (grupo1, grupo2, grupo3, grupo4)
    
palabras = ["sol", "luna", "mar", "estrella", "cielo"]
print(f"palabras agrupadas por longitud: {agrupar_palabras_iterativo(palabras)}")

def agrupar_numeros(numeros):
    if not numeros:
        return ([],[],[])
    positivos, negativos, ceros = agrupar_numeros(numeros[1:])
    if numeros[0] > 0:
        return ([numeros[0]] + positivos, negativos, ceros)
    if numeros[0] < 0:
        return (positivos, [numeros[0]] +  negativos, ceros)
    if numeros[0] == 0:
        return (positivos, negativos, [numeros[0]] + ceros)
    
numeros = [3,-2,7,-5,0,-1,4]
print(f"Agrupar números: {agrupar_numeros(numeros)}")

def agrupar_numeros_cola(numeros, positivos=None, negativos=None, ceros=None):
    if positivos is None:
        positivos = []
    if negativos is None:
        negativos = []
    if ceros is None:
        ceros = []
    if not numeros:
        return (positivos, negativos, ceros)
    if numeros[0] > 0:
        positivos.append(numeros[0])
        return agrupar_numeros_cola(numeros[1:], positivos, negativos, ceros)
    if numeros[0] < 0:
        negativos.append(numeros[0])
        return agrupar_numeros_cola(numeros[1:], positivos, negativos, ceros)
    if numeros[0] == 0:
        ceros.append(numeros[0])
        return agrupar_numeros_cola(numeros[1:], positivos, negativos, ceros)
    
    
numeros = [3,-2,7,-5,0,-1,4]
print(f"Agrupar números: {agrupar_numeros_cola(numeros)}")

def agrupar_numeros_iterativo(numeros):
    positivos = []
    negativos = []
    ceros = []
    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
        if numero < 0:
            negativos.append(numero)
        if numero == 0:
            ceros.append(numero)
    return (positivos, negativos, ceros)
    
numeros = [3,-2,7,-5,0,-1,4]
print(f"Agrupar números: {agrupar_numeros_iterativo(numeros)}")

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > maximo(lista[1:]):
        return lista[0]
    return maximo(lista[1:])

def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] < minimo(lista[1:]):
        return lista[0]
    return minimo(lista[1:])

def max_min(lista):
    if len(lista) == 1:
        return (lista[0], lista[0])
    max_resto, min_resto = max_min(lista[1:])
    maximo = max(lista[0], max_resto)
    minimo = min(lista[0], min_resto)
    return (maximo, minimo)
    
lista = [7,2,9,4,1,8]
print(f"Maximo y mínimo de {lista}: {max_min(lista)}")

def max_min_cola(lista, maximo=None, minimo=None):
    if maximo is None:
        maximo = lista[0]
    if minimo is None:
        minimo = lista[0]
    if not lista:
        return (maximo, minimo)
    if lista[0] > maximo:
        maximo = lista[0]
    if lista[0] < minimo:
        minimo = lista[0]
    return max_min_cola(lista[1:], maximo, minimo)
    
lista = [7,2,9,4,1,8]
print(f"Maximo y mínimo de {lista}: {max_min_cola(lista)}")

def max_min_iterativo(lista):
    maximo = lista[0]
    minimo = lista[0]
    for elem in lista:
        if elem > maximo:
            maximo = elem
        if elem < minimo:
            minimo = elem
    return (maximo, minimo)
        
lista = [7,2,9,4,1,8]
print(f"Maximo y mínimo de {lista}: {max_min_iterativo(lista)}")

def buscar_celda_vacia(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] == 0:
                return (fila, columna)
    return None

def es_valido(tablero, fila, columna, numero):
    if numero in tablero[fila]:
        return False
    for f in range(len(tablero)):
        if tablero[f][columna] == numero:
            return False
    fila_inicio = (fila // 2) * 2
    columna_inicio = (columna // 2) * 2
    for f in range(fila_inicio, fila_inicio + 2):
        for c in range(columna_inicio, columna_inicio + 2):
            if tablero[f][c] == numero:
                return False
    return True

def sudoku(tablero):
    posicion = buscar_celda_vacia(tablero)
    if posicion is None:
        return True
    fila, columna = posicion
    for numero in range(1,5):
        if es_valido(tablero, fila, columna, numero):
            tablero[fila][columna] = numero
            if sudoku(tablero):
                return True
            tablero[fila][columna] = 0
    return False

tablero = [[1,0,3,4], [0,4,1,0], [2,0,4,0], [0,3,0,1]]

if sudoku(tablero):
    print(f"Solución del sudoku: {tablero}")

def cantidad_caminos(fila_actual, columna_actual, fila_destino, columna_destino):
    if (fila_actual == fila_destino and columna_actual == columna_destino):
        return 1
    if (fila_actual > fila_destino or columna_actual > columna_destino):
        return 0
    return (cantidad_caminos(fila_actual + 1, columna_actual, fila_destino,columna_destino)\
        + cantidad_caminos(fila_actual, columna_actual + 1, fila_destino, columna_destino))
        
print(f"Cantidad de caminos de la grilla: {cantidad_caminos(0, 0, 2, 2)}")
        
def caminos(fila, columna, fila_destino, columna_destino, camino=""):
    if (fila == fila_destino and columna == columna_destino):
        return [camino]
    if (fila > fila_destino or columna > columna_destino):
        return []
    return (caminos(fila + 1, columna, fila_destino, columna_destino, camino + "D") + \
    caminos(fila, columna + 1, fila_destino, columna_destino, camino + "R"))
        
print(f"Todos los caminos de la grilla: {caminos(0, 0, 2, 2)}")

def avanzar(posicion, direccion):
    x, y = posicion
    if direccion == 'N':
        return (x - 1, y)
    if direccion == 'S':
        return (x + 1, y)
    if direccion == 'E':
        return (x, y + 1)
    if direccion == 'O':
        return (x, y - 1)

def laberinto(camino, validas, llegada):
    actual = camino[-1]
    if actual == llegada:
        return [camino]
    soluciones = []
    for direccion in ['N','S','E','O']:
        nueva = avanzar(actual, direccion)
        if (nueva in validas and nueva not in camino):
            soluciones.extend(laberinto(camino + [nueva], validas, llegada))
    return soluciones

validas = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
salida = (0,0)
llegada = (2,2)
print(f"Todos los caminos válidos: {laberinto([salida], validas, llegada)}")

#1)

def sumatoria_fila(lista):
    if not lista:
        return 0
    return lista[0] + sumatoria_fila(lista[1:])
    
def obtener_columna_rec(matriz, j, i=0):
    if i >= len(matriz):
        return []
    return [matriz[i][j]] + obtener_columna_rec(matriz, j, i + 1)

def matriz_transpuesta(matriz, j=0):
    if j >= len(matriz[0]):
        return []
    return [obtener_columna_rec(matriz, j)] + matriz_transpuesta(matriz, j + 1)

def restar_esquinas(matriz):
    return - matriz[0][0] - matriz[-1][0] - matriz[0][-1] - matriz[-1][-1]

def suma_bordes(matriz, i=-1):
    if i == 1:
        return restar_esquinas(matriz)
    return sumatoria_fila(matriz[i]) + sumatoria_fila(matriz_transpuesta(matriz)[i]) + \
        + suma_bordes(matriz, i+1)
        
matriz = [[1,2,3], [6,5,9], [8,7,4]]
print(f"Suma de bordes de {matriz}: {suma_bordes(matriz)}")

#2)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class TADListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self._tamaño = 0
    def es_vacia(self):
        return self.cabeza is None
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamaño += 1
    def tamaño(self):
        return self._tamaño
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        encontrado = False

        while actual is not None and not encontrado:
            if actual.dato == dato:
                encontrado = True
            else:
                anterior = actual
                actual = actual.siguiente

        if encontrado:
            if anterior is None:
                self.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            self._tamaño -= 1
            return True
        return False
    def obtener(self, indice):
        if indice < 0 or indice >= self._tamaño:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato
    def __str__(self):
        """Muestra los elementos de la lista en formato visual."""
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos)
    def filtrar_nodos(self, condicion):
        while self.cabeza is not None and not condicion(self.cabeza.dato):
            self.cabeza = self.cabeza.siguiente
            self._tamaño -= 1

        actual = self.cabeza
        while actual is not None and actual.siguiente is not None:
            if not condicion(actual.siguiente.dato):
                actual.siguiente = actual.siguiente.siguiente
                self._tamaño -= 1
            else:
                actual = actual.siguiente

mi_lista = TADListaEnlazada()

mi_lista.agregar(10)
mi_lista.agregar(15)
mi_lista.agregar(20)
mi_lista.agregar(25)
mi_lista.agregar(30)

condicion = lambda x: x % 10 == 0
mi_lista.filtrar_nodos(condicion)
print("Lista con múltiplos de 10:",mi_lista)

#3)

procesar_cadena = lambda letra: lambda accion: lambda lista_cadenas: \
    list(map(accion, filter(lambda x: x[0] == letra, lista_cadenas)))

letra = 'a'
pasar_mayuscula = lambda x: x.upper()
lista_cadenas = ['arbol', 'espejo', 'ala', 'casa', 'alambre']

resultado = procesar_cadena(letra)(pasar_mayuscula)(lista_cadenas)
print("Lista filtrada en mayúsculas:")
print(resultado)

def agregar_elemento_rec(elemento, lista_de_listas):
    if not lista_de_listas:
        return []
    primera_con_elemento = [elemento] + lista_de_listas[0]
    return [primera_con_elemento] + agregar_elemento_rec(elemento, lista_de_listas[1:])

def partes(lista):
    if not lista:
        return [[]]
    primero = lista[0]
    resto_partes = partes(lista[1:])
    con_primero = agregar_elemento_rec(primero, resto_partes)
    return resto_partes + con_primero

def combinaciones_longitud_n(lista, n, i = 0):
    if i == len(partes(lista)):
        return []
    if len(partes(lista)[i]) == n:
        return [partes(lista)[i]] + combinaciones_longitud_n(lista, n, i+1)
    return combinaciones_longitud_n(lista, n, i+1)

lista = [1,2,3,4]
n = 2
print(combinaciones_longitud_n(lista, n))

from functools import reduce

def total_por_categoria(acum, producto):
    cat = producto["categoria"] 
    subtotal = producto["precio"] * producto["cantidad"]
    if cat in acum:
        acum[cat] += subtotal
    else:
        acum[cat] = subtotal
    return acum

carrito = [
    {"producto": "Teclado", "categoria": "tecnologia", "precio": 100, "cantidad": 2},
    {"producto": "Monitor", "categoria": "tecnologia", "precio": 300, "cantidad": 1},
    {"producto": "Manzana", "categoria": "alimentos", "precio": 5, "cantidad": 6},
    {"producto": "Remera", "categoria": "ropa", "precio": 40, "cantidad": 2},
    {"producto": "Banana", "categoria": "alimentos", "precio": 4, "cantidad": 5}
]

frecuencias = reduce(total_por_categoria, carrito, {})  
print(f"Tabla de total por categoría: {frecuencias}")
