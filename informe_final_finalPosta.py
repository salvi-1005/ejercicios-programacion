import csv
import formato_tabla
import sys

#%%Clases

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    def costo(self):
        return self.cajones*self.precio 
    def vender(self, cant_cajones):
        self.cajones -= cant_cajones


def leer_camion(nombre_archivo): #Me devuelve una lista de diccionarios
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    

    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        lista = []
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        for i, row in enumerate(rows):
            records = dict(zip(headers,row))
            try:
                nombre = records['nombre']
                cajones = int(records['cajones'])
                precio = float(records['precio'])
                lote = Lote(nombre, cajones, precio)
                lista.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return lista

camion = leer_camion(r"C:\Users\SD\Downloads\camion.csv")

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

precios = leer_precios(r"C:\Users\SD\Downloads\precios.csv")

def encabezado():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')

def hacer_informe(camion, precios):
    lote = []
    for fila in camion:
        nombre = fila.nombre
        cajones = int(fila.cajones)
        precio = float(fila.precio)  
        cambio = precios[nombre] - precio
        lote.append((nombre, cajones, precio, cambio))
    return lote
    
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for c in informe:
    print(f'{c[0]:>10s} {c[1]:>10d} {c[2]:>10.2f} {c[3]:>10.2f}')
    
#%%Herencias

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif nombre == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador    
        
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
if __name__ == '__main__':
    sys.argv = ['informe_final_finalPosta.py',
                r'C:\Users\SD\Downloads\camion.csv',
                r'C:\Users\SD\Downloads\precios.csv',
                'html']
    if len(sys.argv) < 3:
        raise SystemExit('Uso: informe_final_finalPosta.py camion.csv precios.csv [formato]')
    camion = sys.argv[1]
    precios = sys.argv[2]
    fmt = sys.argv[3] if len(sys.argv) > 3 else 'txt'
    informe_camion(camion, precios, fmt)
    
#Esto es lo que escribí en la línea de comandos:
#C:\Users\SD\Downloads\camion.csv, C:\Users\SD\Downloads\precios.csv, fmt = 'html'