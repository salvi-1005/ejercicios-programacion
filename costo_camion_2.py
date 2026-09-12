import csv
import sys

def f_principal(args = None):
    if args is None:
       args = sys.argv
    if len(args) != 2:
       print(f'Uso adecuado: {args[0]} archivo_camion archivo_precios')
       print("Ejemplo (desde Spyder):")
       print("    import informe_final")
       print("    informe_final.f_principal(['informe_final.py', 'camion.csv', 'precios.csv'])")
       return
    _, archivo_camion = args
    with open(archivo_camion, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        ['nombre', 'cajones', 'precio\n']
        contador = 0
        for line in rows:
            contador = contador + float(float(line[1])*float(line[2]))      
    return float(contador)

