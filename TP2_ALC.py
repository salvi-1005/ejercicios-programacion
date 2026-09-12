import pandas as pd
-import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression

df_nutricional = pd.read_csv('C:/Users/SD/OneDrive/Downloads/tabla_nutricional_SD.csv')

print(df_nutricional.head())

#2)

def evaluar_dieta(df):
    # Márgenes de la OMS
    margenes = {
        'Grasas totales': (15, 30),
        'Ácidos grasos saturados': (0, 10),
        'Ácidos grasos poliinsaturados': (6, 10),
        'Ácidos grasos poliinsaturados n-6': (5, 8),
        'Ácidos grasos poliinsaturados n-3': (1, 2),
        'Ácidos grasos trans': (0, 1),
        'Carbohidratos totales': (55, 75),
        'Azúcares libres': (0, 10),
        'Proteínas': (10, 15),
        'Colesterol': (0, 300),  # mg/día
        'Sodio': (0, 2000),  # mg/día
        'Frutas y verduras': (400, float('inf')),  # g/día
        'Fibra alimentaria total': (25, float('inf'))  # g/día
    }

    # Sumamos los valores correspondientes en el DataFrame
    total_valores = df.sum()

    # Evaluamos los márgenes
    cumple_margenes = True

    # Verificamos cada margen
    for factor, (min_val, max_val) in margenes.items():
        if factor in total_valores:
            valor = total_valores[factor]
            if not (min_val <= valor <= max_val):
                cumple_margenes = False
                break
        else:
            cumple_margenes = False
            break

    return cumple_margenes

#3)

nutrientes = df_nutricional.columns[2:]  # Asumiendo que las primeras dos columnas son 'Alimento' y 'Cantidad'
X = df_nutricional[nutrientes].values

# Normalizar los datos
scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)

# Realizar el ACP
pca = PCA(n_components=2)  # Usamos 2 componentes principales para poder graficar
X_pca = pca.fit_transform(X_normalizado)

# Crear un DataFrame con los resultados del ACP
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['Alimento'] = df_nutricional['Alimento']

# Graficar los resultados
plt.figure(figsize=(10, 8))
plt.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.7)
for i, alimento in enumerate(df_pca['Alimento']):
    plt.text(df_pca['PC1'][i], df_pca['PC2'][i], alimento, fontsize=9)

plt.title('Análisis en Componentes Principales (ACP) de Alimentos')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()

#4)

file_path = 'C:/Users/SD/Downloads/consumidores_libres.csv'

# Cargar el archivo CSV en un DataFrame
df_consumidores = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print(df_consumidores.head())

print(df_consumidores.columns)

nutritional_columns = ['HC (gr)', 'Proteinas (gr)', 'Grasas (gr)', 'Na (gr)', 'Ca (gr)', 'Fe (gr)', 
                       'Azucares Libres (gr)', 'AGS (gr)', 'AGNI (gr)', 'AG p (gr)', 'Fibra (gr)']

# Asegurarse de que todas las columnas están en el DataFrame
nutritional_columns = [col for col in nutritional_columns if col in df_nutricional.columns]

# Si no se encuentran todas las columnas necesarias, mostrar un error
if len(nutritional_columns) < 11:
    print(f"No se encontraron todas las columnas necesarias. Columnas encontradas: {nutritional_columns}")
else:
    # Filtrar el DataFrame para seleccionar solo las columnas necesarias
    X = df_nutricional[nutritional_columns]

    # Normalizar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Realizar el ACP
    pca = PCA(n_components=2)  # Usamos 2 componentes para poder graficar en 2D
    X_pca = pca.fit_transform(X_scaled)

    # Añadir los componentes principales al DataFrame
    df_nutricional['PCA1'] = X_pca[:, 0]
    df_nutricional['PCA2'] = X_pca[:, 1]

    # Graficar los resultados
    plt.figure(figsize=(10, 8))
    plt.scatter(df_nutricional['PCA1'], df_nutricional['PCA2'], s=50)

    # Añadir etiquetas a los puntos
    for i, food in enumerate(df_nutricional['Alimento']):
        plt.text(df_nutricional['PCA1'][i], df_nutricional['PCA2'][i], food)

    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.title('Proyección de Alimentos en el Espacio de Componentes Principales')
    plt.grid(True)
    plt.show()
    
#5)

# Datos de precios mensuales de los alimentos
data = {
    "Producto": ["ACEITE COCINERO GIRASOL", "ARROZ GRANO FINO", "AZUCAR LEDESMA", "FIDEOS GUISEROS", "HARINA DE TRIGO", 
                 "HUEVOS COLOR DOCENA", "PAN FRESCO", "LECHE c/VIT.FORT", "YERBA TARAGUI", "ZANAHORIAS", 
                 "BERENJENAS", "TOMATE PERITA", "CEBOLLA", "PAPA NEGRA", "ACELGA PAQUETE", "NARANJA", "MANZANA", 
                 "BOLA DE LOMO", "ASADO", "PALETA", "CARNE PICADA COMUN"],
    "Diciembre": [2500, 1650, 1990, 1600, 950, 2200, 1650, 1100, 2800, 820, 1200, 1200, 500, 850, 450, 920, 1900, 6200, 5400, 5200, 4200],
    "Enero": [3100, 2300, 2050, 1990, 1250, 2600, 2100, 1210, 3700, 990, 1200, 1100, 700, 890, 620, 1250, 2100, 7200, 6300, 6200, 4800],
    "Febrero": [3450, 2800, 2050, 2150, 1350, 3000, 2200, 1620, 4600, 1100, 1490, 1200, 990, 1000, 1100, 1850, 2400, 8300, 7500, 7100, 5200],
    "Marzo": [3600, 3100, 2100, 2200, 1500, 3400, 2300, 1890, 4950, 1100, 2200, 2300, 1150, 990, 1990, 1900, 2400, 8500, 7600, 7800, 5200],
    "Abril": [3700, 3550, 2100, 2290, 1690, 3800, 2300, 1990, 5500, 1100, 3200, 2700, 1500, 900, 1990, 2200, 2700, 8650, 7750, 7900, 5500]
}

df_precios = pd.DataFrame(data)

# Calcular los aumentos para cada mes usando mínimos cuadrados
meses = np.array([0, 1, 2, 3, 4]).reshape(-1, 1)  # Convertir los meses en una matriz columna

# Crear un DataFrame para almacenar los coeficientes de la regresión
coeficientes = pd.DataFrame(columns=["Producto", "Coeficiente_HC", "Coeficiente_Proteinas", "Coeficiente_Grasas"])

for index, row in df_precios.iterrows():
    precios = row[1:].values.reshape(-1, 1)  # Obtener los precios del producto
    producto = row[0]
    
    # Ajustar una recta de mínimos cuadrados
    model = LinearRegression().fit(meses, precios)
    coeficiente = model.coef_[0][0]
    
    # Calcular los coeficientes de cada nutriente
    # Nota: Esta parte requiere los datos nutricionales de cada producto, que no están en el conjunto de datos de precios
    # Asumiendo que tenemos un DataFrame con los datos nutricionales para cada producto
    # df_nutricion = pd.read_csv('datos_nutricionales.csv')  # Supuesto
    # hc = df_nutricion.loc[df_nutricion["Producto"] == producto, "HC"].values[0]
    # proteinas = df_nutricion.loc[df_nutricion["Producto"] == producto, "Proteinas"].values[0]
    # grasas = df_nutricion.loc[df_nutricion["Producto"] == producto, "Grasas"].values[0]
    
    # Suponiendo valores ficticios para cada nutriente en este ejemplo
    hc = np.random.uniform(0, 10)
    proteinas = np.random.uniform(0, 10)
    grasas = np.random.uniform(0, 10)
    
    # Agregar los coeficientes al DataFrame
    coeficientes = coeficientes.append({
        "Producto": producto, 
        "Coeficiente_HC": coeficiente * hc, 
        "Coeficiente_Proteinas": coeficiente * proteinas, 
        "Coeficiente_Grasas": coeficiente * grasas
    }, ignore_index=True)

# Mostrar la tabla de coeficientes
print(coeficientes)

# Graficar los datos y la recta de mínimos cuadrados para cada nutriente
for index, row in df_precios.iterrows():
    precios = row[1:].values
    producto = row[0]
    
    plt.figure(figsize=(10, 6))
    plt.plot(meses, precios, 'o', label='Datos')
    
    # Ajustar una recta de mínimos cuadrados
    model = LinearRegression().fit(meses, precios)
    precios_ajustados = model.predict(meses)
    
    plt.plot(meses, precios_ajustados, '-', label='Recta de mínimos cuadrados')
    plt.title(f'Precio de {producto} en los últimos 4 meses')
    plt.xlabel('Mes')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid(True)
    plt.show()