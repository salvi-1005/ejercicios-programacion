import numpy as np
import matplotlib.pyplot as plt

#1)

def horner(coefs, x):
    result = coefs[0]
    for i in range(1, len(coefs)):
        result = result * x + coefs[i]
    return result

# Coeficientes del polinomio (del término de mayor grado al menor)
coefs = [2,3,5,7]

# Punto de evaluación
x0 = 3  # por ejemplo

# Evaluar el polinomio en x0 usando numpy.polyval
resultado = np.polyval(coefs, x0)
print(resultado)


#3)

# Definir los datos
data1_x = np.array([-1, 0, 2, 3])
data1_y = np.array([-1, 3, 11, 27])

data2_x = np.array([-1, 0, 1, 2])
data2_y = np.array([-3, 1, 1, 3])

# Función para ajustar un polinomio y graficar
def ajustar_y_graficar(x, y, grados, titulo):
    plt.scatter(x, y, color='red', label='Datos')
    
    for grado in grados:
        coef = np.polyfit(x, y, grado)
        polinomio = np.poly1d(coef)
        xp = np.linspace(min(x), max(x), 100)
        plt.plot(xp, polinomio(xp), label=f'Grado {grado}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(titulo)
    plt.show()

# Ajustar y graficar para el conjunto de datos 1
ajustar_y_graficar(data1_x, data1_y, [1, 2, 3], 'Conjunto de datos 1')

# Ajustar y graficar para el conjunto de datos 2
ajustar_y_graficar(data2_x, data2_y, [1, 2, 3], 'Conjunto de datos 2')

#4)

# Definir los puntos x y sus valores correspondientes y
x = np.array([-1, 0, 2, 3])
y = np.array([-1, 3, 11, 27])

# Calcular la constante que minimiza el error cuadrático
c = np.mean(y)

print(f"La constante que mejor aproxima los puntos en el sentido de mínimos cuadrados es: {c}")

#5)
# Datos de la población
años = np.array([1950, 1960, 1970, 1980, 1990, 2000])
poblacion = np.array([17, 20.5, 23.9, 27.9, 32.6, 36.9])

# Ajuste lineal
coeficientes = np.polyfit(años, poblacion, 1)
a, b = coeficientes

# Función ajustada
def f(x):
    return a * x + b

# Gráfica del ajuste
plt.scatter(años, poblacion, color='blue', label='Datos')
plt.plot(años, f(años), color='red', label=f'Ajuste lineal: f(x) = {a:.2f}x + {b:.2f}')
plt.xlabel('Año')
plt.ylabel('Población (millones)')
plt.legend()
plt.title('Ajuste lineal de la población argentina')
plt.show()

# Inferir la población para los años mencionados
años_inferidos = np.array([1955, 1965, 1975, 1985, 1995])
poblacion_inferida = f(años_inferidos)

print("Población inferida en los años 1955, 1965, 1975, 1985, 1995:")
for año, pobl in zip(años_inferidos, poblacion_inferida):
    print(f"{año}: {pobl:.2f} millones")

# Población real para los años mencionados y cálculo del error
poblacion_real = np.array([18.8, 22.2, 25.9, 30.2, 34.8])
errores = poblacion_real - poblacion_inferida

print("\nErrores al inferir la población:")
for año, error in zip(años_inferidos, errores):
    print(f"{año}: Error de {error:.2f} millones")

# Gráfica con los nuevos datos
plt.scatter(años, poblacion, color='blue', label='Datos')
plt.plot(años, f(años), color='red', label=f'Ajuste lineal: f(x) = {a:.2f}x + {b:.2f}')
plt.scatter(años_inferidos, poblacion_real, color='green', label='Datos reales adicionales')
plt.xlabel('Año')
plt.ylabel('Población (millones)')
plt.legend()
plt.title('Ajuste lineal de la población argentina con datos adicionales')
plt.show()

# Evaluación de la inferencia
mse = np.mean(errores**2)
print(f"\nError cuadrático medio (MSE): {mse:.2f}")

if mse < 1:  # Un umbral arbitrario para decidir si el error es pequeño
    print("La inferencia es razonablemente buena.")
else:
    print("La inferencia no es muy precisa.")
    
#6)
# Construcción de la matriz de Vandermonde
V = np.vander(x, N=len(x), increasing=True)

# Resolución del sistema V * a = y para obtener los coeficientes a
a = np.linalg.solve(V, y)

print("Coeficientes del polinomio:", a)

# Si m > n+1 (más puntos que el grado del polinomio)
a_approx = np.linalg.lstsq(V, y, rcond=None)[0]

print("Coeficientes del polinomio por mínimos cuadrados:", a_approx)

#7)
def f(x):
    return 1 / (1 + 25 * x**2)

def vandermonde_matrix(x):
    return np.vander(x, increasing=True)

def interpolate_polynomial(x, y):
    V = vandermonde_matrix(x)
    return np.linalg.solve(V, y)

def evaluate_polynomial(coeffs, x):
    return np.polyval(coeffs[::-1], x)

def calculate_infinity_norm(f_values, p_values):
    return np.max(np.abs(f_values - p_values))

# Generar puntos equiespaciados y evaluar la función f(x)
def generate_data(n):
    x = np.linspace(-1, 1, n + 1)
    y = f(x)
    return x, y

# Graficar la función y los polinomios interpoladores
n_values = [5, 10, 15]
x_plot = np.linspace(-1, 1, 1000)
f_plot = f(x_plot)

plt.figure(figsize=(14, 8))
plt.plot(x_plot, f_plot, label='f(x)', color='black', linewidth=2)

for n in n_values:
    x, y = generate_data(n)
    coeffs = interpolate_polynomial(x, y)
    p_plot = evaluate_polynomial(coeffs, x_plot)
    
    # Calcular la norma infinito
    infinity_norm = calculate_infinity_norm(f_plot, p_plot)
    
    plt.plot(x_plot, p_plot, label=f'Interpolador p_{n}(x), ||f - p_{n}||∞ = {infinity_norm:.2e}')
    plt.scatter(x, y, marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de f(x) = 1 / (1 + 25x^2)')
plt.legend()
plt.grid(True)
plt.show()

#8)
# Datos de población
years = np.array([1950, 1960, 1970, 1980, 1990, 2000])
population = np.array([17, 20.5, 23.9, 27.9, 32.6, 36.9])

# Linealizar el problema
log_population = np.log(population)

# Ajuste de polinomio de grado 5
coeffs_deg5 = np.polyfit(years, log_population, 5)
poly_deg5 = np.poly1d(coeffs_deg5)

# Evaluación y exponenciación
log_population_fit_deg5 = poly_deg5(years)
population_fit_deg5 = np.exp(log_population_fit_deg5)

# Ajuste de polinomio de grado 1
coeffs_deg1 = np.polyfit(years, log_population, 1)
poly_deg1 = np.poly1d(coeffs_deg1)

# Evaluación y exponenciación
log_population_fit_deg1 = poly_deg1(years)
population_fit_deg1 = np.exp(log_population_fit_deg1)

# Graficar los resultados
plt.figure(figsize=(12, 6))

# Datos originales
plt.scatter(years, population, color='black', label='Datos originales')

# Ajuste de grado 5
years_fit = np.linspace(1950, 2000, 500)
population_fit_deg5_smooth = np.exp(poly_deg5(years_fit))
plt.plot(years_fit, population_fit_deg5_smooth, label='Ajuste de grado 5')

# Ajuste de grado 1
population_fit_deg1_smooth = np.exp(poly_deg1(years_fit))
plt.plot(years_fit, population_fit_deg1_smooth, label='Ajuste de grado 1')

plt.xlabel('Año')
plt.ylabel('Población (millones)')
plt.legend()
plt.title('Ajuste de Población Argentina con Funciones Exponenciales')
plt.grid(True)
plt.show()

# Imprimir la expresión de los polinomios
print("Polinomio de grado 5 (log-transformed):")
print(poly_deg5)

print("\nPolinomio de grado 1 (log-transformed):")
print(poly_deg1)

#9)
# Datos de tiempo y altura
tiempo = np.array([0, 1, 2, 4, 6])
altura = np.array([200, 195, 180, 120, 25])

# Ajuste polinómico de grado 2
coeficientes = np.polyfit(tiempo, altura, 2)
polinomio = np.poly1d(coeficientes)

# Imprimir los coeficientes
print("Coeficientes del polinomio:", coeficientes)

# Evaluar el polinomio ajustado
tiempo_fit = np.linspace(0, 6, 100)
altura_fit = polinomio(tiempo_fit)

# Graficar los datos y el ajuste
plt.scatter(tiempo, altura, color='black', label='Datos originales')
plt.plot(tiempo_fit, altura_fit, label='Ajuste cuadrático $at^2 + b$')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.legend()
plt.grid(True)
plt.show()

# Calcular g a partir del coeficiente a
a = coeficientes[0]
g = -2 * a

# Imprimir el valor de g
print("Valor aproximado de g:", g)

#10)
# Datos de peso y volumen pulmonar
peso = np.array([60, 85, 100, 150, 250])
volumen_pulmonar = np.array([2.3, 4, 5, 9, 19.5])

# Transformar los datos tomando logaritmos
log_peso = np.log(peso)
log_volumen_pulmonar = np.log(volumen_pulmonar)

# Ajuste lineal a los datos transformados
coeficientes = np.polyfit(log_peso, log_volumen_pulmonar, 1)
b = coeficientes[0]
A = coeficientes[1]
a = np.exp(A)

# Imprimir los coeficientes
print("Coeficiente a:", a)
print("Coeficiente b:", b)

# Función de ajuste
def funcion_ajuste(x):
    return a * x**b

# Graficar los datos y la curva de ajuste
peso_fit = np.linspace(min(peso), max(peso), 100)
volumen_pulmonar_fit = funcion_ajuste(peso_fit)

plt.scatter(peso, volumen_pulmonar, color='black', label='Datos originales')
plt.plot(peso_fit, volumen_pulmonar_fit, label='$Y = aX^b$', color='red')
plt.xlabel('Peso (kg)')
plt.ylabel('Volumen pulmonar (l)')
plt.legend()
plt.grid(True)
plt.show()

peso_individuo = 93
volumen_pulmonar_predicho = funcion_ajuste(peso_individuo)

print("Volumen pulmonar predicho para un individuo con peso de 93 kg:", volumen_pulmonar_predicho)

#11)
def minimos_cuadrados(funciones, x, y):
    # Número de funciones
    m = len(funciones)
    # Número de puntos de datos
    n = len(x)
    
    # Construir la matriz de diseño A
    A = np.zeros((n, m))
    for i in range(m):
        A[:, i] = funciones[i](x)
    
    # Resolver A * alpha = y usando mínimos cuadrados
    alpha, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    
    # Construir la función ajustada
    def funcion_ajustada(x):
        return sum(alpha[i] * funciones[i](x) for i in range(m))
    
    return alpha, funcion_ajustada

# Ejemplo de uso:
# Definir algunas funciones de ejemplo
def f1(x):
    return np.ones_like(x)

def f2(x):
    return x

def f3(x):
    return x**2

# Lista de funciones
funciones = [f1, f2, f3]

# Vectores de datos
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Calcular los coeficientes y la función ajustada
alpha, funcion_ajustada = minimos_cuadrados(funciones, x, y)

# Imprimir los coeficientes
print("Coeficientes α:", alpha)

# Graficar los datos y la función ajustada
import matplotlib.pyplot as plt

# Datos originales
plt.scatter(x, y, color='black', label='Datos originales')

# Evaluar la función ajustada
x_fit = np.linspace(min(x), max(x), 100)
y_fit = funcion_ajustada(x_fit)

# Gráfica de la función ajustada
plt.plot(x_fit, y_fit, label='Función ajustada', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()