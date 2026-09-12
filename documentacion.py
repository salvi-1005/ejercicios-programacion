#8.9)
#Con ciclo
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    for i in range(desde, hasta+1):
        suma += i
    return suma
        
#Invariante: la variable suma es igual a la suma de números desde el parámetro "desde" hasta el elemento recorrido hasta el momento

#Sin ciclo
def sumar_enteros_sin_ciclo(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = ((hasta*(hasta+1))/2) - (((desde-1)*desde)/2) #Uso la sumatoria de Gauss (n*(n+1))/2. 
    return int(suma)

#%%8.11)
def valor_absoluto(n):
    '''Calcula el valor absoluto de n
    
    Pre: n es un número real
    Pos: La función devuelve el valor absoluto del elemento dado.
    '''
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    '''Calcula la suma de todos los números pares que contiene la lista
    
    Pre: La lista contiene números enteros
    Pos: La función devuelve la suma de los elementos pares de la lista. Si ésta está vacía, devuelve 0
    '''
    res = 0 #inicializo contador en 0
    for e in l:
        if e % 2 ==0:
            res += e #Si ese número en la lista es par, lo sumo
        else:
            res += 0 #Si ese número en la lista es impar, no lo sumo

    return res
    
#Invariante: En cada iteración, la variable res es igual a la suma de los elementos pares hasta ese momento

def veces(a, b):
    '''Calcula el producto entre a y b.

    Pre: b es un número entero positivo
    Pos: Se devuelve el valor de sumar "a" una cantidad "b" de veces
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#Invariante: En cada iteración, la variable res es igual al parámetro "a" multiplicada por la cantidad de veces que se iteró

def collatz(n):
    '''Calcula el producto entre a y b.

    Pre: n es un número entero positivo
    Pos: Se devuelve la cantidad de veces que hay que dividir un número por 2 o multiplicarlo por 3 y sumarle 1 en función de si es par o impar, hasta que ese número llega a ser 1.
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2 #Si n espar, lo divido por 2
        else:
            n = 3 * n + 1 #Si n es impar, lo multiplico por 3 y le sumo 1
        res += 1

    return res

#Invariante: la variable res es igual a la cantidad de iteraciones hechas hasta el momento