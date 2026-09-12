# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:43:34 2026

@author: SD
"""

class Punto:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Ahora, un objeto de la clase Punto solo puede tener los atributos x e y.
p = Punto(1, 2)
print(p.x, p.y)  # Salida: 1 2
# Intentar agregar un nuevo atributo dará un error
#p.z = 3  # AttributeError: 'Punto' object has no attribute 'z' (si no hubiéramos definido slots funcionaría)

class MiClaseInmutable:
    def __init__(self, valor_inicial):
        self._valor = valor_inicial
    @property
    def valor(self):
        return self._valor

objeto_inmutable = MiClaseInmutable(20)
objeto_inmutable.valor                      # 20
objeto_inmutable.valor = 10                 # AttributeError: property 'valor' of 'MiClaseInmutable' object has no setter
objeto_inmutable._valor = 10                # Modifica el valor
objeto_inmutable.valor                      # 10
