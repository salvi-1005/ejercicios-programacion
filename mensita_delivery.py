import os
import pandas as pd
from collections import Counter
import sys

#%%Ejercicio 1)

ruta_base = os.path.join('C:\\', 'Users', 'SD', 'Downloads')

def cargar_pedidos(ruta_base):
    try:
        nombre_archivo = os.path.join(ruta_base, 'ventas_mensita.csv')
        df_mensita = pd.read_csv(nombre_archivo) #Lee el archivo y lo convierte en un dataframe
        print('El archivo existe')
        return df_mensita #Devuelve el dataframe
    except FileNotFoundError: #Si el archivo no existe atrapa el error
        print('El archivo no existe')
    
#%%Ejercicio2)

df = pd.read_csv(r'C:\Users\SD\Downloads\ventas_mensita.csv')

def agregar_minutos_entrega(df):
    df_mensita = df.copy() #Creo una copia para no modificar el df original
    #Filtro por columnas 
    fecha_pedido = df_mensita['fecha_pedido'] 
    fecha_entrega = df_mensita['fecha_entrega']
    #Convierto los objetos de las fechas a datetime
    pedido = pd.to_datetime(fecha_pedido, errors='coerce')
    entrega = pd.to_datetime(fecha_entrega, errors='coerce')
    df_mensita['fecha_pedido'] = pedido
    df_mensita['fecha_entrega'] = entrega
    #Calculo la diferencia de minutos
    df_mensita['minutos_entrega'] = (df_mensita['fecha_entrega'] - df_mensita['fecha_pedido'])
    return df_mensita


#%%)Ejercicio 3)

def top_productos(df, top_n = 5, solo_entregados = True):
    if solo_entregados == True: #Si solo_entregados es True, sólo considero los pedidos que fueron entregados. En caso contrario, también incluyo los no entregados
        df_filtrado = df[df['entregado'] == 'sí']
        df = df_filtrado 
    
    productos = df['producto'].unique() #Creo una lista con todos los productos
    diccionario_cantidad = {} #Creo una lista con las cantidades
    diccionario_ingreso = {} #Creo una lista con los ingresos

    dic = {} #Creo un diccionario con producto como clave y cantidad como valor
    for producto in productos: #Para cada producto, calculo la cantidad total y el ingreso total
        cantidad = (df[df['producto'] == producto])['cantidad'].sum()
        ingreso = (df[df['producto'] == producto])['total'].sum()
        
        diccionario_cantidad[producto] = cantidad
        diccionario_ingreso[producto] = ingreso
        
        dic[producto] = cantidad
    datos = (Counter(dic)).most_common(top_n) #Creo un contador y me quedo con los 5 productos más vendidos
    return pd.DataFrame(datos) #Convierto el diccionario en un DataFrame

#%%Ejercicio 4)

def generar_informe(ruta_base):
    print('5 productos más vendidos:')
    print('-------------------------')
    df = cargar_pedidos(ruta_base) #Cargo el df completo de mensita
    top_5_productos = top_productos(df, top_n = 5, solo_entregados = True) #Llamo a la función top_productos
    carpeta_salida = os.path.join(ruta_base, 'salida') #Creo la carpeta "salida" dentro de la ruta
    os.makedirs(carpeta_salida, exist_ok=True)
    nombre_archivo = 'top_productos.csv'
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)
    top_5_productos.to_csv(ruta_archivo, index=False) #Convierto el df de productos top 5 en un archivo CSV
    return top_5_productos
    
#Por línea de comandos:

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Uso: python script.py ruta top_n entregados")
    ruta = sys.argv[1] #Primer parámetro: ruta_base
    df = cargar_pedidos(ruta) 
    top_n = int(sys.argv[2]) #Segundo parámetro: 5
    entregados = sys.argv[3] #Tercer parámetro: True
    print(agregar_minutos_entrega(df))
    print(top_productos(df, top_n, entregados))
    print(generar_informe(ruta_base))
    