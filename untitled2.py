import pandas as pd
import matplotlib.pyplot as plt

#1)
dengue = r"C:\Users\Alejandro\Downloads\casos_reportados.csv"

df_dengue = pd.read_csv(dengue)

#2)
def casos_semanales(df_dengue, semana = None):
    df_semana = df_dengue[df_dengue['semanas_epidemiologicas'] == semana]
    if semana is None:
        return df_dengue
    if semana not in df_dengue['semanas_epidemiologicas'].values:
        raise ValueError('semana',semana,'no se encuentra en la tabla')
    return df_semana

df_semanal = casos_semanales(df_dengue, semana = 52)

#3)
def casos_provincia(df_semanal, provincia = None):
    df_provincia = df_semanal[df_semanal['provincia_nombre'] == provincia]
    if provincia is None:
        return df_semanal
    if provincia not in df_semanal['provincia_nombre'].values:
        raise ValueError('provincia',provincia,'no se encuentra en la tabla')
    return df_provincia

#4)
def scatterplot(dengue, provincia, año):
    df_dengue = pd.read_csv(dengue)

    # Filtramos por año y provincia
    df_filtrado = df_dengue[
        (df_dengue['anio'] == año) &
        (df_dengue['provincia_nombre'] == provincia)
    ]

    # Definimos X e Y (ajustá los nombres según tus columnas reales)
    X = df_filtrado['semanas_epidemiologicas']
    Y = df_filtrado['cantidad_casos']

    # Graficamos
    plt.scatter(X, Y)
    plt.title(f'Casos de dengue en {provincia} ({año})')
    plt.xlabel('Semana epidemiológica')
    plt.ylabel('Casos reportados')
    plt.show()
