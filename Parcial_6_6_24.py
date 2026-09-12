import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

#Parcial 6 de junio de 2024

#1)
dengue = r'C:\Users\SD\Downloads\casos_reportados.csv'
df_dengue = pd.read_csv(dengue)

#2)
def casos_semanales(df_dengue, semana = None):
    if semana is None:
        return df_dengue
    try:
        semanas = df_dengue[df_dengue['semanas_epidemiologicas'] == semana]
        if semanas.empty:
            raise ValueError
    except ValueError:
        print(f"Semana {semana} no se encuentra en la tabla.")
        semanas = None
    return semanas
        
#3)
def casos_provincia(df_dengue, provincia = None):
    if provincia is None:
        return df_dengue
    try:
        provincias = df_dengue[df_dengue['provincia_nombre'] == provincia]
        if provincias.empty:
            raise ValueError
    except ValueError:
        print(f"Provincia {provincia} no se encuentra en la tabla.")
        provincias = None
    return provincias

#4)
def scatterplot(dengue, provincia, año):
    df_dengue = pd.read_csv(dengue)
    df_filtrado = df_dengue[(df_dengue['provincia_nombre'] == provincia) & (df_dengue['anio'] == año)]
    X = df_filtrado['cantidad_casos']
    Y = df_filtrado['semanas_epidemiologicas']
    plt.scatter(X,Y)
    plt.xlabel('Casos')
    plt.ylabel('Semana')
    plt.show()
    
if __name__ == '__main__':
    sys.argv = ['Parcial_6_6_24.py',
                r'C:\Users\SD\Downloads\casos_reportados.csv',
                'Chaco', 2018]
    if len(sys.argv) < 4:
        raise SystemExit('Uso: Parcial_6_6_24.py casos_reportados.csv')
    dengue = sys.argv[1]
    provincia = sys.argv[2]
    año = sys.argv[3] 
    scatterplot(dengue, provincia, año)
    
#5)
ruta = os.path.join('C:\\', 'Users', 'SD', 'OneDrive', 'Escritorio', 'casos_dengue')
df_dengue_sin_na = df_dengue.dropna()

def guardar_casos(df, ruta, provincia = None, año = None):

    # Verificar que la ruta exista
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"La ruta '{ruta}' no existe.")

    # Crear carpeta 'datos_dengue' dentro de la ruta
    carpeta_salida = os.path.join(ruta, 'datos_dengue')
    os.makedirs(carpeta_salida, exist_ok=True)

    # Aplicar filtros opcionales
    df_filtrado = df.copy()
    if provincia:
        df_filtrado = df_filtrado[df_filtrado['provincia_nombre'] == provincia]
    if año:
        df_filtrado = df_filtrado[df_filtrado['anio'] == int(año)]

    # Si no hay datos después del filtrado, avisar
    if df_filtrado.empty:
        print("⚠️ No hay datos que coincidan con los filtros dados.")
        return

    # Guardar un archivo CSV por provincia
    for prov, datos_prov in df_filtrado.groupby('provincia_nombre'):
        nombre_archivo = f"{prov.replace(' ', '_')}.csv"
        ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)
        datos_prov.to_csv(ruta_archivo, index=False)
        print(f"✅ Archivo guardado: {ruta_archivo}")
    
    