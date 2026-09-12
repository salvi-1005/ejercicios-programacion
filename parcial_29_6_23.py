import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta
from datetime import datetime
import matplotlib.pyplot as plt
import sys

alumnos = r'C:\Users\SD\Downloads\EstudiantesAprobados.csv'
df_alumnos = pd.read_csv(alumnos)

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

def aprobaron_la_cursada_hace_mas_de_n_años_y_deben_el_final(alumnos, N):
    df_alumnos = pd.read_csv(alumnos)
    hoy = datetime.now()
    df_alumnos["fecha_fin_cursada"] = pd.to_datetime(df_alumnos["fecha_fin_cursada"], errors='coerce')
    sin_final = df_alumnos[np.isnan(df_alumnos['nota_final'])].copy()
    sin_final["años_desde_cursada"] = (hoy - sin_final["fecha_fin_cursada"]).dt.days / 365.25
    resultado = sin_final[sin_final["años_desde_cursada"] > N]
    return resultado
    
def scatterplot(alumnos):
    df_alumnos = pd.read_csv(alumnos)
    df_alumnos["fecha_fin_cursada"] = pd.to_datetime(df_alumnos["fecha_fin_cursada"], errors='coerce')
    df_alumnos["fecha_final"] = pd.to_datetime(df_alumnos["fecha_final"], errors='coerce')
    con_final = df_alumnos.dropna().copy()
    con_final["meses_entre_cursada_y_final"] = (con_final['fecha_final'] - con_final["fecha_fin_cursada"]).dt.days / 30
    X = con_final['nota_final']
    Y = con_final["meses_entre_cursada_y_final"]
    plt.title('notas vs meses')
    plt.xlabel('notas del final')
    plt.ylabel('meses que pasaron desde el fin de la cursada hasta el final')
    plt.scatter(X,Y)
    
def f_principal():
    #sys.argv = ['parcial_29_6_23.py', r'C:\Users\SD\Downloads\EstudiantesAprobados.csv', 'N']
    if len(sys.argv) < 3:
        raise SystemExit('Uso: parcial_29_6_23.py df_alumnos')
    alumnos = sys.argv[1]
    n = int(sys.argv[2]) 
    print(aprobaron_la_cursada_hace_mas_de_n_años_y_deben_el_final(alumnos, n))
    scatterplot(alumnos)    
    
if __name__ == '__main__':
    f_principal()