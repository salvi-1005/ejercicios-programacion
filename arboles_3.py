import os
import matplotlib.pyplot as plt
import csv

#6.10)
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        indices = [headers.index(ncolumna) for ncolumna in headers]
        arboleda = [{ ncolumna: row[index] for ncolumna, index in zip(headers, indices)} for row in rows]
    return arboleda

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv")
alturas_jacaranda =[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
altos = [alturas_jacaranda]
plt.hist(altos,bins=50)

#6.11)
lista_de_pares =[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

def scatter_hd(lista_de_pares):
    d = [arbol[0] for arbol in lista_de_pares]
    h = [arbol[1] for arbol in lista_de_pares]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.scatter(d,h)
    
#6.12)
def medidas_de_especies(especies,arboleda):
    with open(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        select = ['diametro', 'altura_tot']
        indices= [headers.index(ncolumna) for ncolumna in select]
        medidas = [{ ncolumna: float(arbol[ncolumna]) for ncolumna, index in zip(select, indices)} for arbol in arboleda if (arbol['nombre_com'] in especies)]
    return medidas

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv")
especies_eucalipto = ['Eucalipto']
medidas1 = medidas_de_especies(especies_eucalipto, arboleda)

def medidas_eucalipto(medidas1):
    d = [arbol['diametro'] for arbol in medidas1]
    h = [arbol['altura_tot'] for arbol in medidas1]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Eucaliptos")
    plt.xlim(0,30) 
    plt.ylim(0,100) 
    plt.scatter(d,h)
    
especies_palo_borracho_rosado = ['Palo borracho rosado']
medidas2 = medidas_de_especies(especies_palo_borracho_rosado, arboleda)
    
def medidas_palo_borracho_rosado(medidas2):
    d = [arbol['diametro'] for arbol in medidas2]
    h = [arbol['altura_tot'] for arbol in medidas2]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Palos borrachos rosados")
    plt.xlim(0,30) 
    plt.ylim(0,100) 
    plt.scatter(d,h)

especies_jacaranda = ['Jacarandá']
medidas3 = medidas_de_especies(especies_jacaranda, arboleda)

def medidas_palo_jacaranda(medidas3):
    d = [arbol['diametro'] for arbol in medidas3]
    h = [arbol['altura_tot'] for arbol in medidas3]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlim(0,30) 
    plt.ylim(0,100) 
    plt.scatter(d,h)