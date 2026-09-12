lista = [1,2,3,4,5,6,7,8,9,10,11,12]

def devolver(lista, i):
    if i == 0:
        return lista[0]

    return devolver(lista[1:], i - 1)

i = 3
print(f"El elemento que está en el índice {i} de la lista es: {devolver(lista, i)}")

def buscar_indice(lista, numero, indice=0):
    if indice >= len(lista):
        return -1

    if lista[indice] == numero:
        return indice

    return buscar_indice(lista, numero, indice + 1)

print("------------------------------------------------------")
n = 3
print(f"El elemento {n} se encuentra en el índice: {buscar_indice(lista, n)}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print("------------------------------------------------------")
n = 5   
print(f"Factorial de {n}: {factorial(n)}")

from functools import lru_cache as cache

@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
print("------------------------------------------------------")
n = 10   
print(f"Fibonacci de {n}: {fibonacci(n)}")
   
 
def fibonacci_iterativo(n):
    lista = []
    lista.append(0)
    lista.append(1)
    for i in range(2, n+1):
        lista.append(lista[i-1] + lista[i-2])
    return lista[n]
        
 
n = 10  
print(f"Fibonacci de {n}: {fibonacci_iterativo(n)}")   
 

def cant_elementos(lista):
   if len(lista) == 0:
      return 0
   lista.pop(len(lista)-1)
   return 1 + cant_elementos(lista)

print("------------------------------------------------------")
print(f"Cantidad de elementos en la lista: {cant_elementos(lista)}")

#Recursión mutua:

def es_par(n):
    return n == 0 or es_impar(n-1)

def es_impar(n):
    return False if n == 0 else es_par(n-1)

print("------------------------------------------------------")
n = 10
print(f"¿{n} es par? {es_par(n)}")
n = 9
print(f"¿{n} es par? {es_par(n)}")
n = 4
print(f"¿{n} es impar? {es_impar(n)}")
n = 7
print(f"¿{n} es impar? {es_impar(n)}")

#Recursión simple

def es_par2(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return es_par2(n-2)

print("------------------------------------------------------")
n = 2
print(f"¿{n} es par? {es_par2(n)}")
n = 9
print(f"¿{n} es par? {es_par2(n)}")

#Recursión implícita:

def mostrar_paridad(n):
    if es_par(n):
        print(f'{n} es par')
    else:
        print(f'{n} es impar')

print("------------------------------------------------------")
n = 10
mostrar_paridad(n)

#Ejercicio)

def cant_digitos(n):
   if n < 10:
      return 1
   return 1 + cant_digitos(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Cantidad de dígitos de {n}: {cant_digitos(n)}")

def reversa_num(n):
    if n < 10:
        return n
    return (n % 10) * (10**(cant_digitos(n)-1)) + reversa_num(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Reversa de {n}: {reversa_num(n)}")

def imprimir_digitos(n):
    if n == 0:
        return 0
    else:
        c = str(n)[0]
        print(c)
        return imprimir_digitos(n - int(c) * 10**(cant_digitos(n) - 1))

print("------------------------------------------------------")
n = 543
imprimir_digitos(n)

def imprimir_digitos_reversa(n):
    if n == 0:
        return 0
    else:
        print(str(n)[-1])
        return imprimir_digitos_reversa(n // 10)

print("------------------------------------------------------")
n = 543
imprimir_digitos_reversa(n)

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Suma de dígitos de {n}: {suma_digitos(n)}")

def reversa_y_suma(n):
    if n < 10:
        return (n, n)
    return ((n % 10) * (10**(cant_digitos(n)-1)) + reversa_num(n // 10), (n % 10) + suma_digitos(n // 10))

print("------------------------------------------------------")
n = 543
print(f"Reversa y suma de dígitos de {n}: {reversa_y_suma(n)}")

def es_par_n(n):
    if n == 0:
        return True
    if n >= 0:
        return es_impar_n(n-1)
    if n < 0:
        return es_impar_n(n+1)
def es_impar_n(n):
    if n == 0:
        return False
    if n >= 0:
        return es_par_n(n-1)
    if n < 0:
        return es_par_n(n+1)
    
print("------------------------------------------------------")   
n = -40  
print(f"¿{n} es par? {es_par_n(n)}")
n = -9
print(f"¿{n} es par? {es_par_n(n)}")
n = -4
print(f"¿{n} es impar? {es_impar_n(n)}")
n = -7
print(f"¿{n} es impar? {es_impar_n(n)}")

def letras_(S):
    if len(S) == 0:
        return ""
    else:
        return S[0] + "-" + letras_(S[1:len(S)])
    
print("------------------------------------------------------")
print(letras_('Hola'))

def digitos(n):
    if n < 10:
        return str(n)
    else:
        primeros_digitos = n // 10
        ultimo_digito= n % 10
        return digitos(primeros_digitos) + '/n' + str(ultimo_digito)
    
print("------------------------------------------------------")
n = 123456789
print(f"Dígitos: {digitos(n)}")

def pares(n, i=1):
    if i > n - i:
        return

    print(f"Pares que suman {n}: ({i}, {n - i})")
    pares(n, i + 1)

print("------------------------------------------------------")
pares(5)

#2)

def desde_hasta(a,b):
    if a > b:
        return []
    return [a] + desde_hasta(a+1, b)

print("------------------------------------------------------")
a = 1
b = 5
print(f"Números desde {a} hasta {b}: {desde_hasta(a,b)}")

def sumatoria(n):
    if n == 0:
        return 0
    return n + sumatoria(n-1)

print("------------------------------------------------------")
n = 10
print(f"Sumatoria de {n}: {sumatoria(n)}")

def sumatoria_desde_hasta(a, b):
    if len(desde_hasta(a, b)) == 0:
        return 0
    return a + sumatoria_desde_hasta(a+1, b)

print("------------------------------------------------------")
n = 10
a = 1
b = 10
print(f"Sumatoria de {n}: {sumatoria_desde_hasta(a,b)}")

def factorial_desde_hasta(a, b):
    if len(desde_hasta(a, b)) == 0:
        return 1
    return b * factorial_desde_hasta(a, b-1)

print("------------------------------------------------------")
n = 7
a = 1
b = 7
print(f"Factorial de {n}: {factorial_desde_hasta(a, b)}")

def desde_hasta_cola(a, b, acum=None):
    if acum is None:
        acum = []

    if a > b:
        return acum

    acum.append(a)
    return desde_hasta_cola(a + 1, b, acum)

print("------------------------------------------------------")
a = 4
b = 10
print(f"Números desde {a} hasta {b}: {desde_hasta_cola(a, b)}")

#3)

def intercalar_pila(lista1, lista2):
    if len(lista1) == 0:
        return lista2
    if len(lista2) == 0:
        return lista1
    return [lista1[0]] + [lista2[0]] + intercalar_pila(lista1[1:], lista2[1:])

print("------------------------------------------------------")
lista1 = [1,3,5]
lista2 = [2,4,6]

print(f"Números intercalados en las dos listas: {intercalar_pila(lista1, lista2)}")

def intercalar_cola(lista1, lista2, acum=None):
    if acum is None:
        acum = []
    if len(lista1) == 0:
        acum.extend(lista2)
        return acum
    if len(lista2) == 0:
        acum.extend(lista1)
        return acum
    acum.append(lista1[0])
    acum.append(lista2[0])
    return intercalar_cola(lista1[1:], lista2[1:], acum)

lista1 = [1,3,5]
lista2 = [2,4,6]

print(f"Números intercalados en las dos listas: {intercalar_cola(lista1, lista2)}")

#4)

def longitud_recursiva(lista, count=0):
    if not lista:
        return count
    else:
        return longitud_recursiva(lista[1:], count + 1)
    
print("------------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Longitud de la lista: {longitud_recursiva(lista)}")
    
def longitud_iterativa(lista):
    count = 0
    for elem in lista:
        count += 1
    return count

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Longitud de la lista: {longitud_iterativa(lista)}")

#5)

def suma_resta_alternada(lista, acum=0, pos=0):
    if not lista:
        return acum

    if pos < 2:
        acum += lista[0]
    elif pos % 2 == 0:
        acum -= lista[0]
    else:
        acum += lista[0]

    return suma_resta_alternada(lista[1:], acum, pos + 1)

print("------------------------------------------------------")
lista = [1,2,3,4,5]
print(f"Suma y resta alternada: {suma_resta_alternada(lista)}")

def suma_resta_alternada_iterativa(lista):
    acum = 0 
    for i in range(0, len(lista)):
        if i < 2:
            acum += lista[i]
        elif i % 2 == 0:
            acum -= lista[i]
        else:
            acum += lista[i]

    return acum

lista = [1,2,3,4,5]
print(f"Suma y resta alternada: {suma_resta_alternada_iterativa(lista)}")

#6)

def suma_de_digitos(n, acum=0):
    if n < 10:
        return acum + n
    acum += n % 10
    return suma_de_digitos(n // 10, acum)

print("------------------------------------------------------")
n = 345
print(f"La suma de los dígitos de {n} es: {suma_de_digitos(n)}")
    
def suma_de_digitos_iterativa(n):
    acum=0
    for elem in str(n):
        acum += int(elem)
    return acum

n = 345
print(f"La suma de los dígitos de {n} es: {suma_de_digitos(n)}")

#7)

def invertir_cadena(cadena, acum = None):
    if acum is None:
        acum = ''
    if len(cadena) == 0:
        return acum
    acum += cadena[-1]
    return invertir_cadena(cadena[0:len(cadena)-1], acum)

print("------------------------------------------------------")
cadena = 'salvador'
print(f"Cadena invertida: {invertir_cadena(cadena)}")

def invertir_cadena_iterativo(cadena):
    nueva_cadena = ''
    for i in range(len(cadena)-1, -1, -1):
        nueva_cadena += cadena[i]
    return nueva_cadena

cadena = 'salvador'
print(f"Cadena invertida: {invertir_cadena_iterativo(cadena)}")

#8)

def fibonacci_cola(n, a=0, b=1):
    if n == 0:
        return a

    return fibonacci_cola(n - 1, b, a + b)

print("------------------------------------------------------")
n = 10   
print(f"Fibonacci de {n}: {fibonacci_cola(n)}")

#9)

def producto_cola(a, b, acum=0):
    if b == 0:
        return acum
    acum += a
    return producto_cola(a, b-1, acum)

print("------------------------------------------------------")
a = 9
b = 4
print(f"{a}*{b} es {producto_cola(a,b)}")

#10)

def resta_entre_elementos(lista, acum = 0):
    if len(lista) == 0:
        return acum
    acum -= lista[0]
    return resta_entre_elementos(lista[1:], acum)

print("------------------------------------------------------")
lista = [7,3,2,1]
print(f"La resta entre los elementos de la lista es: {resta_entre_elementos(lista)}")

def diferencia_entre_elementos(lista, acum = None):
    if acum is None:
        acum = lista[0]
        return diferencia_entre_elementos(lista[1:], acum)
    if len(lista) == 0:
        return acum
    acum -= lista[0]
    return diferencia_entre_elementos(lista[1:], acum)

lista = [7,3,2,1]
print(f"La diferencia entre los elementos de la lista es: {diferencia_entre_elementos(lista)}")
    
#11)

def potencia_cola(a, b, acum = 1):
    if b == 0:
        return acum
    acum *= a
    return potencia_cola(a, b-1, acum)

print("------------------------------------------------------")
a = 9
b = 3
print(f"{a}**{b} es {potencia_cola(a,b)}")

#12)

def maximo_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > maximo_elemento(lista[1:]):
        return lista[0]
    return maximo_elemento(lista[1:])

print("------------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9]
print(f"El máximo elemento de la lista es el {maximo_elemento(lista)}")

def maximo_elemento_iterativo(lista):
    maximo = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]

    return maximo

lista = [1,2,3,4,5,6,7,8,9]
print(f"El máximo elemento de la lista es el {maximo_elemento_iterativo(lista)}")

#13)

def suma_entre_elementos(lista, acum = 0):
    if len(lista) == 0:
        return acum
    acum += lista[0]
    return suma_entre_elementos(lista[1:], acum)

print("------------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9]
print(f"La suma entre los elementos de la lista es igual a {suma_entre_elementos(lista)}")

#14)

def conjunto_partes_recursivo(lista):
  if not lista:
    return [set()]

  primero = lista[0]
  # Llamada recursiva con el resto de los elementos
  resto_partes = conjunto_partes_recursivo(lista[1:])
  # Duplicamos los subconjuntos agregando el primer elemento a la mitad de ellos
  con_primero = [sub | {primero} for sub in resto_partes]

  return resto_partes + con_primero

print("------------------------------------------------------")
lista = [1,2,3]
print(f"El conjunto de partes de {lista} es {conjunto_partes_recursivo(lista)}")

def conjunto_partes_iterativo(lista):
  # Empezamos con una lista que solo contiene el conjunto vacío
  resultado = [set()]

  # Recorremos cada elemento de la lista original uno por uno
  for elemento in lista:
    # Creamos los nuevos subconjuntos combinando el elemento actual
    nuevos = [sub | {elemento} for sub in resultado]

    # Los añadimos al resultado acumulado
    resultado.extend(nuevos)

  return resultado


mi_lista = [1, 2, 3]
print(f"El conjunto de partes de {lista} es {conjunto_partes_iterativo(lista)}")

#15)

def conjunto_partes_cadena_recursivo(cadena):
  if len(cadena) == 0:
    return [set()]

  primero = cadena[0]
  # Llamada recursiva con el resto de los elementos
  resto_partes = conjunto_partes_cadena_recursivo(cadena[1:])
  # Duplicamos los subconjuntos agregando el primer elemento a la mitad de ellos
  con_primero = [sub | {primero} for sub in resto_partes]

  return resto_partes + con_primero

cadena = 'abc'
print(f"El conjunto de partes de {cadena} es {conjunto_partes_cadena_recursivo(cadena)}")

def conjunto_partes_cadena_iterativo(cadena):
  # Empezamos con una lista que solo contiene el conjunto vacío
  resultado = [set()]

  # Recorremos cada elemento de la lista original uno por uno
  for elemento in cadena:
    # Creamos los nuevos subconjuntos combinando el elemento actual
    nuevos = [sub | {elemento} for sub in resultado]

    # Los añadimos al resultado acumulado
    resultado.extend(nuevos)

  return resultado

cadena = 'abc'
print(f"El conjunto de partes de {cadena} es {conjunto_partes_cadena_iterativo(cadena)}")

def cuenta_reg(num):
    if num == 0:
        print("Inicio")
        return
    print(num)
    cuenta_reg(num - 1)

print("------------------------------------------------------")
num = 10
cuenta_reg(num)

def sublista(lista, pos, longitud):
    if longitud == 0:
        return []
    return [lista[pos]] + sublista(lista, pos + 1, longitud - 1)

print("------------------------------------------------------")
lista = [1,2,3,4,5]
pos = 1
longitud = 4
print(f"Sublista: {sublista(lista, pos, longitud)}")

def sublista_cola(lista, pos, longitud, acum = None):
    if acum is None:
        acum = []
    if longitud == 0:
        return acum
    acum += [lista[pos]]
    return sublista_cola(lista, pos + 1, longitud - 1, acum)

lista = [1,2,3,4,5]
pos = 1
longitud = 4
print(f"Sublista: {sublista_cola(lista, pos, longitud)}")

def esPalindromo(lista):
    if len(lista) <= 1:
        return True
    if lista[0] != lista[-1]:
        return False
    return esPalindromo(lista[1:len(lista)-1])

print("------------------------------------------------------")
lista = [1,2,3,2,1] 
print(f"¿Es palíndromo la lista {lista}?: {esPalindromo(lista)}")

def aplanar(lista):
    if len(lista) == 0:
        return []
    return lista[0] + aplanar(lista[1:])

print("------------------------------------------------------")
lista = [[5,7], [], [3,7,2], [9]]
print(f"Lista {lista} aplanada: {aplanar(lista)}")

def quicksort(lista):
  # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
  if len(lista) <= 1:
    return lista

  # Elegimos el pivote (en este caso, el elemento del medio)
  pivote = lista[len(lista) // 2]

  # Dividimos los elementos en tres grupos
  menores = [x for x in lista if x < pivote]
  iguales = [x for x in lista if x == pivote]
  mayores = [x for x in lista if x > pivote]

  # Llamada recursiva y combinación de resultados
  return quicksort(menores) + iguales + quicksort(mayores)

print("------------------------------------------------------")
# Ejemplo de uso
mi_lista = [36, 7, 23, 1, 45, 12]
lista_ordenada = quicksort(mi_lista)
print(lista_ordenada)  # Resultado: [1, 7, 12, 23, 36, 45]
    
def posiciones_pares(lista, i=0):
    if i == 0:
        print(f"Contenido de las posiciones pares de la lista {lista}:")
    if i == len(lista):
        return
    if i % 2 == 0:
        print(f"{lista[i]}")
    posiciones_pares(lista, i+1)
    
print("------------------------------------------------------")
lista = [10, 5, 2003, 17, 55, 0]
posiciones_pares(lista)

def producto_escalar_pila(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")
    if len(vector1) == 0 and len(vector2) == 0:
        return 0
    return (vector1[0] * vector2[0]) + producto_escalar_pila(vector1[1:], vector2[1:])

print("------------------------------------------------------")
vector1 = [1,3,5,7]
vector2 = [2,4,6,8]
print(f"El producto escalar entre {vector1} y {vector2} es {producto_escalar_pila(vector1, vector2)}")
    
def producto_escalar_cola(vector1, vector2, acum = 0):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")
    if len(vector1) == 0 and len(vector2) == 0:
        return acum
    acum += (vector1[0] * vector2[0])
    return producto_escalar_cola(vector1[1:], vector2[1:], acum)

print("------------------------------------------------------")
vector1 = [1,3,5,7]
vector2 = [2,4,6,8]
print(f"El producto escalar entre {vector1} y {vector2} es {producto_escalar_cola(vector1, vector2)}")

def producto_escalar_iterativo(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")
    contador = 0
    for i in range(0, len(vector1)):
        contador += (vector1[i] * vector2[i])
    return contador

print("------------------------------------------------------")
vector1 = [1,3,5,7]
vector2 = [2,4,6,8]
print(f"El producto escalar entre {vector1} y {vector2} es {producto_escalar_iterativo(vector1, vector2)}")

def busqueda_binaria(lista, objetivo, inicio, fin):
    if inicio > fin:
        return False
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1,fin)

print("------------------------------------------------------")
mi_lista = [1, 7, 12, 23, 36, 45]
objetivo = 7
inicio = 0
fin = 5
lista_ordenada = busqueda_binaria(mi_lista, objetivo, inicio, fin)
print(f"¿El elemento {objetivo} está en la lista? {lista_ordenada}")

def busqueda_binaria_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] > objetivo:
            fin = medio - 1
        else:
            inicio = medio + 1
    return False
    
print("------------------------------------------------------")
mi_lista = [1, 7, 12, 23, 36, 45]
objetivo = 12
lista_ordenada = busqueda_binaria_iterativa(mi_lista, objetivo)
print(f"¿El elemento {objetivo} está en la lista? {lista_ordenada}")

def contar_hacia_atras_par(n):
    if n == 0:
        return
    print(n)
    contar_hacia_atras_impar(n-1)
    
def contar_hacia_atras_impar(n):
    if n == 0:
        return
    print(n)
    contar_hacia_atras_par(n-1)
    
print("------------------------------------------------------")
n = 4
contar_hacia_atras_par(n)

def conjunto_partes_recursivo(lista):
  if not lista:
    return [list()]

  primero = lista[0]
  # Llamada recursiva con el resto de los elementos
  resto_partes = conjunto_partes_recursivo(lista[1:])
  # Duplicamos los subconjuntos agregando el primer elemento a la mitad de ellos
  con_primero = [sub + [primero] for sub in resto_partes]

  return resto_partes + con_primero

print("------------------------------------------------------")
lista = [1,2,3]
print(f"El conjunto de partes de {lista} es {conjunto_partes_recursivo(lista)}")

def combinar_con_uno(x, lista):
    if not lista:
        return []

    return [(x, lista[0])] + combinar_con_uno(x, lista[1:])

def todos_con_todos(lista1, lista2):
    if not lista1:
        return []

    return combinar_con_uno(lista1[0], lista2) + todos_con_todos(lista1[1:], lista2)

print("------------------------------------------------------")
lista1 = [1,2,3]
lista2 = [4,5,6]
print(f"Combinaciones de {lista1} y {lista2}: {todos_con_todos(lista1, lista2)}")

def penultimo_elemento(lista):
    if len(lista) == 2:
        return lista[0]
    return penultimo_elemento(lista[1:])
    
print("------------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9,10]
print(f"El penultimo elemento de la lista {lista} es {penultimo_elemento(lista)}")

def primeros(lista, n):
    if n > len(lista):
        raise ValueError(f"La lista no tiene {n} elementos")
    if len(lista) == 0 or n == 0:
        return []
    return [lista[0]] + primeros(lista[1:], n-1)
    
print("------------------------------------------------------")
lista = [1,2,3,4,5,6,7,8,9,10]
n = 4
print(f"Los {n} primeros números de la lista {lista} son {primeros(lista, n)}")