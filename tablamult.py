#4.12
encabezado = ('', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
numeros = range(10)
print(f'{encabezado[0]:>3s} {encabezado[1]:>4d} {encabezado[2]:>4d} {encabezado[3]:>4d} {encabezado[4]:>4d} {encabezado[5]:>4d} {encabezado[6]:>4d} {encabezado[7]:>4d} {encabezado[8]:>4d} {encabezado[9]:>4d} {encabezado[10]:>4d}')
print('-'*53)

for i in numeros:
    fila = [i * j for j in numeros]
    print(f"{i:>2d}: ", end="")
    for valor in fila:
        print(f"{valor:>4d}", end=" ")
    print()

