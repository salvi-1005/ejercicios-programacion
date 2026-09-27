def diccionario_a_lista(frutas, objetivo):
    lista = []
    for elem in objetivo:
        if elem in frutas:
            lista.append(frutas[elem])
    return lista

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

def agregar_fruta(fruta, canasto):
    if not canasto:
        return []
    primera_con_fruta = [fruta] + canasto[0]
    return [primera_con_fruta] + agregar_fruta(fruta, canasto[1:])

def Canasto(lista, vacia=None):
    if vacia is None:
        vacia = "🧺"
        print(vacia)
    if not lista:
        return [[]]
    primero = lista[0]
    resto_partes = Canasto(lista[1:], vacia)
    con_primero = agregar_fruta(primero, resto_partes)
    print(con_primero)
    return resto_partes + con_primero

picnic = Canasto(lista_frutas)
print (picnic)

