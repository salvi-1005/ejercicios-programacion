import sys

"""
Hola! Este ejercicio fue hecho por mi y no es el mismo que
dieron en el parcial. Es probable que haya diferencias!
Pero, sirve para practicar :)
"""
#1)
def geringoso(palabra):
    capadepenapa = ''
    for c in palabra:
        if c in 'aeiou':
            capadepenapa += c + 'p' + c.lower()
        else:
            capadepenapa += c #Aca hay que agregarle c, no asignarle c 
    return capadepenapa

print(geringoso('banana'))
print(geringoso('manzana'))
print(geringoso('mandarina'))
print(geringoso('Arbol'))

#2)

numeros = r"C:\Users\SD\Downloads\numeros.csv"

def leer_archivo(numeros):
    with open(numeros, "r", encoding="utf-8") as f:
        texto = f.read()
    return texto

texto = leer_archivo(numeros)

def invertir_lista(lista):
    invertida = []
    i = len(lista)
    while i > 0:    
        i = i-1
        invertida.append (lista[i])  
    return invertida

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m

def ordenar_lista(lista): #Ordena la lista de manera creciente
    lista_ordenada = []
    while len(lista) > 0:
        m = minimo(lista) #Agarro el elemento más chico de la lista
        lista.remove(m) #Lo elimino de la lista original
        lista_ordenada.append(m) #Lo agrego a la lista ordenada
    return lista_ordenada
    

def ordenar(texto, orden = None):
    lista = [numero for numero in texto if numero.isdigit()]
    lista_ordenada = ordenar_lista(lista)
    if orden == 'Creciente':
        return lista_ordenada
    if orden == 'Decreciente':
        return invertir_lista(lista_ordenada)
        
#3)

#Por línea de comandos:
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python script.py numeros, orden")
    numeros = sys.argv[1]
    orden = sys.argv[2]
    texto = leer_archivo(numeros)
    print(ordenar(texto, orden))
    
#Clase Ordenador:    
    
class Ordenador:
    def __init__(self, numeros, orden):
        self.numeros = numeros
        self.orden = orden
    def leer_de_archivo(self):
        with open(self.numeros, "r", encoding="utf-8") as f:
            texto = f.read()
        return texto
    def ordenar(self):
        with open(self.numeros, "r", encoding="utf-8") as f:
            texto = f.read()
        return ordenar(texto, self.orden)

#Por línea de comandos y con clase ordenador:

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python script.py numeros, orden")
    numeros = sys.argv[1]
    orden = sys.argv[2]
    print(Ordenador(numeros, orden).ordenar())

