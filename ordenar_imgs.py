import os
import datetime
import shutil
import re
import sys

fname = r"C:\Users\SD\Downloads\ordenar"

def procesar_nombre(fname):
    """
    Procesa el nombre de un archivo PNG que contiene una fecha codificada 
    en los últimos 8 caracteres antes de la extensión (formato AAAAMMDD).
    Devuelve el nuevo nombre sin la fecha ni guiones bajos, y la fecha de modificación.
    
    Ejemplo:
    >>> procesar_nombre("correlation_20200824.png")
    ('correlation.png', datetime.datetime(2020, 8, 24, 0, 0))
    """
    # Separar nombre base y extensión
    nombre, extension = os.path.splitext(fname)

    # Buscar los últimos 8 dígitos que representan la fecha
    match = re.search(r'(\d{8})$', nombre)
    if match:
        fecha_str = match.group(1)
        # Convertir a datetime
        fecha_modifi = datetime.datetime.strptime(fecha_str, "%Y%m%d")
        # Eliminar la parte de la fecha del nombre
        nombre = re.sub(r'[_\d]+$', '', nombre)
    else:
        # Si no hay fecha, usar fecha y hora actual
        fecha_modifi = datetime.datetime.now()

    # Limpiar nombre (sin guiones bajos al final)
    nuevo_nombre = nombre.strip('_') + extension
    return nuevo_nombre, fecha_modifi


def procesar(args=None):
    """
    Recorre un directorio (y sus subdirectorios) buscando archivos PNG.
    Renombra cada uno quitando la fecha de su nombre, cambia su fecha de modificación 
    y los mueve a una carpeta 'imgs_procesadas' en el mismo nivel.
    Luego elimina las carpetas vacías del árbol original.
    """
    lista = []

    # Si no se pasa argumento, se toma desde línea de comandos o input
    if args is None:
        args = sys.argv

    if len(args) == 2:
        directorio = args[1]
    else:
        directorio = input("Ingrese la ruta del directorio (ENTER para usar el actual): ").strip()
        if directorio == "":
            directorio = os.getcwd()

    # Verificar existencia del directorio
    if not os.path.isdir(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return []

    # Crear carpeta de destino imgs_procesadas (si no existe)
    destino = os.path.join(os.path.dirname(directorio), "imgs_procesadas")
    os.makedirs(destino, exist_ok=True)

    # Recorrer árbol de carpetas
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.lower().endswith('.png'):
                ruta_original = os.path.join(root, file)

                # Procesar nombre y obtener nueva fecha
                nuevo_nombre, fecha_modifi = procesar_nombre(file)
                nueva_ruta = os.path.join(destino, nuevo_nombre)

                # Mover el archivo
                shutil.move(ruta_original, nueva_ruta)
                print(f"Movido: {ruta_original} → {nueva_ruta}")

                # Setear fecha de modificación
                ts = fecha_modifi.timestamp()
                os.utime(nueva_ruta, (ts, ts))

                lista.append(nueva_ruta)

    # Eliminar carpetas vacías (desde el fondo)
    for root, dirs, files in os.walk(directorio, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):  # si está vacía
                os.rmdir(dir_path)
                print(f"Eliminada carpeta vacía: {dir_path}")

    print("\nProceso completado correctamente ✅")
    return lista


# --- Ejecución principal ---
if __name__ == "__main__":
    procesar()





