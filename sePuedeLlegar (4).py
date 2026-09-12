from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  return cantEscalas(origen,destino,vuelos,0)

def cantEscalas(origen: str, destino: str, vuelos: List[Tuple[str, str]],escalas:int) -> int :
  posicionOrigen:int= 0
  existeOrigen:bool= False

  for i in range(len(vuelos)):
    if (vuelos[i][0]==origen):
      existeOrigen=True
      posicionOrigen=i
  if not(existeOrigen):
    return -1
  if (vuelos[posicionOrigen][1]==destino):
    return escalas+1
  return cantEscalas(vuelos[posicionOrigen][1],destino,vuelos,escalas+1)

if __name__ == '__main__':
  origen = input()
  origen = origen.strip()
  destino = input()
  destino = destino.strip()
  vuelos = input()
  vuelos = vuelos.strip()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))