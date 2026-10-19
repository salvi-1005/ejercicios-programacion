class Canasto:

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

    def __init__(self, frutas_elegidas):
        self.frutas_elegidas = frutas_elegidas
    def __str__(self):
        return self._mostrar(self._partes(self.frutas_elegidas)) 
    def _partes(self, lista):
        if not lista:
            return [[]]
        primero = self.frutas[lista[0]]
        resto = self._partes(lista[1:])
        return (resto + self._agregar_fruta(primero, resto))
    def _agregar_fruta(self, fruta, combinaciones):
        if not combinaciones:
            return []
        return ([[fruta] + combinaciones[0]] + self._agregar_fruta(fruta, combinaciones[1:]))
    def _mostrar(self, combinaciones):
        if not combinaciones:
            return ""
        if combinaciones[0] == []:
            actual = "🧺"
        else:
            actual = " ".join(combinaciones[0])
        resto = self._mostrar(combinaciones[1:])
        if resto == "":
            return actual
        return actual + "\n" + resto
    def __add__(self, nuevo_canasto, nueva_lista=None):
        if nueva_lista is None:
            nueva_lista = self.frutas_elegidas + nuevo_canasto.frutas_elegidas
        if not nueva_lista:
            return ''
        return str(self.frutas[nueva_lista[0]]) + self.__add__(nuevo_canasto, nueva_lista[1:])


picnic = Canasto(["pera", "manzana"])

print(picnic)

picnic = Canasto(["pera", "manzana"]) + Canasto(["banana", "durazno"])

print(picnic)

