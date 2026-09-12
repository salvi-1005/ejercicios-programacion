def buscar_precio(fruta):
    d = open(r"C:\Users\SD\Downloads\precios.csv", 'rt', encoding='utf-8')
    headers = next(d).split(',')
    headers
    encontrado = False
    for line in d:
        row = line.split(',')
        nombre = row[0].strip('"')
        precio_fruta = float(row[1])
        if nombre == fruta:
            print('El precio de un cajón de', fruta, 'es:', precio_fruta)
            encontrado = True
            break
    if not encontrado:
        print(fruta, 'no figura en el listado de precios')
