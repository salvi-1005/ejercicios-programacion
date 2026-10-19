from collections import deque

class Nodo:
    def __init__(self, valor: int, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
        
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
    def cantidad_hojas(self):
        return self._cantidad_hojas(self.raiz)
    def _cantidad_hojas(self, nodo_actual):
        if nodo_actual is None:
            return 0
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return 1 + self._cantidad_hojas(nodo_actual.izquierdo) + \
                self._cantidad_hojas(nodo_actual.derecho)
        return self._cantidad_hojas(nodo_actual.izquierdo) + \
            self._cantidad_hojas(nodo_actual.derecho)
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
    def camino_raiz_hoja(self, elemento):
        return self._camino_raiz_hoja(self.raiz, elemento)
    def _camino_raiz_hoja(self, nodo, elemento):
        if nodo is None:
            return []
        if nodo.valor == elemento:
            return [nodo.valor]
        camino_izq = self._camino_raiz_hoja(nodo.izquierdo, elemento)
        if camino_izq:
            return [nodo.valor] + camino_izq
        camino_der = self._camino_raiz_hoja(nodo.derecho, elemento)
        if camino_der:
            return [nodo.valor] + camino_der
        return []
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
    def descendientes(self, elemento):
        return self._descendientes(self.raiz, elemento)
    def _descendientes(self, nodo_actual, elemento, llegue_al_elemento=False):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            llegue_al_elemento=True
        if llegue_al_elemento:
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                return []
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is not None):
                return [nodo_actual.izquierdo.valor] + [nodo_actual.derecho.valor] + \
                self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento) + \
                    self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is None):
                return [nodo_actual.izquierdo.valor] + \
                self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento)
            if (nodo_actual.izquierdo is None and nodo_actual.derecho is not None):
                return [nodo_actual.derecho.valor] + \
                self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
        izquierda = self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento)
        if izquierda != None:
            return izquierda
        return self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
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
    def predecesor(self, elemento):
        return self._predecesor(self.raiz, elemento)
    def _predecesor(self, nodo_actual, elemento, lista_ordenada=None):
        if lista_ordenada is None:
            lista_ordenada = self.inorden()
        indice = lista_ordenada.index(elemento)
        if indice == 0:
            return -1
        return lista_ordenada[indice-1]
    def sucesor(self, elemento):
        return self._sucesor(self.raiz, elemento)
    def _sucesor(self, nodo_actual, elemento, lista_ordenada=None):
        if lista_ordenada is None:
            lista_ordenada = self.inorden()
        indice = lista_ordenada.index(elemento)
        if indice == len(lista_ordenada) - 1:
            return -1
        return lista_ordenada[indice+1]
    def predecesor2(self, elemento):
        return self._predecesor2(self.raiz, elemento)
    def _predecesor2(self, nodo_actual, elemento, encontrado=False):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            encontrado = True
        if encontrado:
            return self._maximo(nodo_actual.izquierdo)
        izquierda = self._predecesor2(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._predecesor2(nodo_actual.derecho, elemento, encontrado)
    def sucesor2(self, elemento):
        return self._sucesor2(self.raiz, elemento)
    def _sucesor2(self, nodo_actual, elemento, encontrado=None):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            encontrado = True
        if encontrado:
            return self._minimo(nodo_actual.derecho)
        izquierda = self._predecesor2(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._predecesor2(nodo_actual.derecho, elemento, encontrado)
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
    def insertar4(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
                return
            cola.append(actual.izquierdo)
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
                return
            cola.append(actual.derecho)
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
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [] 
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
            return [nodo_actual.derecho.izquierdo.valor] + \
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
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [] 
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
            return [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.izquierdo is not None \
            and nodo_actual.derecho.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
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
                return []
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] 
                    
        if nodo_actual.derecho.derecho is not None \
            and nodo_actual.derecho.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
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
                return []
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] 
        
        izquierda = self._primos(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._primos(nodo_actual.derecho, nodo)
    def _buscar_familia(self, actual, padre, abuelo, buscado):
        if actual is None:
            return None
        if actual.valor == buscado.valor:
            return (abuelo, padre)
        return (self._buscar_familia(actual.izquierdo, actual, padre, buscado)
        or self._buscar_familia(actual.derecho, actual, padre, buscado))
    def primos2(self, nodo):
        familia = self._buscar_familia(self.raiz, None, None, nodo)
        if familia is None:
            return []
        abuelo, padre = familia
        if abuelo is None:
            return []
        if abuelo.izquierdo is padre:
            tio = abuelo.derecho
        else:
            tio = abuelo.izquierdo
        if tio is None:
            return []
        lista_primos = []
        if tio.izquierdo is not None:
            lista_primos.append(tio.izquierdo.valor)
        if tio.derecho is not None:
            lista_primos.append(tio.derecho.valor)
        return lista_primos
    def _buscar_familia2(self, actual, padre, abuelo, buscado):
        if actual is None:
            return None
        if actual is buscado:
            return (abuelo, padre)
        return (self._buscar_familia(actual.izquierdo, actual, padre, buscado)
        or self._buscar_familia(actual.derecho, actual, padre, buscado))
    def primos3(self, nodo):
        familia = self._buscar_familia2(self.raiz, None, None, nodo)
        if familia is None:
            return []
        abuelo, padre = familia
        if abuelo is None:
            return []
        if abuelo.izquierdo is padre:
            tio = abuelo.derecho
        else:
            tio = abuelo.izquierdo
        if tio is None:
            return []
        lista_primos = []
        if tio.izquierdo is not None:
            lista_primos.append(tio.izquierdo.valor)
        if tio.derecho is not None:
            lista_primos.append(tio.derecho.valor)
        return lista_primos
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
        return f"Preorden: {str(self.preorden_cola())}, Postorden: {str(self.postorden_cola())}, Inorden: {str(self.inorden_cola())}"
    #24)
    def destruir(self):
        self.raiz = None
    def valores_menor_a(self, elemento):
        return self._valores_menor_a(self.raiz, elemento)
    def _valores_menor_a(self, nodo_actual, elemento):
        if nodo_actual is None:
            return []
        if nodo_actual.valor < elemento:
            return [nodo_actual.valor] + self._valores_menor_a(nodo_actual.izquierdo, elemento) + \
                self._valores_menor_a(nodo_actual.derecho, elemento)
        return self._valores_menor_a(nodo_actual.izquierdo, elemento) + \
            self._valores_menor_a(nodo_actual.derecho, elemento)
    def recorrer_mayor_a_menor(self):
        return self._recorrer_mayor_a_menor(self.raiz)
    def _recorrer_mayor_a_menor(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._recorrer_mayor_a_menor(nodo_actual.derecho) + \
            [nodo_actual.valor] + \
            self._recorrer_mayor_a_menor(nodo_actual.izquierdo)
    def convertir_ordenado(self):
        valores = self.preorden()
        valores = self.merge_sort(valores)
        nuevo_arbol = arbol_binario_enteros()
        self._insertar_todos(nuevo_arbol, valores)
        return nuevo_arbol
    def _insertar_todos(self, arbol, lista,i=0):
        if i >= len(lista):
            return
        arbol.insertar(lista[i])
        self._insertar_todos(arbol, lista, i+1)
    def valores(self):
        return self._valores(self.raiz)
    def _valores(self, nodo):
        if nodo is None:
            return []
        return ([nodo.valor] + self._valores(nodo.izquierdo) + self._valores(nodo.derecho))
    def merge_sort(self, lista):
        if len(lista) > 1:
            mitad = len(lista) // 2
            izquierda = lista[:mitad]
            derecha = lista[mitad:]
            self.merge_sort(izquierda)
            self.merge_sort(derecha)
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
        return lista
    def construir_abb_balanceado(self, lista=None):
        if lista is None:
            lista = self.preorden()
            lista = self.merge_sort(lista)
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._construir_abb_balanceado(lista)
        return nuevo_arbol
    def _construir_abb_balanceado(self, lista):
        if not lista:
            return None
        medio = len(lista) // 2
        raiz = Nodo(lista[medio])
        raiz.izquierdo = self._construir_abb_balanceado(lista[:medio])
        raiz.derecho = self._construir_abb_balanceado(lista[medio+1:])
        return raiz
    def busqueda(self, elemento):
        return self._busqueda(self.raiz, elemento)
    def _busqueda(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento:
            return True
        return self._busqueda(nodo_actual.izquierdo, elemento) \
            or self._busqueda(nodo_actual.derecho, elemento)
    def es_bst(self):
        return self._es_bst(self.raiz, None, None)
    def _es_bst(self, nodo, minimo, maximo):
        if nodo is None:
            return True
        if minimo is not None and nodo.valor <= minimo:
            return False
        if maximo is not None and nodo.valor >= maximo:
            return False
        return (self._es_bst(nodo.izquierdo, minimo, nodo.valor) \
            and self._es_bst(nodo.derecho, nodo.valor, maximo))
    
        
arbol_enteros1 = arbol_binario_enteros()
arbol_enteros1.insertar(6)
arbol_enteros1.insertar(4)
arbol_enteros1.insertar(3)
arbol_enteros1.insertar(5)
arbol_enteros1.insertar(8)
arbol_enteros1.insertar(7)

arbol_enteros3 = arbol_binario_enteros()
arbol_enteros3.insertar4(8)
arbol_enteros3.insertar4(5)
arbol_enteros3.insertar4(7)
arbol_enteros3.insertar4(3)
arbol_enteros3.insertar4(6)
arbol_enteros3.insertar4(4)

a = Nodo(6, Nodo(15, Nodo(20), Nodo(1)), Nodo(3, Nodo(7), Nodo(2)))

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

print('Cantidad de hojas del arbol')
print(arbol_enteros1.cantidad_hojas())

print('Altura del arbol')
print(arbol_enteros1.altura())

print('¿Son iguales arbol 1 y arbol 2?')
print(arbol_enteros1.igualdad(arbol_enteros2))

print('Recorrido guiado:')
print(arbol_enteros1.recorrido_guiado(['derecha', 'izquierda']))

elemento = 3
print('Camino raiz-hoja:')
print(arbol_enteros1.camino_raiz_hoja(elemento))

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

dato = 6
print(f"descendientes del {dato}: ")
print(arbol_enteros1.descendientes(dato))

dato = 3
print(f"Antecesores del {dato}: ")
print(arbol_enteros1.antecesores(dato))

dato = 6
print(f"Predecesor del {dato}:")
print(arbol_enteros1.predecesor2(dato))

dato = 6
print(f"Sucesor del {dato}:")
print(arbol_enteros1.sucesor2(dato))

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
print(arbol_enteros1.primos2(nodo))

nodo = arbol_enteros1.raiz.derecho.izquierdo
print(f"Primos del {nodo.valor}: ")
print(arbol_enteros1.primos3(nodo))

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

elemento = 6
print(f"Valores menores a {elemento}: ")
print(arbol_enteros1.valores_menor_a(elemento))

print("Recorrido de mayor a menor: ")
print(arbol_enteros1.recorrer_mayor_a_menor())

print("Arbol ordenado: ")
print(arbol_enteros3.convertir_ordenado())

print("Arbol ordenado balanceado: ")
print(arbol_enteros3.construir_abb_balanceado())

elemento = 5
print(f"¿Está el {elemento} en el arbol 1? ")
print(arbol_enteros1.busqueda(elemento))

print("Recorrido BFS")
print(arbol_enteros1.bfs())

arbol_enteros2.destruir()
print('Arbol enteros destruido')
print(arbol_enteros2)

print('¿Es ABB?')
print(arbol_enteros1.es_bst())

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
    def cantidad_hojas(self):
        return self._cantidad_hojas(self.raiz)
    def _cantidad_hojas(self, nodo_actual):
        if nodo_actual is None:
            return 0
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return 1 + self._cantidad_hojas(nodo_actual.izquierdo) + \
                self._cantidad_hojas(nodo_actual.derecho)
        return self._cantidad_hojas(nodo_actual.izquierdo) + \
            self._cantidad_hojas(nodo_actual.derecho)
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
    def camino_raiz_hoja(self, elemento):
        return self._camino_raiz_hoja(self.raiz, elemento)
    def _camino_raiz_hoja(self, nodo, elemento):
        if nodo is None:
            return []
        if nodo.valor == elemento:
            return [nodo.valor]
        camino_izq = self._camino_raiz_hoja(nodo.izquierdo, elemento)
        if camino_izq:
            return [nodo.valor] + camino_izq
        camino_der = self._camino_raiz_hoja(nodo.derecho, elemento)
        if camino_der:
            return [nodo.valor] + camino_der
        return []  
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
    def descendientes(self, elemento):
        return self._descendientes(self.raiz, elemento)
    def _descendientes(self, nodo_actual, elemento, llegue_al_elemento=False):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            llegue_al_elemento=True
        if llegue_al_elemento:
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                return []
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is not None):
                return [nodo_actual.izquierdo.valor] + [nodo_actual.derecho.valor] + \
                self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento) + \
                    self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is None):
                return [nodo_actual.izquierdo.valor] + \
                self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento)
            if (nodo_actual.izquierdo is None and nodo_actual.derecho is not None):
                return [nodo_actual.derecho.valor] + \
                self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
        izquierda = self._descendientes(nodo_actual.izquierdo, elemento, llegue_al_elemento)
        if izquierda != None:
            return izquierda
        return self._descendientes(nodo_actual.derecho, elemento, llegue_al_elemento)
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
    def predecesor(self, elemento):
        return self._predecesor(self.raiz, elemento)
    def _predecesor(self, nodo_actual, elemento, lista_ordenada=None):
        if lista_ordenada is None:
            lista_ordenada = self.inorden()
        indice = lista_ordenada.index(elemento)
        if indice == 0:
            return -1
        return lista_ordenada[indice-1]
    def sucesor(self, elemento):
        return self._sucesor(self.raiz, elemento)
    def _sucesor(self, nodo_actual, elemento, lista_ordenada=None):
        if lista_ordenada is None:
            lista_ordenada = self.inorden()
        indice = lista_ordenada.index(elemento)
        if indice == len(lista_ordenada) - 1:
            return -1
        return lista_ordenada[indice+1]
    def predecesor2(self, elemento):
        return self._predecesor2(self.raiz, elemento)
    def _predecesor2(self, nodo_actual, elemento, encontrado=False):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            encontrado = True
        if encontrado:
            return self._maximo(nodo_actual.izquierdo)
        izquierda = self._predecesor2(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._predecesor2(nodo_actual.derecho, elemento, encontrado)
    def sucesor2(self, elemento):
        return self._sucesor2(self.raiz, elemento)
    def _sucesor2(self, nodo_actual, elemento, encontrado=None):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == elemento:
            encontrado = True
        if encontrado:
            return self._minimo(nodo_actual.derecho)
        izquierda = self._predecesor2(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._predecesor2(nodo_actual.derecho, elemento, encontrado)
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
    def insertar4(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
                return
            cola.append(actual.izquierdo)
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
                return
            cola.append(actual.derecho)
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
        nuevo_arbol = arbol_binario_genericos()
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
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.derecho is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [] 
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
            return [nodo_actual.derecho.izquierdo.valor] + \
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
                return [nodo_actual.derecho.derecho.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is not None and \
                    nodo_actual.derecho.derecho is None:
                return [nodo_actual.derecho.izquierdo.valor]
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.derecho.izquierdo is None and \
                    nodo_actual.derecho.derecho is None:
                return [] 
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
            return [nodo_actual.derecho.izquierdo.valor] + \
                    [nodo_actual.derecho.derecho.valor]
                    
        if nodo_actual.derecho.izquierdo is not None \
            and nodo_actual.derecho.izquierdo.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
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
                return []
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.derecho is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] 
                    
        if nodo_actual.derecho.derecho is not None \
            and nodo_actual.derecho.derecho.valor == nodo.valor:
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is not None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.derecho.valor] 
            if nodo_actual.izquierdo.izquierdo is not None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is not None:
                return [nodo_actual.izquierdo.izquierdo.valor] 
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
                return []
            if nodo_actual.izquierdo.izquierdo is None and \
                nodo_actual.izquierdo.derecho is None and \
                    nodo_actual.derecho.izquierdo is None:
                return None
            return [nodo_actual.izquierdo.izquierdo] + \
                 [nodo_actual.izquierdo.derecho.valor] 
        
        izquierda = self._primos(nodo_actual.izquierdo, nodo)
        if izquierda != None:
            return izquierda
        return self._primos(nodo_actual.derecho, nodo)
    def _buscar_familia(self, actual, padre, abuelo, buscado):
        if actual is None:
            return None
        if actual.valor == buscado.valor:
            return (abuelo, padre)
        return (self._buscar_familia(actual.izquierdo, actual, padre, buscado)
        or self._buscar_familia(actual.derecho, actual, padre, buscado))
    def primos2(self, nodo):
        familia = self._buscar_familia(self.raiz, None, None, nodo)
        if familia is None:
            return []
        abuelo, padre = familia
        if abuelo is None:
            return []
        if abuelo.izquierdo is padre:
            tio = abuelo.derecho
        else:
            tio = abuelo.izquierdo
        if tio is None:
            return []
        lista_primos = []
        if tio.izquierdo is not None:
            lista_primos.append(tio.izquierdo.valor)
        if tio.derecho is not None:
            lista_primos.append(tio.derecho.valor)
        return lista_primos
    def _buscar_familia2(self, actual, padre, abuelo, buscado):
        if actual is None:
            return None
        if actual is buscado:
            return (abuelo, padre)
        return (self._buscar_familia(actual.izquierdo, actual, padre, buscado)
        or self._buscar_familia(actual.derecho, actual, padre, buscado))
    def primos3(self, nodo):
        familia = self._buscar_familia2(self.raiz, None, None, nodo)
        if familia is None:
            return []
        abuelo, padre = familia
        if abuelo is None:
            return []
        if abuelo.izquierdo is padre:
            tio = abuelo.derecho
        else:
            tio = abuelo.izquierdo
        if tio is None:
            return []
        lista_primos = []
        if tio.izquierdo is not None:
            lista_primos.append(tio.izquierdo.valor)
        if tio.derecho is not None:
            lista_primos.append(tio.derecho.valor)
        return lista_primos
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
    #24)
    def destruir(self):
        self.raiz = None
    def valores_menor_a(self, elemento):
        return self._valores_menor_a(self.raiz, elemento)
    def _valores_menor_a(self, nodo_actual, elemento):
        if nodo_actual is None:
            return []
        if nodo_actual.valor < elemento:
            return [nodo_actual.valor] + self._valores_menor_a(nodo_actual.izquierdo, elemento) + \
                self._valores_menor_a(nodo_actual.derecho, elemento)
        return self._valores_menor_a(nodo_actual.izquierdo, elemento) + \
            self._valores_menor_a(nodo_actual.derecho, elemento)
    def recorrer_mayor_a_menor(self):
        return self._recorrer_mayor_a_menor(self.raiz)
    def _recorrer_mayor_a_menor(self, nodo_actual):
        if nodo_actual is None:
            return []
        return self._recorrer_mayor_a_menor(nodo_actual.derecho) + \
            [nodo_actual.valor] + \
            self._recorrer_mayor_a_menor(nodo_actual.izquierdo)
    def convertir_ordenado(self):
        valores = self.preorden()
        valores = self.merge_sort(valores)
        nuevo_arbol = arbol_binario_genericos()
        self._insertar_todos(nuevo_arbol, valores)
        return nuevo_arbol
    def _insertar_todos(self, arbol, lista,i=0):
        if i >= len(lista):
            return
        arbol.insertar(lista[i])
        self._insertar_todos(arbol, lista, i+1)
    def valores(self):
        return self._valores(self.raiz)
    def _valores(self, nodo):
        if nodo is None:
            return []
        return ([nodo.valor] + self._valores(nodo.izquierdo) + self._valores(nodo.derecho))
    def merge_sort(self, lista):
        if len(lista) > 1:
            mitad = len(lista) // 2
            izquierda = lista[:mitad]
            derecha = lista[mitad:]
            self.merge_sort(izquierda)
            self.merge_sort(derecha)
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
        return lista
    def construir_abb_balanceado(self, lista=None):
        if lista is None:
            lista = self.preorden()
            lista = self.merge_sort(lista)
        nuevo_arbol = arbol_binario_enteros()
        nuevo_arbol.raiz = self._construir_abb_balanceado(lista)
        return nuevo_arbol
    def _construir_abb_balanceado(self, lista):
        if not lista:
            return None
        medio = len(lista) // 2
        raiz = Nodo(lista[medio])
        raiz.izquierdo = self._construir_abb_balanceado(lista[:medio])
        raiz.derecho = self._construir_abb_balanceado(lista[medio+1:])
    def busqueda(self, elemento):
        return self._busqueda(self.raiz, elemento)
    def _busqueda(self, nodo_actual, elemento):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == elemento:
            return True
        return self._busqueda(nodo_actual.izquierdo, elemento) \
            or self._busqueda(nodo_actual.derecho, elemento)
    def es_bst(self):
        return self._es_bst(self.raiz, None, None)
    def _es_bst(self, nodo, minimo, maximo):
        if nodo is None:
            return True
        if minimo is not None and nodo.valor <= minimo:
            return False
        if maximo is not None and nodo.valor >= maximo:
            return False
        return (self._es_bst(nodo.izquierdo, minimo, nodo.valor) \
            and self._es_bst(nodo.derecho, nodo.valor, maximo))
        

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

print('Cantidad de hojas del arbol')
print(arbol_genericos1.cantidad_hojas())

print('Altura del arbol')
print(arbol_genericos1.altura())

print('¿Son iguales arbol 1 y arbol 2?')
print(arbol_genericos1.igualdad(arbol_genericos2))

print('Recorrido guiado:')
print(arbol_genericos1.recorrido_guiado(['derecha', 'izquierda']))

elemento = "Carlos"
print('Camino raiz-hoja:')
print(arbol_genericos1.camino_raiz_hoja(elemento))

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

dato = 'Franco'
print(f"descendientes del {dato}: ")
print(arbol_genericos1.descendientes(dato))

dato = 'Carlos'
print(f"Antecesores de {dato}: ")
print(arbol_genericos1.antecesores(dato))

dato = 'Franco'
print(f"Predecesor del {dato}:")
print(arbol_genericos1.predecesor2(dato))

dato = 'Franco'
print(f"Sucesor del {dato}:")
print(arbol_genericos1.sucesor2(dato))

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
print(arbol_genericos1.primos2(nodo))

nodo = arbol_genericos1.raiz.derecho.izquierdo
print(f"Primos de {nodo.valor}: ")
print(arbol_genericos1.primos3(nodo))

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

elemento = 'Franco'
print(f"Valores menores a {elemento}: ")
print(arbol_genericos1.valores_menor_a(elemento))

print("Recorrido de mayor a menor: ")
print(arbol_genericos1.recorrer_mayor_a_menor())

print("Arbol ordenado: ")
print(arbol_genericos2.convertir_ordenado())

print("Arbol ordenado balanceado: ")
print(arbol_genericos2.construir_abb_balanceado())

elemento = 'Esteban'
print(f"¿Está el {elemento} en el arbol 1? ")
print(arbol_genericos1.busqueda(elemento))

print("Recorrido BFS")
print(arbol_genericos1.bfs())

arbol_genericos2.destruir()
print('Arbol genericos destruido')
print(arbol_genericos2)

print('¿Es ABB?')
print(arbol_genericos1.es_bst())

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
    def destruir(self):
        self.raiz = -1    
    
arbol = ABBArreglo(10)

arbol.insertar(6)
print(arbol)

arbol.insertar(4)
print(arbol)

arbol.insertar(8)
print(arbol)

arbol.insertar(3)
print(arbol)

arbol.destruir()
print(arbol)
        
class Nodo:

    def __init__(self, valor):

        self.valor = valor

        self.izquierdo = None
        self.derecho = None

        self.siguiente = None
        
class arbol_binario_enteros:
    def __init__(self):
        self.raiz = None
    def conectar_inorden(self):
        anterior = [None]
        self._conectar_inorden(self.raiz, anterior)
    def _conectar_inorden(self, nodo_actual, anterior):
        if nodo_actual is None:
            return
        self._conectar_inorden(nodo_actual.izquierdo, anterior)
        if anterior[0] is not None:
            anterior[0].siguiente = nodo_actual
        anterior[0] = nodo_actual
        self._conectar_inorden(nodo_actual.derecho, anterior)
        
#23)

from typing import Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")

class Hoja(Generic[B]):
    def __init__(self, valor: B):
        self.valor = valor
        
class NodoInterno(Generic[A, B]):
    def __init__(self, valor: A, izquierdo, derecho):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
    
class ArbolBinarioHojas(Generic[A,B]):
    def __init__(self, raiz):
        self.raiz = raiz
    def insertar_hoja(self, nodo, valor_interno, valor_hoja):
        if isinstance(nodo, Hoja):
            return NodoInterno(valor_interno, Hoja(nodo.valor), Hoja(valor_hoja))
        return NodoInterno(nodo.valor, self.insertar_hoja(nodo.izquierdo, \
            valor_interno,valor_hoja),nodo.derecho)
    @staticmethod
    def insertar_interno(nodo, hoja_objetivo, valor_interno, nueva_hoja):
        if isinstance(nodo, Hoja):
            if nodo.valor == hoja_objetivo:
                return NodoInterno(valor_interno, Hoja(hoja_objetivo), Hoja(nueva_hoja))
            return nodo
        return NodoInterno(nodo.valor,
        ArbolBinarioHojas.insertar_interno(nodo.izquierdo, hoja_objetivo, \
            valor_interno, nueva_hoja), \
        ArbolBinarioHojas.insertar_interno(nodo.derecho, hoja_objetivo, \
            valor_interno, nueva_hoja))
    def eliminar_hoja(self, nodo, valor):
        if isinstance(nodo, Hoja):
            if nodo.valor == valor:
                raise ValueError("No se puede dejar árbol vacío")
            return nodo
    @staticmethod
    def eliminar_interno(nodo, valor):
        if isinstance(nodo, Hoja):
            return nodo
        if nodo.valor == valor:
            return nodo.derecho
        return NodoInterno(nodo.valor, \
        ArbolBinarioHojas.eliminar_interno(nodo.izquierdo, valor), \
        ArbolBinarioHojas.eliminar_interno(nodo.derecho, valor))
    def es_hoja(nodo):
        return isinstance(nodo, Hoja)
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo):
        if isinstance(nodo, Hoja):
            return 0
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))
    def cantidad_hojas(self):
        return self._cantidad_hojas(self.raiz)
    def _cantidad_hojas(self, nodo):
        if isinstance(nodo, Hoja):
            return 1
        return (self._cantidad_hojas(nodo.izquierdo) + \
            self._cantidad_hojas(nodo.derecho))
    def cantidad_internos(self):
        return self._cantidad_internos(self.raiz)
    def _cantidad_internos(self, nodo):
        if isinstance(nodo, Hoja):
            return 0
        return (1 + self._cantidad_internos(nodo.izquierdo) \
            + self._cantidad_internos(nodo.derecho))
    def cantidad_nodos(self):
        return self.cantidad_hojas() + self.cantidad_internos()
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return ([nodo.valor] + self._preorden(nodo.izquierdo) + \
            self._preorden(nodo.derecho))
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return (self._inorden(nodo.izquierdo) + [nodo.valor] + \
            self._inorden(nodo.derecho))
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return (self._postorden(nodo.izquierdo) + self._postorden(nodo.derecho) + \
            [nodo.valor])
    def igualdad(self, otro):
        return self._igualdad(self.raiz, otro.raiz)
    def _igualdad(self, n1, n2):
        if type(n1) != type(n2):
            return False
        if isinstance(n1, Hoja):
            return n1.valor == n2.valor
        return (n1.valor == n2.valor and self._igualdad(n1.izquierdo, n2.izquierdo) \
            and self._igualdad(n1.derecho, n2.derecho))
    def es_valido(self):
        return (self.cantidad_hojas() == self.cantidad_internos() + 1)
    @staticmethod
    def convertir(nodo):
        if nodo is None:
            raise ValueError("No se puede convertir")
        if (nodo.izquierdo is None and nodo.derecho is None):
            return Hoja(nodo.valor)
        if (nodo.izquierdo is None or nodo.derecho is None):
            raise ValueError("No se puede convertir")
        return NodoInterno(nodo.valor, ArbolBinarioHojas.convertir(nodo.izquierdo), \
            ArbolBinarioHojas.convertir(nodo.derecho))
    def calcular_resultado(self):
        return self._calcular_resultado(self.raiz)
    def _calcular_resultado(self, nodo_actual):
        if isinstance(nodo_actual, Hoja):
            return nodo_actual.valor
        if isinstance(nodo_actual, NodoInterno) and nodo_actual.izquierdo is not None and \
            nodo_actual.derecho is not None:
            if nodo_actual.valor == "+":
                return self._calcular_resultado(nodo_actual.izquierdo) + \
                    self._calcular_resultado(nodo_actual.derecho)
            if nodo_actual.valor == "-":
                return self._calcular_resultado(nodo_actual.izquierdo) - \
                    self._calcular_resultado(nodo_actual.derecho) 
            if nodo_actual.valor == "*":
                return self._calcular_resultado(nodo_actual.izquierdo) * \
                    self._calcular_resultado(nodo_actual.derecho) 
            if nodo_actual.valor == "/":
                return self._calcular_resultado(nodo_actual.izquierdo) / \
                    self._calcular_resultado(nodo_actual.derecho) 
            if nodo_actual.valor == "^":
                return self._calcular_resultado(nodo_actual.izquierdo) ** \
                    self._calcular_resultado(nodo_actual.derecho) 
    def espejo(self):
        nuevo_arbol = ArbolBinarioHojas(self.raiz)
        nuevo_arbol.raiz = self._espejo(self.raiz)
        return nuevo_arbol
    def _espejo(self, nodo_actual):
        if isinstance(nodo_actual, Hoja):
            return nodo_actual
        nuevo = Nodo(nodo_actual.valor)
        nuevo.izquierdo = self._espejo(nodo_actual.derecho)
        nuevo.derecho = self._espejo(nodo_actual.izquierdo)
        return nuevo
    def busqueda(self, elemento):
        return self._busqueda(self.raiz, elemento)
    def _busqueda(self, nodo_actual, elemento):
        if isinstance(nodo_actual, Hoja):
            if nodo_actual.valor == elemento:
                return True
            return False
        if nodo_actual.valor == elemento:
            return True
        return self._busqueda(nodo_actual.izquierdo, elemento) \
            or self._busqueda(nodo_actual.derecho, elemento)
    def destruir(self):
        self.raiz = None
    def __str__(self):
        return f"Preorden: {str(self.preorden())}, Postorden: {str(self.postorden())}, Inorden: {str(self.inorden())}"
            
from abc import ABC, abstractmethod
    
class Operador(ABC):
    simbolo: str  
    @staticmethod
    @abstractmethod  
    def operar(a, b):  
        pass

    def __str__(self) -> str:
        return self.simbolo  
    
class Suma(Operador):
    simbolo: str = '+' 
    @staticmethod
    def operar(a, b): 
        return a + b  
    
class Producto(Operador):
    simbolo: str = '*'  

    @staticmethod
    def operar(a, b):  
        return a * b  

class Resta(Operador):
    simbolo: str = '-' 
    @staticmethod
    def operar(a, b): 
        return a - b  
    
class Division(Operador):
    simbolo: str = '/'  

    @staticmethod
    def operar(a, b):  
        return a / b
    
class Potencia(Operador):
    simbolo: str = '^'  

    @staticmethod
    def operar(a, b):  
        return a ** b
    
class ExpresionAritmetica(ArbolBinarioHojas):

    def evaluar(self):
        return self._evaluar(self.raiz)

    def _evaluar(self, nodo):
        if isinstance(nodo, Hoja):
            return nodo.valor
        return nodo.valor.operar(self._evaluar(nodo.izquierdo), self._evaluar(nodo.derecho))
    
    def __str__(self) -> str:
        return super().__str__()


    
arbol1 = ArbolBinarioHojas(NodoInterno("+", Hoja(3), Hoja(5)))

arbol2 = ArbolBinarioHojas(NodoInterno("*", NodoInterno("+",Hoja(3),Hoja(5)),Hoja(8)))

arbol3 = ArbolBinarioHojas(NodoInterno("*", NodoInterno(
            "+", Hoja(1), Hoja(2)),NodoInterno(
            "-",Hoja(3),Hoja(4))))
                
arbol4 = ArbolBinarioHojas(NodoInterno("/", NodoInterno("*", NodoInterno(
                "+", Hoja(1), Hoja(2)),Hoja(3)),NodoInterno("-",Hoja(4),
            NodoInterno("^",Hoja(5),Hoja(6)))))
                                                  
print(f"Altura arbol 1: {arbol1.altura()}")
print(f"Altura arbol 2: {arbol2.altura()}")
print(f"Altura arbol 3: {arbol3.altura()}")
print(f"Altura arbol 4: {arbol4.altura()}")

print(f"Cantidad de hojas del arbol 1: {arbol1.cantidad_hojas()}")
print(f"Cantidad de hojas del arbol 2: {arbol2.cantidad_hojas()}")
print(f"Cantidad de hojas del arbol 3: {arbol3.cantidad_hojas()}")
print(f"Cantidad de hojas del arbol 4: {arbol4.cantidad_hojas()}")

print(f"Cantidad de nodos internos del arbol 1: {arbol1.cantidad_internos()}")
print(f"Cantidad de nodos internos del arbol 2: {arbol2.cantidad_internos()}")
print(f"Cantidad de nodos internos del arbol 3: {arbol3.cantidad_internos()}")
print(f"Cantidad de nodos internos del arbol 4: {arbol4.cantidad_internos()}")

print(f"Cantidad total de nodos del arbol 1: {arbol1.cantidad_nodos()}")
print(f"Cantidad total de nodos del arbol 2: {arbol2.cantidad_nodos()}")
print(f"Cantidad total de nodos del arbol 3: {arbol3.cantidad_nodos()}")
print(f"Cantidad total de nodos del arbol 4: {arbol4.cantidad_nodos()}")

print(f"Recorrido preorden arbol 1: {arbol1.preorden()}")
print(f"Recorrido preorden arbol 2: {arbol2.preorden()}")
print(f"Recorrido preorden arbol 3: {arbol3.preorden()}")
print(f"Recorrido preorden arbol 4: {arbol4.preorden()}")

print(f"Recorrido inorden arbol 1: {arbol1.inorden()}")
print(f"Recorrido inorden arbol 2: {arbol2.inorden()}")
print(f"Recorrido inorden arbol 3: {arbol3.inorden()}")
print(f"Recorrido inorden arbol 4: {arbol4.inorden()}")

print(f"Recorrido postorden arbol 1: {arbol1.postorden()}")
print(f"Recorrido postorden arbol 2: {arbol2.postorden()}")
print(f"Recorrido postorden arbol 3: {arbol3.postorden()}")
print(f"Recorrido postorden arbol 4: {arbol4.postorden()}")

arbol5 = ArbolBinarioHojas(NodoInterno("*", Hoja(3), Hoja(5)))
print(arbol1.igualdad(arbol5))
print(arbol2.igualdad(arbol5))

print(arbol_enteros1)

arbol_enteros1.insertar(9)
arbol_convertido = ArbolBinarioHojas(ArbolBinarioHojas.convertir(arbol_enteros1.raiz))

print(arbol_convertido.preorden())
print(arbol_convertido.inorden())
print(arbol_convertido.postorden())
print(arbol_convertido.altura())
print(arbol_convertido.cantidad_hojas())
print(arbol_convertido.cantidad_internos())
print(arbol_convertido.es_valido())
                                                            
#arbol4.destruir()
#print(arbol4.raiz)

arbol6 = ArbolBinarioHojas(NodoInterno("+", NodoInterno("*", Hoja(2), NodoInterno("/", Hoja(9),  
          NodoInterno("+", Hoja(2), Hoja(1)))), NodoInterno("-", Hoja(8), 
              NodoInterno("*", Hoja(3), Hoja(4)))))

exp1 = ExpresionAritmetica(NodoInterno(Suma(), Hoja(3), Hoja(5)))
exp2 = ExpresionAritmetica(NodoInterno(Producto(), NodoInterno(Suma(),Hoja(3),Hoja(5)),Hoja(8)))
exp3 = ExpresionAritmetica(NodoInterno(Producto(), NodoInterno(
            Suma(), Hoja(1), Hoja(2)),NodoInterno(
            Resta() ,Hoja(3),Hoja(4))))
exp4 = ExpresionAritmetica(NodoInterno(Division(), NodoInterno(Producto(), NodoInterno(
                Suma(), Hoja(1), Hoja(2)),Hoja(3)),NodoInterno(Resta(), Hoja(4),
            NodoInterno(Potencia(), Hoja(5), Hoja(6)))))
exp5 = ExpresionAritmetica(NodoInterno(Producto(), Hoja(3), Hoja(5)))  
exp6 = ExpresionAritmetica(NodoInterno(Suma(), NodoInterno(Producto(), Hoja(2), 
       NodoInterno(Division(), Hoja(9),  
          NodoInterno(Suma(), Hoja(2), Hoja(1)))), NodoInterno(Resta(), Hoja(8), 
              NodoInterno(Producto(), Hoja(3), Hoja(4)))))                                                         
                                                               
                                                               
print(f"Resultado del arbol 1: {arbol1.calcular_resultado()}")
print(f"Resultado del arbol 2: {arbol2.calcular_resultado()}")
print(f"Resultado del arbol 3: {arbol3.calcular_resultado()}")
print(f"Resultado del arbol 4: {arbol4.calcular_resultado()}")
print(f"Resultado del arbol 5: {arbol5.calcular_resultado()}")
print(f"Resultado del arbol 6: {arbol6.calcular_resultado()}")

print("Versión con herencia")

print(f"Resultado del arbol 1: {exp1.evaluar()}")
print(f"Resultado del arbol 2: {exp2.evaluar()}")
print(f"Resultado del arbol 3: {exp3.evaluar()}")
print(f"Resultado del arbol 4: {exp4.evaluar()}")
print(f"Resultado del arbol 5: {exp5.evaluar()}")
print(f"Resultado del arbol 6: {exp6.evaluar()}")

#Invertir un árbol
#Borrar
#Recorridos transversales (in, pre y post)
#Búsquedas
#Altura/Profundidad
#Contar nodos
#Pred./Suc.
#BST?, ABB?
print(arbol6.espejo())
print(arbol6.busqueda("*"))