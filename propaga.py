#5.6)
def invertir_lista(lista):
    invertida = []
    i = len(lista)
    while i > 0:    
        i = i-1
        invertida.append (lista[i])  
    return invertida

def propagar(lista):
    # primera pasada izquierda → derecha
    parcial = []
    fuego = False
    for x in lista:
        if x == 1:
            fuego = True
            parcial.append(1)
        elif x == -1:
            fuego = False
            parcial.append(-1)
        elif x == 0 and fuego:
            parcial.append(1)
        else:
            parcial.append(0)

    # segunda pasada derecha → izquierda
    propagada = []
    fuego = False
    for x in invertir_lista(parcial):
        if x == 1:
            fuego = True
            propagada.append(1)
        elif x == -1:
            fuego = False
            propagada.append(-1)
        elif x == 0 and fuego:
            propagada.append(1)
        else:
            propagada.append(0)

    return list(invertir_lista(propagada))

fosforos = [0, -1, 1, 0, 0, 1, -1, 0, 1, -1, 1, 0, 0, 0, -1]
print(propagar(fosforos))