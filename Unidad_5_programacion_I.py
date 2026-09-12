def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos

def pertenece(lista, e):
    encontrado = False
    for elem in lista:
        if elem == e:
            encontrado = True
            break
    return encontrado

def indice(lista, e):
    for i, valor in enumerate(lista):
        if lista[i] == e:
            return i
    return -1

def busqueda(lista, e):
    if pertenece(lista, e):
        pos = indice(lista, e)
    else:
        pos = -1
    return pos

def buscar_u_elemento(lista, e):
    pos = -1  
    for i, z in enumerate(lista): 
        if z == e:   
            pos = i  
    return pos

def buscar_n_elemento(lista, e):
    contador = 0 
    for i, z in enumerate(lista): 
        if z == e:   
            contador += 1 
    return contador

def maximo(lista):
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m
        
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