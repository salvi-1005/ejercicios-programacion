import heapq
from guia_arboles import arbol_binario_genericos, Nodo

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
    def listar_nodos(self, vertices=None):
        if vertices is None:
            vertices = sorted(list(self.conjunto_vertices))
        if not vertices:
            return
        print(vertices[0])
        self.listar_nodos(vertices[1:])
    def __str__(self):
        return f"Aristas:{str(self.conjunto_adyacencias)}, vértices:{str(self.conjunto_vertices)}"
        
g = Grafo1()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")
g.agregar_vertice("E")
g.agregar_vertice("F")

g.listar_nodos()

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
    def __init__(self, lista_adyacencia=None):
        # El diccionario almacenará: { nodo: [vecino1, vecino2, ...] }
        if lista_adyacencia is None:
            self.lista_adyacencia = {}
        else:
            self.lista_adyacencia = lista_adyacencia

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
    
    def listar_nodos(self, vertices=None):
        if vertices is None:
            vertices = sorted(list(self.lista_adyacencia))
        if not vertices:
            return
        print(vertices[0])
        self.listar_nodos(vertices[1:])
        
    def es_completo(self, vertices=None):
        if vertices is None:
            vertices = list(self.lista_adyacencia)
        if not vertices:
            return True
        v = vertices[0]
        # Detecta paralelas
        if len(self.lista_adyacencia[v]) != len(set(self.lista_adyacencia[v])):
            return False
        # Detecta bucles
        if v in self.lista_adyacencia[v]:
            return False
        vecinos = set(self.lista_adyacencia[v])
        esperado = set(self.lista_adyacencia)
        esperado.remove(v)
        if vecinos != esperado:
            return False
        return self.es_completo(vertices[1:])
    def _sin_aristas(self, v, vertices):
        if not vertices:
            return True
        if vertices[0] in self.lista_adyacencia[v]:
            return False
        return self._sin_aristas(v, vertices[1:])
    def _verificar_conjunto(self, vertices):
        if len(vertices) <= 1:
            return True
        if not self._sin_aristas(vertices[0], vertices[1:]):
            return False
        return self._verificar_conjunto(vertices[1:])
    def es_bipartito(self, conjunto1, conjunto2):
        return (self._verificar_conjunto(list(conjunto1)) and
        self._verificar_conjunto(list(conjunto2)))
    def _conectado_con_todos(self, u, vertices):
        if not vertices:
            return True
        if vertices[0] not in self.lista_adyacencia[u]:
            return False
        return self._conectado_con_todos(u, vertices[1:])
    def _es_bipartito_completo(self, vertices1, vertices2):
        if not vertices1:
            return True
        if not self._conectado_con_todos(vertices1[0], vertices2):
            return False
        return self._es_bipartito_completo(vertices1[1:], vertices2)
    def es_bipartito_completo(self, conjunto1, conjunto2):
        if not self.es_bipartito(conjunto1, conjunto2):
            return False
        return self._es_bipartito_completo(list(conjunto1), list(conjunto2))
    def _agregar_actual(self, actual, caminos):
        if not caminos:
            return []
        return ([[actual] + caminos[0]] + self._agregar_actual(actual, caminos[1:]))
    def _explorar_vecinos2(self, actual, vecinos, longitud, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        resultado = []
        if vecino not in visitados:
            caminos = self._caminos(vecino, longitud - 1, visitados | {vecino})
            resultado = self._agregar_actual(actual, caminos)
        return (resultado + self._explorar_vecinos2(actual, vecinos[1:], longitud, visitados))
    def caminos(self, origen, longitud):
        return self._caminos(origen, longitud, visitados=None)
    def _caminos(self, actual, longitud, visitados):
        if visitados is None:
            visitados = {actual}
        if longitud == 0:
            return [[actual]]
        return self._explorar_vecinos2(actual, self.lista_adyacencia[actual], longitud, visitados)
    def dfs(self, origen):
        return self._dfs(origen, set())
    def _dfs(self, actual, visitados):
        if actual in visitados:
            return []
        visitados.add(actual)
        return [actual] + self._dfs_vecinos(self.lista_adyacencia[actual], visitados)
    def _dfs_vecinos(self, vecinos, visitados):
        if not vecinos:
            return []
        return (self._dfs(vecinos[0], visitados) + self._dfs_vecinos(vecinos[1:], visitados))
    def dfs_cola(self, origen):
        return self._dfs_cola(origen, set(), [])
    def _dfs_cola(self, actual, visitados, recorrido):
        if actual in visitados:
            return recorrido
        visitados.add(actual)
        recorrido.append(actual)
        return self._dfs_vecinos_cola(self.lista_adyacencia[actual], visitados, recorrido)
    def _dfs_vecinos_cola(self, vecinos, visitados, recorrido):
        if not vecinos:
            return recorrido
        self._dfs_cola(vecinos[0], visitados, recorrido)
        return self._dfs_vecinos_cola(vecinos[1:], visitados, recorrido)
    def bfs(self, origen):
        return self._bfs([origen], set(), [])
    def _bfs(self, cola, visitados, recorrido):
        if not cola:
            return recorrido
        actual = cola[0]
        resto = cola[1:]
        if actual in visitados:
            return self._bfs(resto, visitados, recorrido)
        visitados.add(actual)
        return self._bfs(resto + self.lista_adyacencia[actual], visitados, recorrido + [actual])
    def conectados(self, origen):
        return self.dfs(origen)
    def es_conexo(self):
        if not self.lista_adyacencia:
            return True
        origen = list(self.lista_adyacencia)[0]
        visitados = self.dfs(origen)
        return len(visitados) == len(self.lista_adyacencia)
    def vecinos(self, vertice):
        return self.lista_adyacencia[vertice]
    def camino_sin_ciclos(self, inicio, fin, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio == fin:
            return [inicio]
        visitados.add(inicio)
        return self._camino_sin_ciclos_vecinos(inicio, fin, self.vecinos(inicio), visitados)
    def _camino_sin_ciclos_vecinos(self, actual, destino, vecinos, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        if vecino not in visitados:
            camino = self.camino_sin_ciclos(vecino, destino, visitados | {vecino})
            if camino:
                return [actual] + camino
        return self._camino_sin_ciclos_vecinos(actual, destino, vecinos[1:], visitados)
    
    def __str__(self):
        return f"Lista de adyacencia: {str(self.lista_adyacencia)}"

g = Grafo2()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

g.listar_nodos()

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")
g.agregar_arista("C", "D")

print("¿Es completo el grafo?")
print(g.es_completo())

print("¿Es bipartito el grafo?")
print(g.es_bipartito(("A", "D"), ("C", "B")))

print("¿Es bipartito completo el grafo?")
print(g.es_bipartito_completo(("A", "D"), ("C", "B")))

origen = "A"
longitud = 3
print(f"Caminos desde {origen} de longitud {longitud}")
print(g.caminos(origen, longitud))

print("Recorrido DFS: ")
print(g.dfs("A"))

print("Recorrido BFS: ")
print(g.bfs("A"))

print("Camino sin ciclos: ")
print(g.camino_sin_ciclos("A", "D"))

print("¿Es conexo el grafo 2?")
print(g.es_conexo())

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

    def agregar_arista(self, inicio, fin, peso, bidireccional=True):
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
        i = self.vertices.index(inicio)
        j = self.vertices.index(fin)
        self.matriz[i][j] = peso
        if bidireccional:
            self.matriz[j][i] = peso
            
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
    def listar_nodos(self, l_vertices=None):
        if l_vertices is None:
            l_vertices = sorted(self.vertices)
        if not l_vertices:
            return
        print(l_vertices[0])
        self.listar_nodos(l_vertices[1:])
    def vecinos(self, vertice):
        i = self.vertices.index(vertice)
        return self._vecinos(i, 0)
    def _vecinos(self, fila, columna):
        if columna == len(self.vertices):
            return []
        if self.matriz[fila][columna] == 1:
            return [self.vertices[columna]] + self._vecinos(fila, columna + 1)
        return self._vecinos(fila, columna + 1)
    def _agregar_actual(self, actual, caminos):
        if not caminos:
            return []
        return ([[actual] + caminos[0]] + self._agregar_actual(actual, caminos[1:]))
    def _explorar_vecinos(self, actual, vecinos, longitud, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        resultado = []
        if vecino not in visitados:
            caminos = self._caminos(vecino, longitud - 1, visitados | {vecino})
            resultado = self._agregar_actual(actual, caminos)
        return (resultado + self._explorar_vecinos(actual, vecinos[1:], longitud, visitados))
    def caminos(self, origen, longitud):
        return self._caminos(origen, longitud, {origen})
    def _caminos(self, actual, longitud, visitados):
        if longitud == 0:
            return [[actual]]
        return self._explorar_vecinos(actual, self.vecinos(actual), longitud, visitados)
    def _dfs_vecinos(self, vecinos, visitados):
        if not vecinos:
            return []
        return (self._dfs(vecinos[0], visitados) + self._dfs_vecinos(vecinos[1:], visitados))
    def dfs(self, origen):
        return self._dfs(origen, set())
    def _dfs(self, actual, visitados):
        if actual in visitados:
            return []
        visitados.add(actual)
        return [actual] + self._dfs_vecinos(self.vecinos(actual), visitados)
    def bfs(self, origen):
        return self._bfs([origen], set(), [])
    def _bfs(self, cola, visitados, recorrido):
        if not cola:
            return recorrido
        actual = cola[0]
        resto = cola[1:]
        if actual in visitados:
            return self._bfs(resto, visitados, recorrido)
        visitados.add(actual)
        return self._bfs(resto + self.vecinos(actual), visitados, recorrido + [actual])
    def es_conexo(self):
        if not self.lista_adyacencia:
            return True
        origen = list(self.lista_adyacencia)[0]
        return len(self.dfs(origen)) == len(self.lista_adyacencia)
    def __str__(self):
        return f"Vértices: {str(self.vertices)}, Matriz de adyacencia: {str(self.matriz)}"
    
g = Grafo3()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

g.listar_nodos()

g.agregar_arista("A", "B", 4)
g.agregar_arista("A", "C", 7)
g.agregar_arista("C", "D", 1)
g.agregar_arista("D", "B", 8)

origen = "A"
longitud = 3
print(f"Caminos desde {origen} de longitud {longitud}")
print(g.caminos(origen, longitud))

print("Recorrido DFS: ")
print(g.dfs("A"))

print("Recorrido BFS: ")
print(g.bfs("A"))

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
    def agregar_vertice(self, u):
        if u not in self.grafo:
            self.grafo[u] = []
    def agregar_arista(self, u, v, peso=None):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        if peso is None:
            self.grafo[u].append(v)
            self.aristas.append((u, v))
            
        self.grafo[u].append((v, peso))
        # Guardamos una lista plana de aristas para facilitar Bellman-Ford
        self.aristas.append((u, v, peso))
    def agregar_arista_orientada(self, arista):
        self.agregar_vertice(arista[0])
        self.agregar_vertice(arista[1])
        if len(arista) == 2:
            self.grafo[arista[0]].append(arista[1])
            self.aristas.append(arista)
        else:
            self.grafo[arista[0]].append((arista[1], arista[2]))
            # Guardamos una lista plana de aristas para facilitar Bellman-Ford
            self.aristas.append(arista)
    def agregar_lista_vertices(self, lista):
        if not lista:
            return 
        self.agregar_vertice(lista[0])
        self.agregar_lista_vertices(lista[1:])
    def agregar_aristas_orientadas(self, lista):
        if not lista:
            return 
        self.agregar_arista_orientada(lista[0])
        self.agregar_aristas_orientadas(lista[1:])
    def eliminar_arista(self, arista):
        if arista not in self.aristas:
            return
        self.grafo[arista[0]].remove((arista[1], arista[2]))
        self.aristas.remove(arista)
        
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
    def vecinos(self, vertice):
        return self._vecinos(self.grafo[vertice])
    def _vecinos(self, lista):
        if not lista:
            return []
        vecino, peso = lista[0]
        return [vecino] + self._vecinos(lista[1:])
    def dfs(self, origen):
        return self._dfs(origen, set())
    def _dfs(self, actual, visitados):
        if actual in visitados:
            return []
        visitados.add(actual)
        return [actual] + self._dfs_vecinos(self.vecinos(actual), visitados)
    def _dfs_vecinos(self, vecinos, visitados):
        if not vecinos:
            return []
        return (self._dfs(vecinos[0], visitados) + self._dfs_vecinos(vecinos[1:], visitados))
            
    def es_fuertemente_conexo(self):
        vertices = list(self.grafo)
        return self._es_fuertemente_conexo(vertices)
    def _es_fuertemente_conexo(self, vertices):
        if not vertices:
            return True
        visitados = self.dfs(vertices[0])
        if len(visitados) != len(self.grafo):
            return False
        return self._es_fuertemente_conexo(vertices[1:])
    def bfs(self, origen):
        return self._bfs([origen], set(), [])
    def _bfs(self,cola, visitados, recorrido):
        if not cola:
            return recorrido
        actual = cola[0]
        resto = cola[1:]
        if actual in visitados:
            return self._bfs(resto, visitados, recorrido)
        visitados.add(actual)
        return self._bfs(resto + self.vecinos(actual), visitados, recorrido + [actual])
    def camino_sin_ciclos(self, inicio, fin, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio == fin:
            return [inicio]
        visitados.add(inicio)
        return self._camino_sin_ciclos_vecinos(inicio, fin, self.vecinos(inicio), visitados)
    def _camino_sin_ciclos_vecinos(self, actual, destino, vecinos, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        if vecino not in visitados:
            camino = self.camino_sin_ciclos(vecino, destino, visitados | {vecino})
            if camino:
                return [actual] + camino
        return self._camino_sin_ciclos_vecinos(actual, destino, vecinos[1:], visitados)
    def __str__(self):
        return str(self.grafo)
    def __repr__(self):
        return str(self.grafo)

# --- Pruebas con el ejemplo numérico ---
g = GrafoDirigido()
g.agregar_arista('A', 'B', 4)
g.agregar_arista('A', 'C', 5)
g.agregar_arista('B', 'C', -2)
g.agregar_arista('A', 'D', 3)

print(g)

print("Recorrido dfs: ")
print(g.dfs("A"))

print("Recorrido bfs: ")
print(g.bfs("A"))

print("Camino sin ciclos: ")
print(g.camino_sin_ciclos("A", "D"))

g.eliminar_arista(('B', 'C', -2))

print(g)

print("¿Es fuertemente conexo el grafo?")
print(g.es_fuertemente_conexo())

# Ejecutar el algoritmo desde el nodo 'A'
resultados = g.bellman_ford('A')

if resultados:
    print("Distancias más cortas desde el nodo A:")
    for nodo, dist in resultados.items():
        print(f"Hasta {nodo}: {dist}")

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        if raiz_x != raiz_y:
            self.parent[raiz_y] = raiz_x
            

import heapq

class GrafoPonderado:
    def __init__(self):
        self.lista_adyacencia = {}
        
    def agregar_vertice(self, vertice):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []

    def agregar_arista(self, inicio, fin, peso=None, bidireccional=False):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_vertice(inicio)
        self.agregar_vertice(fin)
        if peso is None:
            self.lista_adyacencia[inicio].append(fin)
            if bidireccional:
                self.lista_adyacencia[fin].append(inicio)
        # Conectamos inicio -> fin
        self.lista_adyacencia[inicio].append((fin, peso))
        
        # Si es un grafo no dirigido (bidireccional), conectamos fin -> inicio
        if bidireccional:
            self.lista_adyacencia[fin].append((inicio, peso))
            
    def _eliminar_referencias(self, vecinos, vertice):
        if not vecinos:
            return []
        destino, peso = vecinos[0]
        if destino == vertice:
            return self._eliminar_referencias(vecinos[1:], vertice)
        return [(destino, peso)] + self._eliminar_referencias(vecinos[1:], vertice)
    
    def eliminar_vertice(self, vertice, lista_vertices=None):
        if lista_vertices is None:
            lista_vertices = list(self.lista_adyacencia)
        if not lista_vertices:
            return
        # Si el vértice existe, lo borro una sola vez
        if vertice in self.lista_adyacencia:
            del self.lista_adyacencia[vertice]
            if vertice in lista_vertices:
                lista_vertices.remove(vertice)
        actual = lista_vertices[0]
        self.lista_adyacencia[actual] = \
          self._eliminar_referencias(self.lista_adyacencia[actual],vertice)
        return self.eliminar_vertice(vertice, lista_vertices[1:])
    
    def eliminar_arista(self, inicio, fin, peso, lista_vertices=None):
        if lista_vertices is None:
            lista_vertices = list(self.lista_adyacencia)
        if not lista_vertices:
            return
        # Si alguno de los dos extremos de la arista no existe, no la borro
        if inicio not in self.lista_adyacencia or fin not in self.lista_adyacencia:
            return
        # Si la arista que quiero borrar no existe, no hago nada
        if (fin, peso) not in self.lista_adyacencia[inicio] and \
            (inicio, peso) not in self.lista_adyacencia[fin]:
            return
        if lista_vertices[0] == inicio:
            self.lista_adyacencia[lista_vertices[0]].remove((fin, peso))
            return self.eliminar_arista(inicio, fin, peso, lista_vertices[1:])
        if lista_vertices[0] == fin:
            self.lista_adyacencia[lista_vertices[0]].remove((inicio, peso))
            return self.eliminar_arista(inicio, fin, peso, lista_vertices[1:])
        return self.eliminar_arista(inicio, fin, peso, lista_vertices[1:])
    def dijkstra(self, origen):
        dist = {nodo:float("inf") for nodo in self.lista_adyacencia}
        dist[origen] = 0
        cola = [(0, origen)]
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
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
        while cola:
            d, u = heapq.heappop(cola)
            if d > dist[u]:
                continue
            if u == destino:
                break
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
        return ruta[::-1], dist[destino]
    def dijkstra_camino2(self, origen, lista_destinos):
        if not lista_destinos:
            return []
        dist, previo = self.dijkstra_camino(origen, lista_destinos[0])
        return [(dist, previo)] + \
            self.dijkstra_camino2(origen, lista_destinos[1:])
    def es_conexo(self):
        if not self.lista_adyacencia:
            return True
        origen = list(self.lista_adyacencia)[0]
        visitados = self.dfs(origen)
        return len(visitados) == len(self.lista_adyacencia)
    def vecinos(self, vertice):
        return self._vecinos(self.lista_adyacencia[vertice])
    def _vecinos(self, lista):
        if not lista:
            return []
        vecino, peso = lista[0]
        return [vecino] + self._vecinos(lista[1:])
    def vecinos_con_peso(self, vertice):
        return self._vecinos_con_peso(self.lista_adyacencia[vertice])
    def _vecinos_con_peso(self, lista):
        if not lista:
            return []
        vecino, peso = lista[0]
        return [vecino] + self._vecinos_con_peso(lista[1:])
    def dfs(self, origen):
        return self._dfs(origen, set())
    def _dfs(self, actual, visitados):
        if actual in visitados:
            return []
        visitados.add(actual)
        return [actual] + self._dfs_vecinos(self.vecinos(actual), visitados)
    def _dfs_vecinos(self, vecinos, visitados):
        if not vecinos:
            return []
        return (self._dfs(vecinos[0], visitados) + self._dfs_vecinos(vecinos[1:], visitados))
    def bfs(self, origen):
        return self._bfs([origen], set(), [])
    def _bfs(self,cola, visitados, recorrido):
        if not cola:
            return recorrido
        actual = cola[0]
        resto = cola[1:]
        if actual in visitados:
            return self._bfs(resto, visitados, recorrido)
        visitados.add(actual)
        return self._bfs(resto + self.vecinos(actual), visitados, recorrido + [actual])
    def camino_sin_ciclos(self, inicio, fin, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio == fin:
            return [inicio]
        visitados.add(inicio)
        return self._camino_sin_ciclos_vecinos(inicio, fin, self.vecinos(inicio), visitados)
    def _camino_sin_ciclos_vecinos(self, actual, destino, vecinos, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        if vecino not in visitados:
            camino = self.camino_sin_ciclos(vecino, destino, visitados | {vecino})
            if camino:
                return [actual] + camino
        return self._camino_sin_ciclos_vecinos(actual, destino, vecinos[1:], visitados)
    def sin_ciclos(self, camino, arco):
        if arco[0] not in camino or arco[1] not in camino:
            return False
        i = camino.index(arco[0])
        j = camino.index(arco[1])
        return abs(i - j) > 1
    def buscar_elemento(self, lista_tuplas, elemento):
        if not lista_tuplas:
            return False
        if elemento in lista_tuplas[0]:
            return True
        return self.buscar_elemento(lista_tuplas[1:], elemento)
    def es_vecino_de(self, vertice1, vertice2, bidireccional=False):
        if vertice1 not in self.lista_adyacencia:
            return False
        if bidireccional and vertice2 not in self.lista_adyacencia:
            return False
        if bidireccional:
            return (self.buscar_elemento(self.lista_adyacencia[vertice1], vertice2) or \
            self.buscar_elemento(self.lista_adyacencia[vertice2], vertice1))
        return self.buscar_elemento(self.lista_adyacencia[vertice1], vertice2)
    def devolver_primer_elemento(self, lista_tuplas):
        if not lista_tuplas:
            return []
        return [lista_tuplas[0][0]] + self.devolver_primer_elemento(lista_tuplas[1:])
    def vecinos_de(self, vertice):
        return self.devolver_primer_elemento(self.lista_adyacencia[vertice])
    def _agregar_actual(self, actual, caminos):
        if not caminos:
            return []
        return ([[actual] + caminos[0]] + self._agregar_actual(actual, caminos[1:]))
    def _explorar_vecinos3(self, actual, destino, vecinos, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        caminos = []
        if vecino not in visitados:
            caminos_vecino = self._todos_los_caminos(vecino, destino, visitados | {vecino})
            caminos = self._agregar_actual(actual, caminos_vecino)
        return (caminos + self._explorar_vecinos3(actual, destino, vecinos[1:], visitados))
    def todos_los_caminos(self, origen, destino):
        return self._todos_los_caminos(origen, destino, {origen})
    def _todos_los_caminos(self, actual, destino, visitados):
        if actual == destino:
            return [[actual]]
        return self._explorar_vecinos3(actual, destino, self.vecinos(actual), visitados)
    def peso_camino(self, camino):
        if len(camino) <= 1:
            return 0
        return (self.peso_arista(camino[0], camino[1]) + self.peso_camino(camino[1:]))
    def peso_arista(self, origen, destino, l_vecinos=None):
        if l_vecinos is None:
            l_vecinos = self.lista_adyacencia[origen]
        if not l_vecinos:
            return None
        if destino in l_vecinos[0]:
            return l_vecinos[0][1]
        return self.peso_arista(origen, destino, l_vecinos[1:])
    def caminos_con_peso(self, origen, destino, l_caminos=None):
        if l_caminos is None:
            l_caminos = self.todos_los_caminos(origen, destino)
        if not l_caminos:
            return []
        return [(l_caminos[0], self.peso_camino(l_caminos[0]))] + \
            self.caminos_con_peso(origen, destino, l_caminos[1:])
    def camino_mas_liviano(self, origen, destino, l_caminos=None):
        if l_caminos is None:
            l_caminos = self.caminos_con_peso(origen, destino)
        if not l_caminos:
            return []
        if len(l_caminos) == 1:
            return l_caminos[0]
        if self.camino_mas_liviano(origen, destino, l_caminos[1:])[1] == []:
            return l_caminos[0]
        if l_caminos[0][1] < self.camino_mas_liviano(origen, destino, l_caminos[1:])[1]:
            return l_caminos[0]
        return self.camino_mas_liviano(origen, destino, l_caminos[1:])
    def camino_mas_pesado(self, origen, destino, l_caminos=None):
        if l_caminos is None:
            l_caminos = self.caminos_con_peso(origen, destino)
        if not l_caminos:
            return []
        if len(l_caminos) == 1:
            return l_caminos[0]
        if self.camino_mas_pesado(origen, destino, l_caminos[1:])[1] == []:
            return l_caminos[0]
        if l_caminos[0][1] > self.camino_mas_pesado(origen, destino, l_caminos[1:])[1]:
            return l_caminos[0]
        return self.camino_mas_pesado(origen, destino, l_caminos[1:])
    def aristas(self):
        return self._aristas(list(self.lista_adyacencia), [], set())
    def _aristas(self, vertices, res, vistas):
        if not vertices:
            return res
        return self._aristas_vertice(vertices[0], self.lista_adyacencia[vertices[0]],
            res, vistas, vertices[1:])
    def _aristas_vertice(self, origen, vecinos, res, vistas, resto_vertices):
        if not vecinos:
            return self._aristas(resto_vertices, res, vistas)
        destino, peso = vecinos[0]
        arista = tuple(sorted([origen, destino]))
        if arista not in vistas:
            vistas.add(arista)
            res.append((origen, destino, peso))
        return self._aristas_vertice(origen, vecinos[1:], res, vistas, resto_vertices)
    def existe_camino(self, origen, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if origen == destino:
            return True
        visitados.add(origen)
        return self._existe_camino_vecinos(self.vecinos(origen), destino, visitados)
    def _existe_camino_vecinos(self, vecinos, destino, visitados):
        if not vecinos:
            return False
        vecino = vecinos[0]
        if vecino not in visitados:
            if self.existe_camino(vecino, destino, visitados | {vecino}):
                return True
        return self._existe_camino_vecinos(vecinos[1:], destino, visitados)
    def kruskal_rec_no_optimizado1(self):
        aristas = sorted(self.aristas(), key=lambda x: x[2])
        mst = GrafoPonderado()
        self._agregar_vertices(list(self.lista_adyacencia), mst)
        return self._kruskal_rec_no_optimizado1(aristas, mst)
    def _kruskal_rec_no_optimizado1(self, aristas, mst):
        if not aristas:
            return mst
        u, v, peso = aristas[0]
        if not mst.existe_camino(u, v):
            mst.agregar_arista(u, v, peso)
        return self._kruskal_rec_no_optimizado1(aristas[1:], mst)
    def kruskal_rec_optimizado1(self):
        aristas = sorted(self.aristas(), key=lambda x: x[2])
        uf = UnionFind(self.lista_adyacencia.keys())
        mst = GrafoPonderado()
        self._agregar_vertices(list(self.lista_adyacencia), mst)
        return self._kruskal_rec_optimizado1(aristas, uf, mst)
    def _kruskal_rec_optimizado1(self, aristas, uf, mst):
        if not aristas:
            return mst
        u, v, peso = aristas[0]
        if uf.find(u) != uf.find(v):
            mst.agregar_arista(u, v, peso)
            uf.union(u, v)
        return self._kruskal_rec_optimizado1(aristas[1:], uf, mst)
    def _construir_grafo(self, aristas, grafo=None):
        if grafo is None:
            grafo = GrafoPonderado()
            self._agregar_vertices(list(self.lista_adyacencia), grafo)
        if not aristas:
            return grafo
        u, v, peso = aristas[0]
        grafo.agregar_arista(u, v, peso)
        return self._construir_grafo(aristas[1:], grafo)
    def _agregar_vertices(self, vertices, grafo):
        if not vertices:
            return
        grafo.agregar_vertice(vertices[0])
        self._agregar_vertices(vertices[1:], grafo)
    def kruskal_rec_no_optimizado2(self):
        aristas = sorted(self.aristas(), key=lambda x: x[2])
        g_aux = GrafoPonderado()
        self._agregar_vertices(list(self.lista_adyacencia), g_aux)
        return self._kruskal_rec_no_optimizado2(aristas, g_aux)
    def _kruskal_rec_no_optimizado2(self, aristas, g_aux):
        if not aristas:
            return []
        u, v, peso = aristas[0]
        if not g_aux.existe_camino(u, v):
            g_aux.agregar_arista(u, v, peso)
            return [(u, v, peso)] + self._kruskal_rec_no_optimizado2(aristas[1:], g_aux)
        return self._kruskal_rec_no_optimizado2(aristas[1:], g_aux)
    def kruskal_rec_optimizado2(self):
        aristas = sorted(self.aristas(), key=lambda x: x[2])
        uf = UnionFind(self.lista_adyacencia.keys())
        return self._kruskal_rec_optimizado2(aristas, uf)
    def _kruskal_rec_optimizado2(self, aristas, uf):
        if not aristas:
            return []
        u, v, peso = aristas[0]
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            return [(u, v, peso)] + self._kruskal_rec_optimizado2(aristas[1:], uf)
        return self._kruskal_rec_optimizado2(aristas[1:], uf)
    def camino_mas_largo(self, origen, destino, caminos=None):
        if caminos is None:
            caminos = self.todos_los_caminos(origen, destino)
        if not caminos:
            return []
        if len(caminos) == 1:
            return caminos[0]
        mejor_resto = self.camino_mas_largo(origen, destino, caminos[1:])
        if len(caminos[0]) > len(mejor_resto):
            return caminos[0]
        return mejor_resto
    def es_arbol_binario(self, raiz):
        if not self.es_conexo():
            return False
        visitados = set()
        return self._es_arbol_binario(raiz, None, visitados)
    def _hijos(self, nodo, padre, l_vecinos=None):
        if l_vecinos is None:
            l_vecinos = self.vecinos(nodo)
        if not l_vecinos:
            return []
        if l_vecinos[0] == padre:
            return self._hijos(nodo, padre, l_vecinos[1:])
        return [l_vecinos[0]] + self._hijos(nodo, padre, l_vecinos[1:])
    def _es_arbol_binario(self, actual, padre, visitados):
        if actual in visitados:
            return False
        visitados.add(actual)
        hijos = self._hijos(actual, padre)
        if len(hijos) > 2:
            return False
        return self._verificar_hijos(hijos, actual, visitados)
    def _verificar_hijos(self, hijos, padre, visitados):
        if not hijos:
            return True
        if not self._es_arbol_binario(hijos[0], padre, visitados):
            return False
        return self._verificar_hijos(hijos[1:], padre, visitados)
    def aArbolBinario(self, raiz):
        nodo_raiz = self._aArbolBinario(raiz, None)
        arbol = arbol_binario_genericos()
        arbol.raiz = nodo_raiz
        return arbol
    def _aArbolBinario(self, actual, padre):
        hijos = self._hijos(actual, padre)
        izquierdo = None
        derecho = None
        if len(hijos) >= 1:
            izquierdo = self._aArbolBinario(hijos[0], actual)
        if len(hijos) == 2:
            derecho = self._aArbolBinario(hijos[1], actual)
        nodo = Nodo(actual)
        nodo.izquierdo = izquierdo
        nodo.derecho = derecho
        return nodo
    def aristas2(self, vertices=None):
        if vertices is None:
            vertices = list(self.lista_adyacencia)
        if not vertices:
            return []
        return [self.lista_adyacencia[vertices[0]]] + self.aristas2(vertices[1:])
    def aristas_sin_peso(self, aristas=None):
        if aristas is None:
            aristas = self.aristas2()
        return [(aristas[0], aristas[1])] + self.aristas_sin_peso(aristas[1:])
    def digrafos(self):
        return self._digrafos(self.aristas(), [])
    def _digrafos(self, aristas, orientadas):
        if not aristas:
            g = GrafoDirigido()
            g.agregar_lista_vertices(list(self.lista_adyacencia))
            g.agregar_aristas_orientadas(orientadas)
            return [g]
        u, v, peso = aristas[0]
        return (self._digrafos(aristas[1:], orientadas + [(u, v)]) + \
            self._digrafos(aristas[1:], orientadas + [(v, u)]))
    def __str__(self):
        return str(self.lista_adyacencia)



g = GrafoPonderado()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")



g.agregar_arista("A", "B", 3)
g.agregar_arista("A", "C", 2)
g.agregar_arista("B", "D", 7)



print("Grafo ponderado: ")
print(g)

print(g.dijkstra("A"))
print(g.dijkstra_camino("A", "D"))
print(g.dijkstra_camino2("A", ["B", "C", "D"]))

print("Recorrido dfs: ")
print(g.dfs("A"))

print("Recorrido bfs: ")
print(g.bfs("A"))

print("Camino sin ciclos: ")
print(g.camino_sin_ciclos("A", "D"))

print(g.sin_ciclos(["A", "B", "C", "D"], ("D", "A")))

print(g.es_vecino_de("A", "B"))

print(g.vecinos_de("A"))


origen = "A"
destino = "D"
print(f"Todos los caminos desde {origen} hasta {destino}: ")
print(g.todos_los_caminos(origen, destino))

print(g.caminos_con_peso(origen, destino))

print(f"Camino más liviano de {origen} a {destino}: ")
print(g.camino_mas_liviano(origen, destino))

print(f"Camino más pesado de {origen} a {destino}: ")
print(g.camino_mas_pesado(origen, destino))

print("Kruskal 1 con existe_camino (devuelve grafo): ")
print(g.kruskal_rec_no_optimizado1())

print("Kruskal optimizado 1 (devuelve grafo): ")
print(g.kruskal_rec_optimizado1())

print("Kruskal 2 con existe_camino (devuelve lista de aristas con peso): ")
print(g.kruskal_rec_no_optimizado2())

print("Kruskal optimizado 2 (devuelve lista de aristas con peso): ")
print(g.kruskal_rec_optimizado2())

print(f"Camino más largo desde {origen} a {destino}: ")
print(g.camino_mas_largo(origen, destino))

raiz = "A"
print(f"¿Es arbol binario el grafo con raiz {raiz}?")
print(g.es_arbol_binario(raiz))

arbol = arbol_binario_genericos()

print("Grafo como arbol: ")
print(g.aArbolBinario("A"))

print("Digrafos contenidos en el grafo: ")
print(g.digrafos())

class Bellman_Ford_Recursivo:
    def __init__(self, vertices, aristas):
        self.vertices = vertices
        self.aristas = aristas
    def bellman_ford_rec(self, origen):
        distancia = {v: float("inf") for v in self.vertices}
        predecesor = {v: None for v in self.vertices}
        distancia[origen] = 0
        self.bellman_ford_iteraciones(len(self.vertices) - 1, self.aristas, distancia, predecesor)
        ciclo = self.detectar_ciclo_negativo(self.aristas, distancia, 0)
        return distancia, predecesor, ciclo
    def bellman_ford_iteraciones(self, k, aristas, distancia, predecesor):
        if k == 0:
            return
        self.relajar_aristas(aristas, distancia, predecesor)
        self.bellman_ford_iteraciones(k - 1, aristas, distancia, predecesor)
    def relajar_aristas(self, aristas, distancia, predecesor):
        if not aristas:
            return
        u, v, peso = aristas[0]
        if distancia[u] != float("inf"):
            if distancia[u] + peso < distancia[v]:
                distancia[v] = (distancia[u] + peso)
                predecesor[v] = u
        self.relajar_aristas(aristas[1:], distancia, predecesor)
    def detectar_ciclo_negativo(self, aristas, distancia, indice):
        if indice == len(aristas):
            return False
        u, v, peso = aristas[indice]
        if distancia[u] != float("inf"):
            if distancia[u] + peso < distancia[v]:
                return True
        return self.detectar_ciclo_negativo(aristas, distancia, indice + 1)
    def reconstruir_camino(self, predecesor, destino):
        if predecesor[destino] is None:
            return [destino]
        return (self.reconstruir_camino(predecesor, predecesor[destino]) + [destino])
    def bellman_ford_camino(self, origen, destino):
        distancia, predecesor, ciclo = self.bellman_ford_rec(origen)
        if ciclo:
            return None
        if distancia[destino] == float("inf"):
            return [], float("inf")
        return (distancia[destino], self.reconstruir_camino(predecesor, destino))
    
b = Bellman_Ford_Recursivo(["S","A","B","C","D"],
[
    ("S","A",3),
    ("S","B",4),
    ("B","A",-2),
    ("A","C",2),
    ("C","D",1)
])

print(b.bellman_ford_camino("S","D"))

import heapq

class Dijkstra_Recursivo:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def dijkstra(self, origen):
        dist = {nodo: float("inf") for nodo in self.lista_adyacencia}
        previo = {}
        dist[origen] = 0
        cola = [(0, origen)]
        self._dijkstra(cola, dist, previo)
        return dist, previo
    def _dijkstra(self, cola, dist, previo):
        if not cola:
            return
        d, u = heapq.heappop(cola)
        if d > dist[u]:
            return self._dijkstra(cola, dist, previo)
        self._relajar_vecinos(u, self.lista_adyacencia[u], d, cola, dist, previo)
        return self._dijkstra(cola, dist, previo)
    def _relajar_vecinos(self,origen, vecinos, dist_u, cola, dist, previo):
        if not vecinos:
            return
        v, peso = vecinos[0]
        if dist_u + peso < dist[v]:
            dist[v] = dist_u + peso
            previo[v] = origen
            heapq.heappush(cola, (dist[v], v))
        self._relajar_vecinos(origen, vecinos[1:], dist_u, cola, dist, previo)
    def reconstruir_camino(self, previo, destino):
        if previo.get(destino) is None:
            return [destino]
        return (self.reconstruir_camino(previo, previo[destino]) + [destino])
    def dijkstra_camino(self, origen, destino):
        dist, previo = self.dijkstra(origen)
        if dist[destino] == float("inf"):
            return [], float("inf")
        return (dist[destino], self.reconstruir_camino(previo, destino))

g = Dijkstra_Recursivo({
    "A": [("B",3), ("C",2)],
    "B": [("D",7)],
    "C": [("D",8)],
    "D": []
})

print(g.dijkstra_camino("A", "D"))
#No funciona con ciclos negativos

class Grafo_Completo(Grafo2):
    def __init__(self, lista_adyacencia):
        super().__init__(lista_adyacencia)
        if not self.es_completo():
            raise ValueError("El grafo no es completo")
    def es_completo(self, vertices=None):
        if vertices is None:
            vertices = list(self.lista_adyacencia)
        if not vertices:
            return True
        v = vertices[0]
        # Detecta paralelas
        if len(self.lista_adyacencia[v]) != len(set(self.lista_adyacencia[v])):
            return False
        # Detecta bucles
        if v in self.lista_adyacencia[v]:
            return False
        vecinos = set(self.lista_adyacencia[v])
        esperado = set(self.lista_adyacencia)
        esperado.remove(v)
        if vecinos != esperado:
            return False
        return self.es_completo(vertices[1:])
    def copiar_lista(self, lista):
        if not lista:
            return []
        return [lista[0]] + self.copiar_lista(lista[1:])
    def copiar_vecinos(self, items, copia = None):
        if copia is None:
            copia = {}
        if not items:
            return copia
        copia[items[0][0]] = self.copiar_lista(items[0][1])
        return self.copiar_vecinos(items[1:], copia)
    def aGrafo(self):
        copia = self.copiar_vecinos(list(self.lista_adyacencia.items()))
        return Grafo2(copia)
    def __str__(self):
        return f"Lista de adyacencia: {str(self.lista_adyacencia)}"
        
g = Grafo_Completo({"A": ["B", "C", "D"],
                    "B": ["A", "C", "D"],
                    "C": ["A", "B", "D"],
                    "D": ["A", "B", "C"]})
    
g.agregar_vertice("E")
g.agregar_arista("D", "E")

print(g)
print(g.aGrafo())

class Grafo_Bipartito_Completo(Grafo2):
    def __init__(self, lista_adyacencia):
        super().__init__(lista_adyacencia)
        if not self.es_bipartito_completo():
            raise ValueError("El grafo no es bipartito completo")
    def _colorear(self, actual, color, colores):
        if actual in colores:
            return colores[actual] == color
        colores[actual] = color
        return self._colorear_vecinos(self.vecinos(actual), 1 - color, colores)
    def _colorear_vecinos(self, vecinos, color, colores):
        if not vecinos:
            return True
        if not self._colorear(vecinos[0], color, colores):
            return False
        return self._colorear_vecinos(vecinos[1:], color, colores)
    def _verificar_bipartito_completo(self, vertices, colores):
        if not vertices:
            return True
        actual = vertices[0]
        if not self._conectado_con_todos_del_otro_color(actual, list(colores), colores):
            return False
        return self._verificar_bipartito_completo(vertices[1:], colores)
    def _conectado_con_todos_del_otro_color(self, actual, vertices, colores):
        if not vertices:
            return True
        otro = vertices[0]
        if actual != otro:
            if colores[actual] != colores[otro]:
                if otro not in self.vecinos(actual):
                    return False
            else:
                if otro in self.vecinos(actual):
                    return False
        return self._conectado_con_todos_del_otro_color(actual, vertices[1:], colores)
    def vecinos(self, vertice):
        return self.lista_adyacencia[vertice]
    def es_bipartito_completo(self):
        vertices = list(self.lista_adyacencia)
        if not vertices:
            return True
        colores = {}
        if not self._colorear(vertices[0], 0, colores):
            return False
        return self._verificar_bipartito_completo(vertices, colores)
    def copiar_vecinos(self, items, copia = None):
        if copia is None:
            copia = {}
        if not items:
            return copia
        copia[items[0][0]] = items[0][1]
        return self.copiar_vecinos(items[1:], copia)
    def aGrafo(self):
        copia = self.copiar_vecinos(list(self.lista_adyacencia.items()))
        return Grafo2(copia)
    def __str__(self):
        return f"Lista de adyacencia: {str(self.lista_adyacencia)}"
    
    
g = Grafo_Bipartito_Completo({"A": ["C", "D"],
                    "B": ["C", "D"],
                    "C": ["A", "B"],
                    "D": ["A", "B"]})

g.eliminar_arista("A", "C")
print(g)
print(g.aGrafo())