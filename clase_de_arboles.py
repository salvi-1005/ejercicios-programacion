class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
    def contar_pares(self):
        if self.izq is None and self.der is None:
            return 0
        propio = 1 if self.valor % 2 == 0 else 0
        return propio + self.izq.contar_pares() + self.der.contar_pares()
    def mostrar_niveles(self, nivel=0):
        if self.izq is None and self.der is None:
            return
        print(f"Nivel: {nivel}, Valor: {self.valor}")
        if self.izq is not None and self.der is None:
            self.izq.mostrar_niveles(nivel+1)
        if self.izq is None and self.der is not None:
            self.der.mostrar_niveles(nivel+1)
        self.izq.mostrar_niveles(nivel+1)
        self.der.mostrar_niveles(nivel+1)
    def maximo(self):
        if self.der is None:
            return self.valor
        return self.der.maximo()
        
a = Nodo(5, Nodo(2, Nodo(1), Nodo(3, None, Nodo(4))), Nodo(9, Nodo(8), Nodo(10)))
print(a.izq.der.valor)

def f(n):
    if n is None:
        return n
    
def contar_pares(n):
    if n is None:
        return 0
    propio = 1 if n.valor % 2 == 0 else 0
    return propio + contar_pares(n.izq) + contar_pares(n.der)

print(f"Cantidad de numeros pares: {contar_pares(a)}")
#print(f"Cantidad de numeros pares: {a.contar_pares()}")

def mostrar_niveles(n, nivel=0):
    if n is None:
        return
    print(f"Nivel: {nivel}, Valor: {n.valor}")
    mostrar_niveles(n.izq, nivel+1)
    mostrar_niveles(n.der, nivel+1)
    
mostrar_niveles(a)

def hay_negativo(n):
    if n is None:
        return False
    return (n.valor < 0 or hay_negativo(n.izq) or hay_negativo(n.der))

print(hay_negativo(a))

def contar_en_nivel(n, nivel):
    if n is None:
        return 0
    
def preorden_print(n):
    if n is None:
        return
    print(n.valor)
    preorden_print(n.izq)
    preorden_print(n.der)
    
print('Preorden: ')
preorden_print(a)

def inorden_print(n):
    if n is None:
        return
    inorden_print(n.izq)
    print(n.valor)
    inorden_print(n.der)
    
print('Inorden: ')
inorden_print(a)

def postorden_print(n):
    if n is None:
        return
    postorden_print(n.izq)
    postorden_print(n.der)
    print(n.valor)
    
print('Postorden: ')
postorden_print(a)

def preorden_lista(n):
    if n is None:
        return []
    return [n.valor] + \
    preorden_lista(n.izq) + \
    preorden_lista(n.der)
    
print('Preorden: ')
print(preorden_lista(a))

def inorden_lista(n):
    if n is None:
        return []
    return inorden_lista(n.izq) + \
    [n.valor] + \
    inorden_lista(n.der)
    
print('Inorden: ')
print(inorden_lista(a))

def postorden_lista(n):
    if n is None:
        return []
    return postorden_lista(n.izq) + \
    postorden_lista(n.der) + \
    [n.valor]
    
print('Postorden: ')
print(postorden_lista(a))
    
def tamaño(n):
    if n is None:
        return 0
    return 1 + tamaño(n.izq) + tamaño(n.der)

print(f"Cantidad de nodos del arbol: {tamaño(a)}")

def suma(n):
    if n is None:
        return 0
    return n.valor + suma(n.izq) + suma(n.der)

print(f"Sumatoria de nodos del arbol: {suma(a)}")

def maximo(n):
    if n.der is None:
        return n.valor
    return maximo(n.der)

print(f"El máximo valor del arbol es {maximo(a)}")

def altura(n):
    if tamaño(n) == 0:
        return -1
    if n is None:
        return 0
    return 1 + max(altura(n.izq), altura(n.der))

print(f"La altura del arbol es: {altura(a)}")

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

def contiene(n, x):
    if n is None:
        return False
    if n.valor == x:
        return True
    return contiene(n.izq, x) or contiene(n.der, x)

x = 9
print(contiene(a, x))
