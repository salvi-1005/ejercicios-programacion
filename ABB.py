class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ABB:
    def __init__(self):
        self.raiz = None
    # ======================
    # INSERCIÓN
    # ======================
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)
    def _insertar(self, nodo_actual, valor):
        if nodo_actual is None:
            return Nodo(valor)
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._insertar(nodo_actual.derecho, valor)
        return nodo_actual
    # ======================
    # RECORRIDOS
    # ======================
    def inorden(self):
        self._inorden(self.raiz)
        print()
    def _inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden(nodo_actual.izquierdo)
            print(nodo_actual.valor, end=" ")
            self._inorden(nodo_actual.derecho)
    def preorden(self):
        self._preorden(self.raiz)
        print()
    def _preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=" ")
            self._preorden(nodo_actual.izquierdo)
            self._preorden(nodo_actual.derecho)
    def postorden(self):
        self._postorden(self.raiz)
        print()
    def _postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden(nodo_actual.izquierdo)
            self._postorden(nodo_actual.derecho)
            print(nodo_actual.valor, end=" ")
    def ordenar_de_mayor_a_menor(self):
        self._ordenar_de_mayor_a_menor(self.raiz)
        print()
    def _ordenar_de_mayor_a_menor(self, nodo_actual):
        if nodo_actual is not None:
            self._ordenar_de_mayor_a_menor(nodo_actual.derecho)
            print(nodo_actual.valor, end=" ")
            self._ordenar_de_mayor_a_menor(nodo_actual.izquierdo)
    # ======================
    # BÚSQUEDA
    # ======================
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    def _buscar(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar(nodo_actual.izquierdo, valor)
        return self._buscar(nodo_actual.derecho, valor)
    def buscar_nodo(self, valor):
        return self._buscar_nodo(self.raiz, valor)
    def _buscar_nodo(self, nodo_actual, valor):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_nodo(nodo_actual.izquierdo, valor)
        return self._buscar_nodo(nodo_actual.derecho, valor)
    # ======================
    # ALTURA
    # ======================
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura(nodo_actual.izquierdo), self._altura(nodo_actual.derecho))
    # ======================
    # CANTIDAD DE NODOS
    # ======================
    def cantidad_nodos(self):
        return self._cantidad_nodos(self.raiz)
    def _cantidad_nodos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return (1 + self._cantidad_nodos(nodo_actual.izquierdo) + 
                self._cantidad_nodos(nodo_actual.derecho))
    # ======================
    # AUXILIARES ELIMINACIÓN
    # ======================
    def _encontrar_maximo_nodo(self, nodo):
        if nodo.derecho is None:
            return nodo
        return self._encontrar_maximo_nodo(nodo.derecho)
    def _encontrar_minimo_nodo(self, nodo):
        if nodo.izquierdo is None:
            return nodo
        return self._encontrar_minimo_nodo(nodo.izquierdo)
    # ======================
    # ELIMINACIÓN POR FUSIÓN
    # ======================
    def eliminar_fusion(self, valor):
        self.raiz = self._eliminar_fusion(self.raiz, valor)
    def _eliminar_fusion(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_fusion(nodo_actual.izquierdo,valor_a_eliminar)
            return nodo_actual
        if valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_fusion(nodo_actual.derecho, valor_a_eliminar)
            return nodo_actual
        # Encontramos el nodo
        if nodo_actual.izquierdo is None:
            return nodo_actual.derecho
        if nodo_actual.derecho is None:
            return nodo_actual.izquierdo
        # Caso de dos hijos → FUSIÓN
        maximo_izq = self._encontrar_maximo_nodo(nodo_actual.izquierdo)
        maximo_izq.derecho = nodo_actual.derecho
        return nodo_actual.izquierdo
    # ======================
    # ELIMINACIÓN POR COPIA
    # ======================
    def eliminar_copia(self, valor):
        self.raiz = self._eliminar_copia(self.raiz, valor)
    def _eliminar_copia(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_copia(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_copia(nodo_actual.derecho, valor_a_eliminar)
        else:
            # Sin hijo izquierdo
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            # Sin hijo derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            # Dos hijos → COPIA DEL SUCESOR
            sucesor = self._encontrar_minimo_nodo(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar_copia(nodo_actual.derecho, sucesor.valor)
        return nodo_actual
    # ======================
    # MÍNIMO Y MÁXIMO
    # ======================
    def minimo(self):
        return self._minimo(self.raiz)
    def _minimo(self, nodo_actual):
        if nodo_actual.izquierdo is None:
            return nodo_actual.valor
        return self._minimo(nodo_actual.izquierdo)
    def maximo(self):
        return self._maximo(self.raiz)
    def _maximo(self, nodo_actual):
        if nodo_actual.derecho is None:
            return nodo_actual.valor
        return self._maximo(nodo_actual.derecho)
    # ======================
    # MENORES A UN VALOR
    # ======================
    def menores_a(self, dato):
        return self._menores_a(self.raiz, dato)
    def _menores_a(self, nodo_actual, dato):
        if nodo_actual is None:
            return []
        if nodo_actual.valor >= dato:
            return self._menores_a(nodo_actual.izquierdo, dato)
        return (self._menores_a(nodo_actual.izquierdo, dato) + 
                [nodo_actual.valor] + self._menores_a(nodo_actual.derecho, dato))
    
arbol = ABB()

for v in [10, 5, 15, 3, 7]:
    arbol.insertar(v)

print("Inorden:")
arbol.inorden()

print("Preorden:")
arbol.preorden()

print("Postorden:")
arbol.postorden()

print("Mayor a menor:")
arbol.ordenar_de_mayor_a_menor()

print("Altura:")
print(arbol.altura())

dato = 7
print(f"Está el {dato}?")
print(arbol.buscar(dato))

print("Mínimo:")
print(arbol.minimo())

print("Máximo:")
print(arbol.maximo())

dato = 10
print(f"Elementos menores a {dato}:")
print(arbol.menores_a(dato))

