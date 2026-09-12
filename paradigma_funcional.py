from functools import reduce

def elevar_al_cuadrado(numero):
    return numero**2

numeros = [1,2,3,4,5]

resultados = list(map(elevar_al_cuadrado, numeros))

print(resultados)

def multiplicar(x,y):
    return x*y

numeros = [1,2,3,4,5]

producto_total = reduce(multiplicar, numeros)

print(f"El producto de los elementos de la lista es: {producto_total}")

multiplicar = lambda x, y: x * y

resultado = multiplicar(3, 5)

print(f"El producto de la multiplicacion es: {resultado}")

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_cuadrados = list(map(lambda x: x ** 2, numeros_pares))

suma_total = reduce(lambda x, y: x + y, numeros_cuadrados)

print(f"Lista_original: {numeros}")

print(f"Números pares: {numeros_pares}")

print(f"Números al cuadrado: {numeros_cuadrados}")

print(f"La suma total es: {suma_total}")

from typing import TypeVar, NamedTuple

T = TypeVar('T')
class ConjuntoInmutable(NamedTuple):
    elementos: tuple  
    def contiene(self, elemento: T) -> bool:
          return elemento in self.elementos

elementos = (1, 2, 3, 4)
conjunto = ConjuntoInmutable(elementos=elementos)
print(conjunto)  
print(conjunto.contiene(3)) 
#conjunto.elementos += (5,) 


def obtener_id(nombre):
    if nombre == 'Juan':
        return 4
    if nombre == 'Ana':
        return 3
    if nombre == 'Pedro':
        return 5
    
nombres = ["Juan", "Ana", "Pedro"]

resultados = list(map(obtener_id, nombres))

print(f"Obtener id: {resultados}")

def contar_letra(cadena, letra):
    return cadena.count(letra)

cadenas = ['casa', 'hogar', 'espacio', 'cuento']
letra = 'a'

resultados = list(map(lambda cadena: contar_letra(cadena, letra), cadenas))
print(f"Cantidad de aes: {resultados}")

def convertir_a_mayuscula(letra):
    return letra.upper()
    
lista = ['hola mundo', 'algoritmos 2']

resultados = list(map(convertir_a_mayuscula, lista))

print(f"Convertir a mayúscula: {resultados}")

def es_primo(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return es_primo(n, i+1)

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_primos = list(filter(es_primo, numeros))

print(f"Números primos: {numeros_primos}")

def longitud_mayor_que_5(cadena):
    return len(cadena) > 5

cadenas = ['lampara','luz','idioma,','ave','computadora','te']

palabras_largas = list(filter(longitud_mayor_que_5, cadenas))

print(f"Palabras con más de 5 letras: {palabras_largas}")

def multiplicar(x,y):
    return x*y

numeros = [1,2,3,4,5]

producto_lista = reduce(multiplicar, numeros)

print(f"Producto de todos los elementos de la lista: {producto_lista}")

def es_mas_larga(palabra1, palabra2):
    if len(palabra1) >= len(palabra2):
        return palabra1
    return palabra2

palabras = ['lampara','luz','idioma,','ave','computadora','te']

palabra_mas_larga = reduce(es_mas_larga, palabras)

print(f"Palabra más larga: {palabra_mas_larga}")

def actualizar_frecuencia(diccionario, elemento):
    if elemento in diccionario:
        diccionario[elemento] += 1
    else:
        diccionario[elemento] = 1
    return diccionario

lista = [1,2,2,3,3,3,4,4,4,4]

frecuencias = reduce(actualizar_frecuencia, lista, {})  
print(f"Tabla de frecuencias de números: {frecuencias}")

letras = ['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']

frecuencias_letras = reduce(actualizar_frecuencia, letras, {})  
print(f"Tabla de frecuencias de letras: {frecuencias_letras}")

potencia_currificada = lambda base: lambda exp: base ** exp 

resultado = potencia_currificada(2)(3)

def potencia(base, exp):
    return base**exp
def potencia_curry(base):
    def potencia_exp(exp):  
        return base**exp
    return potencia_exp  

print(potencia(2, 3))  
print(potencia_curry(2)(3)) 


print(resultado)

sumar10 = (lambda x: x + 10)

resultado = sumar10(potencia_currificada(2)(3))

print(resultado)

def sumar10(num, inc):
    return num + inc
def sumar10_curry(num):
    def incremento(inc):  
        return num + inc
    return incremento  

resultado = potencia_curry(2)(3)
print(sumar10(resultado, 10))  
print(sumar10_curry(resultado)(10)) 

def log(tipo: str):
     def registrar(mensaje: str):   
        print(f"[{tipo.upper()}] {mensaje}")
     return registrar

log_error = log("error")       
log_alerta = log("alerta")     
log_info = log("información")  
log_error("Se ha producido un error crítico")  
log_alerta("Este es un aviso importante")  
log_info("Esto es solo un mensaje informativo")  

#Decoradores)

from typing import Callable

def wrapper(f: Callable[[], None]) -> None:
    f()
    print("Ejecutada f()")

def ejemplo():
    print("Función ejemplo ejecutada.")

wrapper(ejemplo)

from typing import Any

def wrapper(f: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    resultado = f(*args, **kwargs)
    print(f"Ejecutada {f.__name__}()")
    return resultado

def ejemplo(a, b):
    return a + b

wrapper(ejemplo, 6, 4)

def contador(funcion_original):
    cantidad = 0
    def wrapper(*args, **kwargs):
        # 1. Imprime el nombre de la funciÃ³n y sus argumentos
        nonlocal cantidad
        cantidad += 1
        # 2. Ejecuta la funciÃ³n original y guarda su resultado
        resultado = funcion_original(*args, **kwargs)
        print(f"Llamados: {cantidad}")
        return resultado
    return wrapper

@contador
def saludar():
    print("Hola")
    
saludar()
saludar()
saludar()
    
def solo_positivos(funcion_original):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Sólo se aceptan números positivos")
        return funcion_original(*args, **kwargs)
    return wrapper

@solo_positivos
def cuadrado(n):
    return n * n

print(cuadrado(5))
print(cuadrado(1))

def acepta_no_valor(funcion_original):
    def wrapper(arg):
        if arg is None:
            return None 
        return funcion_original(arg)
    return wrapper

@acepta_no_valor
def cuadrado(n):
    return n * n

print(cuadrado(None))
print(cuadrado(None))

    
def memorizar(funcion_original):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Cache: {args}")
            return cache[args]
        resultado = funcion_original(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@memorizar
def fibonacci(n: int) -> int:
  if n == 0:
      return 0
  if n == 1:
      return 1
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))

def memorizar_persona(funcion_original):
    cache = {}
    def wrapper(*args, **kwargs):
        clave = (args, tuple(kwargs.items()))
        if clave in cache:
            print(f"Cache: {clave}")
            return cache[clave]
        resultado = funcion_original(*args, **kwargs)
        cache[clave] = resultado
        return resultado
    return wrapper

@memorizar_persona
def saludar(nombre, edad):
    return (f"Nombre: {nombre}, Edad: {edad}")
    
saludar('Juan', 20)
saludar('Juan', 20)
saludar('Juan', 20)
saludar('Juan', 20)
#Generadores)

def es_par(n):
    return n % 2 == 0

def generador_pares():
    num = 1  
    while True:
            if es_par(num):
                yield num 
            num += 1
            
par_gen = generador_pares() 
print("Primeros 10 números pares")
for _ in range(10): 
    print(next(par_gen))  
    
def es_cuadrado_perfecto(n, i=0):
    if i > n:
        return False
    if i ** 2 == n:
        return True
    return es_cuadrado_perfecto(n, i+1)

      
def generador_cuadrados_perfectos():
    num = 1  
    while True:
            if es_cuadrado_perfecto(num):
                yield num 
            num += 1
            
cuadrados_perfectos_gen = generador_cuadrados_perfectos() 
print("Primeros 10 números cuadrados perfectos")
for _ in range(10): 
    print(next(cuadrados_perfectos_gen)) 
    
def divisores(n, i=1):
    if i > n:
        return []
    if n % i == 0:
        return [i] + divisores(n, i+1)
    return divisores(n, i+1)

def generador_divisores():
    num = 24 
    i = 0
    while i < len(divisores(num)):
        yield divisores(num)[i]
        i += 1
            
gen_divisores = generador_divisores() 
print("Divisores de 24")
for divisor in gen_divisores: 
    print(divisor) 

def fibonacci(n: int) -> int:
  if n == 0:
      return 0
  if n == 1:
      return 1
  return fibonacci(n-1) + fibonacci(n-2)

def generador_fibonacci():
    num = 0  
    while True:
        yield fibonacci(num) 
        num += 1
               
gen_fibonacci = generador_fibonacci() 
print("Primeros 10 números de fibonacci")
for _ in range(10): 
    print(next(gen_fibonacci))  
    
def combinaciones_longitud_2(lista):
    if len(lista) < 2:
        return []
    resultado = []
    for elem in lista[1:]:
        resultado.append([lista[0], elem])
    return resultado + combinaciones_longitud_2(lista[1:])

def combinaciones_longitud_3(lista):
    if len(lista) < 3:
        return []
    resultado = []
    for i in range(len(lista)):
        primero = lista[i]
        resto = lista[i+1:]
        for j in range(len(resto)):
            for k in range(j+1, len(resto)):
                resultado.append([primero, resto[j], resto[k]])
    return resultado

def generador_combinaciones_longitud_2():
    lista = [1,2,3,4,5]
    yield from combinaciones_longitud_2(lista)
               
gen_combinaciones_longitud_2 = generador_combinaciones_longitud_2() 
print("Combinaciones de longitud 2:")
for comb in gen_combinaciones_longitud_2: 
    print(comb)