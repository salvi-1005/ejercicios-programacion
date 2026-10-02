class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
class arbol_binario_enteros:
    def __init__(self):
        self.raiz = None
    def insertar(self, elemento):
        self.raiz = self._insertar(self.raiz, elemento)
    def _insertar(self, nodo_actual, elemento):
        if not isinstance(elemento, int):
            raise TypeError("El ABB sólo admite enteros")
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar(nodo_actual.izquierdo, elemento)
        elif elemento > nodo_actual.valor:
            nodo_actual.derecho = self._insertar(nodo_actual.derecho, elemento)
        return nodo_actual
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
    def eliminar(self, valor_a_eliminar):
        self.raiz = self._eliminar(self.raiz, valor_a_eliminar)
    def _eliminar(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar(nodo_actual.derecho, valor_a_eliminar)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            sucesor = self.minimo(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar(nodo_actual.derecho, sucesor.valor)
        return nodo_actual
    #2)
    def cantidad_nodos(self):
        return self._cantidad_nodos(self.raiz)
    def _cantidad_nodos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._cantidad_nodos(nodo_actual.izquierdo) + \
            self._cantidad_nodos(nodo_actual.derecho)
    def cantidad_nodos_cola(self):
        if self.raiz is None:
            return 0
        cola = [self.raiz]
        cantidad = 0
        while cola:
            actual = cola.pop(0)
            cantidad += 1
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return cantidad
    def es_vacio(self):
        return self.cantidad_nodos == 0
    #3)
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura(nodo_actual.izquierdo), self._altura(nodo_actual.derecho))
    def altura_cola(self):
        return self._altura_cola(self.raiz)
    def _altura_cola(self, nodo_actual, acum=None):
        if acum is None:
            acum = 0
        if nodo_actual is None:
            return acum
        acum += 1
        return max(self._altura_cola(nodo_actual.izquierdo, acum), \
                   self._altura_cola(nodo_actual.derecho, acum))
    #4)
    def igualdad(self, otro):
        return self._igualdad(self.raiz, otro.raiz)
    def _igualdad(self, nodo1, nodo2):
        if nodo1 is None and nodo2 is None:
            return True
        if nodo1 is None or nodo2 is None:
            return False
        if nodo1.valor != nodo2.valor:
            return False
        return (self._igualdad(nodo1.izquierdo, nodo2.izquierdo) \
                and self._igualdad(nodo1.derecho, nodo2.derecho))
    #5)
    def recorrido_guiado(self, direcciones):
        return self._recorrido_guiado(self.raiz, direcciones)
    def _recorrido_guiado(self, nodo_actual, direcciones):
        if not direcciones:
            return nodo_actual.valor
        indice = direcciones[0]
        if indice == 'izquierda' and nodo_actual.izquierdo is None \
            or indice == 'derecha' and nodo_actual.derecho is None:
                raise ValueError('Se acabó el camino')
        if indice == 'izquierda' and nodo_actual.izquierdo is not None:
            return self._recorrido_guiado(nodo_actual.izquierdo, direcciones[1:])
        if indice == 'derecha' and nodo_actual.derecho is not None:
            return self._recorrido_guiado(nodo_actual.derecho, direcciones[1:])
    #6)
    #a)
    def pertenece(self, elemento):
        return self._pertenece(self.raiz, elemento)
    def _pertenece(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento:
            return True
        if nodo_actual.izquierdo is None:
            return self._pertenece(nodo_actual.derecho, elemento)
        if nodo_actual.derecho is None:
            return self._pertenece(nodo_actual.izquierdo, elemento)
        return self._pertenece(nodo_actual.izquierdo, elemento) \
            or self._pertenece(nodo_actual.derecho, elemento)
    #b)
    def nivel(self, elemento):
        return self._nivel(self.raiz, elemento)
    def _nivel(self, nodo_actual, elemento, nivel=0):
        if nodo_actual is None:
            return self.altura() + 1
        if nodo_actual.valor == elemento:
            return nivel
        izquierda = self._nivel(nodo_actual.izquierdo, elemento, nivel + 1)
        if izquierda != self.altura() + 1:
            return izquierda
        return self._nivel(nodo_actual.derecho,elemento,nivel + 1)
    #c)
    def padre(self, elemento):
        return self._padre(self.raiz, elemento)
    def _padre(self, nodo_actual, elemento):
        if nodo_actual is None:
            return -1
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return -1
        if (nodo_actual.izquierdo is not None and nodo_actual.izquierdo.valor == elemento) \
        or (nodo_actual.derecho is not None and nodo_actual.derecho.valor == elemento):
            return nodo_actual.valor
        izquierda = self._padre(nodo_actual.izquierdo, elemento)
        if izquierda != -1:
            return izquierda
        return self._padre(nodo_actual.derecho, elemento)
    #d)
    def hijos(self, elemento):
        return self._hijos(self.raiz, elemento)
    def _hijos(self, nodo_actual, elemento):
        if not self.pertenece(elemento):
            return -1
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return []
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is not None and nodo_actual.derecho is not None):
            return [nodo_actual.izquierdo.valor] + [nodo_actual.derecho.valor] 
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is not None and nodo_actual.derecho is None):
            return [nodo_actual.izquierdo.valor]
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is None and nodo_actual.derecho is not None):
            return [nodo_actual.derecho.valor] 
        izquierda = self._hijos(nodo_actual.izquierdo, elemento)
        if izquierda != []:
            return izquierda
        return self._hijos(nodo_actual.derecho, elemento)
    #e)
    def antecesores(self, elemento):
        return self._antecesores(self.raiz, elemento)
    def _antecesores(self, nodo_actual, elemento):
        if nodo_actual is None:
            return []
        if nodo_actual.valor == elemento:
            return []
        izquierda = self._antecesores(nodo_actual.izquierdo, elemento)
        if izquierda != [] or (nodo_actual.izquierdo is not None \
          and nodo_actual.izquierdo.valor == elemento):
            return [nodo_actual.valor] + izquierda
        derecha = self._antecesores(nodo_actual.derecho, elemento)
        if derecha != [] or (nodo_actual.derecho is not None \
          and nodo_actual.derecho.valor == elemento):
            return [nodo_actual.valor] + derecha
        return []
    #7)
    def es_hoja(self, elemento):
        return self._es_hoja(self.raiz, elemento)
    def _es_hoja(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento and nodo_actual.izquierdo is None \
          and nodo_actual.derecho is None:
            return True
        izquierda = self._es_hoja(nodo_actual.izquierdo, elemento)
        if izquierda != False:
            return izquierda
        return self._es_hoja(nodo_actual.derecho, elemento)
    def sin_hojas(self):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._sin_hojas(self.raiz)
        return nuevo_arbol
    def _sin_hojas(self, nodo_actual):
        if nodo_actual is None:
            return None
        if self.es_hoja(nodo_actual.valor):
            return None
        nuevo = Nodo(nodo_actual.valor)
        nuevo.izquierdo = self._sin_hojas(nodo_actual.izquierdo)
        nuevo.derecho = self._sin_hojas(nodo_actual.derecho)
        return nuevo
    #8)
    def agregar_raiz(self, valor, ramas):
        if not ramas:
            return []
        return ([[valor] + ramas[0]] + self.agregar_raiz(valor, ramas[1:]))
    def agregar_raiz_cola(self, valor, ramas, resultado = None):
        if resultado is None:
            resultado = []
        if not ramas:
            return resultado
        resultado.append([valor] + ramas[0])
        return self.agregar_raiz_cola(valor, ramas[1:], resultado)
    def ramas(self):
        return self._ramas(self.raiz)
    def _ramas(self, nodo_actual):
        if nodo_actual is None:
            return []
        if (nodo_actual.izquierdo is None and nodo_actual.derecho is None):
            return [[nodo_actual.valor]]
        return (self.agregar_raiz(nodo_actual.valor, self._ramas(nodo_actual.izquierdo)) + \
                self.agregar_raiz(nodo_actual.valor, self._ramas(nodo_actual.derecho)))
    #9)
    def es_balanceado(self):
        return self._es_balanceado(self.raiz)
    def _es_balanceado(self, nodo_actual):
        if nodo_actual is None:
            return True
        altura_izq = self._altura(nodo_actual.izquierdo)
        altura_der = self._altura(nodo_actual.derecho)
        if abs(altura_izq - altura_der) > 1:
            return False
        return (self._es_balanceado(nodo_actual.izquierdo) and \
        self._es_balanceado(nodo_actual.derecho))
    #10)
    def espejo(self):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._espejo(self.raiz)
        return nuevo_arbol
    def _espejo(self, nodo_actual):
        if nodo_actual is None:
            return None
        nuevo = Nodo(nodo_actual.valor)
        nuevo.izquierdo = self._espejo(nodo_actual.derecho)
        nuevo.derecho = self._espejo(nodo_actual.izquierdo)
        return nuevo
    #12)
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._inorden(nodo_actual.izquierdo) + \
            [nodo_actual.valor] + \
            self._inorden(nodo_actual.derecho)
    def inorden_cola(self):
        return self._inorden_cola(self.raiz)
    def _inorden_cola(self):
        resultado = []
        pila = []
        actual = self.raiz
        while actual is not None or pila:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
        actual = pila.pop()
        resultado.append(actual.valor)
        actual = actual.derecho
        return resultado
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return [nodo_actual.valor] + \
            self._preorden(nodo_actual.izquierdo) + \
            self._preorden(nodo_actual.derecho)
    def preorden_cola(self):
        return self._preorden_cola(self.raiz)
    def _preorden_cola(self):
        if self.raiz is None:
            return []
        pila = [self.raiz]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.derecho is not None:
                pila.append(actual.derecho)
            if actual.izquierdo is not None:
                pila.append(actual.izquierdo)
        return resultado
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._postorden(nodo_actual.izquierdo) + \
            self._postorden(nodo_actual.derecho) + \
            [nodo_actual.valor]
    def postorden_cola(self):
        return self._postorden_cola(self.raiz)
    def _postorden_cola(self):
        if self.raiz is None:
            return []
        pila = [self.raiz]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.izquierdo is not None:
                pila.append(actual.izquierdo)
            if actual.derecho is not None:
                pila.append(actual.derecho)
        return resultado[::-1]
    #13)
    def bfs(self):
        if self.raiz is None:
            return []
        cola = [self.raiz]
        recorrido = []
        while cola:
            actual = cola.pop(0)
            recorrido.append(actual.valor)
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return recorrido
    #14)
    #Versión que NO admite repetidos:
    def insertar2(self, elemento):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._insertar2(self.raiz, elemento)
        return nuevo_arbol
    def _insertar2(self, nodo_actual, elemento):
        if not isinstance(elemento, int):
            raise TypeError("El ABB sólo admite enteros")
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar2(nodo_actual.izquierdo, elemento)
        elif elemento > nodo_actual.valor:
            nodo_actual.derecho = self._insertar2(nodo_actual.derecho, elemento)
        return nodo_actual
    #Versión que admite repetidos:
    def insertar3(self, elemento):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._insertar3(self.raiz, elemento)
        return nuevo_arbol
    def _insertar3(self, nodo_actual, elemento):
        if not isinstance(elemento, int):
            raise TypeError("El ABB sólo admite enteros")
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar3(nodo_actual.izquierdo, elemento)
        else: 
            nodo_actual.derecho = self._insertar3(nodo_actual.derecho, elemento)
        return nodo_actual
    #15)
    #Versión de copia:
    def eliminar2(self, valor_a_eliminar):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._eliminar2(self.raiz, valor_a_eliminar)
        return nuevo_arbol
    def _eliminar2(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar2(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar2(nodo_actual.derecho, valor_a_eliminar)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            sucesor = self.minimo(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar2(nodo_actual.derecho, sucesor.valor)
        return nodo_actual
    #Versión de fusión:
    def eliminar3(self, valor):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._eliminar3(self.raiz, valor)
        return nuevo_arbol
    def _eliminar3(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar3(nodo_actual.izquierdo,valor_a_eliminar)
            return nodo_actual
        if valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar3(nodo_actual.derecho, valor_a_eliminar)
            return nodo_actual
        if nodo_actual.izquierdo is None:
            return nodo_actual.derecho
        if nodo_actual.derecho is None:
            return nodo_actual.izquierdo
        maximo_izq = self._encontrar_maximo_nodo(nodo_actual.izquierdo)
        maximo_izq.derecho = nodo_actual.derecho
        return nodo_actual.izquierdo
    #17)
    def mostrar(self):
        return self._mostrar(self.raiz, 0)
    def _mostrar(self, nodo_actual, nivel):
        if nodo_actual is None:
            return None
        print(' '*nivel + str(nodo_actual.valor))
        izquierda = self._mostrar(nodo_actual.izquierdo, nivel + 1)
        if izquierda != None:
            return izquierda
        return self._mostrar(nodo_actual.derecho, nivel + 1)
    #18)
    def hermano(self, nodo):
        return self._hermano(self.raiz, nodo)
    def _hermano(self, nodo_actual, nodo):
        if nodo_actual is None:
            return None
        if nodo_actual.izquierdo is not None and nodo_actual.izquierdo.valor == nodo.valor:
            if nodo_actual.derecho is None:
                return None
            return nodo_actual.derecho.valor
        if nodo_actual.derecho is not None and nodo_actual.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo is None:
                return None
            return nodo_actual.izquierdo.valor
        izquierda = self._hermano(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._hermano(nodo_actual.derecho, nodo)
    #19)
    def primos(self, nodo):
        return self._primos(self.raiz, nodo)
    def _primos(self, nodo_actual, nodo):
        if nodo_actual is None:
            return None
        if nodo_actual.izquierdo.izquierdo is not None \
            and nodo_actual.izquierdo.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.izquierdo.derecho is not None \
            and nodo_actual.izquierdo.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo.valor] + \
                [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.izquierdo is not None \
            and nodo_actual.derecho.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.derecho is not None \
            and nodo_actual.derecho.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.izquierdo.valor]
        
        izquierda = self._primos(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._primos(nodo_actual.derecho, nodo)
    #20)
    def ancestro_comun(self, nodo1, nodo2):
        return self._ancestro_comun(self.raiz, nodo1, nodo2)
    def _ancestro_comun(self, nodo_actual, nodo1, nodo2):
        if nodo_actual is None:
            return None
        if nodo_actual.valor in self.antecesores(nodo1.valor) and \
            nodo_actual.valor in self.antecesores(nodo2.valor) and \
             nodo_actual.izquierdo.valor not in self.antecesores(nodo1.valor) and \
              nodo_actual.izquierdo.valor not in self.antecesores(nodo2.valor) and \
               nodo_actual.derecho.valor not in self.antecesores(nodo1.valor) and \
                nodo_actual.derecho.valor not in self.antecesores(nodo2.valor):
            return nodo_actual.valor
        izquierda = self._ancestro_comun(nodo_actual.izquierdo, nodo1, nodo2)
        if izquierda != None:
            return izquierda
        return self._ancestro_comun(nodo_actual.derecho, nodo1, nodo2)
    #21)
    def insertarOrdenado(self, elemento):
        if self.raiz is None:
            self.insertar(elemento)
            return
        if elemento <= self.maximo():
            raise ValueError("El elemento rompe el orden")
        self.insertar(elemento)
        return self
    #22)
    def eliminarOrdenado(self, elemento):
        if elemento != self.maximo():
            raise ValueError('El elemento rompe el orden')
        self.eliminar(elemento)
        return self
    def __str__(self):
        return f"Preorden: {str(self.preorden())}, Postorden: {str(self.postorden())}, Inorden: {str(self.inorden())}"
    
        
arbol_enteros1 = arbol_binario_enteros()
arbol_enteros1.insertar(6)
arbol_enteros1.insertar(4)
arbol_enteros1.insertar(3)
arbol_enteros1.insertar(5)
arbol_enteros1.insertar(8)
arbol_enteros1.insertar(7)

print('Arbol 1')
print(arbol_enteros1)

arbol_enteros2 = arbol_binario_enteros()
arbol_enteros2.insertar(6)
arbol_enteros2.insertar(4)
arbol_enteros2.insertar(3)
arbol_enteros2.insertar(5)
arbol_enteros2.insertar(8)
arbol_enteros2.insertar(7)


print('Arbol 2')
print(arbol_enteros2)

print('Cantidad de nodos del arbol')
print(arbol_enteros1.cantidad_nodos())

print('Altura del arbol')
print(arbol_enteros1.altura())

print('¿Son iguales arbol 1 y arbol 2?')
print(arbol_enteros1.igualdad(arbol_enteros2))

print('Recorrido guiado:')
print(arbol_enteros1.recorrido_guiado(['derecha', 'izquierda']))

dato = 1
print(f"¿Pertenece el {dato} a la lista?")
print(arbol_enteros1.pertenece(dato))

dato = 5
print(f"Nivel del {dato}: ")
print(arbol_enteros1.nivel(dato))

dato = 7
print(f"Padre del {dato}: ")
print(arbol_enteros1.padre(dato))

dato = 6
print(f"Hijos del {dato}: ")
print(arbol_enteros1.hijos(dato))

dato = 3
print(f"Antecesores del {dato}: ")
print(arbol_enteros1.antecesores(dato))

print('Arbol sin hojas: ')
print(arbol_enteros1.sin_hojas())

print('Ramas del arbol: ')
print(arbol_enteros1.ramas())

print('¿Es balanceado el arbol?')
print(arbol_enteros1.es_balanceado())

print('Espejo del arbol')
print(arbol_enteros1.espejo())

dato = 1
print(f"Arbol con el {dato}: ")
print(arbol_enteros2.insertar2(dato))

dato = 8
print(f"Arbol sin el {dato}: ")
print(arbol_enteros2.eliminar2(dato))

print("Imprimir elementos del arbol 1 con indentación correspondiente al nivel: ")
arbol_enteros1.mostrar()

nodo = Nodo(4)
print(f"Hermano del {nodo.valor}: ")
print(arbol_enteros1.hermano(nodo))

nodo = Nodo(7)
print(f"Primos del {nodo.valor}: ")
print(arbol_enteros1.primos(nodo))

nodo1 = Nodo(3)
nodo2 = Nodo(5)
print(f"Primer ancestro comun entre {nodo1.valor} y {nodo2.valor}: ")
print(arbol_enteros1.ancestro_comun(nodo1, nodo2))

dato = 9
print(f"Arbol con el {dato}")
print(arbol_enteros2.insertarOrdenado(dato))

print("Imprimir elementos del arbol 2 con indentación correspondiente al nivel: ")
arbol_enteros2.mostrar()

dato = 9
print(f"Arbol sin el {dato}")
print(arbol_enteros2.eliminarOrdenado(dato))

class arbol_binario_genericos:
    def __init__(self):
        self.raiz = None
    def insertar(self, elemento):
        self.raiz = self._insertar(self.raiz, elemento)
    def _insertar(self, nodo_actual, elemento):
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar(nodo_actual.izquierdo, elemento)
        elif elemento > nodo_actual.valor:
            nodo_actual.derecho = self._insertar(nodo_actual.derecho, elemento)
        return nodo_actual
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
    def eliminar(self, valor_a_eliminar):
        self.raiz = self._eliminar(self.raiz, valor_a_eliminar)
    def _eliminar(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar(nodo_actual.derecho, valor_a_eliminar)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            sucesor = self.minimo(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar(nodo_actual.derecho, sucesor.valor)
        return nodo_actual
    #2)
    def cantidad_nodos(self):
        return self._cantidad_nodos(self.raiz)
    def _cantidad_nodos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._cantidad_nodos(nodo_actual.izquierdo) + \
            self._cantidad_nodos(nodo_actual.derecho)
    def cantidad_nodos_cola(self):
        if self.raiz is None:
            return 0
        cola = [self.raiz]
        cantidad = 0
        while cola:
            actual = cola.pop(0)
            cantidad += 1
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return cantidad
    def es_vacio(self):
        return self.cantidad_nodos == 0
    #3)
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura(nodo_actual.izquierdo), self._altura(nodo_actual.derecho))
    def altura_cola(self):
        return self._altura_cola(self.raiz)
    def _altura_cola(self, nodo_actual, acum=None):
        if acum is None:
            acum = 0
        if nodo_actual is None:
            return acum
        acum += 1
        return max(self._altura_cola(nodo_actual.izquierdo, acum), \
                   self._altura_cola(nodo_actual.derecho, acum))
    #4)
    def igualdad(self, otro):
        return self._igualdad(self.raiz, otro.raiz)
    def _igualdad(self, nodo1, nodo2):
        if nodo1 is None and nodo2 is None:
            return True
        if nodo1 is None or nodo2 is None:
            return False
        if nodo1.valor != nodo2.valor:
            return False
        return (self._igualdad(nodo1.izquierdo, nodo2.izquierdo) \
                and self._igualdad(nodo1.derecho, nodo2.derecho))
    #5)
    def recorrido_guiado(self, direcciones):
        return self._recorrido_guiado(self.raiz, direcciones)
    def _recorrido_guiado(self, nodo_actual, direcciones):
        if not direcciones:
            return nodo_actual.valor
        indice = direcciones[0]
        if indice == 'izquierda' and nodo_actual.izquierdo is None \
            or indice == 'derecha' and nodo_actual.derecho is None:
                raise ValueError('Se acabó el camino')
        if indice == 'izquierda' and nodo_actual.izquierdo is not None:
            return self._recorrido_guiado(nodo_actual.izquierdo, direcciones[1:])
        if indice == 'derecha' and nodo_actual.derecho is not None:
            return self._recorrido_guiado(nodo_actual.derecho, direcciones[1:])
    #6)
    #a)
    def pertenece(self, elemento):
        return self._pertenece(self.raiz, elemento)
    def _pertenece(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento:
            return True
        if nodo_actual.izquierdo is None:
            return self._pertenece(nodo_actual.derecho, elemento)
        if nodo_actual.derecho is None:
            return self._pertenece(nodo_actual.izquierdo, elemento)
        return self._pertenece(nodo_actual.izquierdo, elemento) \
            or self._pertenece(nodo_actual.derecho, elemento)
    #b)
    def nivel(self, elemento):
        return self._nivel(self.raiz, elemento)
    def _nivel(self, nodo_actual, elemento, nivel=0):
        if nodo_actual is None:
            return self.altura() + 1
        if nodo_actual.valor == elemento:
            return nivel
        izquierda = self._nivel(nodo_actual.izquierdo, elemento, nivel + 1)
        if izquierda != self.altura() + 1:
            return izquierda
        return self._nivel(nodo_actual.derecho,elemento,nivel + 1)
    #c)
    def padre(self, elemento):
        return self._padre(self.raiz, elemento)
    def _padre(self, nodo_actual, elemento):
        if nodo_actual is None:
            return -1
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return -1
        if (nodo_actual.izquierdo is not None and nodo_actual.izquierdo.valor == elemento) \
        or (nodo_actual.derecho is not None and nodo_actual.derecho.valor == elemento):
            return nodo_actual.valor
        izquierda = self._padre(nodo_actual.izquierdo, elemento)
        if izquierda != -1:
            return izquierda
        return self._padre(nodo_actual.derecho, elemento)
    #d)
    def hijos(self, elemento):
        return self._hijos(self.raiz, elemento)
    def _hijos(self, nodo_actual, elemento):
        if not self.pertenece(elemento):
            return -1
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return []
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is not None and nodo_actual.derecho is not None):
            return [nodo_actual.izquierdo.valor] + [nodo_actual.derecho.valor] 
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is not None and nodo_actual.derecho is None):
            return [nodo_actual.izquierdo.valor]
        if nodo_actual.valor == elemento and \
            (nodo_actual.izquierdo is None and nodo_actual.derecho is not None):
            return [nodo_actual.derecho.valor] 
        izquierda = self._hijos(nodo_actual.izquierdo, elemento)
        if izquierda != []:
            return izquierda
        return self._hijos(nodo_actual.derecho, elemento)
    #e)
    def antecesores(self, elemento):
        return self._antecesores(self.raiz, elemento)
    def _antecesores(self, nodo_actual, elemento):
        if nodo_actual is None:
            return []
        if nodo_actual.valor == elemento:
            return []
        izquierda = self._antecesores(nodo_actual.izquierdo, elemento)
        if izquierda != [] or (nodo_actual.izquierdo is not None \
          and nodo_actual.izquierdo.valor == elemento):
            return [nodo_actual.valor] + izquierda
        derecha = self._antecesores(nodo_actual.derecho, elemento)
        if derecha != [] or (nodo_actual.derecho is not None \
          and nodo_actual.derecho.valor == elemento):
            return [nodo_actual.valor] + derecha
        return []
    #7)
    def es_hoja(self, elemento):
        return self._es_hoja(self.raiz, elemento)
    def _es_hoja(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento and nodo_actual.izquierdo is None \
          and nodo_actual.derecho is None:
            return True
        izquierda = self._es_hoja(nodo_actual.izquierdo, elemento)
        if izquierda != False:
            return izquierda
        return self._es_hoja(nodo_actual.derecho, elemento)
    def sin_hojas(self):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._sin_hojas(self.raiz)
        return nuevo_arbol
    def _sin_hojas(self, nodo_actual):
        if nodo_actual is None:
            return None
        if self.es_hoja(nodo_actual.valor):
            return None
        nuevo = Nodo(nodo_actual.valor)
        nuevo.izquierdo = self._sin_hojas(nodo_actual.izquierdo)
        nuevo.derecho = self._sin_hojas(nodo_actual.derecho)
        return nuevo
    #8)
    def agregar_raiz(self, valor, ramas):
        if not ramas:
            return []
        return ([[valor] + ramas[0]] + self.agregar_raiz(valor, ramas[1:]))
    def agregar_raiz_cola(self, valor, ramas, resultado = None):
        if resultado is None:
            resultado = []
        if not ramas:
            return resultado
        resultado.append([valor] + ramas[0])
        return self.agregar_raiz_cola(valor, ramas[1:], resultado)
    def ramas(self):
        return self._ramas(self.raiz)
    def _ramas(self, nodo_actual):
        if nodo_actual is None:
            return []
        if (nodo_actual.izquierdo is None and nodo_actual.derecho is None):
            return [[nodo_actual.valor]]
        return (self.agregar_raiz(nodo_actual.valor, self._ramas(nodo_actual.izquierdo)) + \
                self.agregar_raiz(nodo_actual.valor, self._ramas(nodo_actual.derecho)))
    #9)
    def es_balanceado(self):
        return self._es_balanceado(self.raiz)
    def _es_balanceado(self, nodo_actual):
        if nodo_actual is None:
            return True
        altura_izq = self._altura(nodo_actual.izquierdo)
        altura_der = self._altura(nodo_actual.derecho)
        if abs(altura_izq - altura_der) > 1:
            return False
        return (self._es_balanceado(nodo_actual.izquierdo) and \
        self._es_balanceado(nodo_actual.derecho))
    #10)
    def espejo(self):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._espejo(self.raiz)
        return nuevo_arbol
    def _espejo(self, nodo_actual):
        if nodo_actual is None:
            return None
        nuevo = Nodo(nodo_actual.valor)
        nuevo.izquierdo = self._espejo(nodo_actual.derecho)
        nuevo.derecho = self._espejo(nodo_actual.izquierdo)
        return nuevo
    #12)
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._inorden(nodo_actual.izquierdo) + \
            [nodo_actual.valor] + \
            self._inorden(nodo_actual.derecho)
    def inorden_cola(self):
        return self._inorden_cola(self.raiz)
    def _inorden_cola(self):
        resultado = []
        pila = []
        actual = self.raiz
        while actual is not None or pila:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
        actual = pila.pop()
        resultado.append(actual.valor)
        actual = actual.derecho
        return resultado
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return [nodo_actual.valor] + \
            self._preorden(nodo_actual.izquierdo) + \
            self._preorden(nodo_actual.derecho)
    def preorden_cola(self):
        return self._preorden_cola(self.raiz)
    def _preorden_cola(self):
        if self.raiz is None:
            return []
        pila = [self.raiz]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.derecho is not None:
                pila.append(actual.derecho)
            if actual.izquierdo is not None:
                pila.append(actual.izquierdo)
        return resultado
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._postorden(nodo_actual.izquierdo) + \
            self._postorden(nodo_actual.derecho) + \
            [nodo_actual.valor]
    def postorden_cola(self):
        return self._postorden_cola(self.raiz)
    def _postorden_cola(self):
        if self.raiz is None:
            return []
        pila = [self.raiz]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.izquierdo is not None:
                pila.append(actual.izquierdo)
            if actual.derecho is not None:
                pila.append(actual.derecho)
        return resultado[::-1]
    #13)
    def bfs(self):
        if self.raiz is None:
            return []
        cola = [self.raiz]
        recorrido = []
        while cola:
            actual = cola.pop(0)
            recorrido.append(actual.valor)
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return recorrido
    #14)
    #Versión que NO admite repetidos:
    def insertar2(self, elemento):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._insertar2(self.raiz, elemento)
        return nuevo_arbol
    def _insertar2(self, nodo_actual, elemento):
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar2(nodo_actual.izquierdo, elemento)
        elif elemento > nodo_actual.valor:
            nodo_actual.derecho = self._insertar2(nodo_actual.derecho, elemento)
        return nodo_actual
    #Versión que admite repetidos:
    def insertar3(self, elemento):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._insertar3(self.raiz, elemento)
        return nuevo_arbol
    def _insertar3(self, nodo_actual, elemento):
        if nodo_actual is None:
            return Nodo(elemento)
        if elemento < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar3(nodo_actual.izquierdo, elemento)
        else: 
            nodo_actual.derecho = self._insertar3(nodo_actual.derecho, elemento)
        return nodo_actual
    #15)
    #Versión de copia:
    def eliminar2(self, valor_a_eliminar):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._eliminar2(self.raiz, valor_a_eliminar)
        return nuevo_arbol
    def _eliminar2(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar2(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar2(nodo_actual.derecho, valor_a_eliminar)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            sucesor = self.minimo(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar2(nodo_actual.derecho, sucesor.valor)
        return nodo_actual
    #Versión de fusión:
    def eliminar3(self, valor):
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._eliminar3(self.raiz, valor)
        return nuevo_arbol
    def _eliminar3(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar3(nodo_actual.izquierdo,valor_a_eliminar)
            return nodo_actual
        if valor_a_eliminar > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar3(nodo_actual.derecho, valor_a_eliminar)
            return nodo_actual
        if nodo_actual.izquierdo is None:
            return nodo_actual.derecho
        if nodo_actual.derecho is None:
            return nodo_actual.izquierdo
        maximo_izq = self._encontrar_maximo_nodo(nodo_actual.izquierdo)
        maximo_izq.derecho = nodo_actual.derecho
        return nodo_actual.izquierdo
    #17)
    def mostrar(self):
        return self._mostrar(self.raiz, 0)
    def _mostrar(self, nodo_actual, nivel):
        if nodo_actual is None:
            return None
        print(' '*nivel + str(nodo_actual.valor))
        izquierda = self._mostrar(nodo_actual.izquierdo, nivel + 1)
        if izquierda != None:
            return izquierda
        return self._mostrar(nodo_actual.derecho, nivel + 1)
    #18)
    def hermano(self, nodo):
        return self._hermano(self.raiz, nodo)
    def _hermano(self, nodo_actual, nodo):
        if nodo_actual is None:
            return None
        if nodo_actual.izquierdo is not None and nodo_actual.izquierdo.valor == nodo.valor:
            if nodo_actual.derecho is None:
                return None
            return nodo_actual.derecho.valor
        if nodo_actual.derecho is not None and nodo_actual.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo is None:
                return None
            return nodo_actual.izquierdo.valor
        izquierda = self._hermano(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._hermano(nodo_actual.derecho, nodo)
    #19)
    def primos(self, nodo):
        return self._primos(self.raiz, nodo)
    def _primos(self, nodo_actual, nodo):
        if nodo_actual is None:
            return None
        if nodo_actual.izquierdo.izquierdo is not None \
            and nodo_actual.izquierdo.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.izquierdo.derecho is not None \
            and nodo_actual.izquierdo.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo.valor] + \
                [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.izquierdo is not None \
            and nodo_actual.derecho.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.derecho is not None \
            and nodo_actual.derecho.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.derecho.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.izquierdo.valor] + \
                       [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is None:
                return [nodo_actual.izquierdo.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] + \
                [nodo_actual.derecho.izquierdo.valor]
        
        izquierda = self._primos(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._primos(nodo_actual.derecho, nodo)
    #20)
    def ancestro_comun(self, nodo1, nodo2):
        return self._ancestro_comun(self.raiz, nodo1, nodo2)
    def _ancestro_comun(self, nodo_actual, nodo1, nodo2):
        if nodo_actual is None:
            return None
        if nodo_actual.valor in self.antecesores(nodo1.valor) and \
            nodo_actual.valor in self.antecesores(nodo2.valor) and \
             nodo_actual.izquierdo.valor not in self.antecesores(nodo1.valor) and \
              nodo_actual.izquierdo.valor not in self.antecesores(nodo2.valor) and \
               nodo_actual.derecho.valor not in self.antecesores(nodo1.valor) and \
                nodo_actual.derecho.valor not in self.antecesores(nodo2.valor):
            return nodo_actual.valor
        izquierda = self._ancestro_comun(nodo_actual.izquierdo, nodo1, nodo2)
        if izquierda != None:
            return izquierda
        return self._ancestro_comun(nodo_actual.derecho, nodo1, nodo2)
    #21)
    def insertarOrdenado(self, elemento):
        if self.raiz is None:
            self.insertar(elemento)
            return
        if elemento <= self.maximo():
            raise ValueError("El elemento rompe el orden")
        self.insertar(elemento)
        return self
    #22)
    def eliminarOrdenado(self, elemento):
        if elemento != self.maximo():
            raise ValueError('El elemento rompe el orden')
        self.eliminar(elemento)
        return self
    def __str__(self):
        return f"Preorden: {str(self.preorden())}, Postorden: {str(self.postorden())}, Inorden: {str(self.inorden())}"

arbol_genericos1 = arbol_binario_genericos()
arbol_genericos1.insertar("Franco")
arbol_genericos1.insertar("Diego")
arbol_genericos1.insertar("Carlos")
arbol_genericos1.insertar("Esteban")
arbol_genericos1.insertar("Humberto")
arbol_genericos1.insertar("Gaston")

print('Arbol 1')
print(arbol_genericos1)

arbol_genericos2 = arbol_binario_genericos()
arbol_genericos2.insertar("Franco")
arbol_genericos2.insertar("Diego")
arbol_genericos2.insertar("Carlos")
arbol_genericos2.insertar("Esteban")
arbol_genericos2.insertar("Humberto")
arbol_genericos2.insertar("Gaston")

print('Arbol 2')
print(arbol_genericos2)

print('Cantidad de nodos del arbol')
print(arbol_genericos1.cantidad_nodos())

print('Altura del arbol')
print(arbol_genericos1.altura())

print('¿Son iguales arbol 1 y arbol 2?')
print(arbol_genericos1.igualdad(arbol_genericos2))

print('Recorrido guiado:')
print(arbol_genericos1.recorrido_guiado(['derecha', 'izquierda']))

dato = 'a'
print(f"¿Pertenece {dato} a la lista?")
print(arbol_genericos1.pertenece(dato))

dato = 'Esteban'
print(f"Nivel de {dato}: ")
print(arbol_genericos1.nivel(dato))

dato = 'Gaston'
print(f"Padre de {dato}: ")
print(arbol_genericos1.padre(dato))

dato = 'Franco'
print(f"Hijos de {dato}: ")
print(arbol_genericos1.hijos(dato))

dato = 'Carlos'
print(f"Antecesores de {dato}: ")
print(arbol_genericos1.antecesores(dato))

print('Arbol sin hojas: ')
print(arbol_genericos1.sin_hojas())

print('Ramas del arbol: ')
print(arbol_genericos1.ramas())

print('¿Es balanceado el arbol?')
print(arbol_genericos1.es_balanceado())

print('Espejo del arbol')
print(arbol_genericos1.espejo())

dato = 'Alvaro'
print(f"Arbol con {dato}: ")
print(arbol_genericos2.insertar2(dato))

dato = 'Humberto'
print(f"Arbol sin {dato}: ")
print(arbol_genericos2.eliminar2(dato))

print("Imprimir elementos del arbol 1 con indentación correspondiente al nivel: ")
arbol_genericos1.mostrar()

nodo = Nodo('Diego')
print(f"Hermano de {nodo.valor}: ")
print(arbol_genericos1.hermano(nodo))

nodo = Nodo('Gaston')
print(f"Primos de {nodo.valor}: ")
print(arbol_genericos1.primos(nodo))

nodo1 = Nodo('Carlos')
nodo2 = Nodo('Esteban')
print(f"Primer ancestro comun entre {nodo1.valor} y {nodo2.valor}: ")
print(arbol_genericos1.ancestro_comun(nodo1, nodo2))

dato = 'Ignacio'
print(f"Arbol con {dato}")
print(arbol_genericos2.insertarOrdenado(dato))

print("Imprimir elementos del arbol 2 con indentación correspondiente al nivel: ")
arbol_genericos2.mostrar()
dato = 'Ignacio'
print(f"Arbol sin {dato}")
print(arbol_genericos2.eliminarOrdenado(dato))

#16)
class ABBArreglo:
    def __init__(self, capacidad):
        self.valores = [None] * capacidad
        self.izq = [-1] * capacidad
        self.der = [-1] * capacidad
        self.raiz = -1
        self.libre = 0
    def insertar(self, elemento):
        if self.raiz == -1:
            self.raiz = 0
            self.valores[0] = elemento
            self.libre = 1
            return
        self._insertar(self.raiz, elemento)
    def _insertar(self, actual, elemento):
        if elemento < self.valores[actual]:
            if self.izq[actual] == -1:
                nuevo = self.libre
                self.valores[nuevo] = elemento
                self.izq[actual] = nuevo
                self.libre += 1
                return
            return self._insertar(self.izq[actual], elemento)
        else:
            if self.der[actual] == -1:
                nuevo = self.libre
                self.valores[nuevo] = elemento
                self.der[actual] = nuevo
                self.libre += 1
                return
            return self._insertar(self.der[actual],elemento)
    def eliminar(self, elemento):
        self._eliminar(self.raiz, elemento)
    def _eliminar(self, actual, elemento):
        if elemento < self.valores[actual]:
            if self.izq[actual] != -1:
                nuevo = self.libre
                self.valores[nuevo] = None
                self.izq[actual] = -1
                self.libre -= 1
                return
            return self._eliminar(self.izq[actual], elemento)
        if elemento > self.valores[actual]:
            if self.der[actual] != -1:
                nuevo = self.libre
                self.valores[nuevo] = None
                self.der[actual] = -1
                self.libre -= 1
                return
            return self._eliminar(self.izq[actual], elemento)
            
    def __str__(self):
        return (f"valores={self.valores}\n"f"izq={self.izq}\n"f"der={self.der}\n"f"raiz={self.raiz}")
        
arbol = ABBArreglo(10)

arbol.insertar(6)
print(arbol)

arbol.insertar(4)
print(arbol)

arbol.insertar(8)
print(arbol)

arbol.insertar(3)
print(arbol)
        
class Nodo:

    def __init__(self, valor):

        self.valor = valor

        self.izquierdo = None
        self.derecho = None

        self.siguiente = None