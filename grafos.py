import heapq

class Grafo:
    def __init__(self):
        # El diccionario almacenará: { nodo: [vecino1, vecino2, ...] }
        self.lista_adyacencia = {}

    def agregar_vertice(self, vertice):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []

    def agregar_arista(self, inicio, fin, bidireccional=True):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
        
        # Conectamos inicio -> fin
        self.lista_adyacencia[inicio].append(fin)
        
        # Si es un grafo no dirigido (bidireccional), conectamos fin -> inicio
        if bidireccional:
            self.lista_adyacencia[fin].append(inicio)

    def mostrar_grafo(self):
        for vertice, vecinos in self.lista_adyacencia.items():
            print(f"{vertice} -> {vecinos}")

g = Grafo()
g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")

g.mostrar_grafo()
# Salida en consola:
# A -> ['B', 'C']
# B -> ['A', 'D']
# C -> ['A']
# D -> ['B']

def dijkstra(grafo, nodo_inicio):
    # 1. Inicializar las distancias de todos los nodos como infinitas (float('inf'))
    distancias = {nodo: float('inf') for nodo in grafo.lista_adyacencia}
    distancias[nodo_inicio] = 0  # La distancia a sí mismo es cero
    
    # Diccionario para reconstruir la ruta exacta mas corta
    padres = {nodo: None for nodo in grafo.lista_adyacencia}
    
    # 2. Crear la cola de prioridad (Heap). Guarda tuplas: (distancia_acumulada, nodo)
    # Colocamos el nodo de inicio con distancia 0
    cola_prioridad = [(0, nodo_inicio)]
    
    while cola_prioridad:
        # Extrae el nodo con la menor distancia acumulada actual
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si ya encontramos un camino más corto hacia este nodo previamente, lo ignoramos
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        # 3. Revisar los vecinos del nodo actual
        for vecino, peso_arista in grafo.lista_adyacencia[nodo_actual]:
            distancia_nueva = distancia_actual + peso_arista
            
            # Si encontramos un camino más corto hacia el vecino, actualizamos
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                padres[vecino] = nodo_actual  # Guardamos de dónde venimos
                heapq.heappush(cola_prioridad, (distancia_nueva, vecino))
                
    return distancias, padres

def obtener_camino_exacto(padres, destino):
    # Función auxiliar para reconstruir la ruta de nodos desde el origen hasta el destino
    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()  # Invertimos la lista para que vaya de Origen -> Destino
    return camino

# Creamos el mapa
mapa = Grafo()
mapa.agregar_arista("A", "B", 4)  # Ruta A-B: 4km
mapa.agregar_arista("A", "C", 2)  # Ruta A-C: 2km
mapa.agregar_arista("C", "B", 1)  # Ruta C-B: 1km (Desvío más corto para ir de A a B)
mapa.agregar_arista("B", "D", 5)  # Ruta B-D: 5km
mapa.agregar_arista("C", "D", 8)  # Ruta C-D: 8km

# Ejecutamos Dijkstra saliendo desde la ciudad "A"
distancias_minimas, arbol_padres = dijkstra(mapa, "A")

# Consultamos los resultados para llegar a la ciudad "D"
destino_final = "D"
print(f"Distancia mínima desde A hasta {destino_final}: {distancias_minimas[destino_final]} km")

ruta_optima = obtener_camino_exacto(arbol_padres, destino_final)
print(f"Ruta óptima a seguir: {' -> '.join(ruta_optima)}")

# Salida esperada en consola:
# Distancia mínima desde A hasta D: 8 km
# Ruta óptima a seguir: A -> C -> B -> D

class GrafoDirigido:
    def __init__(self):
        # El diccionario guardará: {nodo_origen: [(nodo_destino, peso), ...]}
        self.grafo = {}
        self.aristas = []

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
            
        self.grafo[u].append((v, peso))
        # Guardamos una lista plana de aristas para facilitar Bellman-Ford
        self.aristas.append((u, v, peso))

    def bellman_ford(self, inicio):
        # Paso 1: Inicializar distancias
        vertices = list(self.grafo.keys())
        distancia = {v: float('inf') for v in vertices}
        distancia[inicio] = 0

        # Paso 2: Relajar todas las aristas V - 1 veces
        num_vertices = len(vertices)
        for _ in range(num_vertices - 1):
            for u, v, peso in self.aristas:
                if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso

        # Paso 3: Detectar ciclos negativos
        for u, v, peso in self.aristas:
            if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                print("¡Alerta! El grafo contiene un ciclo negativo.")
                return None

        return distancia

# --- Pruebas con el ejemplo numérico ---
g = GrafoDirigido()
g.agregar_arista('A', 'B', 4)
g.agregar_arista('A', 'C', 5)
g.agregar_arista('B', 'C', -2)

# Ejecutar el algoritmo desde el nodo 'A'
resultados = g.bellman_ford('A')

if resultados:
    print("Distancias más cortas desde el nodo A:")
    for nodo, dist in resultados.items():
        print(f"Hasta {nodo}: {dist}")



