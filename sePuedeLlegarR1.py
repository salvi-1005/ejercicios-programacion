from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  if origen == destino: return -1  
  if not soloParteUnVUeloDeCadaCiudad(vuelos): return -1
  if not soloLlegaUnVueloAcadaCuidad(vuelos): return -1
  if not sinRepetidos(vuelos): return -1

  r = []
  desde = origen
  j = 0
  ruta_completa = False
  while not ruta_completa and j < len(vuelos):
        origen_coincide = False
        i = 0
    
        while not origen_coincide and i < len(vuelos):
            if vuelos[i][0] == desde:
                origen_coincide = True
            else:
                i += 1
    
        if origen_coincide: 
                r.append(vuelos[i]) 
        else: 
                break
        
        if vuelos[i][1] == destino:
            ruta_completa = True
        else:
            j += 1
        
        desde = vuelos[i][1]
    
  if not ruta_completa: r=-1

  if vuelosValidos(r, vuelos) and len(r) >= 1 and r[0][0] == origen and r[len(r) - 1][1] == destino and caminoDeVuelos(r):
      return largoDeRuta(r,origen,destino,vuelos,len(r))
  else:
      return -1

def largoDeRuta(ruta, origen, destino, vuelos, longCamino):
    return len(ruta)

def caminoDeVuelos(ruta):
    es_un_camino = True
    i = 0
    while i < len(ruta) - 1 and es_un_camino: 
        if ruta[i][1] != ruta[i + 1][0]:
            es_un_camino = False
        else:
            i += 1
    return es_un_camino

def vuelosValidos(ruta, vuelos):
    vuelos_válidos = False
    if sinRepetidos(ruta):
        vuelos_válidos = True
        i = 0
        while i < len(ruta) and vuelos_válidos:
            if not hayRuta(vuelos, ruta[i][0], ruta[i][1]):
                vuelos_válidos = False
            else:
                i += 1
    return vuelos_válidos

def hayRuta(vuelos, origen, destino):
    hay_ruta = False
    i = 0
    while not hay_ruta and i < len(vuelos):
        if vuelos[i][0] == origen and vuelos[i][1] == destino:
            hay_ruta = True
        else:
            i += 1
    return hay_ruta

def sinRepetidos(vuelos):
    no_hay_vuelos_repetidos = True
    i = 0
    while no_hay_vuelos_repetidos and i < len(vuelos) - 1:
        j = i + 1
        while no_hay_vuelos_repetidos and j < len(vuelos):
            if vuelos[i] == vuelos[j]:
                no_hay_vuelos_repetidos = False
            else:
                j += 1
        i += 1
    return no_hay_vuelos_repetidos

def soloLlegaUnVueloAcadaCuidad(vuelos):
    destinos_distintos = True
    i = 0
    while destinos_distintos and i < len(vuelos) - 1:
        j = i + 1
        while j < len(vuelos) and destinos_distintos:
            if vuelos[j][1] == vuelos[i][1]:
                destinos_distintos = False
            else:
                j += 1
        i += 1
    return destinos_distintos

def soloParteUnVUeloDeCadaCiudad(vuelos):
    orígenes_distintos = True
    i = 0
    while orígenes_distintos and i < len(vuelos) - 1:
        j = i + 1
        while j < len(vuelos) and orígenes_distintos:
            if vuelos[j][0] == vuelos[i][0]:
                orígenes_distintos = False
            else:
                j += 1
        i += 1
    return orígenes_distintos

if __name__ == '__main__':
  origen = input()
  origen = origen.strip()
  destino = input()
  destino = destino.strip()
  vuelos = input()
  vuelos = vuelos.strip()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))