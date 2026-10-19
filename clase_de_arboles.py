class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
    def contar_pares(self):
        if self.izq is None and self.der is None:
            if self.valor % 2 == 0:
                return 1
            return 0
        if self.izq is None and self.der is not None:
            if self.valor % 2 == 0:
                return 1 + self.der.contar_pares()
            return self.der.contar_pares()
        if self.izq is not None and self.der is None:
            if self.valor % 2 == 0:
                return 1 + self.izq.contar_pares()
            return self.izq.contar_pares()
        if self.izq is not None and self.der is not None:
            if self.valor % 2 == 0:
                return 1 + self.izq.contar_pares() + self.der.contar_pares()
            return self.izq.contar_pares() + self.der.contar_pares()
    def mostrar_niveles(self, nivel=0):
        if self.izq is None and self.der is None:
            print(f"Nivel: {nivel}, Valor: {self.valor}")
            return
        if self.izq is None and self.der is not None:
            print(f"Nivel: {nivel}, Valor: {self.valor}")
            self.der.mostrar_niveles(nivel+1)
        if self.izq is not None and self.der is None:
            print(f"Nivel: {nivel}, Valor: {self.valor}")
            self.izq.mostrar_niveles(nivel+1)
        if self.izq is not None and self.der is not None:
            print(f"Nivel: {nivel}, Valor: {self.valor}")
            self.izq.mostrar_niveles(nivel+1)
            self.der.mostrar_niveles(nivel+1)
    def hay_negativo(self):
        if self.izq is None and self.der is None:
            if self.valor < 0:
                return True
            return False
        if self.izq is None and self.der is not None:
            if self.valor < 0:
                return True
            return self.der.hay_negativo()
        if self.izq is not None and self.der is None:
            if self.valor < 0:
                return True
            return self.izq.hay_negativo()
        return (self.valor < 0 or self.izq.hay_negativo() or self.der.hay_negativo())
    def contar_en_nivel(self, k):
        if self.izq is None and self.der is None:
            if k == 0:
                return 1
            return 0
        if self.izq is None and self.der is not None:
            if k == 0:
                return 1
            return self.der.contar_en_nivel(k-1)
        if self.izq is not None and self.der is None:
            if k == 0:
                return 1
            return self.izq.contar_en_nivel(k-1)
        if self.izq is not None and self.der is not None:
            if k == 0:
                return 1
            return (self.izq.contar_en_nivel(k-1) + self.der.contar_en_nivel(k-1))
    def preorden_print(self):
        if self.izq is None and self.der is None:
            print(self.valor)
            return
        if self.izq is None and self.der is not None:
            print(self.valor)
            self.der.preorden_print()
        if self.izq is not None and self.der is None:
            print(self.valor)
            self.izq.preorden_print()
        if self.izq is not None and self.der is not None:
            print(self.valor)
            self.izq.preorden_print()
            self.der.preorden_print()
    def inorden_print(self):
        if self.izq is None and self.der is None:
            print(self.valor)
            return
        if self.izq is None and self.der is not None:
            print(self.valor)
            self.der.inorden_print()
        if self.izq is not None and self.der is None:
            self.izq.inorden_print()
            print(self.valor)
        if self.izq is not None and self.der is not None:
            self.izq.inorden_print()
            print(self.valor)
            self.der.inorden_print()
    def postorden_print(self):
        if self.izq is None and self.der is None:
            print(self.valor)
            return
        if self.izq is None and self.der is not None:
            self.der.postorden_print()
            print(self.valor)
        if self.izq is not None and self.der is None:
            self.izq.postorden_print()
            print(self.valor)
        if self.izq is not None and self.der is not None:
            self.izq.postorden_print()
            self.der.postorden_print()
            print(self.valor)
    def tamaño(self):
        izq = 0 if self.izq is None else self.izq.tamaño()
        der = 0 if self.der is None else self.der.tamaño()
        return 1 + izq + der
    def suma(self):
        if self.izq is None and self.der is None:
            return self.valor
        if self.izq is None and self.der is not None:
            return self.valor + self.der.suma()
        if self.izq is not None and self.der is None:
            return self.valor + self.izq.suma()
        return self.valor + self.izq.suma() + self.der.suma()
    def maximo(self):
        if self.der is None:
            return self.valor
        return self.der.maximo()
    def altura(self):
        h_izq = -1 if self.izq is None else self.izq.altura()
        h_der = -1 if self.der is None else self.der.altura()
        return 1 + max(h_izq, h_der)
    def contar_hojas(self):
        if self.izq is not None and self.der is None:
            return self.izq.contar_hojas()
        if self.izq is None and self.der is not None:
            return self.der.contar_hojas()
        if self.izq is None and self.der is None:
            return 1 
        return self.izq.contar_hojas() + self.der.contar_hojas()
    def contiene(self, x):
        if self.valor == x:
            return True
        return ((self.izq is not None and self.izq.contiene(x)) or \
        (self.der is not None and self.der.contiene(x)))
    def profundidad(self, x, nivel = 0):
        if self.izq is None and self.der is None:
            if self.valor != x:
                return -1
            return nivel
        if self.valor == x:
            return nivel
        if self.valor > x:
            return self.izq.profundidad(x, nivel+1)
        if self.valor < x:
            return self.der.profundidad(x, nivel+1)
    def nodos_en_nivel(self, k, nivel=0):
        if self.izq is None and self.der is None:
            if nivel == k:
                return [self.valor]
            return []
        if self.izq is None and self.der is not None:
            if nivel == k:
                return [self.valor] + self.der.nodos_en_nivel(k, nivel+1)
            return self.der.nodos_en_nivel(k, nivel+1)
        if self.izq is not None and self.der is None:
            if nivel == k:
                return [self.valor] + self.izq.nodos_en_nivel(k, nivel+1)
            return self.izq.nodos_en_nivel(k, nivel+1)
        if self.izq is not None and self.der is not None:
            if nivel == k:
                return [self.valor] + self.izq.nodos_en_nivel(k, nivel+1) + self.der.nodos_en_nivel(k, nivel+1)
            return self.izq.nodos_en_nivel(k, nivel+1) + self.der.nodos_en_nivel(k, nivel+1)  
    def preorden(self):
        return ([self.valor] + \
        ([] if self.izq is None else self.izq.preorden()) +
        ([] if self.der is None else self.der.preorden()))
    def inorden(self):
        return (([] if self.izq is None else self.izq.inorden()) + \
        [self.valor] + \
        ([] if self.der is None else self.der.inorden()))
    def postorden(self):
        return ( ([] if self.izq is None else self.izq.postorden()) +
        ([] if self.der is None else self.der.postorden()) + \
        [self.valor])
    def preorden_cola(self):
        pila = [self]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.der is not None:
                pila.append(actual.der)
            if actual.izq is not None:
                pila.append(actual.izq)
        return resultado
    def inorden_cola(self):
        resultado = []
        pila = []
        actual = self
        while actual is not None or pila:
            while actual is not None:
                pila.append(actual)
                actual = actual.izq
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.der
        return resultado
    def postorden_cola(self):
        pila = [self]
        resultado = []
        while pila:
            actual = pila.pop()
            resultado.append(actual.valor)
            if actual.izq is not None:
                pila.append(actual.izq)
            if actual.der is not None:
                pila.append(actual.der)
        return resultado[::-1]
    def bfs(self):
        res, cola = [], deque([self])
        while cola:
            nivel = []
            for _ in range(len(cola)):
                n = cola.popleft()      # sacar el primero
                nivel.append(n.valor)
                if n.izq:
                    cola.append(n.izq)
                if n.der:
                    cola.append(n.der)
            res.append(nivel)
        return res
    def busqueda_binaria(self, x, lista=None):
        if lista is None:
            lista = self.inorden()
        if self.izq is None and self.der is None:
            if self.valor != x:
                return -1
            return lista.index(self.valor)
        if x < self.valor:
            return self.izq.busqueda_binaria(x, lista)
        if x > self.valor:
            return self.der.busqueda_binaria(x, lista)
        if x == self.valor:
            return lista.index(self.valor)
        
        
a = Nodo(8, Nodo(3, Nodo(1), Nodo(6, Nodo(4), Nodo(7))), Nodo(10, None, Nodo(14, Nodo(13))))

def combinar(n1, n2):
    return n1 + n2

def f(n):
    if n is None:
        return 
    r_izq = f(n.izq)
    r_der = f(n.der)
    return combinar(r_izq, r_der)
    
    
def contar_pares(n):
    if n is None:
        return 0
    propio = 1 if n.valor % 2 == 0 else 0
    return propio + contar_pares(n.izq) + contar_pares(n.der)

print(f"Cantidad de numeros pares: {contar_pares(a)}")
print(f"Cantidad de numeros pares: {a.contar_pares()}")

def mostrar_niveles(n, nivel=0):
    if n is None:
        return
    print(f"Nivel: {nivel}, Valor: {n.valor}")
    mostrar_niveles(n.izq, nivel+1)
    mostrar_niveles(n.der, nivel+1)
    
mostrar_niveles(a)
a.mostrar_niveles()

def hay_negativo(n):
    if n is None:
        return False
    return (n.valor < 0 or hay_negativo(n.izq) or hay_negativo(n.der))

print(hay_negativo(a))
print(a.hay_negativo())

def contar_en_nivel(n, k):
    if n is None:
        return 0
    if k == 0:
        return 1
    return (contar_en_nivel(n.izq, k-1) + contar_en_nivel(n.der, k-1))

k = 2
print(f"Cantidad de elementos en el nivel {k}: {contar_en_nivel(a, k)}")
print(f"Cantidad de elementos en el nivel {k}: {a.contar_en_nivel(k)}")
    
def preorden_print(n):
    if n is None:
        return
    print(n.valor)
    preorden_print(n.izq)
    preorden_print(n.der)
    
print('Preorden: ')
preorden_print(a)
print('Preorden: ')
a.preorden_print()

def inorden_print(n):
    if n is None:
        return
    inorden_print(n.izq)
    print(n.valor)
    inorden_print(n.der)
    
print('Inorden: ')
inorden_print(a)
print('Inorden: ')
a.inorden_print()

def postorden_print(n):
    if n is None:
        return
    postorden_print(n.izq)
    postorden_print(n.der)
    print(n.valor)
    
print('Postorden: ')
postorden_print(a)
print('Postorden: ')
a.postorden_print()
   
#1)
    
def tamaño(n):
    if n is None:
        return 0
    return 1 + tamaño(n.izq) + tamaño(n.der)

print(f"Cantidad de nodos del arbol: {tamaño(a)}")
print(f"Cantidad de nodos del arbol: {a.tamaño()}")


def suma(n):
    if n is None:
        return 0
    return n.valor + suma(n.izq) + suma(n.der)

print(f"Sumatoria de nodos del arbol: {suma(a)}")
print(f"Sumatoria de nodos del arbol: {a.suma()}")

def maximo(n):
    if n.der is None:
        return n.valor
    return maximo(n.der)

print(f"El máximo valor del arbol es {maximo(a)}")
print(f"El máximo valor del arbol es {a.maximo()}")

#2)

def altura(n):
    if tamaño(n) == 0:
        return -1
    if n is None:
        return 0
    return 1 + max(altura(n.izq), altura(n.der))

print(f"La altura del arbol es: {altura(a)}")
print(f"La altura del arbol es: {a.altura()}")

def contar_hojas(n):
    if n is None:
        return 0
    if n.izq is not None and n.der is None:
        return contar_hojas(n.izq)
    if n.izq is None and n.der is not None:
        return contar_hojas(n.der)
    if n.izq is None and n.der is None:
        return 1 + contar_hojas(n.izq) + contar_hojas(n.der)
    return contar_hojas(n.izq) + contar_hojas(n.der)

print(f"Cantidad de hojas del arbol: {contar_hojas(a)}")
print(f"Cantidad de hojas del arbol: {a.contar_hojas()}")

def contiene(n, x):
    if n is None:
        return False
    if n.valor == x:
        return True
    return contiene(n.izq, x) or contiene(n.der, x)

x = 9
print(contiene(a, x))
print(a.contiene(x))

#3)

def profundidad(a, x, nivel = 0):
    if a is None:
        return -1
    if a.valor == x:
        return nivel
    if a.valor > x:
        return profundidad(a.izq, x, nivel+1)
    if a.valor < x:
        return profundidad(a.der, x, nivel+1)
    
x = 14
print(f"Nivel del {x}: {profundidad(a, x)}")
print(f"Nivel del {x}: {a.profundidad(x)}")
    
def nodos_en_nivel(a, k, nivel=0):
    if a is None:
        return []
    if nivel == k:
        return [a.valor] + nodos_en_nivel(a.izq, k, nivel+1) + nodos_en_nivel(a.der, k, nivel+1)
    return nodos_en_nivel(a.izq, k, nivel+1) + nodos_en_nivel(a.der, k, nivel+1)  
         
k = 2
print(f"Nodos en el nivel {k}: {nodos_en_nivel(a, k)}")
print(f"Nodos en el nivel {k}: {a.nodos_en_nivel(k)}")

#4)

def preorden_lista(n):
    if n is None:
        return []
    return [n.valor] + \
    preorden_lista(n.izq) + \
    preorden_lista(n.der)
    
print('Preorden: ')
print(preorden_lista(a))
print('Preorden: ')
print(a.preorden())

def inorden_lista(n):
    if n is None:
        return []
    return inorden_lista(n.izq) + \
    [n.valor] + \
    inorden_lista(n.der)
    
print('Inorden: ')
print(inorden_lista(a))
print('Inorden: ')
print(a.inorden())

def postorden_lista(n):
    if n is None:
        return []
    return postorden_lista(n.izq) + \
    postorden_lista(n.der) + \
    [n.valor]
    
print('Postorden: ')
print(postorden_lista(a))
print('Postorden: ')
print(a.postorden())

def preorden_cola(a):
    if a is None:
        return []
    pila = [a]
    resultado = []
    while pila:
        actual = pila.pop()
        resultado.append(actual.valor)
        if actual.der is not None:
            pila.append(actual.der)
        if actual.izq is not None:
            pila.append(actual.izq)
    return resultado

print('Preorden cola: ')
print(preorden_cola(a))
print('Preorden cola: ')
print(a.preorden_cola())

def inorden_cola(a):
    resultado = []
    pila = []
    actual = a
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.izq
        actual = pila.pop()
        resultado.append(actual.valor)
        actual = actual.der
    return resultado

print('Inorden cola: ')
print(inorden_cola(a))
print('Inorden cola: ')
print(a.inorden_cola())

def postorden_cola(a):
    if a is None:
        return []
    pila = [a]
    resultado = []
    while pila:
        actual = pila.pop()
        resultado.append(actual.valor)
        if actual.izq is not None:
            pila.append(actual.izq)
        if actual.der is not None:
            pila.append(actual.der)
    return resultado[::-1]

print('Postorden cola: ')
print(postorden_cola(a))
print('Postorden cola: ')
print(a.postorden_cola())

from collections import deque
 
#5)

def bfs(a):
    if a is None:
        return []
    res, cola = [], deque([a])
    while cola:
        nivel = []
        for _ in range(len(cola)):
            n = cola.popleft()      # sacar el primero
            nivel.append(n.valor)
            if n.izq:
                cola.append(n.izq)
            if n.der:
                cola.append(n.der)
        res.append(nivel)
    return res
 
print("Recorrido por niveles (BFS): ")
print(bfs(a))
print("Recorrido por niveles (BFS): ")
print(a.bfs())

def busqueda_binaria(a, x, lista=None):
    if lista is None:
        lista = inorden_lista(a)
    if a is None:
        return -1
    if x < a.valor:
        return busqueda_binaria(a.izq, x, lista)
    if x > a.valor:
        return busqueda_binaria(a.der, x, lista)
    if x == a.valor:
        return lista.index(a.valor)

x = 7
print(f"Indice del elemento {x}: {busqueda_binaria(a, x)}")
print(f"Indice del elemento {x}: {a.busqueda_binaria(x)}")
