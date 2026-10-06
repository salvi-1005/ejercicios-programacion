class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.ultimo = None
    def add(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def add_rec(self, nodo, nuevo):
        if nodo.sig is None:
            nodo.sig = nuevo
            self.ultimo = nuevo
            return
        self.add_rec(nodo.sig, nuevo)
    def add_recursivo(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.add_rec(self.head, nuevo)
    def insert(self, dato):
        nuevo = Nodo(dato)
        nuevo.sig = self.head
        self.head = nuevo
        if self.ultimo is None:
            self.ultimo = nuevo
    def insert_rec(self, nodo, nuevo):
        if nodo is None:
            self.head = nuevo
            if self.ultimo is None:
                self.ultimo = nuevo
            return
        nuevo.sig = nodo
        self.head = nuevo
    def insert_recursivo(self, dato):
        nuevo = Nodo(dato)
        self.insert_rec(self.head, nuevo)
    def rpop(self, nodo):
        if nodo.sig.sig == None:
            nodo.sig = None
            return
        else:
            return self.rpop(nodo.sig)
    def pop_recursivo(self):
        if self.head is None:
            return None
        if self.head.sig is None:
            self.head = None
        return self.rpop(self.head.sig)
    def pop(self):
        if self.head is None:
            return None
        if self.head.sig is None:
            dato = self.head.dato
            self.head = None
            self.ultimo = None
            return dato
        actual = self.head
        while actual.sig.sig is not None:
            actual = actual.sig
        dato = actual.sig.dato
        actual.sig = None
        self.ultimo = actual
        return dato
    def pop2(self):
        if self.head is None:
            return None
        def _pop(node):
            if node.sig is None:
                return None
            node.sig = _pop(node.sig)
            return node
        self.head = _pop(self.head)
    def busqueda(self, dato):
        return self._rbusqueda(self.head, dato)
    def _rbusqueda(self, nodo, dato):
        if nodo is None:
            raise ValueError("No existe dato buscado")
        if nodo.dato == dato:
            return 0
        return 1 + self._rbusqueda(nodo.sig, dato)
    def trunc_despues_rec(self, nodo, dato):
        if nodo is None:
            raise ValueError("Dato no encontrado")
        if nodo.dato == dato:
            nodo.sig = None
            self.ultimo = nodo
            return
        self.trunc_despues_rec(nodo.sig, dato)
    def trunc_despues(self, dato):
        self.trunc_despues_rec(self.head, dato)
    def trunc_antes_rec(self, nodo, dato):
        if nodo is None:
            raise ValueError("Dato no encontrado")
        if nodo.dato == dato:
            return nodo
        return self.trunc_antes_rec(nodo.sig, dato)
    def trunc_antes(self, dato):
        self.head = self.trunc_antes_rec(self.head, dato)
    def exchange_rec(self, nodo, dato1, dato2, nodo1=None, nodo2=None):
        if nodo is None:
            if nodo1 is None or nodo2 is None:
                raise ValueError("Dato no encontrado")
            nodo1.dato, nodo2.dato = (nodo2.dato, nodo1.dato)
            return
        if nodo.dato == dato1:
            nodo1 = nodo
        if nodo.dato == dato2:
            nodo2 = nodo
        self.exchange_rec(nodo.sig, dato1, dato2, nodo1, nodo2)
    def exchange_recursivo(self, dato1, dato2):
        self.exchange_rec(self.head, dato1, dato2)
    def exchange_iterativo(self, dato1, dato2):
        nodo1 = None
        nodo2 = None
        actual = self.head
        while actual is not None:
            if actual.dato == dato1:
                nodo1 = actual
            if actual.dato == dato2:
                nodo2 = actual
            actual = actual.sig
        if nodo1 is None or nodo2 is None:
            raise ValueError("Dato no encontrado")
        nodo1.dato, nodo2.dato = nodo2.dato, nodo1.dato
    def length_iterativo(self):
        cantidad = 0
        actual = self.head
        while actual is not None:
            cantidad += 1
            actual = actual.sig
        return cantidad
    def len_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.len_rec(nodo.sig)
    def length_recursivo(self):
        return self.len_rec(self.head)
    def buscar_rec(self, nodo, dato_b, indice=0):
        if nodo is None:
            return -1
        if nodo.dato == dato_b:
            return indice
        return self.buscar_rec(nodo.sig, dato_b, indice+1)
    def buscar_recursivo(self, dato_b):
        return self.buscar_rec(self.head, dato_b)
    def minimo_lista(self, lista):
        if len(lista) == 1:
            return lista[0]
        minimo_resto = self.minimo_lista(lista[1:])
        if lista[0] < minimo_resto:
            return lista[0]
        return minimo_resto
    def eliminar_primera(self, lista, valor):
        if not lista:
            return []
        if lista[0] == valor:
            return lista[1:]
        return [lista[0]] + self.eliminar_primera(lista[1:], valor)
    def selection_sort_rec(self, lista):
        if len(lista) <= 1:
            return lista
        minimo = self.minimo_lista(lista)
        resto = self.eliminar_primera(lista,minimo)
        return [minimo] + self.selection_sort_rec(resto)
    def a_lista_rec(self, nodo):
        if nodo is None:
            return []
        return [nodo.dato] + self.a_lista_rec(nodo.sig)
    def vaciar_rec(self):
        self.head = None
        self.ultimo = None
    def sort_recursivo(self):
        elementos = self.a_lista_rec(self.head)
        elementos = self.selection_sort_rec(elementos)
        self.head = None
        self.ultimo = None
        def insertar_rec(i):
            if i >= len(elementos):
                return
            self.add(elementos[i])
            insertar_rec(i + 1)
        insertar_rec(0)
    def sort_iterativo(self):
        """
        Bubble sort simple sobre la lista enlazada.
        """
        if self.head is None:
            return
        cambiado = True
        while cambiado:
            cambiado = False
        actual = self.head
        while actual.sig is not None:
            if actual.dato > actual.sig.dato:
                actual.dato, actual.sig.dato = (actual.sig.dato,actual.dato,)
                cambiado = True
            actual = actual.sig
    def busqueda_binaria_rec(self, elementos, dato_b, inicio, fin):
        if inicio > fin:
            return -1
        medio = (inicio + fin) // 2
        if elementos[medio] == dato_b:
            return medio
        if elementos[medio] < dato_b:
            return self.busqueda_binaria_rec(elementos, dato_b, medio + 1, fin)
        if elementos[medio] > dato_b:
            return self.busqueda_binaria_rec(elementos, dato_b, inicio, medio - 1)  
    def busqueda_binaria_recursiva(self, dato_b):
        """
        Solo tiene sentido si la lista está ordenada.
        Convierte a vector para simplificar.
        """
        def lista_a_python(nodo):
            if nodo is None:
                return []
            return [nodo.dato] + lista_a_python(nodo.sig)
        elementos = lista_a_python(self.head)
        return self.busqueda_binaria_rec(elementos, dato_b, 0, len(elementos)-1)
    def __str__(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.sig
        return "[" + "] -> [".join(elementos) + "]"
    def busqueda_binaria(self, dato):
        """
        Solo tiene sentido si la lista está ordenada.
        Convierte a vector para simplificar.
        """
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.sig
        inicio = 0
        fin = len(elementos) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if elementos[medio] == dato:
                return medio
            if elementos[medio] < dato:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1
    def igualdad(self, otro):
        return self._igualdad(self.head, otro.head)
    def _igualdad(self, nodo1, nodo2):
        if nodo1 is None and nodo2 is None:
            return True
        if nodo1 is None or nodo2 is None:
            return False
        if nodo1.dato != nodo2.dato:
            return False
        return self._igualdad(nodo1.sig, nodo2.sig)
    def sumatoria_lista(self):
        return self._sumatoria_lista(self.head)
    def _sumatoria_lista(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return nodo_actual.dato + self._sumatoria_lista(nodo_actual.sig)
    def pertenece(self, elemento):
        return self._pertenece(self.head, elemento)
    def _pertenece(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.dato == elemento:
            return True
        return self._pertenece(nodo_actual.sig, elemento)
    def concatenar(self, otro):
        nueva = LinkedList()
        self._concatenar(nodo1 = self.head, nodo2 = otro.head, resultado = nueva)
        return nueva
    def _concatenar(self, nodo1, nodo2, resultado):
        if nodo1 is None and nodo2 is None:
            return
        if nodo1 is None:
            resultado.add(nodo2.dato)
            return self._concatenar(nodo1, nodo2.sig, resultado)
        if nodo2 is None:
            resultado.add(nodo1.dato)
            return self._concatenar(nodo1.sig, nodo2,resultado)
        resultado.add(nodo1.dato)
        return self._concatenar(nodo1.sig, nodo2,resultado)
    def ultimo_elemento(self):
        return self._ultimo_elemento(self.head)
    def _ultimo_elemento(self, nodo_actual):
        if nodo_actual.sig is None:
            return nodo_actual.dato
        return self._ultimo_elemento(nodo_actual.sig)
    def penultimo_elemento(self):
        return self._penultimo_elemento(self.head)
    def _penultimo_elemento(self, nodo_actual):
        if nodo_actual.sig.sig is None:
            return nodo_actual.dato
        return self._penultimo_elemento(nodo_actual.sig)
    def primeros(self, n):
        return self._primeros(self.head, n)
    def _primeros(self, nodo_actual, n, i=0):
        if i >= n or nodo_actual is None:
            return []
        return [nodo_actual.dato] + self._primeros(nodo_actual.sig, n, i+1)
    def posicion(self, n):
        return self._posicion(self.head, n)
    def _posicion(self, nodo_actual, n, i=0):
        if nodo_actual is None:
            return None
        if i == n:
            return nodo_actual.dato
        return self._primeros(nodo_actual.sig, n, i+1)
    def minimo(self):
        return self._minimo(self.head)
    def _minimo(self, nodo_actual):
        if nodo_actual.sig is None:
            return nodo_actual.dato
        minimo_resto = self._minimo(nodo_actual.sig)
        if nodo_actual.dato < minimo_resto:
            return nodo_actual.dato
        return minimo_resto
    def maximo(self):
        return self._maximo(self.head)
    def _maximo(self, nodo_actual):
        if nodo_actual.sig is None:
            return nodo_actual.dato
        maximo_resto = self._maximo(nodo_actual.sig)
        if nodo_actual.dato > maximo_resto:
            return nodo_actual.dato
        return maximo_resto
    def reversa(self):
        nueva = LinkedList()
        self._reversa(self.head, nueva)
        return nueva
    def _reversa(self, nodo_actual, nueva):
        if nodo_actual is None:
            return 
        self._reversa(nodo_actual.sig, nueva)
        nueva.add(nodo_actual.dato)
    def es_palindromo(self):
        copia_reversa = self.reversa()
        return self.igualdad(copia_reversa)
    def cantidad(self, elemento):
        return self._cantidad(self.head, elemento)
    def _cantidad(self, nodo_actual, elemento):
        if nodo_actual is None:
            return 0
        if nodo_actual.dato == elemento:
            return 1 + self._cantidad(nodo_actual.sig, elemento)
        return self._cantidad(nodo_actual.sig, elemento)
    def sublista(self, posicion, longitud):
        nueva = LinkedList()
        self._sublista(self.head, posicion, longitud, resultado = nueva)
        return nueva
    def _sublista(self, nodo_actual, posicion, longitud, resultado, i=0):
        if nodo_actual is None or i >= posicion + longitud:
            return 
        if i >= posicion and i < posicion + longitud:
            resultado.add(nodo_actual.dato)
            return self._sublista(nodo_actual.sig, posicion, longitud, resultado, i+1)
        return self._sublista(nodo_actual.sig, posicion, longitud, resultado, i+1)
    def intercalar(self, otro):
        nueva = LinkedList()
        self._intercalar(self.head, otro.head, resultado = nueva)
        return nueva
    def _intercalar(self, nodo1, nodo2, resultado):
        if nodo1 is None and nodo2 is None:
            return 
        if nodo1 is not None and nodo2 is None:
            resultado.add(nodo1.dato)
            return self._intercalar(nodo1.sig, nodo2, resultado)
        if nodo1 is None and nodo2 is not None:
            resultado.add(nodo2.dato)
            return self._intercalar(nodo1.sig, nodo2, resultado)
        resultado.add(nodo1.dato)
        resultado.add(nodo2.dato)
        return self._intercalar(nodo1.sig, nodo2.sig, resultado)
    def _particionar(self, nodo_actual, pivote, menores, iguales,mayores):
        if nodo_actual is None:
            return
        if nodo_actual.dato < pivote:
            menores.add(nodo_actual.dato)
        elif nodo_actual.dato > pivote:
            mayores.add(nodo_actual.dato)
        else:
            iguales.add(nodo_actual.dato)
        self._particionar(nodo_actual.sig, pivote, menores, iguales, mayores)
    def quicksort(self):
        if self.head is None or self.head.sig is None:
            return self
        pivote = self.head.dato
        menores = LinkedList()
        iguales = LinkedList()
        mayores = LinkedList()
        self._particionar(self.head, pivote, menores, iguales, mayores)
        menores = menores.quicksort()
        mayores = mayores.quicksort()
        return menores.concatenar(iguales).concatenar(mayores)
    def aplanar(self):
        return self._aplanar(self.head)
    def _aplanar(self, nodo_actual):
        if nodo_actual is None:
            return LinkedList()
        return (nodo_actual.dato.concatenar(self._aplanar(nodo_actual.sig)))
    def longitudLL(self):
        return self._longitudLL(self.head)
    def _longitudLL(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return nodo_actual.dato.length_recursivo() + self._longitudLL(nodo_actual.sig)
    def longitudLL2(self):
        nueva = self.aplanar()
        return self._longitudLL2(nueva.head)
    def _longitudLL2(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._longitudLL2(nodo_actual.sig)
    def agregar_elemento(self, elemento):
        return self._agregar_elemento(self.head, elemento)
    def _agregar_elemento(self, nodo_actual, elemento):
        if nodo_actual is None:
            return LinkedList()
        primera_con_elemento = elemento.concatenar(nodo_actual.dato)
        return primera_con_elemento.concatenar(self._agregar_elemento(nodo_actual.sig, elemento))
    def agregar_a_todas(self, lista_de_partes, elemento):
        return self._agregar_a_todas(lista_de_partes.head, elemento)
    def _agregar_a_todas(self, nodo_actual, elemento):
        if nodo_actual is None:
            return LinkedList()
        nueva = LinkedList()
        sublista = nodo_actual.dato
        copia = LinkedList()
        copia.add(elemento)
        copia = copia.concatenar(sublista)
        nueva.add(copia)
        resto = self._agregar_a_todas(nodo_actual.sig, elemento)
        return nueva.concatenar(resto)
    def partes(self):
        return self._partes(self.head)
    def _partes(self, nodo_actual):
        if nodo_actual is None:
            resultado = LinkedList()
            resultado.add(LinkedList())
            return resultado
        primero = nodo_actual.dato
        resto_partes = self._partes(nodo_actual.sig)
        con_primero = self.agregar_a_todas(resto_partes, primero)
        return resto_partes.concatenar(con_primero)
    def obtener(self, indice):
        return self._obtener(self.head, indice)
    def _obtener(self, nodo, indice):
        if nodo is None:
            raise IndexError
        if indice == 0:
            return nodo.dato
        return self._obtener(nodo.sig, indice - 1)
    def eliminar_posicion(self, indice):
        nueva = LinkedList()
        self._eliminar_posicion(self.head, indice, resultado = nueva)
        return nueva
    def _eliminar_posicion(self, nodo_actual, indice, resultado, i=0):
        if nodo_actual is None:
            return
        if i == indice:
            return self._eliminar_posicion(nodo_actual.sig, indice, resultado, i+1)
        resultado.add(nodo_actual.dato)
        return self._eliminar_posicion(nodo_actual.sig, indice, resultado, i+1)
    def pegar_adelante(self, elemento):
        return self._pegar_adelante(self.head, elemento)
    def _pegar_adelante(self, nodo_actual, elemento):
        if nodo_actual is None:
            return LinkedList()
        nueva_perm = LinkedList()
        nueva_perm.add(elemento)
        nueva_perm = nueva_perm.concatenar(nodo_actual.dato)
        resultado = LinkedList()
        resultado.add(nueva_perm)
        return resultado.concatenar(self._pegar_adelante(nodo_actual.sig,elemento))
    def iterar_elementos_sin_repetir(self):
        return self._iterar_elementos_sin_repetir(self.head)
    def _iterar_elementos_sin_repetir(self, nodo_actual, i=0, usados=None):
        if usados is None:
            usados = LinkedList()
        if i >= self.length_recursivo():
            return LinkedList()
        fijo = self.obtener(i)
        if fijo in usados:
            return self._iterar_elementos_sin_repetir(nodo_actual, i+1, usados)
        nuevo = LinkedList()
        nuevo.add(fijo)
        nuevos_usados = usados.concatenar(nuevo)
        resto = self.eliminar_posicion(i)
        perms_del_resto = resto.permutaciones()
        combinadas = perms_del_resto.pegar_adelante(fijo)
        return combinadas.concatenar \
            (self._iterar_elementos_sin_repetir(nodo_actual, i+1, nuevos_usados))
    def copia(self):
        nueva = LinkedList()
        self._copia(self.head, nueva)
        return nueva
    def _copia(self, nodo_actual, nueva):
        if nodo_actual is None:
            return
        nueva.add(nodo_actual.dato)
        self._copia(nodo_actual.sig, nueva)
    def permutaciones(self):
        return self._permutaciones(self.head)
    def _permutaciones(self, nodo_actual):
        if self.length_recursivo() <= 1:
            resultado = LinkedList()
            copia = self.copia()
            resultado.add(copia)
            return resultado
        return self.iterar_elementos_sin_repetir()
    def combinar_elemento_con_listas(self, x, combinaciones):
        return self._combinar_elemento_con_listas(combinaciones.head, x)
    def _combinar_elemento_con_listas(self, nodo_actual, x):
        if nodo_actual is None:
            return LinkedList()
        nueva_comb = LinkedList()
        nueva_comb.add(x)
        nueva_comb = nueva_comb.concatenar(nodo_actual.dato)
        resultado = LinkedList()
        resultado.add(nueva_comb)
        return resultado.concatenar(self._combinar_elemento_con_listas(nodo_actual.sig, x))
    def combinar_lista_con_todo(self, primera_lista,combinaciones_resto):
        return self._combinar_lista_con_todo(primera_lista.head, combinaciones_resto)
    def _combinar_lista_con_todo(self, nodo1, combinaciones_resto):
        if nodo1 is None:
            return LinkedList()
        combinaciones_del_numero = (self.combinar_elemento_con_listas(nodo1.dato,combinaciones_resto))
        return combinaciones_del_numero.concatenar( \
        self._combinar_lista_con_todo(nodo1.sig, combinaciones_resto))
    def todosConTodosN(self):
        return self._todosConTodosN(self.head)
    def _todosConTodosN(self, nodo_actual):
        if nodo_actual is None:
            resultado = LinkedList()
            vacia = LinkedList()
            resultado.add(vacia)
            return resultado
        primera_lista = nodo_actual.dato
        combinaciones_resto = self._todosConTodosN(nodo_actual.sig)
        return self.combinar_lista_con_todo(primera_lista, combinaciones_resto)
    def __len__(self):
        return self.length_recursivo()
    def __iter__(self):
        yield from self._iter_rec(self.head)
    def _iter_rec(self, nodo):
        if nodo is None:
            return
        yield nodo.dato
        yield from self._iter_rec(nodo.sig)
        
def combinar_elemento_con_listas(x, combinaciones):
    if not combinaciones:
        return []
    # Pegamos el elemento al inicio de la primera sublista y procesamos el resto
    return [[x] + combinaciones[0]] + combinar_elemento_con_listas(x, combinaciones[1:])

# Auxiliar 2: Recorre la primera lista de forma recursiva y junta las combinaciones
def combinar_lista_con_todo(primera_lista, combinaciones_resto):
    if not primera_lista:
        return []
    
    # 1. Combinamos el número actual con todas las combinaciones que venían del resto
    combinaciones_del_numero = combinar_elemento_con_listas(primera_lista[0], combinaciones_resto)
    
    # 2. Avanzamos recursivamente con el siguiente número de la primera lista
    return combinaciones_del_numero + combinar_lista_con_todo(primera_lista[1:], combinaciones_resto)

# Función Principal
def todosConTodosN_pura(listas):
    # Caso base: si no quedan más listas por procesar, devolvemos [[]]
    if not listas:
        return [[]]
    
    primera_lista = listas[0]
    # Resolvemos el subproblema para el resto de las listas mediante recursión
    combinaciones_resto = todosConTodosN_pura(listas[1:])
    
    # En lugar del doble for, disparamos la cadena de funciones auxiliares
    return combinar_lista_con_todo(primera_lista, combinaciones_resto)
          
lista = LinkedList()
lista2 = LinkedList()

lista3 = LinkedList()
lista4 = LinkedList()
lista5 = LinkedList()
lista6 = LinkedList()

lista.add(1)
lista.add(10)
lista.add(25)
lista.add(50)
lista.add(50)
lista.add(50)

lista2.add(1)
lista2.add(10)
lista2.add(25)
lista2.add(50)
lista2.add(50)
lista2.add(50)

lista3.add(2)
lista3.add(3)
lista3.add(4)
lista4.add(5)
lista5.add(6)
lista5.add(7)

lista6.add(lista3)
lista6.add(lista4)
lista6.add(lista5)

print(lista)
print(lista2)

print('¿Son iguales las dos listas?')
print(lista.igualdad(lista2))

print(f"Sumatoria de la lista: {lista.sumatoria_lista()}")

dato = 10
print(f"Pertenece el {dato} a la lista?")
print(lista.pertenece(dato))

print('Concatenación de listas: ')
print(lista.concatenar(lista2))

print(f"El último elemento de la lista es: {lista.ultimo_elemento()}")
print(f"El penúltimo elemento de la lista es: {lista.penultimo_elemento()}")

n = 3
print(f"Los primeros {n} elementos de la lista son {lista.primeros(n)}")

print(f"El minimo elemento de la lista es: {lista.minimo()}")
print(f"El maximo elemento de la lista es: {lista.maximo()}")

print('La reversa de la lista es: ')
print(lista.reversa())

print("Longitud (recursivo):")
print(lista.length_recursivo())

print('¿Es palindromo la lista?')
print(lista.es_palindromo())

dato = 50
print(f"Cantidad de apariciones de {dato} en la lista: {lista.cantidad(dato)}")

posicion = 1
longitud = 3
print(f"Sublista que empieza en la posición {posicion} y tiene longitud {longitud}")
print(lista.sublista(posicion, longitud))

print('Listas intercaladas: ')
print(lista.intercalar(lista2))


lista.add(21)
lista.add(32)
lista.add(17)

print('Lista ordenada con quicksort:')
print(lista.quicksort())

print('Listas sin aplanar:')
print(lista6)

print('Listas aplanadas:')
print(lista6.aplanar())

print(f"longitud de la lista aplanada: {lista6.longitudLL2()}")

print(f"Conjunto de partes de {lista3}")
print(lista3.partes())

print(f"Conjunto de permutaciones de {lista3}")
print(lista3.permutaciones())

print('Combinacion de todos con todos entre las sublistas de la lista 6' )
print(lista6.todosConTodosN())

#Elimino el 50 de la lista:
lista.pop2()

print("Lista sin el 50:")
print(lista)

#Obtengo el índice original del 10:
print("Índice original del 10:")
print(lista.buscar_recursivo(10))

#Cambio de lugar el 10 por el 25:
lista.exchange_recursivo(10, 25)

#Obtengo el nuevo índice del 10:
print("Índice del 10 después del cambio de lugar:")
print(lista.buscar_recursivo(10))

print("Longitud (iterativo) después de eliminar al 50:")
print(lista.length_iterativo())

lista.insert(40)
lista.insert(35)
lista.insert(30)
lista.insert(20)
lista.insert(15)

#Ordeno elementos de menor a mayor:
lista.sort_recursivo()

print(lista)

#Elimino los elementos posteriores al 20:
lista.trunc_despues(20)

print(lista)

lista.add(25)
lista.add(30)
lista.add(35)
lista.add(40)

#Elimino los elementos anteriores al 20:
lista.trunc_antes(20)

print(lista)

lista.insert(1)
lista.insert(10)
lista.insert(15)

#Obtengo el índice del 25:
print(lista.busqueda_binaria_recursiva(25))

