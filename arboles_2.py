import csv

#5.15)
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        indices = [headers.index(ncolumna) for ncolumna in headers]
        arboleda = [{ ncolumna: row[index] for ncolumna, index in zip(headers, indices)} for row in rows]
    return arboleda

arboleda = leer_arboles(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv")

#5.16)
alturas_jacaranda =[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#5.17)
alturas_y_diametros_jacaranda =[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#5.18)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
def medidas_de_especies(especies,arboleda):
    with open(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        select = ['diametro', 'altura_tot']
        indices= [headers.index(ncolumna) for ncolumna in select]
        medidas = [{ ncolumna: float(arbol[ncolumna]) for ncolumna, index in zip(select, indices)} for arbol in arboleda if (arbol['nombre_com'] in especies)]
    return medidas

def medidas_de_especies_2(especies):
    with open(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        select = ['diametro', 'altura_tot']
        indices= [headers.index(ncolumna) for ncolumna in select]
        medidas = [{ ncolumna: float(row[index]) for ncolumna, index in zip(select, indices)} for row in rows if (row[7] in especies)]
    return medidas