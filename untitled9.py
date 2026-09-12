import csv

numeros = [0,1,2,3,4,5,6,7,8,9]
lista = []
suma = 0
for i in numeros:
    lista.append(numeros[i])
    suma = suma + numeros[i]
c = max(lista)
d = min(lista)
print(lista, suma, c, d)

def eliminar(palabras):
    for i in palabras:
        if len(i) < 4:
            palabras.remove(i)
    return(palabras)

def cantidad_de_apariciones(lista, elem):
    contador = 0
    for i in lista:
        if i == elem:
            contador = contador + 1
    return(contador)

def eliminar_duplicados(palabras):
    for i in palabras:
        if cantidad_de_apariciones(palabras, i) > 1:
            palabras.remove(i)
    return(palabras)

def contar_vocales(palabra):
    contador = 0
    for c in palabra:
        if c in 'aeiou':
            contador += 1
    return contador
        
def es_palindromo(palabra):
    palabra = palabra.lower()   
    return palabra == palabra[::-1]

def diccionario_frecuencia(palabras):
    dic = {}
    for c in palabras:
        dic[c] = cantidad_de_apariciones(palabras, c)
    return dic
    
edades = {'juan':20, 'tobias':21, 'pablo':22, 'matias':23, 'nicolas':24}
lista = []
suma = 0
for i in edades:
    lista.append(edades[i])
    suma = suma + edades[i]
print(suma/len(lista))
print (max(edades, key=edades.get))

def factorial(n):
    res = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            res *= i
    return res

def es_primo(n):
    if n < 2:
        return False
    else:
        for i in range (2, n+1):
            if n % i == 0:
                return False
            return True

i = 0
primos = []
while len(primos) < 20:
    if es_primo(i):
        primos.append(i)
    i += 1
print(primos)

def costo_camion_with(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(f).split(',')
        headers
        ['nombre', 'cajones', 'precio\n']
        contador = 0
        for line in rows:
            contador = contador + float(float(line[1])*float(line[2]))      
    return float(contador)

def buscar_precio(fruta):
    with open(r"C:\Users\SD\Downloads\precios.csv", 'rt', encoding='utf-8') as f:
        headers = next(f).split(',')
        headers
        encontrado = False
        for line in f:
            row = line.split(',')
            nombre = row[0].strip('"')
            precio_fruta = float(row[1])
            if nombre == fruta:
                print('El precio de un cajón de', fruta, 'es:', precio_fruta)
                encontrado = True
                break
        if not encontrado:
            raise RuntimeError(fruta, 'no figura en el listado de precios')