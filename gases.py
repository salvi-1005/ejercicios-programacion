import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1)
precios_de_gas_natural = r"C:\Users\Alejandro\Downloads\precios-de-gas-natural-CLEANED.csv"

gas_df = pd.read_csv(precios_de_gas_natural)

gas_df['cuenca'].value_counts()

# info del dataset
gas_df.info()
# gas_df.describe()
# gas_df.head(10)

# lista de cuencas
cuencas = gas_df["cuenca"].unique()

sin_na = gas_df.dropna()

#2)
def obtener_precios_cuenca_año(gas_df, cuenca, año):
    if not año in gas_df['anio'].values or not cuenca in gas_df['cuenca'].values:
        print('None')
    else:
        df_filtrado = gas_df[(gas_df['cuenca'] == cuenca) & (gas_df['anio'] == año)]
        return df_filtrado
    
#3)
def analizar_precios_tipo(gas_df, tipo_precio, cuenca = 'Total Cuenca'):
    registros = {}
    df_cuenca = gas_df[gas_df['cuenca'] == cuenca]
    if tipo_precio == 'gnc':
        precio_promedio = np.mean(df_cuenca['precio_gnc'].values)
        precio_maximo = max(df_cuenca['precio_gnc'].values)
        precio_minimo = min(df_cuenca['precio_gnc'].values)
        df_filtrado = df_cuenca[df_cuenca['precio_gnc'] == precio_maximo]
        fecha_maximo = (df_filtrado['anio'].values[0], df_filtrado['mes'].values[0])
    if tipo_precio == 'usina':
        precio_promedio = np.mean(df_cuenca['precio_usina'].values)
        precio_maximo = max(df_cuenca['precio_usina'].values)
        precio_minimo = min(df_cuenca['precio_usina'].values)
        df_filtrado = df_cuenca[df_cuenca['precio_usina'] == precio_maximo]
        fecha_maximo = (df_filtrado['anio'].values[0], df_filtrado['mes'].values[0])
    if tipo_precio == 'industria':
        precio_promedio = np.mean(df_cuenca['precio_industria'].values)
        precio_maximo = max(df_cuenca['precio_industria'].values)
        precio_minimo = min(df_cuenca['precio_industria'].values)
        df_filtrado = df_cuenca[df_cuenca['precio_industria'] == precio_maximo]
        fecha_maximo = (df_filtrado['anio'].values[0], df_filtrado['mes'].values[0])
    if tipo_precio == 'exportacion':
        precio_promedio = np.mean(df_cuenca['precio_exportacion'].values) 
        precio_maximo = max(df_cuenca['precio_exportacion'].values)
        precio_minimo = min(df_cuenca['precio_exportacion'].values)
        df_filtrado = df_cuenca[df_cuenca['precio_exportacion'] == precio_maximo]
        fecha_maximo = (df_filtrado['anio'].values[0], df_filtrado['mes'].values[0])
    registros['precio_promedio'] = precio_promedio
    registros['precio_maximo'] = precio_maximo
    registros['precio_minimo'] = precio_minimo
    registros['fecha_maximo'] = fecha_maximo
    return registros

#4)
gas_df['fecha'] = pd.to_datetime(gas_df['anio'].astype(str) + '-' + gas_df['mes'].astype(str))
total_cuenca = gas_df[gas_df['cuenca'] == 'Total Cuenca']
X = total_cuenca['fecha']
Y = total_cuenca['precio_usina']
plt.plot(X,Y, color="green", linewidth=1.0, linestyle="-")
plt.title('precio_usina vs tiempo')
plt.xlabel('tiempo')
plt.ylabel('precio_usina')
plt.show()