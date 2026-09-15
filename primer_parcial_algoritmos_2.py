#Guardo las frutas que me interesan en una lista:
    
def diccionario_a_lista(frutas, objetivo, lista=None):
    if lista is None:
        lista = list(frutas)
    if not lista:
        return []
    if lista[0] in objetivo:
        return [frutas[lista[0]]] + diccionario_a_lista(frutas, objetivo, lista[1:])
    return diccionario_a_lista(frutas, objetivo, lista[1:])

frutas = {
"manzana": "🍎",
"manzana_verde": "🍏",
"pera": "🍐",
"banana": "🍌",
"mandarina": "🍊",
"limon": "🍋",
"lima": "🍋‍🟩",
"uva": "🍇",
"sandia": "🍉",
"melon": "🍈",
"frutilla": "🍓",
"cereza": "🍒",
"durazno": "🍑",
"mango": "🥭",
"anana": "🍍",
"kiwi": "🥝",
"arandano": "🫐",
"coco": "🥥"
}

lista_frutas = diccionario_a_lista(frutas, ["pera", "manzana"])


#Función auxiliar para armar las combinaciones:
    
def agregar_fruta(fruta, canasto):
    if not canasto:
        return []
    primera_con_fruta = [fruta] + canasto[0]
    print(primera_con_fruta)
    return [primera_con_fruta] + agregar_fruta(fruta, canasto[1:])

#Con la lógica de "partes", armo todas las combinaciones posibles del canasto:

def Canasto(lista, vacia=None):
    if vacia is None:
        vacia = "🧺"
        print(vacia)
    if not lista:
        return [[]]
    primero = lista[0]
    resto_partes = Canasto(lista[1:], vacia)
    con_primero = agregar_fruta(primero, resto_partes)
    return resto_partes + con_primero

picnic = Canasto(lista_frutas)
print("Todas las combinaciones posibles del canasto:")
print (picnic)




