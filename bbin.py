#7.12)
def insertar(lista, x):
    izquierda = 0
    derecha = len(lista)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda

