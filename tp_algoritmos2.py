class Ruta:
    def __init__(self, destino, distancia, riesgo):
        self.destino = destino
        self.distancia = distancia
        self.riesgo = riesgo
    def costo(self):
        return self.distancia + 5 * self.riesgo
    def __repr__(self):
        return f"distancia: {self.distancia}, riesgo: {self.riesgo}"

Cusco_Anta = Ruta("Anta", 20, 8)
Cusco_Chinchero = Ruta("Chinchero", 15, 2)
Anta_Ollantaytambo = Ruta("Ollantaytambo", 25, 8)
Chinchero_Urubamba = Ruta("Urubamba", 20, 1)
Urubamba_Pachar = Ruta("Pachar", 10, 1)
Pachar_Ollantaytambo = Ruta("Ollantaytambo", 8, 1)

import heapq

class Grafo:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def dijkstra(self, origen):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        dist[origen] = 0
        cola = [(0, origen)]
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            for v, distancia, riesgo in self.lista_adyacencia[u]:
                peso = distancia + 5 * riesgo
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
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            for v, distancia, riesgo in self.lista_adyacencia[u]:
                peso = distancia + 5 * riesgo
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
    def __str__(self):
        return str(self.lista_adyacencia)

grafo = Grafo({"Cusco": [("Chinchero", 15, 2), ("Anta", 20, 8)],
         "Anta": [("Cusco", 20, 8), ("Ollantaytambo", 25, 8)],
         "Urubamba": [("Chinchero", 20, 1), ("Pachar", 10, 1)],
         "Chinchero": [("Cusco", 15, 2), ("Urubamba", 20, 1)],
         "Pachar": [("Urubamba", 10, 1), ("Ollantaytambo", 8, 1)],
         "Ollantaytambo": [("Anta", 25, 8), ("Pachar", 8, 1)]})

#print(grafo)
print("Costo desde Cusco hasta las demás ciudades: ")
print(grafo.dijkstra("Cusco"))

print("Costo total desde Cusco hasta Ollantaytambo: ")
print(grafo.dijkstra_camino("Cusco", "Ollantaytambo"))


