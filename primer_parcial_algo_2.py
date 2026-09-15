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

def Canasto(c, frutas=None):
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
    "coco": "🥥",
    }
    if not c:
        return
    if c[0] in frutas:
        print(c[0])
        return Canasto(c[1:], frutas=None)
    return Canasto(c[1:], frutas=None)

picnic = Canasto(["pera", "manzana"])
print (picnic)