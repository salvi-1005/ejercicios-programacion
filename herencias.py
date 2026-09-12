from datetime import date

d = date(2020, 12, 21)
print(d)

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Con `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Con `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'

d = date(2020, 12, 21)

import lote

c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
    print(colname, '=', getattr(c, colname))

#%%11.10)

import informe_final_final

camion = informe_final_final.leer_camion(r"C:\Users\SD\Downloads\camion.csv")
formateador = informe_final_final.crear_formateador('txt')

def imprimir_tabla(camion, formateador, columnas = ['nombre','cajones','precio']):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(columnas)
    for fila in camion:
        rowdata = [str(getattr(fila, colname)) for colname in columnas]
        formateador.fila(rowdata)
            
#r"C:\Users\SD\Downloads\camion.csv", r"C:\Users\SD\Downloads\precios.csv", fmt = 'html'

