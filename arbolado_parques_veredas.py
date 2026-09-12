import pandas as pd

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
print(df_tipas)

df_tipas.boxplot('diametro_pecho', by = 'ambiente')
df_tipas.boxplot('altura', by = 'ambiente')
