class Destino:
    def __init__(self, nombre, sig=None):
        self.nombre = nombre
        self.sig = sig

class Historial:
    def __init__(self, head):
        self.head = None
        self.ultimo = None
    def agregar_destino(self, destino):
        nuevo = Destino(destino)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def eliminar_destino(self, destino):
        return self._eliminar_destino(self.head, destino)
    def _eliminar_destino(self, destino_actual, destino):
        if destino_actual is None:
            return None
        if destino_actual.nombre == destino:
            return destino_actual.siguiente 
        destino_actual.siguiente = self._eliminar_recursivo(destino_actual.siguiente, destino)
        return destino_actual

class Pelicula:
    def __init__(self, nombre, codigo, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.codigo = codigo
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Codigo: {self.codigo}"
    
class Videoclub:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def obtener_menor_codigo(self):
        return self._obtener_menor_codigo(self.raiz)
    def _obtener_menor_codigo(self, nodo_actual):
        if nodo_actual.izquierdo is None:
            return nodo_actual.codigo
        return self._obtener_menor_codigo(nodo_actual.izquierdo)
    def eliminar_pelicula(self, valor_a_eliminar):
        self.raiz = self._eliminar_pelicula(self.raiz, valor_a_eliminar)
    def _eliminar_pelicula(self, nodo_actual, valor_a_eliminar):
        if nodo_actual is None:
            return None
        if valor_a_eliminar < nodo_actual.codigo:
            nodo_actual.izquierdo = self._eliminar_pelicula(nodo_actual.izquierdo, valor_a_eliminar)
        elif valor_a_eliminar > nodo_actual.codigo:
            nodo_actual.derecho = self._eliminar_pelicula(nodo_actual.derecho, valor_a_eliminar)
        else:
            # Caso 1: sin hijo izquierdo
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            # Caso 2: sin hijo derecho
            if nodo_actual.derecho is None:
                return nodo_actual.izquierdo
        # Caso 3: dos hijos
            sucesor = self._obtener_menor_codigo(nodo_actual.derecho)
            nodo_actual.codigo = sucesor
            nodo_actual.derecho = self._eliminar_pelicula(nodo_actual.derecho, sucesor)
        return nodo_actual
    def buscar_pelicula(self, id_pelicula):
        return self._buscar_pelicula(self.raiz, id_pelicula)
    def _buscar_pelicula(self, nodo_actual, id_pelicula):
        if nodo_actual is None:
            return False
        if nodo_actual.codigo == id_pelicula:
            return True
        if nodo_actual.codigo > id_pelicula: 
            return self._buscar_pelicula(nodo_actual.izquierdo, id_pelicula)
        if nodo_actual.codigo < id_pelicula: 
            return self._buscar_pelicula(nodo_actual.derecho, id_pelicula)
    def listar_ordenado(self):
        return self._listar_ordenado(self.raiz)
    def _listar_ordenado(self, nodo_actual):
        if nodo_actual is None:
            return []
        return (
        self._listar_ordenado(nodo_actual.izquierdo)
        + [(nodo_actual.nombre, nodo_actual.codigo)]
        + self._listar_ordenado(nodo_actual.derecho))
    def __str__(self):
        return "\n".join(str(x) for x in self.listar_ordenado())

    
v = Videoclub(Pelicula("Matrix", 6, Pelicula("Titanic", 3, Pelicula("Rocky", 2), Pelicula("Lost", 4)), 
                       Pelicula("Avatar", 8, Pelicula("Avengers", 7), Pelicula("It", 9))))

print("Lista ordenada por código: ")
print(v)

print("¿Está la película 2?")
print(v.buscar_pelicula(2))

print("Menor código: ")
print(v.obtener_menor_codigo())

v.eliminar_pelicula(2)

print("Después de eliminar la película 2: ")

print("Lista ordenada por código: ")
print(v)

print("¿Está la película 2?")
print(v.buscar_pelicula(2))

print("Menor código: ")
print(v.obtener_menor_codigo())