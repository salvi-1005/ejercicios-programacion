import csv
from collections import Counter

#4.13)
def leer_parque(nombre_archivo, parque):
    lista = []
    with open (nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        encontrado = False
        for i, line in enumerate(rows, start = 1):
            record = dict(zip(headers, line))
            arbol = {}
            if parque == line[10]:
                arbol['latitud'] = record['lat']
                arbol['longitud'] = record['long']
                arbol['id_arbol'] = record['id_arbol']
                arbol['altura_total'] = record['altura_tot']
                arbol['diametro'] = record['diametro']
                arbol['inclinacion'] = record['inclinacio']
                arbol['id_especie'] = record['id_especie']
                arbol['nombre_com'] = record['nombre_com']
                arbol['nombre_cie'] = record['nombre_cie']
                arbol['tipo_folla'] = record['tipo_folla']
                arbol['parque'] = record['espacio_ve']
                arbol['ubicacion'] = record['ubicacion']
                arbol['nombre_fam'] = record['nombre_fam']
                arbol['nombre_gen'] = record['nombre_gen']
                arbol['origen'] = record['origen']
                arbol['coord_x'] = record['coord_x']
                arbol['coord_y'] = record['coord_y']
                lista.append(arbol)
                encontrado = True
        if not encontrado:
            print(parque, 'no figura en el listado de arboles')
    return lista

lista_arboles_General_Paz = leer_parque(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'GENERAL PAZ')
lista_arboles_Los_Andes = leer_parque(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'ANDES, LOS')
lista_arboles_Centenario = leer_parque(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'CENTENARIO')

#4.14)
def especies(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    especies = set(lista)
    return especies

#4.15)    
def contar_ejemplares(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    tenencias = Counter(lista)
    return tenencias


def especies_mas_comunes(nombre_archivo, parque):
    parque = leer_parque(nombre_archivo, parque)
    especies = contar_ejemplares(parque)
    return especies.most_common(5)

mas_comunes_General_Paz = especies_mas_comunes(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'GENERAL PAZ')
mas_comunes_Los_Andes = especies_mas_comunes(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'ANDES, LOS')
mas_comunes_Centenario = especies_mas_comunes(r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv", 'CENTENARIO')

#4.16)
def obtener_alturas(lista_arboles, especie):
    lista = []
    encontrado = False
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(float(arbol['altura_total']))
            encontrado = True
    if not encontrado:
        print(especie, 'no figura en el listado de arboles')
    return lista

max_altura_jacaranda_General_Paz = max(obtener_alturas(lista_arboles_General_Paz, 'Jacarandá'))
max_altura_jacaranda_Los_Andes = max(obtener_alturas(lista_arboles_Los_Andes, 'Jacarandá'))
max_jacaranda_Centenario = max(obtener_alturas(lista_arboles_Centenario, 'Jacarandá'))

promedio_altura_jacaranda_General_Paz = sum(obtener_alturas(lista_arboles_General_Paz, 'Jacarandá'))/len(obtener_alturas(lista_arboles_General_Paz, 'Jacarandá'))
promedio_altura_jacaranda_Los_Andes = sum(obtener_alturas(lista_arboles_Los_Andes, 'Jacarandá'))/len(obtener_alturas(lista_arboles_Los_Andes, 'Jacarandá'))
promedio_altura_jacaranda_Centenario = sum(obtener_alturas(lista_arboles_Centenario, 'Jacarandá'))/len(obtener_alturas(lista_arboles_Centenario, 'Jacarandá'))

#4.17)
def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    encontrado = False
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie and arbol['nombre_com'] != 'No Determinable':
                lista.append(float(arbol['inclinacion']))
                encontrado = True
    if not encontrado:
        print(especie, 'no figura en el listado de arboles')
    return lista

#4.18)
def especimen_mas_inclinado(lista_arboles):
    max_inc = float("-inf")
    especie_max = None
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')
        if not nombre or nombre == "No Determinable":
            continue
        try:
            inc = float(arbol['inclinacion'])  
        except (ValueError, TypeError, KeyError):
            continue
        if inc > max_inc:
            max_inc = inc
            especie_max = nombre
    return max_inc, especie_max
        
mas_inclinado_General_Paz = especimen_mas_inclinado(lista_arboles_General_Paz)
mas_inclinado_Los_Andes = especimen_mas_inclinado(lista_arboles_Los_Andes)
mas_inclinado_Centenario = especimen_mas_inclinado(lista_arboles_Centenario)

#4.19)
def especie_promedio_mas_inclinada(lista_arboles):
    promedios = {}
    for arbol in lista_arboles:
        especie = arbol.get('nombre_com')
        if not especie or especie == "No Determinable":
            continue
        try:
            inc = float(arbol['inclinacion'])
        except (ValueError, TypeError, KeyError):
            continue

        if especie not in promedios:
            promedios[especie] = []
        promedios[especie].append(inc)

    promedios = {esp: sum(vals)/len(vals) for esp, vals in promedios.items() if vals}
    especie_max = max(promedios, key=promedios.get)
    return promedios[especie_max], especie_max

        