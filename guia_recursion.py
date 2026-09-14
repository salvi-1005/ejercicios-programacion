#1)

def sumatoria(n: int) -> int:
    if n == 0:
        return 0
    return n + sumatoria(n-1)

print(sumatoria(10))

#2)

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(7))
    
#3)

def fibonacciRecursivo(n: int) -> int:
  if n == 0:
      return 0
  if n == 1:
      return 1
  return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

n = 4
resultado = fibonacciRecursivo(n)
print(f"El {n}-ésimo término de la sucesión de Fibonacci es {resultado}")

#4)

def producto(z: int, v: int) -> int:
  if z == 0 or v == 0:
      return 0
  if v < 0:
        return -producto(z, -v)
  return z + producto(z, v - 1)

z = 2
v = 4
resultado = producto(z,v)
print(f"{z} * {v} es {resultado}")

#5)

def potencia(x: int, y: int) -> float:
  if x == 0 and y != 0:
      return 0
  if y == 0:
      return 1
  if y < 0:
      return 1/potencia(x, -y)
  return x * potencia(x, y - 1)

x = 2
y = 4
resultado = potencia(x,y)
print(f"{x} ^ {y} es {resultado}")

#6)

def cociente(dividendo: int, divisor: int) -> int:
    if dividendo < divisor:
        return 0
    return 1 + cociente(dividendo - divisor, divisor)

dividendo = 7
divisor = 2
resultado = cociente(dividendo, divisor)
print(f"{dividendo} / {divisor} es {resultado}")

def resto(dividendo: int, divisor: int) -> int:
    if dividendo < divisor:
        return dividendo
    return resto(dividendo - divisor, divisor)

dividendo = 7
divisor = 2
resultado = resto(dividendo, divisor)
print(f"el resto de {dividendo} / {divisor} es {resultado}")

#7)
#a)

def decimalBinario(n):
    if n < 2:
        return str(n)
    else:
        return decimalBinario(n // 2) + str(n % 2)
    
n = 11
print(f"El {n} en binarios es {decimalBinario(n)}")

#b)

def cambioBaseDecimal(n, b):
    if n < b:
        return str(n)
    else:
        return cambioBaseDecimal(n // b, b) + str(n % b)
    
n = 11
b = 3
print(f"{n} en base {b} es {cambioBaseDecimal(n, b)}")

#c)

def unosBinario(b):
    if b % 10 != 0 and b % 10 != 1:
        raise ValueError("El número debe estar en formato binario")
    if b == 0:
        return 0
    if b == 1:
        return 1
    if b % 10 == 0:
        return unosBinario(b // 10)
    if b % 10 == 1:
        return 1 + unosBinario(b // 10) 
    
b = 100101
print(f"La cantidad de unos de {b} es {unosBinario(b)}")

#d)

def binarioDecimal(b):
    if b < 10:
        return b
    return int(str(b)[0]) * (2**(len(str(b))-1)) + binarioDecimal(int(str(b)[1:]))

b = 1011
print(f"El {b} en decimal es {binarioDecimal(b)}")

#8)

def mcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return mcd(b, resto(a, b))

a = 7
b = 2
resultado = mcd(a, b)
print(f"el mcd entre {dividendo} y {divisor} es {resultado}")
    
#9)
#a)

def buscar_factores(numero: int, div: int) -> None:
        if numero <= 1:
            return
        if numero % div == 0:
            print(div)
            buscar_factores(numero // div, div)
        else:
            buscar_factores(numero, div + 1)
    
            
def factores_a(n: int) -> None:
    buscar_factores(n, 2)


print("Factores de 20 (con repetición):")
factores_a(20) # Imprime: 2, 2, 5
    
#b)

def buscar_factores_unicos(numero: int, div: int) -> None:
        if numero <= 1:
            return
        if numero % div == 0:
            print(div)
            # Para no repetir, dividimos TODO lo que se pueda por este divisor
            while numero % div == 0:
                numero //= div
            buscar_factores_unicos(numero, div + 1)
        else:
            buscar_factores_unicos(numero, div + 1)
            
def factores_b(n: int) -> None:
    buscar_factores_unicos(n, 2)

# Prueba para el número 20
print("\nFactores de 20 (sin repetición):")
factores_b(20) # Imprime: 2, 5

#10)

def calcular_combinatorio(n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
    
def combinatorio(n, k):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return combinatorio(n - 1, k - 1) + combinatorio(n - 1, k)

n = 4
k = 2
print(f"combinatorio en base a {n} y {k}:")
print(combinatorio(n,k))

#11)
#a)

def cantDigitos(n):
    if n < 10 and n > -10:
        return 1
    return 1 + cantDigitos(n//10)

n = 400
print(f"cantidad de digitos de {n}:")
print(cantDigitos(n))

#b)

def reversaNum(n):
    if n < 10:
        return n
    resto = n // 10
    return (n % 10) * (10 ** cantDigitos(resto)) + reversaNum(resto)

n = 48556
print(f"la reversa de {n} es:")
print(reversaNum(n))

#c)

def sumaDigitos(n):
    if n < 10:
        return n
    return n % 10 + sumaDigitos(n // 10)

n = 123456789
print(f"la suma de los dígitos de {n} es:")
print(sumaDigitos(n))

#d)

def reversaNumSumaDigitos(n):
    if n < 10:
        return (n, n)
    return ((n % 10) * (10 ** cantDigitos(n // 10)) + reversaNum(n // 10), n % 10 + sumaDigitos(n // 10))

n = 123456789
print(f"la reversa y la suma de los dígitos de {n} respectivamente son:")
print(reversaNumSumaDigitos(n))

def doble(n):
    num_s = str(n)
    if len(num_s) == 0:
        return 0, ''
    suma, reverso = doble(num_s[1:])
    print(reverso, suma)
    return int(num_s[0]) + suma, reverso + num_s[0]

n = 543
print(f"Reversa y suma de dígitos de {n}: {doble(n)}")

#12)

from functools import lru_cache as cache

@cache
def Ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ackermann(m - 1, 1)
    if m != 0 and n != 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))

m = 2
n = 3
print(f"Ackermann entre {m} y {n} es:")
print(Ackermann(m, n))

#13)

def raizCuadrada(A):
    if A == 1:
        return 1
    return (1/2)*(raizCuadrada(A-1) + (A/raizCuadrada(A-1)))

A = 16
print(f"La raíz cuadrada de {A} es:")
print(raizCuadrada(A))

#14)

def taylor(x, tol, n=0):
    termino = ((-1) ** n) * (x ** (2*n + 1)) / factorial(2*n + 1)

    if abs(termino) < tol:
        return 0

    return termino + taylor(x, tol, n + 1)

x = 4
tol = 3
print(f"El polinomio de taylor de {x} y {tol} es:")
print(taylor(x, tol))

#15)

def pares(n, i=1):
    if i > n - i:
        return

    print(f"({i}, {n - i})")
    pares(n, i + 1)

# Ejemplo
pares(5)

#16)
#a)

def desdeHasta(a, b):
    if a > b:
        return []
    return [a] + desdeHasta(a + 1, b)
    
a = 4
b = 12
print(f"Números desde {a} hasta {b}:")
print(desdeHasta(a,b))

#b)

def sumatoriaDesdeHasta(n: int) -> int:
    lista = desdeHasta(0, n)
    if n == 0:
        return 0
    return n + sumatoria(lista[n-1])

print(sumatoria(10))

def factorialDesdeHasta(n: int) -> int:
    lista = desdeHasta(0, n)
    if n <= 1:
        return 1
    return n * factorial(lista[n-1])

print(factorial(7))

#25)
#TAD Lista de enteros

class ListaEnt:
    def __init__(self, cabeza=None, cola=None):
        self.cabeza = cabeza
        self.cola = cola
    def es_vacia(self):
        return self.cabeza is None
    @staticmethod
    def agregar(lista, valor):
        return ListaEnt(valor, lista)
    def eliminar(self, valor):
        if self.es_vacia():
            return self
        if self.cabeza == valor:
            return self.cola
        return ListaEnt(self.cabeza, self.cola.eliminar(valor))
    def tamaño(self):
        if self.es_vacia():
            return 0
        return 1 + self.cola.tamaño()
    def obtener(self, indice):
        if self.es_vacia():
            raise IndexError("Índice fuera de rango")

        if indice == 0:
            return self.cabeza

        return self.cola.obtener(indice - 1)
    def __str__(self):
        if self.es_vacia():
            return ""

        if self.cola.es_vacia():
            return str(self.cabeza)

        return f"{self.cabeza} -> {self.cola}"
    

# Crear la lista
lista = ListaEnt()

lista = ListaEnt.agregar(lista, 30)
lista = ListaEnt.agregar(lista, 20)
lista = ListaEnt.agregar(lista, 10)

print("Lista inicial:", lista)  # Salida: 10, 20, 30
print("Tamaño:", lista.tamaño())  # Salida: 3

# Obtener un elemento por índice
print("Elemento en índice 1:", lista.obtener(1))  # Salida: 20

# Eliminar un elemento
lista_eliminada = lista.eliminar(20)
print("Lista tras eliminar el 20:", lista_eliminada)  # Salida: 10, 30

#26)
#a)
#TAD Lista enlazada

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
    
# Crear la lista
mi_lista = TADListaEnlazada()

# Agregar elementos
mi_lista.agregar(10)
mi_lista.agregar(20)
mi_lista.agregar(30)

print("Lista inicial:", mi_lista)  # Salida: 10 -> 20 -> 30
print("Tamaño:", mi_lista.tamaño())  # Salida: 3

# Obtener un elemento por índice
print("Elemento en índice 1:", mi_lista.obtener(1))  # Salida: 20

# Eliminar un elemento
mi_lista.eliminar(20)
print("Lista tras eliminar el 20:", mi_lista)  # Salida: 10 -> 30

#b)
#TAD Lista doblemente enlazada

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class TADListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamaño = 0
    def es_vacia(self):
        return self.cabeza is None
    def agregar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.es_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self._tamaño += 1
    def agregar_al_principio(self, dato):
        """Añade un elemento al inicio de la lista (Eficiencia O(1))."""
        nuevo_nodo = NodoDoble(dato)
        
        if self.es_vacia():
            # Si está vacía, el nuevo nodo es tanto la cabeza como la cola
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            # El nuevo nodo apunta al que antes era el primero
            nuevo_nodo.siguiente = self.cabeza
            # El antiguo primer nodo ahora tiene al nuevo nodo por detrás
            self.cabeza.anterior = nuevo_nodo
            # La cabeza de la lista pasa a ser el nuevo nodo
            self.cabeza = nuevo_nodo
            
        self._tamaño += 1
    def insertar_en_posicion(self, indice, dato):
        """Inserta un dato en cualquier posición válida de la lista."""
        # Validar el rango del índice
        if indice < 0 or indice > self._tamaño:
            raise IndexError("Índice fuera de rango")
        
        # Caso 1: Insertar al principio
        if indice == 0:
            self.agregar_al_principio(dato)
            return

        # Caso 2: Insertar al final
        if indice == self._tamaño:
            self.agregar_al_final(dato)
            return

        # Caso 3: Insertar en el medio
        nuevo_nodo = NodoDoble(dato)
        
        # Optimización: buscar desde cabeza o cola según cercanía
        if indice < self._tamaño / 2:
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self._tamaño - indice):
                actual = actual.anterior

        # Reenlazar los punteros (nos metemos entre 'actual.anterior' y 'actual')
        nuevo_nodo.siguiente = actual
        nuevo_nodo.anterior = actual.anterior
        
        actual.anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self._tamaño += 1

    def tamaño(self):
        return self._tamaño
    def eliminar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                # Caso 1: Es el único nodo o es la cabeza
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                    else:
                        self.cola = None  # La lista quedó vacía
                # Caso 2: Es el último nodo (la cola)
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                # Caso 3: Es un nodo intermedio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                self._tamaño -= 1
                return True  # Eliminado con éxito
            actual = actual.siguiente
        return False  # No se encontró el dato
    def obtener(self, indice):
        """Devuelve el valor en la posición indicada de manera eficiente."""
        if indice < 0 or indice >= self._tamaño:
            raise IndexError("Índice fuera de rango")
        
        # Optimización: si el índice está en la segunda mitad, empezamos desde la cola
        if indice < self._tamaño / 2:
            # Buscar desde el inicio (cabeza) hacia adelante
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
        else:
            # Buscar desde el final (cola) hacia atrás
            actual = self.cola
            for _ in range(self._tamaño - 1 - indice):
                actual = actual.anterior
                
        return actual.dato
    def mostrar_adelante(self):
        """Recorre la lista desde la cabeza hasta la cola."""
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

    def mostrar_atras(self):
        """Recorre la lista al revés, desde la cola hasta la cabeza."""
        elementos = []
        actual = self.cola
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        return " <-> ".join(elementos)
    
# Crear la lista

lista = TADListaDoblementeEnlazada()

# Insertamos al principio
lista.agregar_al_principio(10)
lista.agregar_al_principio(5)

print("Luego de agregar al principio:", lista.mostrar_adelante())
# Salida: 5 <-> 10 <-> 20 <-> 30
print("Nuevo tamaño:", lista.tamaño())

# Insertamos al final
lista.agregar_al_final(10)
lista.agregar_al_final(30)
print("Inicial:", lista.mostrar_adelante())  # 10 <-> 30

# Insertar el 20 en la posición 1 (en el medio)
lista.insertar_en_posicion(1, 20)
print("Intermedio:", lista.mostrar_adelante())  # 10 <-> 20 <-> 30

# Insertar al principio usando este mismo método
lista.insertar_en_posicion(0, 5)
print("Al principio:", lista.mostrar_adelante())  # 5 <-> 10 <-> 20 <-> 30

#c)
#Arreglo unidimensional estático

import numpy as np

class A:
    def __init__(self, dato):
        self.dato = dato
    def __str__(self):
        return (f"{self.dato}")
    def __repr__(self):
        return (f"{self.dato}")
    def __eq__(self, otro):
        return isinstance(otro, A) and self.dato == otro.dato

class TADArreglo:
    def __init__(self, tamaño):
        self.array = np.empty(tamaño, dtype=object)
        self._tamaño = tamaño
    def agregar(self, dato, indice):
        nuevo_elemento = A(dato)
        self.array[indice] = nuevo_elemento
    def tamaño(self):
        return (f"El tamaño es {self._tamaño}")
    def eliminar(self, dato):
        nuevo_elemento = A(dato)
        if nuevo_elemento not in self.array:
            raise ValueError("El elemento {dato} no está en la lista")
        for i in range(0, self._tamaño):
            if self.array[i] == nuevo_elemento:
                self.array[i] = None
                return
    def obtener(self, indice):
        return self.array[indice]
    def __str__(self):
        """Muestra los elementos de la lista en formato visual."""
        elementos = []
        i = 0
        while i < self._tamaño:
            elementos.append(str(self.array[i]))
            i += 1
        return ", ".join(elementos)
    
# Crear la lista
mi_arreglo = TADArreglo(10)

# Agregar elementos
mi_arreglo.agregar(10,1)
mi_arreglo.agregar(20,4)
mi_arreglo.agregar(30,7)

print("Lista inicial:", mi_arreglo)  
print("Tamaño:", mi_arreglo.tamaño())  

# Obtener un elemento por índice
print("Elemento en índice 1:", mi_arreglo.obtener(1))  

# Eliminar un elemento
mi_arreglo.eliminar(20)
print("Lista tras eliminar el 20:", mi_arreglo) 

#27)

def longitud(lista):
    if not lista:
        return 0
    return 1 + longitud(lista[1:])

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Cantidad de elementos de la lista {lista}: {longitud(lista)}")

#28)

def igualdad_de_listas(lista1, lista2):
    if not lista1 and not lista2:
        return True
    if lista1[0] != lista2[0] or len(lista1) != len(lista2):
        return False
    return igualdad_de_listas(lista1[1:], lista2[1:])

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
print(f"¿Son iguales las listas {lista1} y {lista2}? {igualdad_de_listas(lista1, lista2)}")

#29)

def sumatoriaLista(lista):
    if not lista:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sumatoriaLista(lista[1:])
    
lista = [1,2,3,4,5,6,7,8,9,10]
print(f"La sumatoria de los elementos de la lista {lista} es {sumatoriaLista(lista)}")

#30)

def pertenece(lista, n):
    if not lista:
        return False
    if lista[0] == n:
        return True
    return pertenece(lista[1:], n)

lista = [1,2,3,4,5,6,7,8,9,10]
n = 10
print(f"¿El elemento {n} pertenece a la lista {lista}? {pertenece(lista, n)}")

#31)

def concatenacion(lista1, lista2):
    if not lista1:
        return lista2
    return [lista1[0]] + concatenacion(lista1[1:], lista2) 

lista1 = [1,2,3]
lista2 = [4,5,6,7,8,9]

print(f"Concatenacion de {lista1} y {lista2}: {concatenacion(lista1, lista2)}")

#32)

def ultimo(lista):
    if len(lista) == 1:
        return lista[0]
    return ultimo(lista[1:])

lista = [1,2,3,4,5]
print(f"El último elemento de la lista {lista} es {ultimo(lista)}")

#33)

def penultimo(lista):
    if len(lista) == 2:
        return lista[0]
    return penultimo(lista[1:])

lista = [1,2,3,4,5]
print(f"El penúltimo elemento de la lista {lista} es {penultimo(lista)}")

#34)

def primeros(lista, n):
    if len(lista) < n:
        raise ValueError(f"La lista no tiene {n} elementos")
    if n == 0:
        return []
    return [lista[0]] + primeros(lista[1:], n-1)

lista = [1,2,3,4,5,6]
n = 3
print(f"Los primeros {n} números de la lista {lista} son {primeros(lista, n)}")

#35)

def posicion(lista, n):
    if n >= len(lista):
        raise IndexError("Índice fuera de rango")
    if n == 0:
        return lista[n]
    return posicion(lista[1:], n-1)

lista = [0,1,2,3,4,5,6]
n = 3
print(f"El elemento que está en la posición {n} de la lista{lista} es {posicion(lista, n)}")

#36)

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > maximo(lista[1:]):
        return lista[0]
    return maximo(lista[1:])

lista = [6,3,7,5,4,1]
print(f"El máximo elemento de la lista {lista} es {maximo(lista)}")

#37)

def reversa(lista):
    if not lista:
        return []
    if len(lista) == 1:
        return [lista[0]]
    return [lista[-1]] + reversa(lista[0:-1])

lista = [1,2,3,4,5]
print(f"La reversa de la lista {lista} es {reversa(lista)}")

#38)
#a)

def es_palindromo(lista):
    if not lista or len(lista) == 1:
        return True
    if lista[0] != lista[-1]:
        return False
    return es_palindromo(lista[1:-1])

lista = [1,2,3,3,2,1]
print(f"¿Es palíndromo la lista {lista}? {es_palindromo(lista)}")

#b)

def es_palindromo_b(lista):
    return lista == reversa(lista)

lista = [1,2,3,3,2,1]
print(f"¿Es palíndromo la lista {lista}? {es_palindromo_b(lista)}")

#39)

def cantidad(lista, n):
    if not lista:
        return 0
    if lista[0] == n:
        return 1 + cantidad(lista[1:], n)
    return cantidad(lista[1:], n)

lista = [1,2,2,3,3,3]
n = 3
print(f"El elemento {n} aparece {cantidad(lista, n)} veces en la lista {lista}")

#40)

def sublista(lista, pos, long):
    if long + pos > len(lista):
        raise ValueError("La lista no tiene suficiente longitud")
    if long == 0:
        return []
    return [lista[pos]] + sublista(lista, pos+1, long-1)

lista = [1,2,3,4,5,6]
pos = 1
long = 5
print(f"La sublista de {lista} que arranca en el índice {pos} y tiene longitud {long} es {sublista(lista, pos, long)}")

#41)

def intercalar(lista1, lista2):
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    return [lista1[0]] + [lista2[0]] + intercalar(lista1[1:], lista2[1:])

lista1 = [1,3,5]
lista2 = [2,4,6]
print(f"Intercalación de {lista1} y {lista2}: {intercalar(lista1, lista2)}")

#42)

def aplanar(lista):
    if not lista:
        return []
    if len(lista) == 1:
        return lista[0]
    return lista[0] + aplanar(lista[1:])

lista = [[5,7], [], [3,7,2], [9]]
print(f"Lista {lista} aplanada: {aplanar(lista)}")

#43)

def longitudLL(lista):
    lista_aplanada = aplanar(lista)
    if not lista_aplanada:
        return 0
    return 1 + longitudLL([lista_aplanada[1:]])

lista = [[5,7], [], [3,7,2], [9]]
print(f"La longitud total de la lista {lista} es: {longitudLL(lista)}")

#44)

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

# Ejemplo de uso
mi_lista = [36, 7, 23, 1, 45, 12]
lista_ordenada = quicksort(mi_lista)
print(lista_ordenada)  # Resultado: [1, 7, 12, 23, 36, 45]

#45)

def partes(lista):
  if not lista:
    return [list()]
  primero = lista[0]
  resto_partes = partes(lista[1:])
  con_primero = [sub + [primero] for sub in resto_partes]
  return resto_partes + con_primero

lista = [1,2,3]
print(f"El conjunto de partes de {lista} es {partes(lista)}")

# Auxiliar recursiva: toma un elemento y lo inserta al principio de cada sublista
def agregar_elemento_rec(elemento, lista_de_listas):
    # Caso base: si ya procesamos todas las sublistas, devolvemos una lista vacía
    if not lista_de_listas:
        return []
    
    # Toma la primera sublista, le concatena el elemento, y procesa recursivamente el resto
    primera_con_elemento = [elemento] + lista_de_listas[0]
    return [primera_con_elemento] + agregar_elemento_rec(elemento, lista_de_listas[1:])

# Función Principal de Partes
def partes_pura(lista):
    # Caso base: las partes de una lista vacía es una lista que contiene a la lista vacía [[]]
    if not lista:
        return [[]]
    
    primero = lista[0]
    resto_partes = partes_pura(lista[1:])
    
    # En lugar de usar un for, llamamos a la auxiliar recursiva
    con_primero = agregar_elemento_rec(primero, resto_partes)
    
    # Concatenamos de forma pura ambos bloques de resultados
    return resto_partes + con_primero

# Prueba de ejecución
print("Partes puras de [1, 2, 3]:")
print(partes_pura([1, 2, 3]))
# Salida: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]


#46)

def permutaciones(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    for i in range(len(lista)):
        primero = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([primero] + p)
    return resultado

lista = [6,2,3]
print(f"Las permutaciones de {lista} son {permutaciones(lista)}")

# Auxiliar 1: Pega un elemento al inicio de cada una de las permutaciones generadas
def pegar_adelante_rec(elemento, permutaciones_del_resto):
    if not permutaciones_del_resto:
        return []
    return [[elemento] + permutaciones_del_resto[0]] + pegar_adelante_rec(elemento, permutaciones_del_resto[1:])

# Auxiliar 2: Simula el ciclo 'for' que recorre las posiciones (i) de la lista
def iterar_elementos_rec(lista, i=0):
    # Caso base del bucle ficticio: si el índice llega al final de la lista
    if i >= len(lista):
        return []
    
    # Extraemos el elemento en la posición 'i' sin usar ciclos
    fijo = lista[i]
    resto = lista[:i] + lista[i+1:]
    
    # 1. Permutamos recursivamente el resto
    perms_del_resto = permutaciones_pura(resto)
    # 2. Le pegamos el elemento fijo adelante a todas esas permutaciones obtenidas
    combinadas = pegar_adelante_rec(fijo, perms_del_resto)
    
    # 3. Avanzamos a la siguiente posición (i + 1) simulando el paso del bucle
    return combinadas + iterar_elementos_rec(lista, i + 1)

# Función Principal de Permutaciones
def permutaciones_pura(lista):
    # Caso base: si tiene 0 o 1 elemento, su única permutación es ella misma
    if len(lista) <= 1:
        return [lista]
    
    # Delegamos todo el recorrido e inserciones a la función recursiva de control de índices
    return iterar_elementos_rec(lista)

# Prueba de ejecución
print("\nPermutaciones puras de [1, 2, 3]:")
print(permutaciones_pura([2, 2, 3]))
# Salida: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def permutaciones_iterativas(lista):
    actual = sorted(lista)
    resultado = [list(actual)]
    while True:
        i = -1
        for k in range(len(actual) - 2, -1, -1):
            if actual[k] < actual[k + 1]:
                i = k
                break
        if i == -1:
            break
        j = -1
        for k in range(len(actual) - 1, i, -1):
            if actual[i] < actual[k]:
                j = k
                break
        actual[i], actual[j] = actual[j], actual[i]
        actual[i + 1:] = reversed(actual[i + 1:])
        resultado.append(list(actual))
    return resultado

lista = [1, 2, 3]
print(f"Las permutaciones de {lista} son: {permutaciones_iterativas(lista)}")

def permutaciones_sin_repetidos(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    usados = set()
    for i in range(len(lista)):
        if lista[i] in usados:
            continue
        usados.add(lista[i])
        primero = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones_sin_repetidos(resto):
            resultado.append([primero] + p)
    return resultado

lista = [2, 2, 3]
print(f"Las permutaciones de {lista} son: {permutaciones_sin_repetidos(lista)}")

#47)

def combinar_con_uno(x, lista):
    if not lista:
        return []
    return [(x, lista[0])] + combinar_con_uno(x, lista[1:])

def todos_con_todos(lista1, lista2):
    if not lista1:
        return []

    return combinar_con_uno(lista1[0], lista2) + todos_con_todos(lista1[1:], lista2)

lista1 = [1,2,3]
lista2 = [4,5,6]
print(f"Combinaciones de {lista1} y {lista2}: {todos_con_todos(lista1, lista2)}")

#48)

def todosConTodosN(listas):
    # Caso base: si no hay listas, devolvemos una lista con una sublista vacía
    if not listas:
        return [[]]
    
    # Tomamos la primera lista y resolvemos el problema para el resto de las listas
    primera_lista = listas[0]
    combinaciones_resto = todosConTodosN(listas[1:])
    
    # Combinamos cada elemento de la primera lista con los resultados del resto
    resultado = []
    for elemento in primera_lista:
        for comb in combinaciones_resto:
            resultado.append([elemento] + comb)
            
    return resultado


lista = [[6,2,3],[7,5],[9,4]]
print(f"Combinaciones de {lista}: {todosConTodosN(lista)}")

#49)

class Lista:
    def __init__(self, cabeza=None, cola=None):
        self.cabeza = cabeza
        self.cola = cola
    def es_vacia(self):
        return self.cabeza is None
    @staticmethod
    def agregar(lista, valor):
        return Lista(valor, lista)
    def eliminar(self, valor):
        if self.es_vacia():
            return self
        if self.cabeza == valor:
            return self.cola
        return Lista(self.cabeza, self.cola.eliminar(valor))
    def tamaño(self):
        if self.es_vacia():
            return 0
        return 1 + self.cola.tamaño()
    def obtener(self, indice):
        if self.es_vacia():
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            return self.cabeza
        return self.cola.obtener(indice - 1)
    def convertir_a_lista(self):
        if self.es_vacia():
            return []
        return [self.cabeza] + self.cola.convertir_a_lista()
    def __str__(self):
        if self.es_vacia():
            return ""
        if self.cola.es_vacia():
            return str(self.cabeza)
        return f"{self.cabeza}, {self.cola}" 
    

# Crear la lista
lista = Lista()

lista = Lista.agregar(lista, 'hola')
lista = Lista.agregar(lista, 20)
lista = Lista.agregar(lista, ['a','b','c'])

print("Lista inicial:", lista)  # Salida: 10, 20, 30
print("Tamaño:", lista.tamaño())  # Salida: 3

# Obtener un elemento por índice
print("Elemento en índice 1:", lista.obtener(1))  # Salida: 20

# Eliminar un elemento
lista_eliminada = lista.eliminar(20)
print("Lista tras eliminar el 20:", lista_eliminada)  # Salida: 10, 30

#50)

class Nat:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("No valen números negativos")
        self.a = a
        self.b = b
    @staticmethod
    def suma(a, b):
        if b == 0:
            return a
        return 1 + Nat.suma(a, b - 1)
    @staticmethod
    def producto (a, b):
        if b == 0:
            return 0
        return a + Nat.producto(a, b - 1)
    
a = 4
b = 6
natural = Nat(a,b)
print(f"suma: {natural.suma(a,b)}")
print(f"producto: {natural.producto(a,b)}")

#51)

class NatLista:
    def __init__(self, n):
        self.lista = [1] * n
    @staticmethod
    def suma(lista1, lista2):
        if not lista2:
            return len(lista1)
        return NatLista.suma(lista1 + [1],lista2[1:])
    @staticmethod
    def producto(lista1, lista2):
        if not lista2:
            return 0

        return len(lista1) + NatLista.producto(lista1, lista2[1:])
   
a = NatLista(4)
b = NatLista(6)
print(f"suma: {a.suma(a.lista, b.lista)}")
print(f"producto: {a.producto(a.lista, b.lista)}")

#52)

class Conjunto:
    def __init__(self):
        self.lista = Lista()
    def agregar(self, elemento):
        if self.pertenece(elemento):
            raise ValueError("Elemento repetido")
        self.lista = Lista.agregar(self.lista, elemento)
    def eliminar(self, elemento):
        if not self.pertenece(elemento):
            raise ValueError("No pertenece al conjunto")
        self.lista = self.lista.eliminar(elemento)
    def pertenece(self, elemento):
        if self.lista.es_vacia():
            return False
        if self.lista.cabeza == elemento:
            return True
        return Conjunto._pertenece_rec(self.lista.cola, elemento)
    @staticmethod
    def _pertenece_rec(lista, elemento):
        if lista.es_vacia():
            return False
        if lista.cabeza == elemento:
            return True
        return Conjunto._pertenece_rec(lista.cola, elemento)
    def convertir_a_lista(self):
        return self.lista.convertir_a_lista()
    def __str__(self):
        return "{" + str(self.lista) + "}"

conjunto = Conjunto()

conjunto.agregar(33)
conjunto.agregar(58)
conjunto.agregar(95)

print(conjunto)
print(conjunto.pertenece(58))

conjunto.eliminar(58)

print(conjunto)
print(conjunto.pertenece(58))

print(conjunto.convertir_a_lista())

#53)

def mostrar_elementos(lista):
    if lista.es_vacia():
        return
    print(lista.cabeza)
    mostrar_elementos(lista.cola)

lista = Lista()

lista = Lista.agregar(lista, 'hola')
lista = Lista.agregar(lista, 4)
lista = Lista.agregar(lista, 'robot')
lista = Lista.agregar(lista, 55)

print("Elementos de la lista:")
mostrar_elementos(lista)

#54)

def posiciones_pares(lista, i=0):
    if i >= len(lista):
        return
    print(lista[i])
    return posiciones_pares(lista, i+2)

lista = [0,1,2,3,4,5,6]
posiciones_pares(lista)

#55)

def producto_escalar(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Los tamaños de las listas deben ser iguales")
    if not lista1 and not lista2:
        return 0
    return (lista1[0] * lista2[0]) + producto_escalar(lista1[1:], lista2[1:])

lista1 = [1,2,3,4]
lista2= [5,6,7,8]
print(f"El producto escalar entre {lista1} y {lista2} es {producto_escalar(lista1, lista2)}")

#56)

def busqueda_binaria_recursiva(lista, objetivo, inicio = 0, fin = len(lista)-1):
    if inicio > fin:
        return False
        
    medio = (inicio + fin) // 2
    
    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)

mi_lista = [1, 7, 12, 23, 36, 45]
objetivo = 12
lista_ordenada = busqueda_binaria_recursiva(mi_lista, objetivo)
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
    
mi_lista = [1, 7, 12, 23, 36, 45]
objetivo = 13
lista_ordenada = busqueda_binaria_iterativa(mi_lista, objetivo)
print(f"¿El elemento {objetivo} está en la lista? {lista_ordenada}")

#57)

def mostrarElementos(lista, nueva_lista = None):
    if nueva_lista is None:
        nueva_lista = []
    if not lista:
        return nueva_lista
    nueva_lista.append(lista[0])  
    return mostrarElementos(lista[1:], nueva_lista)
    
    
def mostrarElementosTriangular(lista):
    if not lista:
        return 
    print(mostrarElementos(lista))  
    return mostrarElementosTriangular(lista[1:])

lista = [1,2,3,4,5,6,7]
mostrarElementosTriangular(lista)

def mostrarElementosTriangularInvertido(lista, nivel=0):
    if not lista:
        return

    print("   " * nivel, mostrarElementos(lista))

    mostrarElementosTriangularInvertido(lista[1:], nivel + 1)
    
mostrarElementosTriangularInvertido(lista)

#58)

#a)

class MatrizCuadradaLista:
    def __init__(self, n, valor=0):
        self.n = n
        self.filas = TADListaEnlazada()
        for _ in range(n):
            fila = TADListaEnlazada()
            for _ in range(n):
                fila.agregar(valor)
            self.filas.agregar(fila)
    def obtener(self, fila, columna):
        fila_lista = self.filas.obtener(fila)
        return fila_lista.obtener(columna)
    def modificar(self, fila, columna, valor):
        fila_lista = self.filas.obtener(fila)
        actual = fila_lista.cabeza
        for _ in range(columna):
            actual = actual.siguiente
        actual.dato = valor
    def __str__(self):
        resultado = ""
        fila_actual = self.filas.cabeza
        while fila_actual:
            columna_actual = fila_actual.dato.cabeza
            while columna_actual:
               resultado += str(columna_actual.dato) + "\t"
               columna_actual = columna_actual.siguiente
            resultado += "\n"
            fila_actual = fila_actual.siguiente
        return resultado
    
m = MatrizCuadradaLista(3)

m.modificar(0, 0, 7)
m.modificar(1, 1, 4)
m.modificar(2, 2, 9)

print(m)

print(m.obtener(1,1))

#b)

class MatrizCuadradaArreglo:
    def __init__(self, dimension, valor_inicial=0):
        """Inicializa la matriz cuadrada de forma recursiva"""
        if dimension <= 0:
            raise ValueError("La dimensión debe ser un entero positivo.")
        self.n = dimension
        self.datos = self._crear_matriz_rec(dimension, dimension, valor_inicial)

    def _crear_fila_rec(self, columnas, valor):
        """Caso base: genera una fila de ceros/valores recursivamente"""
        if columnas == 0:
            return []
        return [valor] + self._crear_fila_rec(columnas - 1, valor)

    def _crear_matriz_rec(self, filas, columnas, valor):
        """Caso base: junta las filas recursivamente para armar la matriz"""
        if filas == 0:
            return []
        fila = self._crear_fila_rec(columnas, valor)
        return [fila] + self._crear_matriz_rec(filas - 1, columnas, valor)

    def obtener(self, fila, columna):
        self._validar_indices(fila, columna)
        return self.datos[fila][columna]

    def modificar(self, fila, columna, valor):
        self._validar_indices(fila, columna)
        self.datos[fila][columna] = valor

    def es_diagonal(self):
        """Determina si es diagonal iniciando la recursión en (0, 0)"""
        return self._es_diagonal_rec(0, 0)

    def _es_diagonal_rec(self, f, c):
        # Caso base 1: Si procesamos todas las filas, es diagonal
        if f == self.n:
            return True
        # Caso base 2: Si terminamos una fila, pasamos a la siguiente fila (columna 0)
        if c == self.n:
            return self._es_diagonal_rec(f + 1, 0)
        # Caso base 3: Si no está en la diagonal principal y no es cero, se rompe
        if f != c and self.datos[f][c] != 0:
            return False
        # Paso recursivo: Evalúa la siguiente columna
        return self._es_diagonal_rec(f, c + 1)

    def _validar_indices(self, fila, columna):
        if not (0 <= fila < self.n) or not (0 <= columna < self.n):
            raise IndexError("Índices fuera de rango.")

    def __str__(self):
        """Representación en texto armada de forma recursiva"""
        return self._str_rec(0)

    def _str_rec(self, f):
        if f == self.n:
            return ""
        fila_texto = "\t".join(map(str, self.datos[f]))
        salto = "\n" if f < self.n - 1 else ""
        return fila_texto + salto + self._str_rec(f + 1)

# 1. Crear matriz de 3x3 recursivamente
matriz_rec = MatrizCuadradaArreglo(3, valor_inicial=0)

# 2. Modificar elementos (así simulamos una matriz diagonal)
matriz_rec.modificar(0, 0, 7)
matriz_rec.modificar(1, 1, 4)
matriz_rec.modificar(2, 2, 9)

# 3. Mostrar usando el método __str__ recursivo
print("Matriz generada:")
print(matriz_rec)

# 4. Verificar propiedad diagonal mediante recursión
print("\n¿Es una matriz diagonal?:", matriz_rec.es_diagonal())

# 5. Si rompemos la diagonalidad:
matriz_rec.modificar(0, 1, 3)
print("¿Sigue siendo diagonal tras modificar (0,1)?:", matriz_rec.es_diagonal())

#59)

def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] < minimo(lista[1:]):
        return lista[0]
    return minimo(lista[1:])

lista = [6,3,7,5,4,1]
print(f"El minimo elemento de la lista {lista} es {minimo(lista)}")

def minimoCuadrado(matriz):
    if len(matriz) == 1:
        return minimo(matriz[0])
    if minimo(matriz[0]) < minimoCuadrado(matriz[1:]):
        return minimo(matriz[0])
    return minimoCuadrado(matriz[1:])

matriz = [[6,3,7],[5,4,1],[9,2,8]]
print(f"El minimo elemento de la matriz {matriz} es {minimoCuadrado(matriz)}")

#60)

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > maximo(lista[1:]):
        return lista[0]
    return maximo(lista[1:])

lista = [6,3,7,5,4,1]
print(f"El máximo elemento de la lista {lista} es {maximo(lista)}")

def maximosCuadrado(matriz):
    if len(matriz) == 1:
        return [maximo(matriz[0])]
    return [maximo(matriz[0])] + maximosCuadrado(matriz[1:])

matriz = [[6,3,7],[5,4,1],[9,2,8]]
print(f"Los máximos elementos de cada fila de la matriz {matriz} es {maximosCuadrado(matriz)}")

#61)

def diagonalPrincipal(matriz, i=0):
    if i >= len(matriz):
        return []
    return [matriz[i][i]] + diagonalPrincipal(matriz, i+1)
    
    
matriz = [[6,3,7],
          [5,4,1],
          [9,2,8]]
print(f"La diagonal principal de la matriz {matriz} está compuesta por {diagonalPrincipal(matriz)}")

#62)

def matriz_transpuesta(matriz, j=0):
    if j >= len(matriz[0]):
        return []
    columna = []
    for i in range(len(matriz)):
        columna.append(matriz[i][j])
    return [columna] + matriz_transpuesta(matriz, j+1)
    
matriz = [[6,3,7],
          [5,4,1],
          [9,2,8]]
print(matriz_transpuesta(matriz))

# Auxiliar: Extrae una columna específica 'j' de la matriz
def obtener_columna_rec(matriz, j, i=0):
    if i >= len(matriz):
        return []
    return [matriz[i][j]] + obtener_columna_rec(matriz, j, i + 1)

# Función Principal: Transpone la matriz recorriendo las columnas 'j'
def matriz_transpuesta_pura(matriz, j=0):
    # Caso base: si ya procesamos todas las columnas
    if j >= len(matriz[0]):
        return []
    
    # Paso recursivo: armamos la columna j y pasamos a la j+1
    return [obtener_columna_rec(matriz, j)] + matriz_transpuesta_pura(matriz, j + 1)

# Prueba
matriz = [[6, 3, 7], [5, 4, 1], [9, 2, 8] ]
print(matriz_transpuesta_pura(matriz))
# Salida: [[6, 5, 9], [3, 4, 2], [7, 1, 8]]


def esSimetrica(matriz, i=0):
    matriz_transp = matriz_transpuesta(matriz)
    if matriz[0][i:] != matriz_transp[i]:
        return False
    if not matriz or i >= len(matriz):
        return True
    return esSimetrica(matriz[1:], i+1)

matriz = [[6,5,9],
          [5,4,1],
          [9,1,8]]
print(f"Es simétrica la matriz {matriz}? {esSimetrica(matriz)}")

def esSimetrica2(matriz, transp=None, i=0):
    if transp is None:
        transp = matriz_transpuesta(matriz)
    if i >= len(matriz):
        return True
    if matriz[i] != transp[i]:
        return False
    return esSimetrica2(matriz, transp, i+1)

matriz = [[6,5,9],
          [5,4,1],
          [9,1,8]]
print(f"Es simétrica la matriz {matriz}? {esSimetrica2(matriz)}")

#63)

def triangularInferior(matriz, matriz_triangular = None, filas = None, i=1):
    if matriz_triangular is None:    
        matriz_triangular = []
    if filas is None:
        filas = []
    if i >= len(matriz):
        return matriz_triangular
    for j in range(len(matriz[i])):
        fila = [matriz[i][j] for j in range(len(matriz[i])) if i > j]
    matriz_triangular.append(fila)
    return triangularInferior(matriz, matriz_triangular, filas, i+1) 

matriz = [[6,5,9,4,1],
          [5,4,1,8,3],
          [9,1,8,5,2],
          [6,3,1,7,4],
          [0,2,6,9,5]]

print(f"La matriz triangular inferior de {matriz} es {triangularInferior(matriz)}")
     
# Auxiliar: Construye una fila cortando los elementos hasta que j < i
def filtrar_fila_rec(fila_matriz, i, j=0):
    if j >= len(fila_matriz) or j >= i:
        return []
    return [fila_matriz[j]] + filtrar_fila_rec(fila_matriz, i, j + 1)

# Función Principal: Recorre las filas de la matriz
def triangular_inferior_pura(matriz, i=1):
    if i >= len(matriz):
        return []
    
    # Procesamos la fila actual de forma recursiva
    fila_filtrada = filtrar_fila_rec(matriz[i], i)
    
    # Avanzamos a la siguiente fila
    return [fila_filtrada] + triangular_inferior_pura(matriz, i + 1)

# Prueba
matriz = [[6, 5, 9],
          [5, 4, 1],
          [9, 1, 8]]
print(triangular_inferior_pura(matriz))
# Salida: [[5], [9, 1]]


#64)
    
def ElementosDiagonal(matriz, i=0):
    if i >= len(matriz):
        return []
    return [matriz[i][i]] + ElementosDiagonal(matriz, i+1)

def cantidadApariciones(lista, n):
    if not lista:
        return 0
    if lista[0] == n:
        return 1 + cantidadApariciones(lista[1:], n)
    return cantidadApariciones(lista[1:], n)

def cantidadElementoDiagonal(matriz, elementos_diagonal=None, matriz_transp=None, 
                             i=0):
    if elementos_diagonal is None:
        elementos_diagonal = ElementosDiagonal(matriz)
    if matriz_transp is None:
        matriz_transp = matriz_transpuesta(matriz)
    if i >= len(elementos_diagonal):
        return []
    return [cantidadApariciones(matriz_transp[i], elementos_diagonal[i])] + \
        cantidadElementoDiagonal(matriz, elementos_diagonal, matriz_transp , i+1)
  
matriz = [['A','B','H','P'],
          ['A','I','J','P'],
          ['K','I','H','L'],
          ['A','N','H','O']]  
print(f"Lista de cantidad de apariciones de cada elemento de la diagonal por columna:{cantidadElementoDiagonal(matriz)}")

#65)

def moneda_falsa(monedas):

    if len(monedas) == 1:
        return monedas[0]

    medio = len(monedas) // 2

    izquierda = monedas[:medio]
    derecha = monedas[medio:2*medio]
    sobrante = monedas[2*medio:]
    
    if sum(izquierda) < sum(derecha):
        return moneda_falsa(izquierda)

    if sum(derecha) < sum(izquierda):
        return moneda_falsa(derecha)

    return moneda_falsa(sobrante)

monedas = [30] + [40]*29
print(f"La moneda falsa es la {moneda_falsa(monedas)}")
        
#66)

def moneda_falsa_mejorado(monedas):

    if len(monedas) == 1:
        return monedas[0]

    if len(monedas) == 2:
        return min(monedas)

    if len(monedas) == 3:
        return min(monedas)
    tercio = len(monedas) // 3

    primero = monedas[:tercio]
    segundo = monedas[tercio:2*tercio]
    tercero = monedas[2*tercio:3*tercio]
    sobrante = monedas[3*tercio:]
    
    if sum(primero) < sum(segundo):
        return moneda_falsa_mejorado(primero)
    if sum(segundo) < sum(primero):
        return moneda_falsa_mejorado(segundo)
    if sum(segundo) < sum(tercero):
        return moneda_falsa_mejorado(segundo)
    if sum(tercero) < sum(segundo):
        return moneda_falsa_mejorado(tercero)
    if sum(primero) < sum(tercero):
        return moneda_falsa_mejorado(primero)
    if sum(tercero) < sum(primero):
        return moneda_falsa_mejorado(tercero)

    return moneda_falsa_mejorado(sobrante)

monedas = [40]*15 + [30] + [40]*14
print(f"La moneda falsa es la {moneda_falsa(monedas)}")

#67)

def hanoi(n, origen=None, auxiliar=None, destino=None):
    if origen is None:
        origen = [i for i in range(n, 0, -1)] #Discos apilados con el más grande en la base y el más chico en el tope
    if auxiliar is None:
        auxiliar = []
    if destino is None:
        destino = []
    if not origen and not auxiliar: #Si origen y auxiliar están vacías, ya pasé todo a destino y terminé
        return origen, auxiliar, destino
    if not destino and len(origen) > 0: #Si no hay nada en destino y todavía hay discos en origen, paso todo a auxiliar
        auxiliar.append(origen.pop(len(origen)-1))
    if not origen and len(auxiliar) > 0: #Si origen está vacía y auxiliar todavía tiene discos, paso los discos a destino
        destino.append(auxiliar.pop(len(auxiliar)-1))
    return hanoi(n, origen, auxiliar, destino)

n = 4
print(f"Torre de Hanoi con {n} discos: {hanoi(n)}")

def hanoi2(n, origen, auxiliar, destino):
    if n == 1:
        print(f"({origen} - {destino})")
        return
    hanoi2(n - 1, origen, destino, auxiliar)
    print(f"({origen} - {destino})")
    hanoi2(n - 1, auxiliar, origen, destino)
    
n = 4
origen = "A"
auxiliar = "B"
destino = "C"
hanoi2(n, origen, auxiliar, destino)

def movimientos_hanoi(n: int) -> int:
    if n == 1:
        return 1
    else:
        return (2 * movimientos_hanoi(n - 1)) + 1
    
n = 4
print(f"movimientos de hanoi: {movimientos_hanoi(n)}")

#68)

import random

def es_salida(pos, llegada):
    return pos == llegada

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
    
def hay_paso(posicion, coordenadas_validas):
    return posicion in coordenadas_validas

from typing import List, Tuple

Posicion = Tuple[int, int]
def laberinto(camino_previo: List[Posicion], coordenadas_validas, llegada) -> (bool, List[Posicion]):
    posicion_actual = camino_previo[-1]
    if es_salida(posicion_actual, llegada):
        return True, camino_previo
    else:
        salida_encontrada = False
        solucion = camino_previo
        direcciones = ['N', 'S', 'O', 'E']
        random.shuffle(direcciones)
        while direcciones and not salida_encontrada:
            nueva_posicion = avanzar(posicion_actual, direcciones.pop())
            if hay_paso(nueva_posicion, coordenadas_validas) and nueva_posicion not in camino_previo:
                camino_actual = camino_previo.copy()
                camino_actual.append(nueva_posicion)
                salida_encontrada, solucion = laberinto(camino_actual, coordenadas_validas, llegada)
        return salida_encontrada, solucion
    
coordenadas_validas = [(0,0),(0,1),(0,2),(1,2),(2,2)]
salida = (0,0)
llegada = (2,2)
print(laberinto([salida], coordenadas_validas, llegada))

#69)

def es_posicion_valida(coordenada1, coordenada2):
    if coordenada1[0] == coordenada2[0]:
        return False
    if coordenada1[1] == coordenada2[1]:
        return False
    if abs(coordenada1[0] - coordenada2[0]) == abs(coordenada1[1] - coordenada2[1]):
        return False
    return True

def es_segura(nueva, reinas):
    for reina in reinas:
        if not es_posicion_valida(nueva, reina):
            return False
    return True

def es_solucion_valida(reinas):
    for i in range(len(reinas)):
        for j in range(i + 1, len(reinas)):
            if not es_posicion_valida(reinas[i], reinas[j]):
                return False
    return True

Posicion = Tuple[int, int]

def ocho_reinas(reinas):
    if len(reinas) == 8:
        return es_solucion_valida(reinas), reinas
    fila = len(reinas)
    for columna in range(8):
        nueva = (fila, columna)
        if es_segura(nueva, reinas):
            encontrado, solucion = ocho_reinas(reinas + [nueva])
            if encontrado:
                return True, solucion
    return False, []
    
reinas = []
print(ocho_reinas(reinas))

#70)

#Sí, pueden evitarse los punteros explícitos utilizando referencias 
#administradas por el lenguaje (como en Python o Java) o representaciones 
#basadas en índices sobre arreglos. Sin embargo, toda estructura recursiva 
#necesita algún mecanismo para referenciar otros elementos de la misma 
#estructura, por lo que conceptualmente siempre existe algún tipo de enlace 
#entre los nodos.

#71)

def sumatoria_cola(n, acum=0):
    if n == 0:
        return acum
    acum += n
    return sumatoria_cola(n-1, acum)
    
n = 10
print(sumatoria_cola(n))

def factorial_cola(n, acum=1):
    if n == 0:
        return acum
    acum *= n
    return factorial_cola(n-1, acum)
    
n = 5
print(factorial_cola(n))

def producto_cola(m, n, acum=0):
    if m == 0:
        return acum
    acum += n
    return producto_cola(m-1, n, acum)

m = 4
n = 9
print(producto_cola(4, 9))
    
def pares_pila(n, i=1):
    if i > n - i:
        return
    pares_pila(n, i + 1)
    print(f"({i}, {n - i})")

pares_pila(5)

def desde_hasta_cola(desde, hasta, acum=None):
    if acum is None:
        acum = []
    if desde > hasta:
        return acum
    acum.append(desde)
    return desde_hasta_cola(desde + 1, hasta, acum)

desde = 4
hasta = 10
print(desde_hasta_cola(desde, hasta))

def pertenece_cola(lista, elem, i=0):
    if i >= len(lista):
        return False
    if lista[i] == elem:
        return True
    return pertenece_cola(lista, elem, i+1)

lista = [2,4,6,8,10]
elem = 4
print(pertenece_cola(lista, elem))

def concatenacion_cola(lista1, lista2, acum=None):
    if acum is None:
        acum = []
    if not lista1:
        return acum + lista2
    acum.append(lista1[0])
    return concatenacion_cola(lista1[1:], lista2, acum)

lista1 = [1,2,3,4]
lista2 = [5,6,7]
print(concatenacion_cola(lista1, lista2))

def reversa_cola(lista, acum=None):
    if acum is None:
        acum = []
    if not lista:
        return acum
    acum.append(lista[-1])
    return reversa_cola(lista[:len(lista)-1], acum)

lista = [1,2,3,4,5,6,7,8,9,10]
print(reversa_cola(lista))

def intercalar_cola(lista1, lista2, acum=None):
    if acum is None:
        acum = []
    if not lista1:
        return acum + lista2
    if not lista2:
        return acum + lista1
    acum.append(lista1[0])
    acum.append(lista2[0])
    return intercalar_cola(lista1[1:], lista2[1:], acum)

lista1 = [1,3,5,7]
lista2 = [2,4,6]
print(intercalar_cola(lista1, lista2))

def todosConUno_cola(lista, n, acum=None):
    if acum is None:
        acum = []
    if not lista:
        return acum
    acum.append((n,lista[0]))
    return todosConUno_cola(lista[1:], n, acum)

def todosConTodos_cola(lista1, lista2, acum=None):
    if acum is None:
        acum = []
    if not lista1:
        return acum
    acum.append(todosConUno_cola(lista2, lista1[0]))
    return todosConTodos_cola(lista1[1:], lista2, acum)

lista1 = [1,2,3]
lista2 = [4,5,6]
print(todosConTodos_cola(lista1, lista2))
    
#a)

def sumatoria_iterativo(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma
    
n = 10
print(sumatoria_iterativo(n))

def factorial_iterativo(n):
    producto = 1
    for i in range(1, n+1):
        producto *= i
    return producto
    
n = 5
print(factorial_iterativo(n))

def producto_iterativo(m, n):
    producto = 0
    for i in range(m):
        producto += n
    return producto

m = 4
n = 9
print(producto_iterativo(m, n))
    
def pares_iterativo(n):
    i = 1
    while i <= n - i:
        print(f"({i}, {n - i})")
        i += 1
    return

pares_iterativo(5)

def desde_hasta_iterativo(desde, hasta):
    lista = []
    i = desde
    while i <= hasta: 
        lista.append(i)
        i += 1
    return lista

desde = 4
hasta = 10
print(desde_hasta_iterativo(desde, hasta))

def pertenece_iterativo(lista, elem):
    for elemento in lista:
        if elemento == elem:
            return True
    return False

lista = [2,4,6,8,10]
elem = 4
print(pertenece_iterativo(lista, elem))

def concatenacion_iterativo(lista1, lista2):
    concatenacion = []
    for i in range(len(lista1)):
        concatenacion.append(lista1[i])
    for i in range(len(lista2)):
        concatenacion.append(lista2[i])
    return concatenacion

lista1 = [1,2,3,4]
lista2 = [5,6,7]
print(concatenacion_iterativo(lista1, lista2))

def reversa_iterativo(lista):
    reversa = []
    for i in range(len(lista)-1,-1,-1):
        reversa.append(lista[i])
    return reversa

lista = [1,2,3,4,5,6,7,8,9,10]
print(reversa_iterativo(lista))

def intercalar_iterativo(lista1, lista2):
    intercalacion = []
    if len(lista1) < len(lista2):
        for i in range(len(lista1)):
            intercalacion.append(lista1[i])
            intercalacion.append(lista2[i])
        intercalacion += lista2[len(lista1):len(lista2)]
    if len(lista1) > len(lista2):
        for i in range(len(lista2)):
            intercalacion.append(lista1[i])
            intercalacion.append(lista2[i])
        intercalacion += lista1[len(lista2):len(lista1)]
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            intercalacion.append(lista1[i])
            intercalacion.append(lista2[i])
    return intercalacion
            
lista1 = [1,3,5,7]
lista2 = [2,4,6]
print(intercalar_iterativo(lista1, lista2))

def todosConUno_iterativo(lista, n):
    acumulado = []
    for i in range(len(lista)):
        acumulado.append((lista[i], n))
    return acumulado

def todosConTodos_iterativo(lista1, lista2):
    acumulado = []
    for i in range(len(lista1)):
        acumulado.append(todosConUno_iterativo(lista2, lista1[i]))
    return acumulado

lista1 = [1,2,3]
lista2 = [4,5,6]
print(todosConTodos_iterativo(lista1, lista2))

#b)

class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0
    
class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, x):
        self.items.append(x)
    def desapilar(self):
        if self.esta_vacia():
            raise ValueError('La pila esta vacia')
        return self.items.pop(-1)
    def esta_vacia(self):
        return len(self.items) == 0
    def tamaño(self):
        return len(self.items)

def sumatoria_pila(n):
    pila = Pila()
    for i in range(n+1):
        pila.apilar(i)
    resultado = 0
    while not pila.esta_vacia():
        resultado += pila.desapilar()
    return resultado

n = 10
print(f"La sumatoria de {n} es {sumatoria_pila(n)}")

def factorial_pila(n):
    pila = Pila()
    for i in range(1,n+1):
        pila.apilar(i)
    resultado = 1
    while not pila.esta_vacia():
        resultado *= pila.desapilar()
    return resultado

n = 5
print(f"El factorial de {n} es {factorial_pila(n)}")

def producto_pila(m, n):
    pila = Pila()
    for i in range(n):
        pila.apilar(m)
    resultado = 0
    while not pila.esta_vacia():
        resultado += pila.desapilar()
    return resultado

m = 4
n = 9
print(f"El producto entre {m} y {n} es {producto_pila(m, n)}")

def pares_pila(n):
    pila = Pila()
    i = 1
    while i <= n - i:
        pila.apilar((i, n - i))
        i += 1
    resultado = []
    while not pila.esta_vacia():
        resultado += [(pila.desapilar())]
    return resultado

n = 5
print(f"Los pares que suman {n} son {pares_pila(n)}")

def desde_hasta_pila(desde, hasta):
    pila = Pila()
    i = hasta
    while i >= desde: 
        pila.apilar(i)
        i -= 1
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado

desde = 4
hasta = 10
print(f"Lista de números desde {desde} hasta {hasta}: {desde_hasta_pila(desde, hasta)}")

def pertenece_pila(lista, elem):
    pila = Pila()
    for i in range(len(lista)):
        pila.apilar(lista[i])
    while not pila.esta_vacia():
        if pila.desapilar() == elem:
            return True
    return False
    
        
lista = [2,4,6,8,10]
elem = 4
print(f"{elem} pertenece a la lista {lista}? {pertenece_pila(lista, elem)}")

def concatenacion_pila(lista1, lista2):
    pila = Pila()
    for i in range(len(lista2)-1,-1,-1):
        pila.apilar(lista2[i])
    for i in range(len(lista1)-1,-1,-1):
        pila.apilar(lista1[i])
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado

lista1 = [1,2,3,4]
lista2 = [5,6,7]
print(f"Concatenacion entre {lista1} y {lista2}: {concatenacion_pila(lista1, lista2)}")

def reversa_pila(lista):
    pila = Pila()
    for i in range(len(lista)):
        pila.apilar(lista[i])
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Reversa de la lista {lista}: {reversa_pila(lista)}")

def intercalar_pila(lista1, lista2):
    pila = Pila()
    if len(lista1) < len(lista2):
        for i in range(len(lista2)-1,len(lista1)-1,-1):
            pila.apilar(lista2[i])
        for i in range(len(lista1)-1,-1,-1):
            pila.apilar(lista2[i])
            pila.apilar(lista1[i])
    if len(lista1) > len(lista2):
        for i in range(len(lista1)-1,len(lista2)-1,-1):
            pila.apilar(lista1[i])
        for i in range(len(lista2)-1,-1,-1):
            pila.apilar(lista2[i])
            pila.apilar(lista1[i])
    if len(lista1) == len(lista2):
        for i in range(len(lista1)-1,-1,-1):
            pila.apilar(lista2[i])
            pila.apilar(lista1[i])
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado
            
lista1 = [1,3,5,7]
lista2 = [2,4,6]
print(f"Intercalación entre {lista1} y {lista2}: {intercalar_pila(lista1, lista2)}")

def todosConUno(lista, n):
    acumulado = []
    for i in range(len(lista)):
        acumulado.append((lista[i], n))
    return acumulado

def todosConTodos_pila(lista1, lista2):
    pila = Pila()
    for i in range(len(lista1)):
        pila.apilar(todosConUno(lista2, lista1[i]))
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado

lista1 = [1,2,3]
lista2 = [4,5,6]
print(f"Combinación de todos con todos entre {lista1} y {lista2}: {todosConTodos_pila(lista1, lista2)}")

#72)

def mcd_recursivo(a: int, b: int) -> int:
    if b == 0:
        return a
    return mcd_recursivo(b, a % b)

def mcd_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 8
b = 4
resultado = mcd_iterativo(a, b)
print(f"el mcd entre {a} y {b} es {resultado}")

#73)

def suma_alternada_pila(lista):
    if not lista:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0] - lista[1] + suma_alternada_pila(lista[2:])

lista = [1,2,3,4,5]
print(f"suma alternada de {lista}: {suma_alternada_pila(lista)}")

def suma_alternada_cola(lista, acum=0):
    if not lista:
        return acum
    if len(lista) == 1:
        return acum + lista[0]
    acum += lista[0]
    acum -= lista[1]
    return suma_alternada_cola(lista[2:], acum)

lista = [1,2,3,4,5]
print(f"suma alternada de {lista}: {suma_alternada_cola(lista)}")

#74)

def fibonacci_pila(n):
  lista = []
  for i in range(2):
      lista.append(i)
  for i in range(2, n+1):
      lista.append(lista[i-1] + lista[i-2])
  pila = Pila()
  for i in range(len(lista)):
      pila.apilar(lista[i])
  resultado = pila.desapilar()
  return resultado

n = 9
resultado = fibonacci_pila(n)
print(f"El {n}-ésimo término de la sucesión de Fibonacci es {resultado}")

def combinatorio_pila(n, k):
    pila = Pila()
    pila.apilar(factorial(n)//(factorial(k)*factorial(n-k)))
    resultado = pila.desapilar()
    return resultado

n = 4
k = 2
print(f"combinatorio en base a {n} y {k}:")
print(combinatorio_pila(n,k))

def ackermann_pila(m, n):
    pila = Pila()
    pila.apilar(m)
    while not pila.esta_vacia():
        m = pila.desapilar()
        if m == 0:
            n += 1
        elif n == 0:
            pila.apilar(m - 1)
            n = 1
        else:
            pila.apilar(m - 1)
            pila.apilar(m)
            n -= 1
    return n

m = 2
n = 2
print(f"Ackermann entre {m} y {n}: {ackermann_pila(m,n)}")

def partes_pila(cadena):
    pila = Pila()
    partes = [list()]
    for elemento in cadena:
        nuevos = [sub + [elemento] for sub in partes]
        partes.extend(nuevos)
    for i in range(len(partes)):
        pila.apilar(partes[i])
    resultado = []
    while not pila.esta_vacia():
        resultado += [pila.desapilar()]
    return resultado

lista = ['A','B','C','D','E']
print(partes_pila(lista))

def hanoi_pila(n):
    pila = Pila()
    pila.apilar((n, 'A', 'B', 'C'))
    while not pila.esta_vacia():
        n, origen, auxiliar, destino = pila.desapilar()
        if n == 1:
            print(f"({origen}-{destino})")
        else:
            pila.apilar((n-1, auxiliar, origen, destino))
            pila.apilar((1, origen, auxiliar, destino))
            pila.apilar((n-1, origen, destino, auxiliar))
            
n = 4
hanoi_pila(n)

def sierpinski_pila(n):
    pila = Pila()
    while n >= 0:
        pila.apilar(n)
        n -= 1
    resultado = ["*"]
    pila.desapilar()  # elimina el 0 porque ya tenemos el caso base
    while not pila.esta_vacia():
        pila.desapilar()
        ancho = len(resultado[-1])
        arriba = [" " * ((ancho + 1) // 2) + fila + " " * ((ancho + 1) // 2) for fila in resultado]
        abajo = [fila + " " + fila for fila in resultado]
        resultado = arriba + abajo
    return resultado
            
for linea in sierpinski_pila(4):
    print(linea)