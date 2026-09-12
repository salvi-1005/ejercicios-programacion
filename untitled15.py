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
