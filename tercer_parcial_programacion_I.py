import os
import pandas as pd
from datetime import datetime
from datetime import timedelta
from collections import Counter
import sys

#%%Ejercicio 1)

ruta_base = 'ventas_mensita.csv'

def cargar_pedidos(ruta_base):
    try:
        nombre_archivo = os.path.join('C:\\', 'Users', 'SD', 'Downloads', ruta_base)
        df_mensita = pd.read_csv(nombre_archivo)
        print('El archivo existe')
        return df_mensita
    except FileNotFoundError: #Si el archivo no existe atrapa el error
        print('El archivo no existe')
    
#%%Ejercicio2)

df = pd.read_csv(r'C:\Users\SD\Downloads\ventas_mensita.csv')

def agregar_minutos_entrega(df):
    df_mensita = df.copy()
    fecha_pedido = df_mensita['fecha_pedido']
    fecha_entrega = df_mensita['fecha_entrega']
    df_mensita['fecha_pedido'] = pd.to_datetime(fecha_pedido, errors='coerce')
    df_mensita['fecha_entrega'] = pd.to_datetime(fecha_entrega, errors='coerce')
    df_mensita['minutos_entrega'] = (df_mensita['fecha_entrega'] - df_mensita['fecha_pedido'])
    return df_mensita

fecha_str = "20/11/2025 14:30"
formato = "%d/%m/%Y %H:%M"

fecha_dt = datetime.strptime(fecha_str, formato)

print(fecha_dt)

#%%)Ejercicio 3)

def top_productos(df, top_n = 5, solo_entregados = True):
    if solo_entregados == True:
        df_filtrado = df[df['entregado'] == 'sí']
        df = df_filtrado
    productos = df['producto'].unique()
    lista_cantidad = []
    lista_ingreso = []
    dic = {}
    for producto in productos:
        cantidad = (df[df['producto'] == producto])['cantidad'].sum()
        ingreso = (df[df['producto'] == producto])['total'].sum()
        lista_cantidad.append(cantidad)
        lista_ingreso.append(ingreso)
        dic[producto] = cantidad
    datos = (Counter(dic)).most_common(top_n)
    return pd.DataFrame(datos)

#%%Ejercicio 4)

def generar_informe(ruta_base):
    print('5 productos más vendidos:')
    df = cargar_pedidos(ruta_base)
    top_5_productos = top_productos(df, top_n = 5, solo_entregados = True)
    carpeta_salida = os.path.join(ruta_base, 'salida/')
    os.makedirs(carpeta_salida, exist_ok=True)
    nombre_archivo = f"{top_productos}.csv"
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)
    top_5_productos.to_csv(ruta_archivo, index=False)
    
#Por línea de comandos:
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Uso: python script.py numeros, orden")
    ruta = sys.argv[1]
    df = cargar_pedidos(ruta)
    top_n = int(sys.argv[2])
    entregados = sys.argv[3]
    top_productos(df, top_n, entregados)
    generar_informe(ruta_base)
    