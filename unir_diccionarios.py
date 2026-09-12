from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
    unión_diccionarios = {}
    for diccionario in a_unir:
        for clave in diccionario:
            if clave in unión_diccionarios:
                unión_diccionarios[clave].append(diccionario[clave])
            else:
                unión_diccionarios[clave] = [diccionario[clave]]
    return unión_diccionarios


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))