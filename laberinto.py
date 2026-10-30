import random

def es_salida(pos, llegada):
    return pos == llegada

def avanzar(posicion, direccion):
    x, y = posicion
    if direccion == 'N':
        return (x - 1, y)
    if direccion == 'S':
        return (x + 1, y)
    if direccion == 'E':
        return (x, y + 1)
    if direccion == 'O':
        return (x, y - 1)
    
def hay_paso(posicion, coordenadas_validas):
    return posicion in coordenadas_validas

from typing import List, Tuple

Posicion = Tuple[int, int]
def laberinto(camino_previo: List[Posicion], coordenadas_validas, llegada) -> (bool, List[Posicion]):
    posicion_actual = camino_previo[-1]
    if es_salida(posicion_actual, llegada):
        return True, camino_previo
    else:
        salida_encontrada = False
        solucion = camino_previo
        direcciones = ['N', 'S', 'O', 'E']
        random.shuffle(direcciones)
        while direcciones and not salida_encontrada:
            nueva_posicion = avanzar(posicion_actual, direcciones.pop())
            if hay_paso(nueva_posicion, coordenadas_validas) and nueva_posicion not in camino_previo:
                camino_actual = camino_previo.copy()
                camino_actual.append(nueva_posicion)
                salida_encontrada, solucion = laberinto(camino_actual, coordenadas_validas, llegada)
        return salida_encontrada, solucion
    
coordenadas_validas = [(0,0),(0,1),(0,2),(1,2),(2,2)]
salida = (0,0)
llegada = (2,2)
#print(laberinto([salida], coordenadas_validas, llegada))

class Laberinto:
    def __init__(self, vertices):
        self.coordenadas_validas = coordenadas_validas
    def es_salida(self, pos, llegada):
        return pos == llegada
    def avanzar(self, posicion, direccion):
        x, y = posicion
        if direccion == 'N':
            return (x - 1, y)
        if direccion == 'S':
            return (x + 1, y)
        if direccion == 'E':
            return (x, y + 1)
        if direccion == 'O':
            return (x, y - 1)
    def hay_paso(self, posicion):
        return posicion in self.coordenadas_validas
    def vecinos(self, coordenada):
        direcciones = ['N','S','E','O']
        return self._vecinos(coordenada, direcciones)
    def _vecinos(self, coordenada, direcciones):
        if not direcciones:
            return []
        vecino = self.avanzar(coordenada, direcciones[0])
        if vecino in self.coordenadas_validas:
            return [vecino] + self._vecinos(coordenada, direcciones[1:])
        return self._vecinos(coordenada, direcciones[1:])
    def hay_camino(self, actual, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if actual == destino:
            return True
        visitados.add(actual)
        return self._hay_camino_vecinos(self.vecinos(actual), destino, visitados)
    def _hay_camino_vecinos(self, vecinos, destino, visitados):
        if not vecinos:
            return False
        vecino = vecinos[0]
        if vecino not in visitados:
            if self.hay_camino(vecino, destino, visitados):
                return True
        return self._hay_camino_vecinos(vecinos[1:], destino, visitados)
    def camino(self, actual, destino, visitados=None):
        if visitados is None:
            visitados = set()
        if actual == destino:
            return [actual]
        visitados.add(actual)
        return self._camino_vecinos(actual, self.vecinos(actual), destino, visitados)
    def _camino_vecinos(self, actual, vecinos, destino, visitados):
        if not vecinos:
            return []
        vecino = vecinos[0]
        if vecino not in visitados:
            camino = self.camino(vecino, destino, visitados | {vecino})
            if camino:
                return [actual] + camino
        return self._camino_vecinos(actual, vecinos[1:], destino, visitados)
    def _explorar_direcciones(self, posicion_actual, camino_previo, llegada, direcciones):
        if not direcciones:
            return False, []
        nueva_posicion = self.avanzar(posicion_actual, direcciones[0])
        if (self.hay_paso(nueva_posicion) and nueva_posicion not in camino_previo):
            camino_actual = camino_previo.copy()
            camino_actual.append(nueva_posicion)
            salida_encontrada, solucion = self.hay_camino2(camino_actual, llegada)
            if salida_encontrada:
                return True, solucion
        return self._explorar_direcciones(posicion_actual, camino_previo, llegada, direcciones[1:])
    def hay_camino2(self, camino_previo, llegada):
        posicion_actual = camino_previo[-1]
        if self.es_salida(posicion_actual, llegada):
            return True, camino_previo
        direcciones = ['N', 'S', 'O', 'E']
        random.shuffle(direcciones)
        return self._explorar_direcciones(posicion_actual, camino_previo, llegada, direcciones)
        
l = Laberinto([(0,0),(0,1),(0,2),(1,2),(2,2)])
salida = (0,0)
llegada = (2,2)
print(l.hay_camino2([salida], llegada))
