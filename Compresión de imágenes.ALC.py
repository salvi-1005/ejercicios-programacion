import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Cargar la imagen
imagen = plt.imread('quijote.jpg.png')

# Imprimir la imagen
print(imagen)

if len(imagen.shape) == 3:
    imagen = np.mean(imagen, axis=2)

# Mostrar la imagen con la gama de colores por defecto
plt.imshow(imagen)
plt.title("Imagen con gama de colores por defecto")
plt.show()

# Mostrar la imagen en blanco y negro
plt.imshow(imagen, cmap="gray")
plt.title("Imagen en blanco y negro")
plt.show()

def truncated_svd(A, r):
    # Calcular la descomposición en valores singulares
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    
    # Truncar las matrices U, V y el vector s
    U_tilde = U[:, :r]
    s_tilde = s[:r]
    V_tilde = Vt[:r, :]
    
    # Devolver la tupla con la dimensión original de la matriz, U_tilde, s_tilde y V_tilde
    return (A.shape, U_tilde, s_tilde, V_tilde)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una matriz de ejemplo
    A = np.random.rand(5, 3)
    r = 2  # Número de valores singulares a mantener

    # Calcular la SVD truncada
    resultado = truncated_svd(A, r)

    # Mostrar los resultados
    print("Dimensiones originales de la matriz A:", resultado[0])
    print("Matriz U_tilde:")
    print(resultado[1])
    print("Vector de valores singulares s_tilde:")
    print(resultado[2])
    print("Matriz V_tilde:")
    print(resultado[3])
    
def reconstruct_matrix(dimensions, U_tilde, s_tilde, V_tilde):
    n, m = dimensions
    
    # Crear U' y V' expandiendo U_tilde y V_tilde con ceros
    U_prime = np.zeros((n, n))
    V_prime = np.zeros((m, m))
    
    U_prime[:, :U_tilde.shape[1]] = U_tilde
    V_prime[:V_tilde.shape[0], :] = V_tilde
    
    # Crear la matriz diagonal Sigma'
    Sigma_prime = np.zeros((n, m))
    np.fill_diagonal(Sigma_prime, np.append(s_tilde, np.zeros(min(n, m) - len(s_tilde))))
    
    # Calcular la matriz B
    B = np.dot(np.dot(U_prime, Sigma_prime), V_prime)
    
    return B

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz original y descomposición SVD truncada del ejemplo anterior
    A = np.random.rand(5, 3)
    r = 2

    # Calcular la SVD truncada
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    U_tilde = U[:, :r]
    s_tilde = s[:r]
    V_tilde = Vt[:r, :]
    dimensions = A.shape

    # Reconstruir la matriz
    B = reconstruct_matrix(dimensions, U_tilde, s_tilde, V_tilde)
    
    print("Matriz original A:")
    print(A)
    print("Matriz reconstruida B:")
    print(B)

def calcular_error_relativo(s, r):
    return s[r] / s[0]

def calcular_proporcion_compresion(n, m, r):
    return (n * m) / ((n + m) * r + r + 2)

r = 50  # Valor de r
dims, U_tilde, s_tilde, V_tilde = truncated_svd(imagen, r)
imagen_reconstruida = reconstruct_matrix(dims, U_tilde, s_tilde, V_tilde)

error_relativo = calcular_error_relativo(s_tilde, r)
proporcion_compresion = calcular_proporcion_compresion(dims[0], dims[1], r)

print(f"Para r={r}:")
print(f"Error relativo de aproximación: {error_relativo}")
print(f"Proporción de compresión: {proporcion_compresion}")

plt.imshow(imagen_reconstruida, cmap='gray')
plt.title(f'Imagen reconstruida con r={r}')
plt.show()
    
    