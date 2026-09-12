import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = r'C:\Users\SD\Downloads\Titanic_Dataset.csv'
#%%1er parcial
#1)
def cuantas_personas_hay(titanic):
    contador = 0
    with open(titanic, 'rt', encoding='utf-8') as f: #Abro el archivo
        rows = csv.reader(f)
        headers = next(rows) #Salteo la linea con los nombres de las columnas
        headers
        try:
            for line in rows:
                contador +=1
        except:
            print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    return (contador)

print(cuantas_personas_hay(titanic))

#2)
def seleccionar_columnas(titanic, columnas = None):
    df_titanic = pd.read_csv(titanic)
    if columnas is None:
        return df_titanic
    else:
        return df_titanic[columnas]
    
#3)
def sobrevivientes_y_muertos(titanic):
    sobrevivientes = 0
    muertos = 0
    with open(titanic, 'rt', encoding='utf-8') as f: #Abro el archivo
        rows = csv.reader(f)
        headers = next(rows) #Salteo la linea con los nombres de las columnas
        headers
        try:
            for line in rows:
                if int(line[1]) == 1: 
                    sobrevivientes += 1
                if int(line[1]) == 0:
                    muertos += 1
        except:
            print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    return(sobrevivientes,muertos)

print(sobrevivientes_y_muertos(titanic))

#4)
def precio_promedio(titanic):
    precios_sobrevivientes = []
    precios_muertos = []
    with open(titanic, 'rt', encoding='utf-8') as f: #Abro el archivo
        rows = csv.reader(f)
        headers = next(rows) #Salteo la linea con los nombres de las columnas
        headers
        try:
            for line in rows:
                if int(line[1]) == 1: 
                    precios_sobrevivientes.append(float(line[9]))
                if int(line[1]) == 0:
                    precios_muertos.append(float(line[9]))
        except:
            print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    promedio_precios_sobrevivientes = np.mean(precios_sobrevivientes)
    promedio_precios_muertos = np.mean(precios_muertos)
    return (promedio_precios_sobrevivientes,promedio_precios_muertos)

print(precio_promedio(titanic))

#5)
def edad_promedio(path):
    with open(path, 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)  # saltea encabezado

        edad_sobrevivientes = []
        edad_muertos = []

        for line in rows:
            edad = line[5].strip()  # saca espacios en blanco

            if edad == '':
                continue  # si está vacío, lo salteo

            if int(line[1]) == 1:
                edad_sobrevivientes.append(float(edad))
            elif int(line[1]) == 0:
                edad_muertos.append(float(edad))

        prom_s = sum(edad_sobrevivientes) / len(edad_sobrevivientes)
        prom_m = sum(edad_muertos) / len(edad_muertos)

        return prom_s, prom_m

print(edad_promedio(titanic))

#6)
def supervivencia_por_genero(titanic):
    hombres_sobrevivientes = 0
    mujeres_sobrevivientes = 0
    with open(titanic, 'rt', encoding='utf-8') as f: #Abro el archivo
        rows = csv.reader(f)
        headers = next(rows) #Salteo la linea con los nombres de las columnas
        headers
        try:
            for line in rows:
                if int(line[1]) == 1 and line[4] == 'male': 
                   hombres_sobrevivientes += 1
                if int(line[1]) == 1 and line[4] == 'female':
                   mujeres_sobrevivientes += 1
        except:
            print('File Not Found Error') #Si le mando el archivo equivocado, atrapa el error
    return (hombres_sobrevivientes, mujeres_sobrevivientes)

print(supervivencia_por_genero(titanic))

#%%2do parcial

#1)
def df_cuantas_personas_hay(titanic):
    df_titanic = pd.read_csv(titanic)
    return df_titanic['Name'].count

#2)
def df_seleccionar_columnas(titanic, columnas, supervivencia):
    df_titanic = pd.read_csv(titanic)
    if supervivencia not in [0, 1]:
        raise ValueError('ingresen 0 o 1')
    df_filtrado = df_titanic[df_titanic['Survived'] == supervivencia]
    return df_filtrado[columnas]
        
#3)
def analisis(titanic):
    return (precio_promedio(titanic), edad_promedio(titanic), supervivencia_por_genero(titanic))
    
#4)
df_titanic = pd.read_csv(titanic)
tarifas_sobrevivientes = df_titanic[df_titanic['Survived'] == 1]['Fare']
tarifas_muertos = df_titanic[df_titanic['Survived'] == 0]['Fare']

plt.hist(tarifas_sobrevivientes)
plt.title('tarifas_sobrevivientes')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

from datetime import datetime

ahora = datetime.now()
print(ahora.year)   # Año
print(ahora.month)  # Mes
print(ahora.day)    # Día
print(ahora.hour)   # Hora
print(ahora.minute) # Minuto
print(ahora.second) # Segundo