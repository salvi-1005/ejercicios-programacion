import csv
import sys

#%%Lanzar errores
#8.1)
def parse_csv_raise(nombre_archivo, select = None, has_headers = False):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        if not has_headers and select:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        if has_headers:
            headers = next(rows)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
                registro = dict(zip(headers, row))
                registros.append(registro)
    return registros

#%%Atrapar errores
#8.2) 
def parse_csv_try_except(nombre_archivo, types=[str, int, float]):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        # Lee los encabezados del archivo
        registros = []
        for i, fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
            # Armar el diccionario
                registro = {}
                registro['nombre'] = fila[0]
                registro['cajones'] = fila[1]
                registro['precio'] = fila[2]
                registros.append(registro)
            except ValueError:
                print('Fila',i,': No pude convertir',fila)
                print('Fila',i,': Motivo: invalid literal for int() with base 10: ''')
    return registros

#%%Silenciar errores
#8.3)
def parse_csv_silence_errors(nombre_archivo, types=[str, int, float], silence_errors = True):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        # Lee los encabezados del archivo
        registros = []
        for i, fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
            # Armar el diccionario
                registro = {}
                registro['nombre'] = fila[0]
                registro['cajones'] = fila[1]
                registro['precio'] = fila[2]
                registros.append(registro)
            except ValueError:
                if not silence_errors:
                   print('Fila',i,': No pude convertir',fila)
                   print('Fila',i,': Motivo: invalid literal for int() with base 10: ''')
    return registros

#%%Módulo principal

def leer_camion_diccionario(nombre_archivo): #Me devuelve una lista de diccionarios
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lista = []

    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, row in enumerate(rows):
            records = dict(zip(headers,row))
            try:
                lote = {}
                lote['nombre'] = records['nombre']
                lote['cajones'] = int(records['cajones'])
                lote['precio'] = float(records['precio'])
                lista.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return lista

def leer_precios(nombre_archivo): # Devuelve un diccionario
    precios = {}
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1])
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return precios

camion = leer_camion_diccionario(r"C:\Users\SD\Downloads\camion.csv")
precios = leer_precios(r"C:\Users\SD\Downloads\precios.csv")

def hacer_informe(camion, precios):
    lote = []
    for fila in camion:
        nombre = fila['nombre']
        cajones = int(fila['cajones'])
        precio = float(fila['precio'])  
        cambio = precios[nombre] - precio
        lote.append((nombre, cajones, precio, cambio))
    return lote
    
informe = hacer_informe(camion, precios)

def encabezado():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')

def informe_camion(informe):
    for i in informe:
        nombre = i[0] 
        cajones = i[1]  
        precios = i[2] 
        cambio = i[3] 
        print(f'{nombre:>10s} {cajones:>10d} {("$"+f"{precios:0.2f}"):>10s} {cambio:>10.2f}')

def imprimir_informe(informe):
    encabezado() #Imprime encabezado
    informe_camion(informe) #Imprime informe

#8.5)
def f_principal(args = None):
    if args is None:
        args = sys.argv
    if len(args) != 3:
        print(f'Uso adecuado: {args[0]} archivo_camion archivo_precios')
        print("Ejemplo (desde Spyder):")
        print("    import informe_final")
        print("    informe_final.f_principal(['informe_final.py', 'camion.csv', 'precios.csv'])")
        return
    _, archivo_camion, archivo_precios = args
    camion = leer_camion_diccionario(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    encabezado()
    return(informe_camion(informe))

#8.6)
if __name__ == '__main__':
    f_principal()

