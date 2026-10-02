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
    def minimo_rec(self, lista):
        if len(lista) == 1:
            return lista[0]
        minimo_resto = self.minimo_rec(lista[1:])
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
        minimo = self.minimo_rec(lista)
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
        return " -> ".join(elementos)
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

lista = LinkedList()

lista.add(1)
lista.add(10)
lista.add(25)
lista.add(50)

print(lista)

print("Longitud (recursivo):")
print(lista.length_recursivo())

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

