#Listas enlazadas
#1)

class Destino:
    def __init__(self, nombre, sig=None):
        self.nombre = nombre
        self.sig = sig

class Historial:
    def __init__(self):
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
        self.head = self._eliminar_destino(self.head, destino)
    def _eliminar_destino(self, destino_actual, destino):
        if destino_actual is None:
            return None
        if destino_actual.nombre == destino:
            if destino_actual == self.ultimo:
                self.ultimo = None  # o el anterior
            return destino_actual.sig
        destino_actual.sig = self._eliminar_destino(destino_actual.sig, destino)
        return destino_actual
    def buscar_destino(self, destino):
        return self._buscar_destino(self.head, destino)
    def _buscar_destino(self, nodo_actual, destino):
        if nodo_actual is None:
            return False
        if nodo_actual.nombre == destino:
            return True
        return self._buscar_destino(nodo_actual.sig, destino)
    def listar_ordenado(self):
        return self._listar_ordenado(self.head)
    def _listar_ordenado(self, nodo_actual):
        if nodo_actual is None:
            return []
        return [nodo_actual.nombre] + self._listar_ordenado(nodo_actual.sig)
    def _a_string(self, elementos):
        if not elementos:
            return ""
        if len(elementos) == 1:
            return str(elementos[0])
        return (str(elementos[0]) + "\n" + self._a_string(elementos[1:]))
    def __str__(self):
        return self._a_string(self.listar_ordenado())
    
h = Historial()

h.agregar_destino("Mar Del Plata") 
h.agregar_destino("Bahia Blanca") 
h.agregar_destino("Bariloche")
h.agregar_destino("El Calafate")
h.agregar_destino("Ushuaia")

d = "Bariloche"

print(f"¿Está {d} en el historial?")
print(h.buscar_destino(d))

print("Historial ordenado: ")
print(h)

h.eliminar_destino(d)

print(f"Despues de eliminar {d}: ")

print(f"¿Está {d} en el historial?")
print(h.buscar_destino(d))

print("Historial ordenado: ")
print(h)

#2)

class Vagon:
    def __init__(self, nombre, sig=None):
        self.nombre = nombre
        self.sig = sig
        
class Tren:
    def __init__(self):
        self.head = None
        self.ultimo = None
    def agregar_vagon(self, destino):
        nuevo = Vagon(destino)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def eliminar_vagon(self, vagon):
        self.head = self._eliminar_vagon(self.head, vagon)
    def _eliminar_vagon(self, vagon_actual, vagon):
        if vagon_actual is None:
            return None
        if vagon_actual.nombre == vagon:
            if vagon_actual == self.ultimo:
                self.ultimo = None  # o el anterior
            return vagon_actual.sig
        vagon_actual.sig = self._eliminar_vagon(vagon_actual.sig, vagon)
        return vagon_actual
    def contar_vagones(self):
        return self._contar_vagones(self.head)
    def _contar_vagones(self, vagon_actual):
        if vagon_actual is None:
            return 0
        return 1 + self._contar_vagones(vagon_actual.sig)
    def obtener_ultimo_vagon(self):
        return self._obtener_ultimo_vagon(self.head)
    def _obtener_ultimo_vagon(self, vagon_actual):
        if vagon_actual.sig is None:
            return vagon_actual.nombre
        return self._obtener_ultimo_vagon(vagon_actual.sig)

t = Tren()

t.agregar_vagon("Manuel Belgrano") 
t.agregar_vagon("Jose de San Martin") 
t.agregar_vagon("Manuel Alberti")
t.agregar_vagon("Nestor Kirchner")
t.agregar_vagon("Juan Manuel De Rosas")

v = "Juan Manuel De Rosas"

print("Cantidad de vagones en el tren: ")
print(t.contar_vagones())

print("Último vagón del tren: ")
print(t.obtener_ultimo_vagon())

t.eliminar_vagon(v)

print(f"Despues de eliminar {v}: ")

print("Cantidad de vagones en el tren: ")
print(t.contar_vagones())

print("Último vagón del tren: ")
print(t.obtener_ultimo_vagon())

#3)

class Cancion:
    def __init__(self, nombre, sig=None):
        self.nombre = nombre
        self.sig = sig

class Playlist:
    def __init__(self):
        self.head = None
        self.ultimo = None
    def agregar_cancion(self, cancion):
        nuevo = Cancion(cancion)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def eliminar_cancion(self, cancion):
        self.head = self._eliminar_cancion(self.head, cancion)
    def _eliminar_cancion(self, cancion_actual, cancion):
        if cancion_actual is None:
            return None
        if cancion_actual.nombre == cancion:
            if cancion_actual == self.ultimo:
                self.ultimo = None  # o el anterior
            return cancion_actual.sig
        cancion_actual.sig = self._eliminar_cancion(cancion_actual.sig, cancion)
        return cancion_actual
    def listar_ordenado(self):
        return self._listar_ordenado(self.head)
    def _listar_ordenado(self, cancion_actual):
        if cancion_actual is None:
            return []
        return [cancion_actual.nombre] + self._listar_ordenado(cancion_actual.sig)
    def _a_string(self, elementos):
        if not elementos:
            return ""
        if len(elementos) == 1:
            return str(elementos[0])
        return (str(elementos[0]) + "\n" + self._a_string(elementos[1:]))
    def __str__(self):
        return self._a_string(self.listar_ordenado())

p = Playlist()

p.agregar_cancion("Antes y Despues") 
p.agregar_cancion("Eye of a Tiger") 
p.agregar_cancion("Champagne Supernova")
p.agregar_cancion("Lamento Boliviano")
p.agregar_cancion("Paint it Black")

c = "Eye of a Tiger"

print("Mostrar playlist: ")
print(p)

p.eliminar_cancion(c)

print(f"Despues de eliminar {c}: ")

print("Mostrar playlist: ")
print(p)

#Árboles

#4)

class Libro:
    def __init__(self, nombre, codigo, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.codigo = codigo
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"
    
class Biblioteca:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def insertar(self, nombre, codigo):
        self.raiz = self._insertar(self.raiz, nombre, codigo)
    def _insertar(self, libro_actual, nombre, codigo):
        if libro_actual is None:
            return Libro(nombre, codigo)
        if codigo < libro_actual.codigo:
            libro_actual.izquierdo = self._insertar(libro_actual.izquierdo, nombre, codigo)
        elif codigo > libro_actual.codigo:
            libro_actual.derecho = self._insertar(libro_actual.derecho, nombre, codigo)
        return libro_actual
    def obtener_menor_codigo(self):
        return self._obtener_menor_codigo(self.raiz)
    def _obtener_menor_codigo(self, libro_actual):
        if libro_actual.izquierdo is None:
            return (libro_actual.nombre, libro_actual.codigo)
        return self._obtener_menor_codigo(libro_actual.izquierdo)
    def minimo_nodo(self):
        return self._minimo_nodo(self.raiz)
    def _minimo_nodo(self, nodo_actual):
        if nodo_actual.izquierdo is None:
            return Libro(nodo_actual.nombre, nodo_actual.codigo)
        return self._minimo_nodo(nodo_actual.izquierdo)
    def eliminar_libro(self, libro_a_eliminar):
        self.raiz = self._eliminar_libro(self.raiz, libro_a_eliminar)
    def _eliminar_libro(self, libro_actual, libro_a_eliminar):
        if libro_actual is None:
            return None
        if libro_a_eliminar < libro_actual.codigo:
            libro_actual.izquierdo = self._eliminar_libro(libro_actual.izquierdo, libro_a_eliminar)
        elif libro_a_eliminar > libro_actual.codigo:
            libro_actual.derecho = self._eliminar_libro(libro_actual.derecho, libro_a_eliminar)
        else:
            # Caso 1: sin hijo izquierdo
            if libro_actual.izquierdo is None:
                return libro_actual.derecho
            # Caso 2: sin hijo derecho
            if libro_actual.derecho is None:
                return libro_actual.izquierdo
        # Caso 3: dos hijos
            sucesor = self._minimo_nodo(libro_actual.derecho)
            libro_actual.nombre = sucesor.nombre
            libro_actual.codigo = sucesor.codigo
            libro_actual.derecho = self._eliminar_libro(libro_actual.derecho, sucesor.codigo)
        return libro_actual
    def buscar_libro(self, id_libro):
        return self._buscar_libro(self.raiz, id_libro)
    def _buscar_libro(self, libro_actual, id_libro):
        if libro_actual is None:
            return False
        if libro_actual.codigo == id_libro:
            return True
        if libro_actual.codigo > id_libro: 
            return self._buscar_libro(libro_actual.izquierdo, id_libro)
        if libro_actual.codigo < id_libro: 
            return self._buscar_libro(libro_actual.derecho, id_libro)
        
b = Biblioteca()

b.insertar("La Odisea", 9) 
b.insertar("Pajaros en la Boca", 7) 
b.insertar("Frankestein", 8)
b.insertar("Matilda", 4)
b.insertar("Los Ojos de la Noche", 2)
b.insertar("El Espejo Africano", 3)
b.insertar("Martin Fierro", 6)
                                    
c = 2
print(f"¿Está el libro {c}?")
print(b.buscar_libro(c))

print("Menor código: ")
print(b.obtener_menor_codigo())

b.eliminar_libro(c)

print(f"Después de eliminar el libro {c}: ")

print(f"¿Está el libro {c}?")
print(b.buscar_libro(c))

print("Menor código: ")
print(b.obtener_menor_codigo())
    
#5)

class Pelicula:
    def __init__(self, nombre, codigo, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.codigo = codigo
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"

class Videoclub:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def obtener_menor_codigo(self):
        return self._obtener_menor_codigo(self.raiz)
    def _obtener_menor_codigo(self, nodo_actual):
        if nodo_actual.izquierdo is None:
            return (nodo_actual.nombre, nodo_actual.codigo)
        return self._obtener_menor_codigo(nodo_actual.izquierdo)
    def minimo_nodo(self):
        return self._minimo_nodo(self.raiz)
    def _minimo_nodo(self, nodo_actual):
        if nodo_actual.izquierdo is None:
            return Pelicula(nodo_actual.nombre, nodo_actual.codigo)
        return self._minimo_nodo(nodo_actual.izquierdo)
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
            sucesor = self._minimo_nodo(nodo_actual.derecho)
            nodo_actual.nombre = sucesor.nombre
            nodo_actual.codigo = sucesor.codigo
            nodo_actual.derecho = self._eliminar_pelicula(nodo_actual.derecho, sucesor.codigo)
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
    def _a_string(self, elementos):
        if not elementos:
            return ""
        if len(elementos) == 1:
            return str(elementos[0])
        return (str(elementos[0]) + "\n" + self._a_string(elementos[1:]))
    def __str__(self):
        return self._a_string(self.listar_ordenado())
    

    
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

#6)

class Persona:
    def __init__(self, nombre, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Codigo: {self.nombre}"
    
class Arbol_Genealogico:
    def __init__(self, raiz):
        self.raiz = raiz
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura(nodo_actual.izquierdo), self._altura(nodo_actual.derecho))
    def camino_raiz_hoja(self, elemento):
        return self._camino_raiz_hoja(self.raiz, elemento)
    def _camino_raiz_hoja(self, nodo, elemento):
        if nodo is None:
            return []
        if nodo.nombre == elemento:
            return [nodo.nombre]
        camino_izq = self._camino_raiz_hoja(nodo.izquierdo, elemento)
        if camino_izq:
            return [nodo.nombre] + camino_izq
        camino_der = self._camino_raiz_hoja(nodo.derecho, elemento)
        if camino_der:
            return [nodo.nombre] + camino_der
        return []  
    def antecesores(self, elemento):
        return self._antecesores(self.raiz, elemento)
    def _antecesores(self, nodo_actual, elemento):
        if nodo_actual is None:
            return []
        if nodo_actual.nombre == elemento:
            return []
        izquierda = self._antecesores(nodo_actual.izquierdo, elemento)
        if izquierda != [] or (nodo_actual.izquierdo is not None \
          and nodo_actual.izquierdo.nombre == elemento):
            return [nodo_actual.nombre] + izquierda
        derecha = self._antecesores(nodo_actual.derecho, elemento)
        if derecha != [] or (nodo_actual.derecho is not None \
          and nodo_actual.derecho.nombre == elemento):
            return [nodo_actual.nombre] + derecha
        return []
    
a = Arbol_Genealogico(Persona("Tito", Persona("Paula", Persona("Salvador", None, None), None), 
                      Persona("Chiqui", Persona("Juan", None, None), 
                                        Persona("Milagros", None, None))))
print("Altura del arbol: ")
print(a.altura())

p = "Salvador"
print(f"Camino desde la raíz hasta {p}: ")
print(a.camino_raiz_hoja(p))

print(f"Antecesores de {p}: ")
print(a.antecesores(p))

#7)

class Empleado:
    def __init__(self, nombre, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Codigo: {self.nombre}"
    
class Organigrama:
    def __init__(self, raiz):
        self.raiz = raiz
    def maximo(self):
        return self._maximo(self.raiz)
    def _maximo(self, nodo_actual):
        if nodo_actual.derecho is None:
            return nodo_actual.nombre
        return self._maximo(nodo_actual.derecho)
    def jefe_inmediato(self, empleado):
        return self._jefe_inmediato(self.raiz, empleado)
    def _jefe_inmediato(self, nodo_actual, empleado):
        if nodo_actual is None:
            return -1
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            return -1
        if (nodo_actual.izquierdo is not None and nodo_actual.izquierdo.nombre == empleado) \
        or (nodo_actual.derecho is not None and nodo_actual.derecho.nombre == empleado):
            return nodo_actual.nombre
        izquierda = self._jefe_inmediato(nodo_actual.izquierdo, empleado)
        if izquierda != -1:
            return izquierda
        return self._jefe_inmediato(nodo_actual.derecho, empleado)
    def subordinados(self, empleado):
        return self._subordinados(self.raiz, empleado)
    def _subordinados(self, nodo_actual, empleado, llegue_al_elemento=False):
        if nodo_actual is None:
            return None
        if nodo_actual.nombre == empleado:
            llegue_al_elemento=True
        if llegue_al_elemento:
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                return []
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is not None):
                return [nodo_actual.izquierdo.nombre] + [nodo_actual.derecho.nombre] + \
                self._subordinados(nodo_actual.izquierdo, empleado, llegue_al_elemento) + \
                    self._subordinados(nodo_actual.derecho, empleado, llegue_al_elemento)
            if (nodo_actual.izquierdo is not None and nodo_actual.derecho is None):
                return [nodo_actual.izquierdo.nombre] + \
                self._subordinados(nodo_actual.izquierdo, empleado, llegue_al_elemento)
            if (nodo_actual.izquierdo is None and nodo_actual.derecho is not None):
                return [nodo_actual.derecho.nombre] + \
                self._subordinados(nodo_actual.derecho, empleado, llegue_al_elemento)
        izquierda = self._subordinados(nodo_actual.izquierdo, empleado, llegue_al_elemento)
        if izquierda != None:
            return izquierda
        return self._subordinados(nodo_actual.derecho, empleado, llegue_al_elemento)
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura(nodo_actual.izquierdo), self._altura(nodo_actual.derecho))
    
    
a = Organigrama(Empleado("Tito", Empleado("Paula", Empleado("Salvador", None, None), None), 
                      Empleado("Chiqui", Empleado("Juan", None, None), 
                                        Empleado("Milagros", None, None))))

p = "Chiqui"
print(f"Jefe inmediato de {p}: ")
print(a.jefe_inmediato(p))

print(f"Subordinados de {p}: ")
print(a.subordinados(p))

print("Altura del arbol: ")
print(a.altura())

#8)

class Producto:
    def __init__(self, nombre, codigo, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.codigo = codigo
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"
    
class Catalogo:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def producto_con_menor_codigo(self):
        return self._producto_con_menor_codigo(self.raiz)
    def _producto_con_menor_codigo(self, producto_actual):
        if producto_actual.izquierdo is None:
            return (producto_actual.nombre, producto_actual.codigo)
        return self._producto_con_menor_codigo(producto_actual.izquierdo)
    def producto_con_mayor_codigo(self):
        return self._producto_con_mayor_codigo(self.raiz)
    def _producto_con_mayor_codigo(self, producto_actual):
        if producto_actual.derecho is None:
            return (producto_actual.nombre, producto_actual.codigo)
        return self._producto_con_mayor_codigo(producto_actual.derecho)
    def predecesor(self, elemento):
        return self._predecesor(self.raiz, elemento)
    def _predecesor(self, nodo_actual, elemento, encontrado=False):
        if nodo_actual is None:
            return None
        if nodo_actual.codigo == elemento:
            encontrado = True
        if encontrado:
            if nodo_actual.izquierdo is None:
                return None
            return self._producto_con_mayor_codigo(nodo_actual.izquierdo)
        izquierda = self._predecesor(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._predecesor(nodo_actual.derecho, elemento, encontrado)
    def sucesor(self, elemento):
        return self._sucesor(self.raiz, elemento)
    def _sucesor(self, nodo_actual, elemento, encontrado=False):
        if nodo_actual is None:
            return None
        if nodo_actual.codigo == elemento:
            encontrado = True
        if encontrado:
            if nodo_actual.derecho is None:
                return None
            return self._producto_con_menor_codigo(nodo_actual.derecho)
        izquierda = self._sucesor(nodo_actual.izquierdo, elemento, encontrado)
        if izquierda != None:
            return izquierda
        return self._sucesor(nodo_actual.derecho, elemento, encontrado)

c = Catalogo(Producto("Milka", 4, Producto("Tita", 3, Producto("Rhodesia", 2, None, None), None), 
                      Producto("Block", 6, Producto("Shot", 5, None, None), 
                                        Producto("Milagros", 7, None, None))))

p = 6

print("Producto con menor código: ")
print(c.producto_con_menor_codigo())

print("Producto con mayor código: ")
print(c.producto_con_mayor_codigo())

print(f"Predecesor de {p}: ")
print(c.predecesor(p))

print(f"Sucesor de {p}: ")
print(c.sucesor(p))

#9)

class Elemento:
    def __init__(self, nombre, codigo, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.codigo = codigo
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"
    
class Inventario:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def insertar(self, nombre, codigo):
        self.raiz = self._insertar(self.raiz, nombre, codigo)
    def _insertar(self, elemento_actual, nombre, codigo):
        if elemento_actual is None:
            return Elemento(nombre, codigo)
        if codigo < elemento_actual.codigo:
            elemento_actual.izquierdo = self._insertar(elemento_actual.izquierdo, nombre, codigo)
        elif codigo > elemento_actual.codigo:
            elemento_actual.derecho = self._insertar(elemento_actual.derecho, nombre, codigo)
        return elemento_actual
    def obtener_menor_codigo(self):
        return self._obtener_menor_codigo(self.raiz)
    def _obtener_menor_codigo(self, elemento_actual):
        if elemento_actual.izquierdo is None:
            return (elemento_actual.nombre, elemento_actual.codigo)
        return self._obtener_menor_codigo(elemento_actual.izquierdo)
    def minimo_nodo(self):
        return self._minimo_nodo(self.raiz)
    def _minimo_nodo(self, elemento_actual):
        if elemento_actual.izquierdo is None:
            return Elemento(elemento_actual.nombre, elemento_actual.codigo)
        return self._minimo_nodo(elemento_actual.izquierdo)
    def eliminar_elemento(self, elemento_a_eliminar):
        self.raiz = self._eliminar_elemento(self.raiz, elemento_a_eliminar)
    def _eliminar_elemento(self, elemento_actual, elemento_a_eliminar):
        if elemento_actual is None:
            return None
        if elemento_a_eliminar < elemento_actual.codigo:
            elemento_actual.izquierdo = self._eliminar_elemento(elemento_actual.izquierdo, elemento_a_eliminar)
        elif elemento_a_eliminar > elemento_actual.codigo:
            elemento_actual.derecho = self._eliminar_elemento(elemento_actual.derecho, elemento_a_eliminar)
        else:
            # Caso 1: sin hijo izquierdo
            if elemento_actual.izquierdo is None:
                return elemento_actual.derecho
            # Caso 2: sin hijo derecho
            if elemento_actual.derecho is None:
                return elemento_actual.izquierdo
        # Caso 3: dos hijos
            sucesor = self._minimo_nodo(elemento_actual.derecho)
            elemento_actual.nombre = sucesor.nombre
            elemento_actual.codigo = sucesor.codigo
            elemento_actual.derecho = self._eliminar_elemento(elemento_actual.derecho, sucesor.codigo)
        return elemento_actual
    def buscar_elemento(self, id_elemento):
        return self._buscar_elemento(self.raiz, id_elemento)
    def _buscar_elemento(self, elemento_actual, id_elemento):
        if elemento_actual is None:
            return False
        if elemento_actual.codigo == id_elemento:
            return True
        if elemento_actual.codigo > id_elemento: 
            return self._buscar_elemento(elemento_actual.izquierdo, id_elemento)
        if elemento_actual.codigo < id_elemento: 
            return self._buscar_elemento(elemento_actual.derecho, id_elemento)
        
i = Inventario()

i.insertar("Coca Cola", 9) 
i.insertar("Seven Up", 7) 
i.insertar("Fanta", 8)
i.insertar("Pepsi", 4)
i.insertar("Sprite", 2)
i.insertar("Paso de los Toros", 3)
i.insertar("Schweppes", 6)
                                    
e = 2
print(f"¿Está el elemento {e}?")
print(i.buscar_elemento(e))

i.eliminar_elemento(e)

print(f"Después de eliminar el elemento {e}: ")

print(f"¿Está el elemento {e}?")
print(i.buscar_elemento(e))

#Grafos

#10)

class Red_De_Estaciones:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def vecinos(self, vertice):
        return self._vecinos(self.lista_adyacencia[vertice])
    def _vecinos(self, lista):
        if not lista:
            return []
        vecino = lista[0]
        return [vecino] + self._vecinos(lista[1:])
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
    
r = Red_De_Estaciones({"Echeverria": ["Monroe", "De Los Incas"],
                       "Monroe": ["Congreso", "Migueletes"],
                       "Malabia": ["Federico Lacroze", "Estado De Israel"],
                       "De Los Incas": ["Malabia"],
                       "Congreso": [],
                       "Migueletes": [],
                       "Federico Lacroze": [],
                       "Estado De Israel": []})

origen = "Malabia"
destino = "Echeverria"
print(f"Hay camino de {origen} a {destino}?")
print(r.existe_camino(origen, destino))

origen = "Echeverria"
destino = "Malabia"
print(f"Hay camino de {origen} a {destino}?")
print(r.existe_camino(origen, destino))

#11 y 12)

class Red_Social:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def es_conexo(self):
        if not self.lista_adyacencia:
            return True
        origen = list(self.lista_adyacencia)[0]
        visitados = self.dfs(origen)
        return len(visitados) == len(self.lista_adyacencia)
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
    def vecinos(self, vertice):
        return self._vecinos(self.lista_adyacencia[vertice])
    def _vecinos(self, lista):
        if not lista:
            return []
        vecino = lista[0]
        return [vecino] + self._vecinos(lista[1:])
    
r = Red_Social({"Salvador": ["Martin", "Tomas"],
                       "Martin": ["Sofia", "Franco"],
                       "Tomas": ["Federico", "Martin"],
                       "Sofia": ["Agustin", "Candela"],
                       "Franco": ["Tomas", "Agustin"],
                       "Agustin": ["Salvador", "Federico"],
                       "Candela": ["Sofia", "Martin"],
                       "Federico": ["Salvador", "Tomas"]})

print("¿Es conexa la red?")
print(r.es_conexo())

origen = "Salvador"
print(f"Usuarios alcanzables desde {origen}: ")
print(r.dfs(origen))

#Agrego un usuario Rodrigo sin amigos:
r = Red_Social({"Salvador": ["Martin", "Tomas"],
                       "Martin": ["Sofia", "Franco"],
                       "Tomas": ["Federico", "Martin"],
                       "Sofia": ["Agustin", "Candela"],
                       "Franco": ["Tomas", "Agustin"],
                       "Agustin": ["Salvador", "Federico"],
                       "Candela": ["Sofia", "Martin"],
                       "Federico": ["Salvador", "Tomas"],
                       "Rodrigo": []})

print("¿Es conexa la red?")
print(r.es_conexo())

origen = "Rodrigo"
print(f"Usuarios alcanzables desde {origen}: ")
print(r.dfs(origen))

#13)

import heapq

class Ciudad:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def camino_minimo(self, origen, destino):
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
    
c = Ciudad({"Nazarre 4711": [("Beiro 3934", 6), ("Arregui 4000", 18)],
            "Gualeguaychu 3031": [("Arregui 4000", 4)],
            "Beiro 3934": [("Gualeguaychu 3031", 7)],
            "Arregui 4000": [("Nazarre 4711", 5)]})

origen = "Nazarre 4711"
destino = "Arregui 4000"
print(f"Camino más corto desde {origen} hasta {destino}: ")
print(c.camino_minimo(origen, destino))

#14)

class Comercio:
    def __init__(self, cuentas, transferencias):
        self.cuentas = cuentas
        self.transferencias = transferencias
    def agregar_cuenta(self, cuenta):
        # Si el nodo no existe, lo creamos con una lista vacía de vecinos
        if cuenta not in self.cuentas:
            self.cuentas.append(cuenta)
    def agregar_transferencia(self, inicio, fin, comision, reintegro, bidireccional=False):
        # Aseguramos que ambos nodos existan en el grafo
        self.agregar_cuenta(inicio)
        self.agregar_cuenta(fin)
            
        # Conectamos inicio -> fin
        self.transferencias.append((inicio, fin, comision, reintegro))
        if bidireccional:
            self.transferencias.append((fin, inicio, comision, reintegro))
    def relajar(self, u, v, comision, reintegro, distancia, predecesor):
        if distancia[u] == float("inf"):
            return False
        nueva = distancia[u] + comision - reintegro
        if nueva < distancia[v]:
            distancia[v] = nueva
            predecesor[v] = u
            return True
        return False
    def bellman_ford(self, origen):
        distancia = {v: float("inf") for v in self.cuentas}
        predecesor = {v: None for v in self.cuentas}
        distancia[origen] = 0
        for pasada in range(len(self.cuentas)-1):
            hubo_cambios = False
            for u, v, comision, reintegro in self.transferencias:
                if self.relajar(u, v, comision, reintegro, distancia, predecesor):
                    hubo_cambios = True
            if not hubo_cambios:
                break
        for u, v, comision, reintegro in self.transferencias:
            if self.relajar(u, v, comision, reintegro, distancia, predecesor):
                return distancia, predecesor, True
        return distancia, predecesor, False
    def reconstruir_camino(self, predecesor, distancia, destino):
        if distancia[destino] == float('inf'):
            return None
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = predecesor[actual]
        return camino[::-1]
    def costo_minimo(self, origen, destino):
        distancia, predecesor, ciclo = self.bellman_ford(origen)
        if ciclo:
            return None
        camino = self.reconstruir_camino(predecesor, distancia, destino)
        if camino is None:
            return [], float("inf")
        return (distancia[destino], camino)
    def __str__(self):
        return f"Cuentas:{str(self.cuentas)}, Transferencias:{str(self.transferencias)}"
    
c = Comercio(["banco", "bill_a", "bill_b", "bill_c", "tienda"],
             [("banco", "bill_a", 40, 0), ("banco", "bill_b", 25, 0), 
              ("bill_a", "tienda", 30, 0), ("bill_b", "bill_c", 15, 35),
              ("bill_c", "bill_a", 10, 0), ("bill_c", "tienda", 60, 0),
              ("bill_b", "tienda", 70, 0)])

#Sin ciclo:
print(c.costo_minimo("banco", "tienda"))

c.agregar_transferencia("bill_a", "bill_b", 10, 30)

#Con ciclo:
print(c.costo_minimo("banco", "tienda"))

#15)

class Producto:
    def __init__(self, nombre, codigo, sig=None):
        self.nombre = nombre
        self.codigo = codigo
        self.sig = sig
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"

class Carrito:
    def __init__(self, head=None, ultimo=None):
        self.head = head
        self.ultimo = ultimo
    def agregar_producto(self, nombre, codigo):
        nuevo = Producto(nombre, codigo)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def quitar_producto(self, nombre, codigo):
        producto = Producto(nombre, codigo)
        self.head = self._quitar_producto(self.head, producto)
    def _quitar_producto(self, producto_actual, producto):
        if producto_actual is None:
            return None
        if (producto_actual.nombre == producto.nombre and producto_actual.codigo == producto.codigo):
            if producto_actual == self.ultimo:
                self.ultimo = None  # o el anterior
            return producto_actual.sig
        producto_actual.sig = self._quitar_producto(producto_actual.sig, producto)
        return producto_actual
    def total(self):
        return self._total(self.head)
    def _total(self, producto_actual):
        if producto_actual is None:
            return 0
        return 1 + self._total(producto_actual.sig)
    
c = Carrito()

c.agregar_producto("Leche Sancor", 4) 
c.agregar_producto("Yerba Mañanita", 7) 
c.agregar_producto("Chocolate Aguila", 3)
c.agregar_producto("Salsa Arcor", 10)
c.agregar_producto("Papas Fritas Lays", 1)

print("Cantidad de productos en el carrito: ")
print(c.total())

nombre = "Salsa Arcor"
codigo = 10

c.quitar_producto(nombre, codigo)

print(f"Después de eliminar {(nombre, codigo)}")

print("Cantidad de productos en el carrito: ")
print(c.total())

#16)

class Jugador:
    def __init__(self, nombre, sig=None):
        self.nombre = nombre
        self.sig = sig
    def __repr__(self):
        return f"Nombre: {self.nombre}"

class Equipo:
    def __init__(self, head=None, ultimo=None):
        self.head = head
        self.ultimo = ultimo
    def agregar_jugador(self, nombre):
        nuevo = Jugador(nombre)
        if self.head is None:
            self.head = nuevo
            self.ultimo = nuevo
            return
        self.ultimo.sig = nuevo
        self.ultimo = nuevo
    def eliminar_jugador(self, nombre):
        jugador = Jugador(nombre)
        self.head = self._eliminar_jugador(self.head, jugador)
    def _eliminar_jugador(self, jugador_actual, jugador):
        if jugador_actual is None:
            return None
        if jugador_actual.nombre == jugador.nombre:
            if jugador_actual == self.ultimo:
                self.ultimo = None  # o el anterior
            return jugador_actual.sig
        jugador_actual.sig = self._eliminar_jugador(jugador_actual.sig, jugador)
        return jugador_actual
    def cantidad_jugadores(self):
        return self._cantidad_jugadores(self.head)
    def _cantidad_jugadores(self, jugador_actual):
        if jugador_actual is None:
            return 0
        return 1 + self._cantidad_jugadores(jugador_actual.sig)
    
e = Equipo()

e.agregar_jugador("Fernandez") 
e.agregar_jugador("Rodriguez") 
e.agregar_jugador("Gonzalez")
e.agregar_jugador("Martinez")
e.agregar_jugador("Jimenez")

print("Cantidad de jugadores en el equipo: ")
print(e.cantidad_jugadores())

nombre = "Rodriguez"

e.eliminar_jugador(nombre)

print(f"Después de eliminar a {nombre}")

print("Cantidad de jugadores en el equipo: ")
print(e.cantidad_jugadores())

#17)

class Contacto:
    def __init__(self, nombre, telefono, izquierdo=None, derecho=None):
        self.nombre = nombre
        self.telefono = telefono
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}"
    
class Agenda:
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
        self.raiz = raiz
    def agregar_contacto(self, nombre, telefono):
        self.raiz = self._agregar_contacto(self.raiz, nombre, telefono)
    def _agregar_contacto(self, contacto_actual, nombre, telefono):
        if contacto_actual is None:
            return Contacto(nombre, telefono)
        if nombre < contacto_actual.nombre:
            contacto_actual.izquierdo = self._agregar_contacto(contacto_actual.izquierdo, nombre, telefono)
        elif nombre > contacto_actual.nombre:
            contacto_actual.derecho = self._agregar_contacto(contacto_actual.derecho, nombre, telefono)
        return contacto_actual
    def minimo_nodo(self):
        return self._minimo_nodo(self.raiz)
    def _minimo_nodo(self, contacto_actual):
        if contacto_actual.izquierdo is None:
            return Contacto(contacto_actual.nombre, contacto_actual.telefono)
        return self._minimo_nodo(contacto_actual.izquierdo)
    def eliminar_contacto(self, nombre, telefono):
        self.raiz = self._eliminar_contacto(self.raiz, nombre, telefono)
    def _eliminar_contacto(self, contacto_actual, nombre, telefono):
        if contacto_actual is None:
            return None
        if nombre < contacto_actual.nombre:
            contacto_actual.izquierdo = self._eliminar_contacto(contacto_actual.izquierdo, nombre, telefono)
        elif nombre > contacto_actual.nombre:
            contacto_actual.derecho = self._eliminar_contacto(contacto_actual.derecho, nombre, telefono)
        else:
            # Caso 1: sin hijo izquierdo
            if contacto_actual.izquierdo is None:
                return contacto_actual.derecho
            # Caso 2: sin hijo derecho
            if contacto_actual.derecho is None:
                return contacto_actual.izquierdo
        # Caso 3: dos hijos
            sucesor = self._minimo_nodo(contacto_actual.derecho)
            contacto_actual.nombre = sucesor.nombre
            contacto_actual.telefono = sucesor.telefono
            contacto_actual.derecho = self._eliminar_contacto(contacto_actual.derecho, sucesor.nombre, sucesor.telefono)
        return contacto_actual
    def buscar_contacto(self, nombre, telefono):
        return self._buscar_contacto(self.raiz, nombre, telefono)
    def _buscar_contacto(self, elemento_actual, nombre, telefono):
        if elemento_actual is None:
            return False
        if elemento_actual.nombre == nombre and elemento_actual.telefono == telefono:
            return True
        if elemento_actual.nombre > nombre: 
            return self._buscar_contacto(elemento_actual.izquierdo, nombre, telefono)
        if elemento_actual.nombre < nombre: 
            return self._buscar_contacto(elemento_actual.derecho, nombre, telefono)
        
a = Agenda()

a.agregar_contacto("Salvador", 44816375) 
a.agregar_contacto("Paula", 67932540) 
a.agregar_contacto("Alejandro", 41727364)
a.agregar_contacto("Roberto", 46838602)
a.agregar_contacto("Graciela", 45671897)
a.agregar_contacto("Victoria", 45674434)
a.agregar_contacto("Carlos", 45667876)
                                    
nombre = "Victoria"
telefono = 45674434

print(f"¿Está el contacto {(nombre, telefono)} en la agenda?")
print(a.buscar_contacto(nombre, telefono))

a.eliminar_contacto(nombre, telefono)

print(f"Después de eliminar el contacto {(nombre, telefono)}: ")

print(f"¿Está el contacto {(nombre, telefono)} en la agenda?")
print(a.buscar_contacto(nombre, telefono))

#18)

class Mapa:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
    def nodos(self):
        return list(self.lista_adyacencia)
    def vecinos(self, nodo):
        return self.lista_adyacencia[nodo]

class Dijkstra:
    def __init__(self, mapa):
        self.mapa = mapa
    def camino_minimo(self, origen, destino):
        # 1. Inicializar las distancias
            dist = {nodo: float("inf") for nodo in self.mapa.lista_adyacencia}
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
                for v, peso in self.mapa.lista_adyacencia[u]:
                    nueva_distancia = distancia_actual + peso
                    if nueva_distancia < dist[v]:
                        dist[v] = nueva_distancia
                        previo[v] = u
                        heapq.heappush(cola, (dist[v], v))
        
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
        return (f"Nodos: {self.cantidad_nodos}\n" f"Distancia: {self.distancia} km")
    
m = Mapa({"Nazarre 4711": [("Beiro 3934", 6), ("Arregui 4000", 18)],
            "Gualeguaychu 3031": [("Arregui 4000", 4)],
            "Beiro 3934": [("Gualeguaychu 3031", 7)],
            "Arregui 4000": [("Nazarre 4711", 5)]})

d = Dijkstra(m)

origen = "Nazarre 4711"
destino = "Arregui 4000"
print(f"Camino más corto desde {origen} hasta {destino}: ")
print(d.camino_minimo(origen, destino))
    
#Árboles de expresiones

from typing import Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}"

class Hoja(Generic[B]):
    def __init__(self, valor: B):
        self.valor = valor
    def __repr__(self):
        return f"{self.valor}"
        
class NodoInterno(Generic[A, B]):
    def __init__(self, valor: A, izquierdo, derecho):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
    def __repr__(self):
        return f"{self.valor}"
    
class ArbolBinarioHojas(Generic[A,B]):
    def __init__(self, raiz):
        self.raiz = raiz
    def insertar_hoja(self, nodo, valor_interno, valor_hoja):
        if isinstance(nodo, Hoja):
            return NodoInterno(valor_interno, Hoja(nodo.valor), Hoja(valor_hoja))
        return NodoInterno(nodo.valor, self.insertar_hoja(nodo.izquierdo, \
            valor_interno,valor_hoja),nodo.derecho)
    @staticmethod
    def insertar_interno(nodo, hoja_objetivo, valor_interno, nueva_hoja):
        if isinstance(nodo, Hoja):
            if nodo.valor == hoja_objetivo:
                return NodoInterno(valor_interno, Hoja(hoja_objetivo), Hoja(nueva_hoja))
            return nodo
        return NodoInterno(nodo.valor,
        ArbolBinarioHojas.insertar_interno(nodo.izquierdo, hoja_objetivo, \
            valor_interno, nueva_hoja), \
        ArbolBinarioHojas.insertar_interno(nodo.derecho, hoja_objetivo, \
            valor_interno, nueva_hoja))
    def eliminar_hoja(self, nodo, valor):
        if isinstance(nodo, Hoja):
            if nodo.valor == valor:
                raise ValueError("No se puede dejar árbol vacío")
            return nodo
    @staticmethod
    def eliminar_interno(nodo, valor):
        if isinstance(nodo, Hoja):
            return nodo
        if nodo.valor == valor:
            return nodo.derecho
        return NodoInterno(nodo.valor, \
        ArbolBinarioHojas.eliminar_interno(nodo.izquierdo, valor), \
        ArbolBinarioHojas.eliminar_interno(nodo.derecho, valor))
    def es_hoja(nodo):
        return isinstance(nodo, Hoja)
    def altura(self):
        return self._altura(self.raiz)
    def _altura(self, nodo):
        if isinstance(nodo, Hoja):
            return 0
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))
    def cantidad_hojas(self):
        return self._cantidad_hojas(self.raiz)
    def _cantidad_hojas(self, nodo):
        if isinstance(nodo, Hoja):
            return 1
        return (self._cantidad_hojas(nodo.izquierdo) + \
            self._cantidad_hojas(nodo.derecho))
    def cantidad_internos(self):
        return self._cantidad_internos(self.raiz)
    def _cantidad_internos(self, nodo):
        if isinstance(nodo, Hoja):
            return 0
        return (1 + self._cantidad_internos(nodo.izquierdo) \
            + self._cantidad_internos(nodo.derecho))
    def cantidad_nodos(self):
        return self.cantidad_hojas() + self.cantidad_internos()
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return ([nodo.valor] + self._preorden(nodo.izquierdo) + \
            self._preorden(nodo.derecho))
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return (self._inorden(nodo.izquierdo) + [nodo.valor] + \
            self._inorden(nodo.derecho))
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo):
        if isinstance(nodo, Hoja):
            return [nodo.valor]
        return (self._postorden(nodo.izquierdo) + self._postorden(nodo.derecho) + \
            [nodo.valor])
    def __str__(self):
        return f"Preorden: {str(self.preorden())}, Postorden: {str(self.postorden())}, Inorden: {str(self.inorden())}"

from abc import ABC, abstractmethod
    
class Operador(ABC):
    simbolo: str  
    @staticmethod
    @abstractmethod  
    def operar(a, b):  
        pass

    def __str__(self) -> str:
        return self.simbolo  
    
class Suma(Operador):
    simbolo: str = '+' 
    @staticmethod
    def operar(a, b): 
        return a + b 
    def __repr__(self):
        return f"{self.simbolo}"
    
class Producto(Operador):
    simbolo: str = '*'  

    @staticmethod
    def operar(a, b):  
        return a * b  
    def __repr__(self):
        return f"{self.simbolo}"

class Resta(Operador):
    simbolo: str = '-' 
    @staticmethod
    def operar(a, b): 
        return a - b  
    def __repr__(self):
        return f"{self.simbolo}"
    
class Division(Operador):
    simbolo: str = '/'  

    @staticmethod
    def operar(a, b):  
        return a / b
    def __repr__(self):
        return f"{self.simbolo}"
    
class Potencia(Operador):
    simbolo: str = '^'  

    @staticmethod
    def operar(a, b):  
        return a ** b
    def __repr__(self):
        return f"{self.simbolo}"
    
class Mayor(Operador):
    simbolo: str = '>'  

    @staticmethod
    def operar(a, b):  
        return a > b
    def __repr__(self):
        return f"{self.simbolo}"
    
class Menor(Operador):
    simbolo: str = '<'  

    @staticmethod
    def operar(a, b):  
        return a < b
    def __repr__(self):
        return f"{self.simbolo}"
    
class y(Operador):
    simbolo: str = 'y'  

    @staticmethod
    def operar(a, b):  
        return a and b
    def __repr__(self):
        return f"{self.simbolo}"
    
class o(Operador):
    simbolo: str = 'o'  

    @staticmethod
    def operar(a, b):  
        return a or b
    def __repr__(self):
        return f"{self.simbolo}"
    
class ExpresionAritmetica(ArbolBinarioHojas):

    def evaluar(self):
        return self._evaluar(self.raiz)

    def _evaluar(self, nodo):
        if isinstance(nodo, Hoja):
            return nodo.valor
        return nodo.valor.operar(self._evaluar(nodo.izquierdo), self._evaluar(nodo.derecho))
    
    def __str__(self) -> str:
        return super().__str__()

#1)

class Calculadora_De_Descuentos:
    def __init__(self, precio, impuestos, descuento):
        self.precio = precio
        self.impuestos = impuestos
        self.descuento = descuento
    def calcular_monto_total(self):
        cuenta = ExpresionAritmetica(NodoInterno(Producto(), 
                NodoInterno(Suma(),Hoja(self.precio),Hoja(self.impuestos)),Hoja(self.descuento)))
        return cuenta.evaluar()

c = Calculadora_De_Descuentos(1000, 200, 0.8)

print("------------------------------------------")
print(f"1) Monto total: {c.calcular_monto_total()}")

#2)

class Calculadora_Cientifica:
    def __init__(self, expresion):
        self.expresion = expresion
    def calcular_resultado(self):
        return self.expresion.evaluar()
    def __str__(self):
        return f"Resultado: {self.calcular_resultado()}"

c = Calculadora_Cientifica(ExpresionAritmetica(NodoInterno(Producto(), NodoInterno(Suma(), Hoja(3), Hoja(5)), 
                NodoInterno(Resta(), Hoja(10), Hoja(2)))))

print(f"2) {c}")

#3)

class Cliente:
    def __init__(self, ingresos, antiguedad):
        self.ingresos = ingresos
        self.antiguedad = antiguedad
    @staticmethod   
    def decidir(cliente):
        cumple_ingresos = ExpresionAritmetica(NodoInterno(Mayor(),Hoja(cliente.ingresos), Hoja(500000))).evaluar()
        cumple_antiguedad = ExpresionAritmetica(NodoInterno(Mayor(),Hoja(cliente.antiguedad), Hoja(2))).evaluar()
        if cumple_ingresos and cumple_antiguedad:
            return True
        return False
        
c = Cliente(600000, 3)
print(f"3) {c.decidir(c)}")

#4)

class Paciente:
    def __init__(self, temperatura):
        self.temperatura = temperatura
    def diagnosticar(self):
        tiene_fiebre = ExpresionAritmetica(NodoInterno(Mayor(),Hoja(self.temperatura), Hoja(37))).evaluar()
        if tiene_fiebre:
            return "¿Tiene tos?"
        return "¿Tiene dolor muscular?"
    
p = Paciente(38)
print(f"4) {p.diagnosticar()}")

#5)

class Evaluacion_De_Impuestos:
    def __init__(self, monto_base, iva, descuento):
        self.monto_base = monto_base
        self.iva = iva
        self.descuento = descuento
    def monto_final(self):
        cuenta = ExpresionAritmetica(NodoInterno(Resta(), 
                NodoInterno(Suma(),Hoja(self.monto_base),Hoja(self.iva)),Hoja(self.descuento)))
        return cuenta.evaluar()

e = Evaluacion_De_Impuestos(2000, 400, 200)
print(f"5) Monto final: {e.monto_final()}")

#6)

class Interpretador_Logico:
    def __init__(self, expresion):
        self.expresion = expresion
    def evaluar(self):
        return self.expresion.evaluar()
A = True
B = False
C = False
i = Interpretador_Logico(ExpresionAritmetica(NodoInterno(o(), NodoInterno(y(), Hoja(A), Hoja(B)), Hoja(C))))
print(f"6) {i.evaluar()}")

#7)

class Sistema_De_Recomendacion:
    def __init__(self, gusto):
        self.gusto = gusto
    def evaluar(self):
        le_gusta_ciencia_ficción = ExpresionAritmetica(NodoInterno(Mayor(),Hoja(self.gusto), Hoja(60))).evaluar()
        if le_gusta_ciencia_ficción:
            return "¿Le gusta acción?"
        return "¿Prefiere drama?"
    
s = Sistema_De_Recomendacion(61)
print(f"7) {s.evaluar()}")

#8)

class Empresa_De_Seguros:
    def __init__(self, cobertura_base, extras, factor_de_riesgo):
        self.cobertura_base = cobertura_base
        self.extras = extras
        self.factor_de_riesgo = factor_de_riesgo
    def cotizar(self):
        costo = ExpresionAritmetica(NodoInterno(Producto(), 
                NodoInterno(Suma(),Hoja(self.cobertura_base),Hoja(self.extras)),Hoja(self.factor_de_riesgo)))
        return costo.evaluar()

e = Empresa_De_Seguros(10000, 1500, 3)
print(f"8) Costo: {e.cotizar()}")

#9)

class Expresion:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def evaluar(self):
        expresion = ExpresionAritmetica(NodoInterno(Producto(), 
                NodoInterno(Suma(),Hoja(self.a),Hoja(self.b)), Hoja(self.c)))
        return expresion.evaluar()

e = Expresion(3, 5, 2)
print(f"9) Resultado: {e.evaluar()}")

#10)

class Recorrer_Expresion:
    def __init__(self, raiz):
        self.raiz = raiz
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor) + " "
        return (str(nodo.valor) + " " + self._preorden(nodo.izquierdo) + \
            self._preorden(nodo.derecho))
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor)
        return ("(" + self._inorden(nodo.izquierdo) + " " + str(nodo.valor) + " "
            + self._inorden(nodo.derecho)+ ")")
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor) + " "
        return (self._postorden(nodo.izquierdo) + self._postorden(nodo.derecho) + \
            str(nodo.valor) + " ")
            
e = Recorrer_Expresion(NodoInterno(Producto(), 
     NodoInterno(Suma(),Hoja("a"),Hoja("b")), Hoja("c")))

print("10)")
print(e.preorden())
print(e.inorden())
print(e.postorden())

#11)

class Optimizacion_Salarial:
    def __init__(self, sueldo, bono, descuento):
        self.sueldo = sueldo
        self.bono = bono
        self.descuento = descuento
    def evaluar(self):
        costo = ExpresionAritmetica(NodoInterno(Producto(), 
                NodoInterno(Suma(),Hoja(self.sueldo),Hoja(self.bono)),
                NodoInterno(Resta(), Hoja(1), Hoja(self.descuento))))
        return costo.evaluar()

o = Optimizacion_Salarial(360000, 150000, 0.2)
print(f"11) Costo: {o.evaluar()}")

#12)

class Evaluador_Financiero:
    def __init__(self, capital, tasa, n):
        self.capital = capital
        self.tasa = tasa
        self.n = n
    def evaluar(self):
        costo = ExpresionAritmetica(NodoInterno(Producto(), 
                Hoja(self.capital),
                NodoInterno(Potencia(), NodoInterno(Suma(), Hoja(1), Hoja(self.tasa)), Hoja(self.n))))
        return costo.evaluar()

e = Evaluador_Financiero(4, 4, 3)
print(f"12) Costo: {e.evaluar()}")

#13)

class Compilador_Simplificado:
    def __init__(self, raiz):
        self.raiz = raiz
    def preorden(self):
        return self._preorden(self.raiz)
    def _preorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor) + " "
        return (str(nodo.valor) + " " + self._preorden(nodo.izquierdo) + \
            self._preorden(nodo.derecho))
    def inorden(self):
        return self._inorden(self.raiz)
    def _inorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor)
        return ("(" + self._inorden(nodo.izquierdo) + " " + str(nodo.valor) + " "
            + self._inorden(nodo.derecho)+ ")")
    def postorden(self):
        return self._postorden(self.raiz)
    def _postorden(self, nodo):
        if isinstance(nodo, Hoja):
            return str(nodo.valor) + " "
        return (self._postorden(nodo.izquierdo) + self._postorden(nodo.derecho) + \
            str(nodo.valor) + " ")
            
c = Compilador_Simplificado(NodoInterno(Producto(), 
     NodoInterno(Suma(),Hoja(4),Hoja(3)), Hoja(2)))

print("13)")
print(c.preorden())
print(c.inorden())
print(c.postorden())