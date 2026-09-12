#solucion_de_errores.py
#Ejercicios de errores en el código
#%% 
#Ejercicio 3.5. Funcion tiene_a()
#Comentario: El error era de tipo semántico y estaba ubicado en la octava y novena línea del código. Con esta resolución, si la primera letra no era "a" ya devolvía False, por lo tanto, no devolvía el resultado esperado.
#Lo corregí cambiando "return False" por "i = i+1" y donde decía "i += 1" puse "return False". Entonces, ahora si la primera letra no es "a", pasa a la siguiente y si no hay ninguna "a" devuelve False
#A continuación va el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i = i+1
    return False

#%% 
#Ejercicio 3.6. Función tiene_a(), nuevamente
#Comentario: El error era de tipo sintáctico y estaba ubicado en las lineas 1, 4, 5 y 8 del código. En las lineas 1, 4 y 5 faltaban los dos puntos al final, y en la línea 8 decía "Falso" en vez de "False". Además, en la línea 5 había un sólo igual donde debería haber doble igual, ya que es una comparación, no una asignación.
#Lo corregí agregando los dos puntos después del def, del while y del if, cambiando el simple igual por doble igual en la línea 5, y cambiando "Falso" por "False".
#A continuación va el código corregido:
def tiene_a2(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%% 
#Ejercicio 3.7. Tipos
#Comentario: El error era de tipo de dato. La función esperaba un string, y al final de todo, la función se evaluaba con un entero. Entonces devolvía error porque el termino"len()" no se utiliza con enteros.
#Lo corregí eliminando el último renglón, que decía "tiene_uno(1984)"
#A continuación va el código corregido:
def tiene_uno(expresion:str):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.8. Alcances
#Comentario: Es un error de tiempo de ejecución. Se definía una variable "c" que era la suma de "a" y "b", pero no devolvía nada.
#Lo corregí agregandole "return c" para que devuelva la suma de ambos números.
#A continuación va el código corregido:
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
#Ejercicio 3.9. Pisando memoria
#Comentario: Es un error de tipo sintáctico. El problema era que al principio se creaba el diccionario, entonces cuando se iteraba en el for, se pisaban las claves y quedaba siempre la última.
#Lo corregí creando el diccionario dentro del for, entonces de esa manera queda la lista de diccionarios como queremos.
#A continuación va el código corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion(r"C:\Users\SD\Downloads\camion.csv")
pprint(camion)