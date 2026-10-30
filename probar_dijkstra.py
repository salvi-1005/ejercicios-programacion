
from pathlib import Path
import heapq
import osmnx as ox
import networkx as nx

# Archivo del mapa vial
CARPETA = Path(__file__).resolve().parent
ARCHIVO_MAPA = CARPETA / "calles_ruta_principal.graphml"

class Mapa:

    def __init__(self, archivo):
        self.grafo = ox.load_graphml(archivo)

    def nodos(self):
        return self.grafo.nodes

    def vecinos(self, nodo):
        return list(self.grafo.nodes[nodo])

class Dijkstra:

    def __init__(self, mapa):
        self.mapa = mapa

    def camino_minimo(self, origen, destino):
        # 1. Inicializar las distancias
            dist = {nodo: float("inf") for nodo in self.mapa.grafo.nodes}
            previo = {}
        
            dist[origen] = 0
            cola = [(0, origen)]
        
            # 2. Procesar primero el nodo con menor distancia
            while cola:
                distancia_actual, u = heapq.heappop(cola)
        
                # Ignorar entradas antiguas de la cola
                if distancia_actual > dist[u]:
                    continue
        
                # Si llegamos al destino, podemos terminar
                if u == destino:
                    break
        
                # 3. Relajar las aristas que salen de u
                for v, datos in self.mapa.grafo[u].items():
                    for clave, atributos in datos.items():
                        peso = atributos.get("length")
        
                        if peso is None:
                            continue
        
                        nueva_distancia = distancia_actual + float(peso)
        
                        if nueva_distancia < dist[v]:
                            dist[v] = nueva_distancia
                            previo[v] = u
                            heapq.heappush(
                                cola,
                                (nueva_distancia, v)
                            )
        
            # Si no se pudo llegar al destino
            if dist[destino] == float("inf"):
                return None, float("inf")
        
            # Reconstruir el camino desde el destino
            ruta = [destino]
        
            while ruta[-1] != origen:
                ruta.append(previo[ruta[-1]])
        
            ruta.reverse()
        
            return Ruta(ruta, dist[destino])

class Ruta:
    def __init__(self, nodos, distancia):
        self.nodos = nodos
        self.distancia = distancia
    @property
    def cantidad_nodos(self):
        return len(self.nodos)
    @property
    def _distancia(self):
        return self.distancia
    def __str__(self):
        return (
            f"Nodos: {self.cantidad_nodos}\n"
            f"Distancia: {self.distancia/1000:.2f} km"
        )

def main():
    if not ARCHIVO_MAPA.exists():
        print("No se encontró el archivo del mapa vial.")
        return

    print("Cargando el mapa vial de San Martín...")
    G = ox.load_graphml(ARCHIVO_MAPA)

    # Origen: UNSAM, Campus Miguelete
    lat_origen = -34.579839
    lon_origen = -58.526695

    # Destino: zona de Villa Ballester
    lat_destino = -34.54947
    lon_destino = -58.54786

    # Encontrar los nodos viales más cercanos
    origen = ox.distance.nearest_nodes(
        G, X=lon_origen, Y=lat_origen
    )

    destino = ox.distance.nearest_nodes(
        G, X=lon_destino, Y=lat_destino
    )

    mapa = Mapa(ARCHIVO_MAPA)

    dijkstra = Dijkstra(mapa)

    print("Calculando la ruta más corta con Dijkstra...")

    try:
        ruta = dijkstra.camino_minimo(origen, destino)

        if ruta is None:
            print("No se encontró una ruta entre esos puntos.")
            return

        print("\n=== RUTA MÁS CORTA EN SAN MARTÍN ===")
        print(f"Nodos de la ruta: {ruta.cantidad_nodos}")
        print(f"Distancia total: {ruta._distancia / 1000:.2f} km")

    except (KeyError, nx.NetworkXError) as error:
        print(f"No se pudo calcular la ruta: {error}")


if __name__ == "__main__":
    main()


