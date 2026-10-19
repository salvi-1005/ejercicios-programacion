import heapq

#Versión Conjunto de nodos y aristas

class Grafo1:
    def __init__(self):
        self.conjunto_adyacencias = set()
        self.conjunto_vertices = set()
    def agregar_vertice(self, vertice):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if vertice not in self.conjunto_vertices:
            self.conjunto_vertices.add(vertice)
    def agregar_arista(self, inicio, fin, bidireccional=True):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
            
        # Conectamos inicio -> fin
        self.conjunto_adyacencias.add((inicio, fin))
            
        if bidireccional:
            self.conjunto_adyacencias.add((fin, inicio))
    def eliminar_vertice(self, vertice, aristas=None):
        if aristas is None:
            aristas = list(self.conjunto_adyacencias)
        if not aristas:
            return
        # Si el nodo existe, lo borramos 
        if vertice in self.conjunto_vertices:
            self.conjunto_vertices.remove(vertice)
        #Si el vertice está involucrado en alguna conexión, borro esa conexión, sino, sigo de largo.
        if vertice in aristas[0]:
            self.conjunto_adyacencias.remove(aristas[0])
            return self.eliminar_vertice(vertice, aristas[1:])
        return self.eliminar_vertice(vertice, aristas[1:])
    def eliminar_arista(self, arista, bidireccional=True):
        if arista in self.conjunto_adyacencias:
            self.conjunto_adyacencias.remove(arista)
            if bidireccional and arista[::-1] in self.conjunto_adyacencias:
                self.conjunto_adyacencias.remove(arista[::-1])
    def es_vecino_de(self, vertice1, vertice2, aristas=None):
        if aristas is None:
            aristas = list(self.conjunto_adyacencias)
        if not aristas:
            return False
        if (vertice1, vertice2) == aristas[0] or (vertice2, vertice1) == aristas[0]:
            return True
        return self.es_vecino_de(vertice1, vertice2, aristas[1:])
    def vecinos_de(self, vertice, bidireccional=True, aristas=None, res=None):
        if aristas is None:
            aristas = list(self.conjunto_adyacencias)
        if res is None:
            res = []
        if not aristas:
            return res
        if aristas[0][0] == vertice:
            if aristas[0][1] not in res:
                res.append(aristas[0][1])
            return self.vecinos_de(vertice, bidireccional, aristas[1:], res)
        if bidireccional:
            if aristas[0][1] == vertice:
                if aristas[0][0] not in res:
                    res.append(aristas[0][0])
                return self.vecinos_de(vertice, bidireccional, aristas[1:], res)
        return self.vecinos_de(vertice, bidireccional, aristas[1:], res)
    
    def dfs(self, origen):
        return self._dfs(origen, set())
    def _dfs(self, origen, visitados):
        if origen in visitados:
            return []
        visitados.add(origen)
        return [origen] + self._dfs_vecinos(origen, list(self.conjunto_adyacencias), visitados)
    def _dfs_vecinos(self, origen, aristas, visitados):
        if aristas == []:
            return []
        inicio, fin = aristas[0]
        if inicio == origen:
            return (self._dfs(fin, visitados) + self._dfs_vecinos(origen, aristas[1:], visitados))
        return self._dfs_vecinos(origen, aristas[1:], visitados)
    def bfs(self, origen):
        return self._bfs([origen], set())
    def _bfs(self, cola, visitados):
        if cola == []:
            return []
        vertice = cola[0]
        cola = cola[1:]
        if vertice in visitados:
            return self._bfs(cola, visitados)
        visitados.add(vertice)
        vecinos = self.vecinos_de(vertice)
        return ([vertice] + self._bfs(cola + vecinos, visitados))
    
    def existe_camino(self, origen, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if origen == destino:
            return True
        visitados.add(origen)
        return self._explorar_aristas(list(self.conjunto_adyacencias), origen, destino, visitados)
    def _explorar_aristas(self, aristas, origen, destino, visitados):
        if aristas == []:
            return False
        inicio, fin = aristas[0]
        if inicio == origen and fin not in visitados:
            if self.existe_camino(fin, destino, visitados):
                return True
        return self._explorar_aristas(aristas[1:], origen, destino, visitados)
    def __str__(self):
        return f"Aristas:{str(self.conjunto_adyacencias)}, vértices:{str(self.conjunto_vertices)}"
        
g = Grafo1()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")
g.agregar_vertice("E")
g.agregar_vertice("F")

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("C", "D")
g.agregar_arista("D", "B")
g.agregar_arista("E", "F")

print("Versión Conjunto de aristas y vértices")

print(g)

print("Vértices: ")
print(g.conjunto_vertices)

print("Aristas: ")
print(g.conjunto_adyacencias)

vertice1 = "A"
vertice2 = "B"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

origen = "A"
print("Recorrido DFS:")
print(g.dfs(origen))

origen = "A"
print("Recorrido BFS:")
print(g.bfs(origen))

origen = "A"
destino = "C"
print(f"Existe camino de {origen} a {destino}? {g.existe_camino(origen, destino)}")

print(set(g.dfs("A")) == {"A","B","C","D"})
print(set(g.bfs("A")) == {"A","B","C","D"})

g.eliminar_vertice("A")
g.eliminar_arista(("C", "D"))

print("Después de eliminar: ")

print("Vértices después de eliminar el A: ")
print(g.conjunto_vertices)

print("Aristas después de eliminar el (C, D): ")
print(g.conjunto_adyacencias)

vertice1 = "A"
vertice2 = "B"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

origen = "A"
print("Recorrido DFS:")
print(g.dfs(origen))

origen = "A"
print("Recorrido BFS:")
print(g.bfs(origen))

origen = "A"
destino = "C"
print(f"Existe camino de {origen} a {destino}? {g.existe_camino(origen, destino)}")

#Versión lista de adyacencia

class Grafo2:
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
            
    def eliminar_vertice(self, vertice, lista_vertices=None):
        if lista_vertices is None:
            lista_vertices = list(self.lista_adyacencia)
        if not lista_vertices:
            return
        # Si el nodo existe, lo borramos 
        if vertice in self.lista_adyacencia:
            del self.lista_adyacencia[vertice]
            lista_vertices.remove(vertice)
        #Si el vertice está involucrado en alguna conexión, borro esa conexión, sino, sigo de largo.
        if vertice in self.lista_adyacencia[lista_vertices[0]]:
            self.lista_adyacencia[lista_vertices[0]].remove(vertice)
            return self.eliminar_vertice(vertice, lista_vertices[1:])
        return self.eliminar_vertice(vertice, lista_vertices[1:])
    
    def eliminar_arista(self, inicio, fin, lista_vertices=None):
        if lista_vertices is None:
            lista_vertices = list(self.lista_adyacencia)
        if not lista_vertices:
            return
        # Si alguno de los dos extremos de la arista no existe, no la borro
        if inicio not in self.lista_adyacencia or fin not in self.lista_adyacencia:
            return
        # Si la arista que quiero borrar no existe, no hago nada
        if fin not in self.lista_adyacencia[inicio] and \
            inicio not in self.lista_adyacencia[fin]:
            return
        if lista_vertices[0] == inicio:
            self.lista_adyacencia[lista_vertices[0]].remove(fin)
            return self.eliminar_arista(inicio, fin, lista_vertices[1:])
        if lista_vertices[0] == fin:
            self.lista_adyacencia[lista_vertices[0]].remove(inicio)
            return self.eliminar_arista(inicio, fin, lista_vertices[1:])
        return self.eliminar_arista(inicio, fin, lista_vertices[1:])
    
    def es_vecino_de(self, vertice1, vertice2, bidireccional=True):
        if vertice1 not in self.lista_adyacencia:
            return False
        if bidireccional and vertice2 not in self.lista_adyacencia:
            return False
        if bidireccional:
            return (vertice2 in self.lista_adyacencia[vertice1] or \
            vertice1 in self.lista_adyacencia[vertice2])
        return vertice2 in self.lista_adyacencia[vertice1]
    
    def vecinos_de(self, vertice):
        return self.lista_adyacencia[vertice]
            
    def hay_camino(self, origen, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if origen == destino:
            return True
        visitados.add(origen)
        return self._explorar_vecinos(self.lista_adyacencia[origen], destino, visitados)

    def _explorar_vecinos(self, vecinos, destino, visitados, i=0):
        if i >= len(vecinos):
            return False
        vecino = vecinos[i]
        if vecino not in visitados:
            if self.hay_camino(vecino, destino, visitados):
                return True
        return self._explorar_vecinos(vecinos, destino,visitados, i + 1)

    def __str__(self):
        return f"Lista de adyacencia: {str(self.lista_adyacencia)}"

g = Grafo2()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("C", "D")
g.agregar_arista("D", "B")

print("Versión lista de adyacencia: ")

print(g)

vertice1 = "B"
vertice2 = "D"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

g.eliminar_vertice("A")
g.eliminar_arista("B", "D")

print("Después de eliminar: ")

print(g)

vertice1 = "B"
vertice2 = "D"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

class Grafo3:
    def __init__(self):
        self.vertices = []
        self.matriz = []
        
    def agregar_vertice(self, vertice):
        if vertice in self.vertices:
            return
        self.vertices.append(vertice)
        self._agregar_columna(self.matriz)
        self.matriz.append([0] * len(self.vertices))
        
    def _agregar_columna(self, filas):
        if not filas:
            return
        filas[0].append(0)
        self._agregar_columna(filas[1:])

    def agregar_arista(self, inicio, fin, bidireccional=True):
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
        i = self.vertices.index(inicio)
        j = self.vertices.index(fin)
        self.matriz[i][j] = 1
        if bidireccional:
            self.matriz[j][i] = 1
            
    def eliminar_vertice(self, vertice):
        if vertice not in self.vertices:
            return
        i = self.vertices.index(vertice)
        self.vertices.pop(i)
        self.matriz.pop(i)
        self._eliminar_columna(self.matriz, i)
    
    def _eliminar_columna(self, filas, i):
        if not filas:
            return
        filas[0].pop(i)
        self._eliminar_columna(filas[1:], i)
    
    def eliminar_arista(self, inicio, fin, bidireccional=True):
        if not inicio in self.vertices or not fin in self.vertices:
            return
        i = self.vertices.index(inicio)
        j = self.vertices.index(fin)
        if self.matriz[i][j] == 0:
            return
        self.matriz[i][j] = 0
        if bidireccional:
            self.matriz[j][i] = 0
        
    def es_vecino_de(self, vertice1, vertice2, bidireccional=True):
        if vertice1 not in self.vertices or vertice2 not in self.vertices:
            return False
        i = self.vertices.index(vertice1)
        j = self.vertices.index(vertice2)
        if bidireccional and (self.matriz[i][j] == 0 or self.matriz[j][i] == 0):
            return False
        if not bidireccional and self.matriz[i][j] == 0 and self.matriz[j][i] == 0:
            return False
        return True
    
    def vecinos_de(self, vertice, j=0, fila=None):
        if vertice not in self.vertices:
            return []
        i = self.vertices.index(vertice)
        if fila is None:
            fila = self.matriz[i]
        if j == len(fila):
            return []
        if fila[j] == 1:
            return [self.vertices[j]] + self.vecinos_de(vertice, j+1, fila)
        return self.vecinos_de(vertice, j+1, fila)
    
    def __str__(self):
        return f"Vértices: {str(self.vertices)}, Matriz de adyacencia: {str(self.matriz)}"
    
g = Grafo3()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("C", "D")
g.agregar_arista("D", "B")

print("Versión matriz de adyacencia: ")

print(g)

vertice1 = "B"
vertice2 = "D"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

g.eliminar_vertice("A")
g.eliminar_arista("B", "D")

print("Después de eliminar: ")

print(g)

vertice1 = "B"
vertice2 = "D"
print(f"¿{vertice1} es vecino de {vertice2}?: {g.es_vecino_de(vertice1, vertice2)}")

vertice = "B"
print(f"Vecinos de {vertice}: {g.vecinos_de(vertice)}")

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
mapa = Grafo2()
mapa.agregar_arista("A", "B", 4)  # Ruta A-B: 4km
mapa.agregar_arista("A", "C", 2)  # Ruta A-C: 2km
mapa.agregar_arista("C", "B", 1)  # Ruta C-B: 1km (Desvío más corto para ir de A a B)
mapa.agregar_arista("B", "D", 5)  # Ruta B-D: 5km
mapa.agregar_arista("C", "D", 8)  # Ruta C-D: 8km

# Ejecutamos Dijkstra saliendo desde la ciudad "A"
#distancias_minimas, arbol_padres = dijkstra(mapa, "A")

# Consultamos los resultados para llegar a la ciudad "D"
destino_final = "D"
#print(f"Distancia mínima desde A hasta {destino_final}: {distancias_minimas[destino_final]} km")

#ruta_optima = obtener_camino_exacto(arbol_padres, destino_final)
#print(f"Ruta óptima a seguir: {' -> '.join(ruta_optima)}")

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



