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

class Grafo_Dijkstra:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []
    def agregar_arista(self, inicio, fin, peso, bidireccional=False):
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
        self.lista_adyacencia[inicio].append((fin, peso))
        if bidireccional:
            self.lista_adyacencia[fin].append((inicio, peso))
    def eliminar_arista(self, inicio, fin, peso, lista_vertices=None):
        if lista_vertices is None:
            lista_vertices = list(self.lista_adyacencia)
        if not lista_vertices:
            return
        if inicio not in self.lista_adyacencia or fin not in self.lista_adyacencia:
            return
        if (fin, peso) not in self.lista_adyacencia[inicio] and \
            (inicio, peso) not in self.lista_adyacencia[fin]:
            return
        if lista_vertices[0] == inicio:
            self.lista_adyacencia[lista_vertices[0]].remove((fin, peso))
            return self.eliminar_arista(inicio, fin, peso, lista_vertices[1:])
        return self.eliminar_arista(inicio, fin, peso, lista_vertices[1:])
    def dijkstra(self, origen):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        dist[origen] = 0
        cola = [(0, origen)]
        visitados = set()
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            visitados.add(u)
            for v, peso in self.lista_adyacencia[u]:
                nueva = d + peso
                if nueva < dist[v]:
                    dist[v] = nueva
                    heapq.heappush(cola, (nueva, v))
        return dist 
    def dijkstra_camino(self, origen, destino):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        previo = {}
        dist[origen] = 0
        cola = [(0, origen)]
        visitados = set()
        while cola:
            d, u = heapq.heappop(cola)
            if u in visitados:
                continue
            visitados.add(u)
            for v, peso in self.lista_adyacencia[u]:
                if d + peso < dist[v]:
                    dist[v] = d + peso
                    previo[v] = u
                    heapq.heappush(cola, (dist[v], v))
        if dist[destino] == float("inf"):
            return None, float("inf")
        ruta = [destino]
        while ruta[-1] != origen:
            ruta.append(previo[ruta[-1]])
        return dist[destino], ruta[::-1] 
    def inalcanzables(self, origen):
        distancias = self.dijkstra(origen)
        return self._inalcanzables(list(distancias.items()))

    def _inalcanzables(self, items):
        if not items:
            return []
        vertice, distancia = items[0]
        if distancia == float("inf"):
            return [vertice] + self._inalcanzables(items[1:])
        return self._inalcanzables(items[1:])
    def __str__(self):
        return str(self.lista_adyacencia)

g = Grafo_Dijkstra({"A": [("B", 7), ("C", 2)],
         "B": [("D", 1)],
         "C": [("B", 3), ("D", 8)],
         "D": [("E", 2)],
         "E": []})

print("Distancias_minimas: ")
print(g.dijkstra("A"))

print("Camino más barato: ")
print(g.dijkstra_camino("A", "E"))

origen = "B"
print(f"Vértices inalcanzables para {origen}: ")
print(g.inalcanzables(origen))

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

class Mapa:
    distancias = [("Buenos Aires", "Rosario", 300), ("Buenos Aires", "Mar Del Plata", 400), 
                     ("Rosario", "Cordoba", 400), ("Buenos Aires", "Cordoba", 700),
                     ("Cordoba", "Mendoza", 650), ("Rosario", "Mendoza", 950)]
    def __init__(self):
        self.lista_adyacencia = {}
    def construir(self, aristas):
        if not aristas:
            return self.lista_adyacencia
        if aristas[0][0] not in self.lista_adyacencia and aristas[0][1] not in self.lista_adyacencia:
            self.lista_adyacencia[aristas[0][0]] = []
            self.lista_adyacencia[aristas[0][1]] = []
            self.lista_adyacencia[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
            self.lista_adyacencia[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
            return self.construir(aristas[1:])
        if aristas[0][0] not in self.lista_adyacencia and aristas[0][1] in self.lista_adyacencia:
            self.lista_adyacencia[aristas[0][0]] = []
            self.lista_adyacencia[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
            self.lista_adyacencia[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
            return self.construir(aristas[1:])
        if aristas[0][0] in self.lista_adyacencia and aristas[0][1] not in self.lista_adyacencia:
            self.lista_adyacencia[aristas[0][1]] = []
            self.lista_adyacencia[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
            self.lista_adyacencia[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
            return self.construir(aristas[1:])
        self.lista_adyacencia[aristas[0][1]].append((aristas[0][0], aristas[0][2]))
        self.lista_adyacencia[aristas[0][0]].append((aristas[0][1], aristas[0][2]))
        return self.construir(aristas[1:])
    def dijkstra(self, origen):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        dist[origen] = 0
        cola = [(0, origen)]
        visitados = set()
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            visitados.add(u)
            for v, peso in self.lista_adyacencia[u]:
                nueva = d + peso
                if nueva < dist[v]:
                    dist[v] = nueva
                    heapq.heappush(cola, (nueva, v))
        return dist 
    def dijkstra_camino(self, origen, destino):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        previo = {}
        dist[origen] = 0
        cola = [(0, origen)]
        visitados = set()
        while cola:
            d, u = heapq.heappop(cola)
            if u in visitados:
                continue
            visitados.add(u)
            for v, peso in self.lista_adyacencia[u]:
                if d + peso < dist[v]:
                    dist[v] = d + peso
                    previo[v] = u
                    heapq.heappush(cola, (dist[v], v))
        if dist[destino] == float("inf"):
            return None, float("inf")
        ruta = [destino]
        while ruta[-1] != origen:
            ruta.append(previo[ruta[-1]])
        return dist[destino], ruta[::-1] 
    def __str__(self):
        grafo = self.construir(self.distancias)
        return str(grafo)

mapa = Mapa()
print("Mapa completo de rutas y distancias: ")
print(mapa)

print("Distancias desde Buenos Aires: ")
print(mapa.dijkstra("Buenos Aires"))

print("Camino más corto desde Mar Del Plata a Mendoza")
print(mapa.dijkstra_camino("Mar Del Plata", "Mendoza"))

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
    "B": [("C", -2)],
    "C": [("A", 1)]
}

print(bellman_ford(grafo, "A"))
print(bellman_ford_camino(grafo, "A", "C"))

#Dijkstra
#Dijkstra +
#Bellman Ford
#add
#delete

from collections import deque

class GrafoConjuntos:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
    def agregar_vertice(self, vertice):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if vertice not in self.nodos:
            self.nodos.add(vertice)
    def agregar_arista(self, inicio, fin, peso, bidireccional=False):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
            
        # Conectamos inicio -> fin
        self.aristas[(inicio, fin)] = peso
        if bidireccional:
            self.aristas[(fin, inicio)] = peso
    def eliminar_vertice(self, vertice, l_aristas=None):
        if l_aristas is None:
            l_aristas = list(self.aristas)
        if not l_aristas:
            return
        # Si el nodo existe, lo borramos 
        if vertice in self.nodos:
            self.nodos.remove(vertice)
        #Si el vertice está involucrado en alguna conexión, borro esa conexión, sino, sigo de largo.
        if vertice in l_aristas[0]:
            self.aristas.remove(l_aristas[0])
            return self.eliminar_vertice(vertice, l_aristas[1:])
        return self.eliminar_vertice(vertice, l_aristas[1:])
    def eliminar_arista(self, arista, bidireccional=True):
        if arista in self.aristas:
            self.aristas.remove(arista)
            if bidireccional and arista[::-1] in self.aristas:
                self.aristas.remove(arista[::-1])
    def es_vecino_de(self, vertice1, vertice2, l_aristas=None):
        if l_aristas is None:
            l_aristas = list(self.aristas)
        if not l_aristas:
            return False
        if (vertice1, vertice2) == l_aristas[0] or (vertice2, vertice1) == l_aristas[0]:
            return True
        return self.es_vecino_de(vertice1, vertice2, l_aristas[1:])
    def vecinos_de(self, vertice, bidireccional=True, l_aristas=None, res=None):
        if l_aristas is None:
            l_aristas = list(self.aristas)
        if res is None:
            res = []
        if not l_aristas:
            return res
        if l_aristas[0][0] == vertice:
            if l_aristas[0][1] not in res:
                res.append(l_aristas[0][1])
            return self.vecinos_de(vertice, bidireccional, l_aristas[1:], res)
        if bidireccional:
            if l_aristas[0][1] == vertice:
                if l_aristas[0][0] not in res:
                    res.append(l_aristas[0][0])
                return self.vecinos_de(vertice, bidireccional, l_aristas[1:], res)
        return self.vecinos_de(vertice, bidireccional, l_aristas[1:], res)
    def vecinos(self, vertice, bidireccional=True, l_aristas=None):
        if l_aristas is None:
            l_aristas = list(self.aristas)
        if not l_aristas:
            return []
        arista = l_aristas[0]
        if arista[0] == vertice:
            return [(arista[1], self.aristas[arista])] + self.vecinos(vertice, bidireccional, l_aristas[1:])
        if bidireccional and arista[1] == vertice:
            return [(arista[0], self.aristas[arista])] + self.vecinos(vertice, bidireccional, l_aristas[1:])
        return self.vecinos(vertice, bidireccional, l_aristas[1:])
    def dijkstra_camino(self, origen, destino):
        dist = {nodo:float("inf") for nodo in self.nodos}
        previo = {}
        dist[origen] = 0
        cola = [(0, origen)]
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            if u == destino:
                break
            for v, peso in self.vecinos(u):
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
    def dijkstra_mejorado(self, inicio, destino):
        dist = {nodo: float("inf") for nodo in self.nodos}
        previo = {}
        dist[inicio] = 0
        cola = deque([inicio])
        while cola:
            u = cola.popleft()
            for v, peso in self.vecinos(u, bidireccional=False):
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    previo[v] = u
                    if v not in cola:
                        cola.append(v)
        if dist[destino] == float("inf"):
            return None, float("inf")
        camino = [destino]
        while camino[-1] != inicio:
            camino.append(previo[camino[-1]])
        return camino[::-1], dist[destino]
    def dijkstra_mejorado_recursivo(self, inicio, destino):
        dist = {nodo: float("inf")for nodo in self.nodos}
        previo = {}
        dist[inicio] = 0
        cola = deque([inicio])
        self._dijkstra_rec(cola, dist, previo)
        if dist[destino] == float("inf"):
            return None, float("inf")
        camino = [destino]
        while camino[-1] != inicio:
            camino.append(previo[camino[-1]])
        return camino[::-1], dist[destino]
    def _dijkstra_rec(self, cola, dist, previo):
        if not cola:
            return
        u = cola.popleft()
        vecinos = self.vecinos(u, bidireccional=False)
        self._procesar_vecinos(u, vecinos, cola, dist, previo)
        self._dijkstra_rec(cola, dist, previo)
    def _procesar_vecinos(self, u, vecinos, cola, dist, previo):
        if not vecinos:
            return
        v, peso = vecinos[0]
        if dist[u] + peso < dist[v]:
            dist[v] = dist[u] + peso
            previo[v] = u
            if v not in cola:
                cola.append(v)
        self._procesar_vecinos(u, vecinos[1:], cola, dist, previo)
    def bellman_ford_camino(self, origen, destino):
        dist = {nodo: float("inf") for nodo in self.nodos}
        previo = {}
        dist[origen] = 0
        n = len(self.nodos)
        # Relajación
        for _ in range(n - 1):
            for u in self.nodos:
                for v, peso in self.vecinos(u, bidireccional=False):
                    if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                        dist[v] = dist[u] + peso
                        previo[v] = u
        # Detección de ciclo negativo
        for u in self.nodos:
            for v, peso in self.vecinos(u, bidireccional=False):
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
    def __str__(self):
        return f"Aristas:{str(self.aristas)}, vértices:{str(self.nodos)}"
    
g = GrafoConjuntos()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

g.agregar_arista("A", "B", -5)
g.agregar_arista("A", "C", 1)
g.agregar_arista("B", "D", 4)
g.agregar_arista("C", "D", 4)

print(g)

print(g.es_vecino_de("A", "D"))
print(g.vecinos_de("A"))

print("Dijkstra: ")
#print(g.dijkstra_camino("A", "D"))

print("Dijkstra mejorado: ")
print(g.dijkstra_mejorado("A", "D"))

print(g.bellman_ford_camino("A", "D"))

vertices = ["S", "A", "B", "C", "D"]

aristas = [("C", "D", -1), ("A", "D", 5), ("B", "D", 8), ("A", "C", 4),("B", "A", -2),
    ("S", "A", 6),("S", "B", 3), ("D", "A", -3)]


def relajar(u, v, peso, distancia, predecesor):
    if distancia[u] == float("inf"):
        return False
    nueva = distancia[u] + peso
    if nueva < distancia[v]:
        distancia[v] = nueva
        predecesor[v] = u
        return True
    return False

def bellman_ford(vertices, aristas, origen):
    distancia = {v: float("inf") for v in vertices}
    predecesor = {v: None for v in vertices}
    distancia[origen] = 0
    for pasada in range(len(vertices)-1):
        hubo_cambios = False
        for u, v, peso in aristas:
            if relajar(u, v, peso, distancia, predecesor):
                hubo_cambios = True
        if not hubo_cambios:
            break
    for u, v, peso in aristas:
        if relajar(u, v, peso, distancia, predecesor):
            return distancia, predecesor, True
    return distancia, predecesor, False

print(bellman_ford(vertices, aristas, "A"))

def reconstruir_camino(predecesor, distancia, destino):
    if distancia[destino] == float('inf'):
        return None
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = predecesor[actual]
    return camino[::-1]

distancia, predecesor, hay_ciclo = bellman_ford(vertices, aristas, "D")
if hay_ciclo:
    print("Hay un ciclo negativo alcanzable")
else:
    for v in vertices:
        camino = reconstruir_camino(predecesor, distancia, v)
        print(v, distancia[v], camino)
       
def bellman_ford_camino(vertices, aristas, origen, destino):
    distancia, predecesor, ciclo = bellman_ford(vertices, aristas, origen)
    if ciclo:
        raise ValueError("El grafo tiene un ciclo negativo")
    camino = reconstruir_camino(predecesor, distancia, destino)
    if camino is None:
        return [], float("inf")
    return (camino, distancia[destino])

print(bellman_ford_camino(vertices, aristas, "S", "D"))
       
#ejercicios:

def distancias_minimas(vertices, aristas, origen):
    distancia = {v: float('inf') for v in vertices}
    distancia[origen] = 0
    for _ in range(len(vertices) - 1):
        for u, v, peso in aristas:
            if distancia[u] == float('inf'):
                continue
            if distancia[u] + peso < distancia[v]:
                distancia[v] = distancia[u] + peso
    return distancia
    
print(distancias_minimas(vertices, aristas, "S"))

def bellman_ford_con_ciclos(vertices, aristas, origen):
    distancia = distancias_minimas(vertices, aristas, origen)
    for u, v, peso in aristas:
        if distancia[u] == float('inf'):
            continue                  # no alcanzable: no cuenta
        if distancia[u] + peso < distancia[v]:
            return distancia, True      # todavía mejora: ciclo
    return distancia, False    

print(bellman_ford_con_ciclos(vertices, aristas, "S"))

#1)
cuentas = ["banco", "bill_a", "bill_b", "bill_c", "tienda"]

transferencias = [("banco", "bill_a", 40), ("banco", "bill_b", 25), ("bill_a", "tienda", 30), 
           ("bill_b", "bill_c", -20),("bill_c", "bill_a", 10), ("bill_c", "tienda", 60),
           ("bill_b", "tienda", 70)]

def costo_minimo(cuentas, transferencias, origen, destino):
    distancia, predecesor, ciclo = bellman_ford(cuentas, transferencias, origen)
    if ciclo:
        return None
    camino = reconstruir_camino(predecesor, distancia, destino)
    if camino is None:
        return [], float("inf")
    return (distancia[destino], camino)


print(costo_minimo(cuentas, transferencias, "banco", "tienda"))
#salida: (45, ['banco', 'bill_b', 'bill_c', 'bill_a', 'tienda'])

transferencias = [("banco", "bill_a", 40), ("banco", "bill_b", 25), ("bill_a", "tienda", 30), 
           ("bill_b", "bill_c", -20),("bill_c", "bill_a", 10), ("bill_c", "tienda", 60),
           ("bill_b", "tienda", 70), ("bill_a", "bill_b", -30)]

print(costo_minimo(cuentas, transferencias, "banco", "tienda"))
#En este caso, hay ciclo negativo entre bill_a, bill_b y bill_c
#salida: None

#2)
vertices = ["S", "A", "B", "C", "D"]

aristas = [("C", "D", 1), ("B", "A", -2), ("A", "C", 2),
    ("S", "A", 3),("S", "B", 4)]

lista_adyacencia = {"S": [("A", 3), ("B", 4)],
                    "A": [("C", 2)],
                    "B": [("A", -2)],
                    "C": [("D", 1)],
                    "D": []}
def costo_minimo(vertices, aristas, origen, destino):
    distancia, predecesor, ciclo = bellman_ford(vertices, aristas, origen)
    if ciclo:
        return None
    camino = reconstruir_camino(predecesor, distancia, destino)
    if camino is None:
        return [], float("inf")
    return (distancia[destino], camino)

print(costo_minimo(vertices, aristas, "S", "D"))

def dijkstra_camino(lista_adyacencia, origen, destino):
    dist = {nodo:float("inf") for nodo in lista_adyacencia}
    previo = {}
    dist[origen] = 0
    cola = [(0, origen)]
    visitados = set()
    while cola:
        d, u = heapq.heappop(cola)
        if u in visitados:
            continue
        visitados.add(u)
        for v, peso in lista_adyacencia[u]:
            if d + peso < dist[v]:
                dist[v] = d + peso
                previo[v] = u
                heapq.heappush(cola, (dist[v], v))
    if dist[destino] == float("inf"):
        return None, float("inf")
    ruta = [destino]
    while ruta[-1] != origen:
        ruta.append(previo[ruta[-1]])
    return dist[destino], ruta[::-1]      

#Dijkstra con peso negativo:
print(dijkstra_camino(lista_adyacencia, "S", "D"))
#Dijkstra falla porque cuando un nodo sale de la cola de prioridad, su distancia ya es definitiva.
#Entonces, no tiene en cuenta el -2.

#Cambio B -> A por +2:
aristas = [("C", "D", 1), ("B", "A", 2), ("A", "C", 2),
    ("S", "A", 3),("S", "B", 4)]

lista_adyacencia = {"S": [("A", 3), ("B", 4)],
                    "A": [("C", 2)],
                    "B": [("A", 2)],
                    "C": [("D", 1)],
                    "D": []}

print(costo_minimo(vertices, aristas, "S", "D"))
print(dijkstra_camino(lista_adyacencia, "S", "D"))
#Con B -> A = +2, los dos algoritmos coinciden porque todos los pesos son positivos.

class GrafoConjuntos2:
    def __init__(self, vertices, aristas):
        self.vertices = vertices
        self.aristas = aristas
    def agregar_vertice(self, vertice):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if vertice not in self.vertices:
            self.vertices.append(vertice)
    def agregar_arista(self, inicio, fin, peso, bidireccional=False):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
            
        # Conectamos inicio -> fin
        self.aristas.append((inicio, fin, peso))
        if bidireccional:
            self.aristas.append((fin, inicio, peso))
    def eliminar_arista(self, inicio, fin, peso, bidireccional=False):
        if (inicio, fin, peso) not in self.aristas:
            return
        self.aristas.remove((inicio, fin, peso))
        if bidireccional:
            self.aristas.remove((inicio, fin, peso))
    def relajar(self, u, v, peso, distancia, predecesor):
        if distancia[u] == float("inf"):
            return False
        nueva = distancia[u] + peso
        if nueva < distancia[v]:
            distancia[v] = nueva
            predecesor[v] = u
            return True
        return False
    def bellman_ford(self, origen):
        distancia = {v: float("inf") for v in self.vertices}
        predecesor = {v: None for v in self.vertices}
        distancia[origen] = 0
        for pasada in range(len(self.vertices)-1):
            hubo_cambios = False
            for u, v, peso in self.aristas:
                if self.relajar(u, v, peso, distancia, predecesor):
                    hubo_cambios = True
            if not hubo_cambios:
                break
        for u, v, peso in self.aristas:
            if self.relajar(u, v, peso, distancia, predecesor):
                return distancia, predecesor, True
        return distancia, predecesor, False
    def reconstruir_camino(self, predecesor, distancia, destino):
        if distancia[destino] == float('inf'):
            return None
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = predecesor[actual]
        return camino[::-1]
    def costo_minimo(self, origen, destino):
        distancia, predecesor, ciclo = self.bellman_ford(origen)
        if ciclo:
            return None
        camino = self.reconstruir_camino(predecesor, distancia, destino)
        if camino is None:
            return [], float("inf")
        return (distancia[destino], camino)
    def distancias_minimas(self, origen):
        distancia = {v: float('inf') for v in self.vertices}
        distancia[origen] = 0
        for _ in range(len(self.vertices) - 1):
            for u, v, peso in self.aristas:
                if distancia[u] == float('inf'):
                    continue
                if distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
        return distancia
    def bellman_ford_con_ciclos(self, origen):
        distancia = self.distancias_minimas(self.vertices, self.aristas, origen)
        for u, v, peso in self.aristas:
            if distancia[u] == float('inf'):
                continue                  # no alcanzable: no cuenta
            if distancia[u] + peso < distancia[v]:
                return distancia, True      # todavía mejora: ciclo
        return distancia, False 
    def mostrar(self, origen):
        distancia, predecesor, hay_ciclo = self.bellman_ford(origen)
        if hay_ciclo:
            print("Hay un ciclo negativo alcanzable")
        else:
            lineas = []
            for v in self.vertices:
                camino = self.reconstruir_camino(predecesor, distancia, v)
                lineas.append(f"{v} {distancia[v]} {camino}")
        return "\n".join(lineas)
    def __str__(self):
        return str(self.mostrar("S"))
    
g = GrafoConjuntos2(["S", "A", "B", "C", "D"], 
    [("C", "D", 1), ("B", "A", -2), ("A", "C", 2), ("S", "A", 3),("S", "B", 4)])

gd = Grafo_Dijkstra({"S": [("A", 3), ("B", 4)],
                    "A": [("C", 2)],
                    "B": [("A", -2)],
                    "C": [("D", 1)],
                    "D": []})

print("Con peso negativo: ")
print(f"Bellman Ford: {g.costo_minimo('S', 'D')}")
print(f"Dijkstra: {gd.dijkstra_camino('S', 'D')}")

g.eliminar_arista("B", "A", -2)
g.agregar_arista("B", "A", 2)
gd.eliminar_arista("B", "A", -2)
gd.agregar_arista("B", "A", 2)

print("Sin peso negativo: ")
print(f"Bellman Ford: {g.costo_minimo('S', 'D')}")
print(f"Dijkstra: {gd.dijkstra_camino('S', 'D')}")

print(g)
    
class Comercio:
    def __init__(self, cuentas, transferencias):
        self.cuentas = cuentas
        self.transferencias = transferencias
    def agregar_cuenta(self, cuenta):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if cuenta not in self.cuentas:
            self.cuentas.append(cuenta)
    def agregar_transferencia(self, inicio, fin, comision, reintegro, bidireccional=False):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_cuenta(inicio)
        self.agregar_cuenta(fin)
            
        # Conectamos inicio -> fin
        self.transferencias.append((inicio, fin, comision, reintegro))
        if bidireccional:
            self.transferencias.append((fin, inicio, comision, reintegro))
    def relajar(self, u, v, comision, reintegro, distancia, predecesor):
        if distancia[u] == float("inf"):
            return False
        nueva = distancia[u] + comision - reintegro
        if nueva < distancia[v]:
            distancia[v] = nueva
            predecesor[v] = u
            return True
        return False
    def bellman_ford(self, origen):
        distancia = {v: float("inf") for v in self.cuentas}
        predecesor = {v: None for v in self.cuentas}
        distancia[origen] = 0
        for pasada in range(len(self.cuentas)-1):
            hubo_cambios = False
            for u, v, comision, reintegro in self.transferencias:
                if self.relajar(u, v, comision, reintegro, distancia, predecesor):
                    hubo_cambios = True
            if not hubo_cambios:
                break
        for u, v, comision, reintegro in self.transferencias:
            if self.relajar(u, v, comision, reintegro, distancia, predecesor):
                return distancia, predecesor, True
        return distancia, predecesor, False
    def reconstruir_camino(self, predecesor, distancia, destino):
        if distancia[destino] == float('inf'):
            return None
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = predecesor[actual]
        return camino[::-1]
    def costo_minimo(self, origen, destino):
        distancia, predecesor, ciclo = self.bellman_ford(origen)
        if ciclo:
            return None
        camino = self.reconstruir_camino(predecesor, distancia, destino)
        if camino is None:
            return [], float("inf")
        return (distancia[destino], camino)
    def __str__(self):
        return f"Cuentas:{str(self.cuentas)}, Transferencias:{str(self.transferencias)}"
    
c = Comercio(["banco", "bill_a", "bill_b", "bill_c", "tienda"],
             [("banco", "bill_a", 40, 0), ("banco", "bill_b", 25, 0), 
              ("bill_a", "tienda", 30, 0), ("bill_b", "bill_c", 15, 35),
              ("bill_c", "bill_a", 10, 0), ("bill_c", "tienda", 60, 0),
              ("bill_b", "tienda", 70, 0)])

print(c.costo_minimo("banco", "tienda"))

c.agregar_transferencia("bill_a", "bill_b", 10, 30)

print(c.costo_minimo("banco", "tienda"))

#Binary heap