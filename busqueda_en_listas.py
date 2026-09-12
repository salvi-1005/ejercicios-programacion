#5.4)
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

