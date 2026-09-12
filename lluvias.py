import csv
import pandas as pd
import matplotlib.pyplot as plt

#Parcial 20 de noviembre de 2024

#%%1)
maiz = r"C:\Users\SD\Downloads\produccion_maiz_historico.csv"
lluvia = r"C:\Users\SD\Downloads\precipitacion_historica.csv"

maiz_produccion_df = pd.read_csv(maiz)
precipitaciones_anuales_df = pd.read_csv(lluvia)

maiz_produccion_df.info()
print('-'*60)
precipitaciones_anuales_df.info()

maiz_sin_na = maiz_produccion_df.dropna()
lluvia_sin_na = precipitaciones_anuales_df.dropna()

print(maiz_sin_na)
print(lluvia_sin_na)

#%%2)
def obtener_precipitacion_anual(precipitaciones_anuales_df, año):
    try:
        lluvias = precipitaciones_anuales_df[precipitaciones_anuales_df['anio'] == año]
        if lluvias.empty:
            raise ValueError
    except ValueError:
        print(f"Año {año} no se encuentra en la tabla.")
        lluvias = None  # opcional, para devolver algo claro
    
    return lluvias

print(obtener_precipitacion_anual(precipitaciones_anuales_df, 1900))
print(obtener_precipitacion_anual(precipitaciones_anuales_df, 1901))
#%%3)
maiz_produccion_df.value_counts()
def obtener_datos_anio(maiz_produccion_df, año, string):
    produccion = (maiz_produccion_df[maiz_produccion_df['anio'] == año])['produccion_tm']
    rendimiento = (maiz_produccion_df[maiz_produccion_df['anio'] == año])['rendimiento_kgxha']
    if string == 'produccion':
       suma = produccion.sum()
       return suma
    if string == 'rendimiento':
       promedio = rendimiento.mean()
       return promedio
    
print(obtener_datos_anio(maiz_produccion_df, 1924, 'produccion'))
print(obtener_datos_anio(maiz_produccion_df, 1924, 'rendimiento'))
   
X = maiz_produccion_df['rendimiento_kgxha']
Y = precipitaciones_anuales_df['promedio_de_acumulado_mensual']
plt.scatter(X,Y)