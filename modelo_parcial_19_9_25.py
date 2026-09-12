#1)
#El enfoque imperativo detalla la secuencia exacta de órdenes usando variables mutables,
#bucles y condiciones. En cambio, el paradigma funcional resuelve problemas evaluando 
#expresiones y transformando datos. Éstos no cambian, se crean nuevos valores en lugar
#de modificar los existentes devolviendo siempre el mismo resultado.
#En pocas palabras, el imperativo detalla el cómo, y el funcional detalla el qué.
#Por ejemplo, para calcular la suma o el producto entre dos elementos, preferiría usar 
#el funcional, porque devuelve siempre el mismo resultado. En cambio para manejar 
#listas preferiría el enfoque imperativo porque la lista es un tipo mutable, se pueden 
#agregar o eliminar elementos y recorrer la lista mediante un for o while.

#2)

#Elijo invertir lista:
def invertir_lista_recursivo(lista):
    if not lista:
        return[]
    return [lista[-1]] + invertir_lista_recursivo(lista[0:len(lista)-1])

print('Invertir lista recursivo')
print(invertir_lista_recursivo([1,2,3,4,5]))

def invertir_lista_funcional(lista):
    return lista[::-1]

print('Invertir lista funcional')
print(invertir_lista_funcional([1,2,3,4,5]))

def invertir_lista_iterativo(lista):
    lista_nueva = []
    for i in range(len(lista)-1, -1, -1):
        lista_nueva.append(lista[i])
    return lista_nueva

print('Invertir lista iterativo')
print(invertir_lista_iterativo([1,2,3,4,5]))

#Elijo permutar los elementos de una lista:
    
def permutaciones_recursivo(lista):
    if len(lista) <= 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
        primero = lista[i]

        resto = lista[:i] + lista[i+1:]

        for p in permutaciones_recursivo(resto):
            resultado.append([primero] + p)

    return resultado

print('Permutaciones recursiva')
lista = [1,2,3]
print(f"Las permutaciones de {lista} son {permutaciones_recursivo(lista)}")

def permutaciones_funcional(lista):
    if len(lista) <= 1:
        return [lista]
    
    return [
        [lista[i]] + resto
        for i in range(len(lista))
        for resto in permutaciones_funcional(lista[:i] + lista[i+1:])
    ]

print('Permutaciones funcional')
elementos = [1, 2, 3]
print(f"Las permutaciones de {lista} son {permutaciones_funcional(elementos)}")

def permutaciones_iterativo(lista):
    actual = sorted(lista)
    resultado = [list(actual)]
    while True:
        i = -1
        for k in range(len(actual) - 2, -1, -1):
            if actual[k] < actual[k + 1]:
                i = k
                break
        if i == -1:
            break
        j = -1
        for k in range(len(actual) - 1, i, -1):
            if actual[i] < actual[k]:
                j = k
                break
        actual[i], actual[j] = actual[j], actual[i]
        actual[i + 1:] = reversed(actual[i + 1:])
        resultado.append(list(actual))
    return resultado

print('Permutaciones iterativa')
elementos = [1, 2, 3]
print(f"Las permutaciones de {lista} son {permutaciones_iterativo(elementos)}")

#Elijo sumar los elementos de una lista:

def sumatoria_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + sumatoria_recursiva(lista[1:])

print('Sumatoria recursiva:')
print(sumatoria_recursiva([1,2,3,4,5]))

from functools import reduce

def sumar(x,y):
    return x+y

numeros = [1,2,3,4,5]

sumatoria_funcional = reduce(sumar, numeros)

print('Sumatoria funcional:')
print(sumatoria_funcional)

def sumatoria_iterativa(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return suma

print('Sumatoria iterativa:')
print(sumatoria_iterativa([1,2,3,4,5]))

#3)

def anota(funcion_original):
    def wrapper(*args, **kwargs):
        # 1. Imprime el nombre de la función y sus argumentos
        print(f"Llamando a la función '{funcion_original.__name__}'")
        print(f"  - Argumentos posicionales (args): {args}")
        print(f"  - Argumentos de palabra clave (kwargs): {kwargs}")
        
        # 2. Ejecuta la función original y guarda su resultado
        resultado = funcion_original(*args, **kwargs)
        
        return resultado
    return wrapper

# --- Prueba del decorador ---

@anota
def registrar_usuario(nombre, edad, rol="usuario"):
    print(f"-> [Éxito] {nombre} ({edad} años) registrado como {rol}.\n")

# Ejecución con diferentes argumentos
registrar_usuario("Lucas", 28)
registrar_usuario("Elena", 34, rol="administrador")

def anota(funcion):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}{args}")
        return funcion(*args, **kwargs)
    return wrapper


@anota
def sumatoria_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + sumatoria_recursiva(lista[1:])

sumatoria_recursiva([1,2,3])
    