## INDICE:

def busqueda1(lista, elem):
    for i in range(0, len(lista)):
        if lista[i] == elem:
            return i
    return -1


lista1 = [0, 1, 2, 3, 4, 5]
elem = 5

print(f"El elemento {elem} se ubica en el índice {busqueda1(lista1, elem)}")


## ENUMERATE:

def busqueda2(lista, elem):
    for indice, valor in enumerate(lista):
        if elem == valor:
            return indice
    return -1


lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elem = 9

print(f"El elemento {elem} se ubica en el índice {busqueda2(lista2, elem)}")


## CANTIDAD DE VECES QUE APARECE UN NUMERO:

def cantidadDeApariciones(lista, n):
    contador = 0

    for elem in lista:
        if elem == n:
            contador += 1

    return contador


lista3 = [1, 1, 2, 2, 2, 3, 3, 3, 3]
n = 3

print(f"El elemento {n} aparece {cantidadDeApariciones(lista3, n)} veces en la lista")


## INDICE DE LA ULTIMA VEZ QUE APARECE:

def ultimaAparicion(lista, elem):
    i = len(lista) - 1  # recorro la lista al revés

    while i >= 0:
        if lista[i] == elem:
            return i
        i -= 1

    return -1


lista4 = [1, 2, 3, 2, 4, 3, 5, 5]
elem = 2

print(
    f"La ultima vez que aparece el elemento {elem} en la lista es en el índice "
    f"{ultimaAparicion(lista4, elem)}"
)


## PROPAGAR:

def propagar(lista):
    i = 0

    while i < len(lista) - 1:
        if lista[i + 1] == 0 and lista[i] == 1:
            lista[i + 1] = 1  # si el mío está apagado y el de la izquierda está prendido

        if lista[i + 1] == 1 and lista[i] == 0:
            lista[i] = 1  # si el mío está apagado y el de la derecha está prendido

        i += 1

    j = len(lista) - 1

    while j > 0:
        if lista[j - 1] == 0 and lista[j] == 1:
            lista[j - 1] = 1  # si el mío está apagado y el de la izquierda está prendido

        if lista[j - 1] == 1 and lista[j] == 0:
            lista[j] = 1  # si el mío está apagado y el de la derecha está prendido

        j -= 1

    return lista


fosforos = [0, -1, 1, 0, 0, 1, -1, 0, 1, -1, 1, 0, 0, 0, -1]

print(f"Fósforos: {propagar(fosforos)}")


## CLASE MI CLASE:

class MiClase:
    def __init__(self, val):
        self.valor = val

    def __str__(self):
        return self.valor


A = "algo"

print(A.__str__())


## CLASE PERSONA:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __dimetunombre__(self):
        return self.nombre

    def __dimetuedad__(self):
        return self.edad

    def __eq__(self, otro):
        return (
            isinstance(otro, Persona)
            and self.nombre == otro.nombre
            and self.edad == otro.edad
        )

    def __hash__(self):
        return hash((self.nombre, self.edad))


## CLASE MILISTA:

class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)
    def __getitem__(self, indice):
        return self.elementos[indice]
    def __setitem__(self, key, value):
        self.elementos[key] = value

mi_lista = MiLista([1, 2, 3])
print(mi_lista[1])
mi_lista[2] = 4
print(mi_lista[2])

juana = Persona("juana", 23)
juana2 = Persona("juana", 23)

print(juana == juana2)
print(juana.__dimetunombre__() == juana2.__dimetunombre__())
print(juana.__dimetuedad__() == juana2.__dimetuedad__())

print(juana.__repr__())
print(juana.__eq__(juana2))

juana == juana2

print(juana.__hash__())
print(juana2.__hash__())


## CLASE CONTADOR:

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual < self.limite:
            self.actual += 1
            return self.actual
        else:
            raise StopIteration

contador = Contador(5)
for num in contador:
    print(num)

class Ejemplo1:
    def __init__(self, valor):
        self._protegido = valor

    def mostrar(self):
        return f'Valor protegido: {self._protegido}'

objeto1 = Ejemplo1(10)
print(objeto1.mostrar())  # Salida: Valor protegido: 10

# Acceder directamente al atributo "protegido"
print(objeto1._protegido)  # Salida: 10
