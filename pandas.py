import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

fname = r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv"
df = pd.read_csv(fname)

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')


cant_ejemplares = df['nombre_com'].value_counts()

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

s2.plot()

w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()

df_walk_suav.to_csv(r"C:\Users\SD\Downloads\caminata_apostolica.csv")

#%%9.6)
arboles = r"C:\Users\SD\Downloads\arbolado-publico-lineal-2017-2018.csv"
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_arboles = pd.read_csv(arboles)
df_lineal = df_arboles[cols_sel]

#Imprimí las diez especies más frecuentes con sus respectivas cantidades:
especies = df_lineal['nombre_cientifico'].value_counts()
print(especies[1:11])

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#%%9.7)
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#9.8)
parques = r"C:\Users\SD\Downloads\arbolado-en-espacios-verdes.csv"
veredas = r"C:\Users\SD\Downloads\arbolado-publico-lineal-2017-2018.csv"

df_parques = pd.read_csv(parques)
df_veredas = pd.read_csv(veredas)

columnas_parque = ['diametro','altura_tot']
columnas_vereda = ['diametro_altura_pecho','altura_arbol']

df_tipas_parques = (df_parques[df_parques['nombre_com'] == 'Tipa blanca'][columnas_parque]).copy()
df_tipas_veredas = (df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][columnas_vereda]).copy()

df_tipas_parques_renombrado = df_tipas_parques.rename(columns={"diametro": "diametro_pecho","altura_tot": "altura"})
df_tipas_veredas_renombrado = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro_pecho","altura_arbol": "altura"})

df_tipas_parques_renombrado['ambiente'] = ['parque']*len(df_tipas_parques_renombrado) 
df_tipas_veredas_renombrado['ambiente'] = ['vereda']*len(df_tipas_veredas_renombrado)

df_tipas = pd.concat([df_tipas_veredas_renombrado, df_tipas_parques_renombrado])

df_tipas.boxplot('diametro_pecho', by = 'ambiente')
df_tipas.boxplot('altura', by = 'ambiente')