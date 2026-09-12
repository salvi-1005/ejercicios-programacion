class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar(nodo_actual, valor):
    # Caso base: si el árbol/subárbol está vacío, creamos el nodo
    if nodo_actual is None:
        return Nodo(valor)
    
    # Si el valor es menor, vamos a la izquierda
    if valor < nodo_actual.valor:
        nodo_actual.izquierdo = insertar(nodo_actual.izquierdo, valor)
    # Si el valor es mayor, vamos a la derecha
    elif valor > nodo_actual.valor:
        nodo_actual.derecho = insertar(nodo_actual.derecho, valor)
        
    return nodo_actual

# Uso
raiz = None
valores = [10, 5, 15, 3, 7]
for v in valores:
    raiz = insertar(raiz, v)

def inorden(nodo_actual):
    if nodo_actual is not None:
        # 1. Recorrer subárbol izquierdo
        inorden(nodo_actual.izquierdo)
        # 2. Visitar nodo actual
        print(nodo_actual.valor, end=" ")
        # 3. Recorrer subárbol derecho
        inorden(nodo_actual.derecho)

# Muestra: 3 5 7 10 15
inorden(raiz) 
print()

def preorden(nodo_actual):
    if nodo_actual is not None:
        # 1. Visitar nodo actual
        print(nodo_actual.valor, end=" ")
        # 2. Recorrer subárbol izquierdo
        preorden(nodo_actual.izquierdo)
        # 3. Recorrer subárbol derecho
        preorden(nodo_actual.derecho)
        
# Muestra: 10 5 3 7 15
preorden(raiz)
print()  
        
def postorden(nodo_actual):
    if nodo_actual is not None:
        # 1. Recorrer subárbol izquierdo
        postorden(nodo_actual.izquierdo)
        # 2. Recorrer subárbol derecho
        postorden(nodo_actual.derecho)
        # 3. Visitar nodo actual
        print(nodo_actual.valor, end=" ")
        
# Muestra: 3 7 5 15 10
postorden(raiz)
print()

def calcular_altura(nodo_actual):
    # Caso base: un árbol vacío tiene altura 0
    if nodo_actual is None:
        return 0
    
    # Calcular la altura de cada subárbol
    altura_izquierda = calcular_altura(nodo_actual.izquierdo)
    altura_derecha = calcular_altura(nodo_actual.derecho)
    
    # La altura actual es 1 (el nodo actual) más la altura del hijo más alto
    return 1 + max(altura_izquierda, altura_derecha)

print(f"altura máxima: {calcular_altura(raiz)}")
print()

def encontrar_minimo(nodo_actual):
    # Función auxiliar para buscar el nodo más a la izquierda (el menor)
    while nodo_actual.izquierdo is not None:
        nodo_actual = nodo_actual.izquierdo
    return nodo_actual

def eliminar_nodo(nodo_actual, valor_a_eliminar):
    # Caso base: el árbol está vacío o el valor no existe
    if nodo_actual is None:
        return None

    # 1. Buscar el nodo a eliminar en los subárboles
    if valor_a_eliminar < nodo_actual.valor:
        nodo_actual.izquierdo = eliminar_nodo(nodo_actual.izquierdo, valor_a_eliminar)
    elif valor_a_eliminar > nodo_actual.valor:
        nodo_actual.derecho = eliminar_nodo(nodo_actual.derecho, valor_a_eliminar)
    
    # 2. ¡Encontramos el nodo a eliminar!
    else:
        # Caso 1 y 2: Sin hijos o con un solo hijo (derecho)
        if nodo_actual.izquierdo is None:
            return nodo_actual.derecho
        
        # Caso 2: Con un solo hijo (izquierdo)
        elif nodo_actual.derecho is None:
            return nodo_actual.izquierdo

        # Caso 3: El nodo tiene DOS hijos
        # Buscamos el nodo más pequeño del subárbol derecho
        sucesor = encontrar_minimo(nodo_actual.derecho)
        # Reemplazamos el valor del nodo actual por el del sucesor
        nodo_actual.valor = sucesor.valor
        # Eliminamos recursivamente el sucesor en el subárbol derecho
        nodo_actual.derecho = eliminar_nodo(nodo_actual.derecho, sucesor.valor)

    return nodo_actual

# Ejemplo de uso en la raíz de tu árbol actual
print("Estructura original (Preorden):")
preorden(raiz)
print()

# Supongamos que queremos borrar el nodo 5 (que tiene dos hijos: 3 y 7)
raiz = eliminar_nodo(raiz, 5)

print("Estructura tras eliminar el 5 (Preorden):")
preorden(raiz)
print()


def buscar_nodo(nodo_actual, valor_a_buscar):
    # Caso base 1: El nodo es None (el valor no está en el árbol)
    # Caso base 2: Encontramos el nodo con el valor buscado
    if nodo_actual is None or nodo_actual.valor == valor_a_buscar:
        return nodo_actual
    
    # Si el valor es menor, buscamos recursivamente en la izquierda
    if valor_a_buscar < nodo_actual.valor:
        return buscar_nodo(nodo_actual.izquierdo, valor_a_buscar)
    
    # Si el valor es mayor, buscamos recursivamente en la derecha
    return buscar_nodo(nodo_actual.derecho, valor_a_buscar)

# Definimos el número que queremos buscar
numero = 7

# Llamamos a la función de búsqueda
resultado = buscar_nodo(raiz, numero)

# Evaluamos e imprimimos el resultado
if resultado is not None:
    print(f"El elemento {numero} SÍ existe en el árbol.")
else:
    print(f"El elemento {numero} NO se encuentra en el árbol.")

def cantidadDeNodos(nodo_actual):
    if nodo_actual is None:
        return 0
    return 1 + cantidadDeNodos(nodo_actual.izquierdo) + cantidadDeNodos(nodo_actual.derecho)

print(f"La cantidad de nodos del arbol es: ")
print(cantidadDeNodos(raiz))

