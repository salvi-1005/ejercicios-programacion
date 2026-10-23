grafo = {"A": [("B", 4), ("C", 1)],
         "B": [("D", 1)],
         "C": [("B", 2), ("D", 5)],
         "D": []}

for vecino, peso in grafo["C"]:
    print(vecino, peso)
    
import heapq
def dijkstra(grafo, origen):
    dist = {nodo:float("inf") for nodo in grafo}
    dist[origen] = 0
    cola = [(0, origen)]
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist[u]:
            continue
        for v, peso in grafo[u]:
            nueva = d + peso
            if nueva < dist[v]:
                dist[v] = nueva
                heapq.heappush(cola, (nueva, v))
    return dist           

print(dijkstra(grafo, "A"))

#Ejercicios)
#1)
grafo = {"A": [("B", 7), ("C", 2)],
         "B": [("D", 1)],
         "C": [("B", 3), ("D", 8)],
         "D": [("E", 2)],
         "E": []}
#2)
print(dijkstra(grafo, "A"))
# B no vale 7 porque si voy de A a C y de C a B, el costo total es 5, que es menor a 7

#3)
def dijkstra_camino(grafo, origen, destino):
    dist = {nodo:float("inf") for nodo in grafo}
    previo = {}
    dist[origen] = 0
    cola = [(0, origen)]
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist[u]:
            continue
        for v, peso in grafo[u]:
            if d + peso < dist[v]:
                dist[v] = d + peso
                previo[v] = u
                heapq.heappush(cola, (dist[v], v))
    if dist[destino] == float("inf"):
        return None, float("inf")
    ruta = [destino]
    while ruta[-1] != origen:
        ruta.append(previo[ruta[-1]])
    return ruta[::-1], dist[destino]               

print(dijkstra_camino(grafo, "A", "E"))

#4)
def construir(aristas, lista = None):
    if lista is None:
        lista = {}
    if not aristas:
        return lista
    if aristas[0][0] not in lista and aristas[0][1] not in lista:
        lista[aristas[0][0]] = []
        lista[aristas[0][1]] = []
        lista[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
        lista[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
        return construir(aristas[1:], lista)
    if aristas[0][0] not in lista and aristas[0][1] in lista:
        lista[aristas[0][0]] = []
        lista[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
        lista[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
        return construir(aristas[1:], lista)
    if aristas[0][0] in lista and aristas[0][1] not in lista:
        lista[aristas[0][1]] = []
        lista[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
        lista[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
        return construir(aristas[1:], lista)
    lista[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
    lista[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
    return construir(aristas[1:], lista)  

grafo_mapa = construir([("Buenos Aires", "Rosario", 300), ("Buenos Aires", "Mar Del Plata", 400), 
                 ("Rosario", "Cordoba", 400), ("Buenos Aires", "Cordoba", 700),
                 ("Cordoba", "Mendoza", 650), ("Rosario", "Mendoza", 950)])

print("Grafo con lista de adyacencia: ")
print(grafo_mapa)

print("Distancias desde Buenos Aires: ")
print(dijkstra(grafo_mapa, "Buenos Aires"))

print("Camino más corto desde Mar Del Plata a Mendoza")
print(dijkstra_camino(grafo_mapa, "Mar Del Plata", "Mendoza"))

#5)
def inalcanzables(grafo, origen):
    distancias = dijkstra(grafo, origen)
    return _inalcanzables(list(distancias.items()))

def _inalcanzables(items):
    if not items:
        return []
    vertice, distancia = items[0]
    if distancia == float("inf"):
        return [vertice] + _inalcanzables(items[1:])
    return _inalcanzables(items[1:])
    

g5 = {
    "A": [("B", 1)],
    "B": [("C", 2)],
    "C": [],
    "D": [("A", 4)],
    "E": []
    }

origen = "A"
print(f"Vértices inalcanzables para {origen}: ")
print(inalcanzables(g5, origen))

#Bellman Ford

def bellman_ford(grafo, origen):
    dist = {nodo: float("inf") for nodo in grafo}
    dist[origen] = 0
    n = len(grafo)
    # Relajación
    for _ in range(n - 1):
        for u in grafo:
            for v, peso in grafo[u]:
                if dist[u] != float("inf") and \
                   dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
    # Detección de ciclo negativo
    for u in grafo:
        for v, peso in grafo[u]:
            if dist[u] != float("inf") and \
               dist[u] + peso < dist[v]:
                raise ValueError("El grafo tiene un ciclo negativo")
    return dist

def bellman_ford_camino(grafo, origen, destino):
    dist = {nodo: float("inf") for nodo in grafo}
    previo = {}
    dist[origen] = 0
    n = len(grafo)
    # Relajación
    for _ in range(n - 1):
        for u in grafo:
            for v, peso in grafo[u]:
                if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    previo[v] = u
    # Detección de ciclo negativo
    for u in grafo:
        for v, peso in grafo[u]:
            if dist[u] != float("inf") and \
               dist[u] + peso < dist[v]:
                raise ValueError("El grafo tiene un ciclo negativo")
    # Destino inalcanzable
    if dist[destino] == float("inf"):
        return None, float("inf")
    # Reconstrucción del camino
    camino = [destino]
    while camino[-1] != origen:
        camino.append(previo[camino[-1]])
    camino.reverse()
    return camino, dist[destino]

grafo = {
    "A": [("B", 1)],
    "B": [("C", -3)],
    "C": [("A", 1)]
}

print(bellman_ford(grafo, "A"))
print(bellman_ford_camino(grafo, "A", "E"))