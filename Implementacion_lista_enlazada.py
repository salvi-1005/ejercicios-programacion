class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
    
class LinkedList:
    def __init__(self):
        self.head: Nodo
        self.ultimo: Lucas
    def add(self, dato):
        Nnodo = Nodo(self.dato)
        self.ultimo.sig = Nnodo
        self.ultimo = Nnodo
    def insert(self, dato):
        self.head = Nodo(dato, self.head)       
    def rpop(self, nodo):
        if nodo.sig.sig is None:
            nodo.sig = None
        self.rpop(nodo.sig)
    def pop(self, nodo):
        return rpop(self.nodo)
    def busqueda(self, dato):
        return self.Rbusqueda(self.head, dato)
    def rbusqueda(nodo, dato):
        if nodo.sig is None:
            raise ValueError("No existe dato buscado")
        if nodo.dato == dato:
            return 0 + self.rbusqueda(nodo.siguiente, dato)
    def exchange(self, dato):
            
        
            

#(Juan, dato)

#head: Juan
#head.sig.dato -> b
#head.sig.sig.dato -> c
#if head.sig.sig.sig = dato
#-> dato3

#Add (agregar al final):

#Insert
#Pop
#--Trunc
#Busqueda: nro nodo (valor)
#--Exchange (valor)
#--Busqueda binaria
#--len
#--sort

Juan = Nodo("B", Lucas)
Maria = Nodo("A", Juan)
Lucas = Nodo("C")
Pedro = Nodo("D")

