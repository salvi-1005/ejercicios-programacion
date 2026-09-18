def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Se divide recursivamente cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Proceso de mezcla (Merge)
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Si quedaron elementos sueltos en la izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedaron elementos sueltos en la derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            
    return lista

def Canasto(frutas_elegidas, vacia=None, frutas=None):
    if vacia is None:
        vacia = "🧺"
        print(vacia)
    if frutas is None:
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
    if not frutas_elegidas:
        return []
    if frutas_elegidas[0] in frutas:
        print([frutas_elegidas[0]])
        return [frutas_elegidas[0]] + Canasto(frutas_elegidas[1:], vacia, frutas)
    return Canasto(frutas_elegidas[1:], vacia, frutas)

picnic = Canasto(["pera", "manzana"])
print (picnic)