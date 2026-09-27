from typing import Any, Generic, TypeVar 
from typing import List
from functools import reduce


T = TypeVar( 'T') 

class ArbolN( Generic[T]): 
    def __init__(self, dato: T):
        self ._dato: T = dato
        self ._subarboles: List[ArbolN[T]] = []

    @property 
    def dato(self) -> T: 
        return self._dato 

    @dato.setter 
    def dato(self, valor : T): 
        self._dato = valor 
    
    @property 
    def subarboles(self):
        return self ._subarboles 
    
    @subarboles.setter 
    def subarboles(self, subarboles):
        self ._subarboles = subarboles
        
    def insertar_subarbol(self, subarbol):    
        self.subarboles.append(subarbol) 
        
    def es_hoja(self) -> bool:    
        return self.subarboles == []
    
    def altura_recursion_multiple(self) -> int: 
        if self.es_hoja(): 
            return 1 
        else: 
            return 1 + max([subarbol.altura() for subarbol in self .subarboles])
        
    def altura_bucle(self) -> int:        
        altura_actual = 0 
        for subarbol in self .subarboles:            
            altura_actual = max (altura_actual, subarbol.altura()) 
        return altura_actual + 1
    
    def altura(self) ->  int:
        def altura_n(bosque: List[ ArbolN[T]]) -> int: 
            if not bosque: 
                return 0 
            else: 
                return max(bosque[0].altura(), altura_n(bosque[1 :])) 
        return 1 + altura_n( self .subarboles)
    
    def preorder_funcional( self ) -> List [T]:
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.preorder(), self .subarboles, [self.dato])
    
    def preorder_imperativo(self) -> List [T]:    
        recorrido = [self .dato] 
        for subarbol in self .subarboles:        
            recorrido += subarbol.preorder() 
        return recorrido
    
    def preorder( self ) -> List [T]: 
        def preorder_n( bosque : List[ ArbolN[T]]) -> List [T]: 
            if not bosque: 
                return [] 
            else: 
                return bosque[0].preorder() + preorder_n(bosque[1:])
        return [self.dato] + preorder_n(self.subarboles)
        
    def postorder_funcional( self ) -> List [T]:
        return reduce(lambda recorrido, subarbol: recorrido + \
                      subarbol.postorden(), self .subarboles, [self.dato])
    
    def postorder_imperativo(self) -> List [T]:    
        recorrido = [self .dato] 
        for subarbol in self .subarboles:        
            recorrido += subarbol.postorder() 
        return recorrido
    
    def postorder( self ) -> List [T]: 
        def postorder_n( bosque : List[ ArbolN[T]]) -> List [T]: 
            if not bosque: 
                return [] 
            else: 
                return bosque[0].postorder() + postorder_n(bosque[1:]) 
        return postorder_n(self.subarboles) + [self.dato]
        
    def nivel(self, dato: T, niv=0):
        if self.dato == dato:
            return niv
        for subarbol in self._subarboles:
            resultado = subarbol.nivel(dato, niv+1)
            if resultado is not None:
                return resultado
        return None  
    
    def copiar(self):
        copia = ArbolN(self.dato)
        copia.subarboles = [subarbol.copiar() for subarbol in self.subarboles]
        return copia
    
    def __str__(self):
        return f"Preorden: {str(self.preorder())}, Postorden: {str(self.postorder())}"
    
    def sin_hojas(self):
        if self.es_hoja():
            return None
        copia = ArbolN(self.dato)
        copia.subarboles = [subarbol.sin_hojas() \
                    for subarbol in self.subarboles if not subarbol.es_hoja()]
        return copia
    
    def ramas(self):
        if self.es_hoja():
            return [[self.dato]]
        resultado = []
        for subarbol in self.subarboles:
            for rama in subarbol.ramas():
                resultado.append([self.dato] + rama)
        return resultado
    
    def contiene(self, valor):
        if self.dato == valor:
            return True
        return any(subarbol.contiene(valor) for subarbol in self.subarboles)
    
    def antecesores(self, valor):
        if self.dato == valor:
            return None
        copia = ArbolN(self.dato)
        copia.subarboles = []
        for subarbol in self.subarboles:
            if subarbol.contiene(valor):
                resultado = subarbol.antecesores(valor)
                if resultado is not None:
                    copia.subarboles.append(resultado)
        return copia
    
    def recorrido_guiado(self, direcciones):
        if not direcciones:
            return self.dato
        indice = direcciones[0]
        if indice >= len(self.subarboles):
            raise IndexError("Movimiento inválido")
        return self.subarboles[indice].recorrido_guiado(direcciones[1:])
    
raiz = ArbolN(10)

nodo5 = ArbolN(5)
nodo15 = ArbolN(15)
nodo20 = ArbolN(20)

nodo3 = ArbolN(3)
nodo7 = ArbolN(7)

nodo5.subarboles = [nodo3, nodo7]

raiz.subarboles = [nodo5, nodo15, nodo20]

print(raiz.nivel(3))
copia = raiz.copiar()
print(copia)

copia = raiz.copiar()

copia.subarboles[0].dato = 999

print(raiz)
print(copia)

sacar_hojas = raiz.sin_hojas()
print("Árbol sin hojas:")
print(sacar_hojas)

todas_las_ramas = raiz.ramas()
print("Todas las ramas:")
print(todas_las_ramas)

dato = 7
antecesores_dato = raiz.antecesores(dato)
print(f"Antecesores de {dato}:")
print(antecesores_dato)

print(nodo5.ramas())
print(7 in nodo5.ramas())

direcciones = [0,1]
recorrido = raiz.recorrido_guiado(direcciones)
print(f"Recorrido guiado por {direcciones}")
print(recorrido)