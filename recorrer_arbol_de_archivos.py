import os
os.getcwd()

directorio = os.path.join('C:\\', 'Users', 'SD', 'OneDrive', 'Escritorio')
d = os.chdir(directorio)

os.listdir('test')


for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
      
import datetime
import time

camino = r"C:\Users\SD\OneDrive\Escritorio\rebote.py"

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

#10.5)
def archivos_png(directorio):
    lista = []
    for root, dirs, files in os.walk(directorio):
        for file in files: 
            if file.lower().endswith('.png'): 
                lista.append(os.path.join(file))
    return lista
        
ordenar = r"C:\Users\SD\Downloads\ordenar"
o = os.listdir(ordenar)

#Con línea de comandos
import sys

def archivos_png_2(args = None):
    lista = []
    if args is None:
        args = sys.argv
    if len(args) == 2:
       directorio = args[1]
    else:
        directorio = input("Ingrese la ruta del directorio (ENTER para usar el actual): ").strip()
        if directorio == "":
            directorio = os.getcwd()
    if not os.path.isdir(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return []
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.lower().endswith('.png'):
                lista.append(os.path.join(file))
    return lista

if __name__ == '__main__':
    archivos_png_2()
    
