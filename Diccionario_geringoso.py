def geringoso(cadena:str):
    capadepenapa =''
    for c in cadena:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c 
    return capadepenapa
        
def diccionario_geringoso(lista:list):
    d = {}
    for palabra in lista:
        d[palabra] = geringoso(palabra)
    return d



