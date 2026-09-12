#%%2)
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

notas = r"C:\Users\SD\Downloads\notas_materias.csv"

df_notas = pd.read_csv(notas)

#a)
sin_duplicados = df_notas.drop_duplicates() 

#b)
def promedio(df_notas, materia):
    df_filtrado = df_notas[df_notas['materia'] == materia]
    if df_filtrado.empty:
        print(f"No se encontraron registros para la materia '{materia}'.")
        return None
    print("\n=== Registros ===")
    for _, fila in df_filtrado.iterrows():
        print(f"{fila['nombre']} {fila['apellido']} — Nota: {fila['nota_final']}")
    promedio = np.mean(df_filtrado['nota_final'])
    print(f"\nPromedio general de {materia}: {promedio:.2f}")
    return promedio

#c)
def boxplot(df_notas, materia):
    df_filtrado = df_notas[df_notas['materia'] == materia]
    if df_filtrado.empty:
        print(f"No hay datos para la materia '{materia}'")
        return
    plt.figure(figsize=(5, 6))
    plt.boxplot(df_filtrado["nota_final"], labels=[materia])
    plt.title(f"Distribución de notas finales en {materia}")
    plt.ylabel("Nota final")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
    
#%%3)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python script.py archivo_notas.csv materia")
    ruta_csv = sys.argv[1]
    materia = sys.argv[2]
    df = pd.read_csv(ruta_csv)
    print(promedio(df, materia))
    boxplot(df, materia)