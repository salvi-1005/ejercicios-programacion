import numpy as np
from scipy.optimize import line_search

#1)
def jacobi(A, b, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)
    D = np.diag(A)
    R = A - np.diagflat(D)
    
    for k in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Jacobi method converged in {k} iterations.")
            return x_new
        x = x_new
    print("Jacobi method did not converge within the maximum number of iterations.")
    return x

def gauss_seidel(A, b, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)
    
    for k in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Gauss-Seidel method converged in {k} iterations.")
            return x_new
        x = x_new
    print("Gauss-Seidel method did not converge within the maximum number of iterations.")
    return x

# Ejemplo de uso
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]], dtype=float)
b = np.array([15, 10, 10, 10], dtype=float)

x_jacobi = jacobi(A, b)
x_gauss_seidel = gauss_seidel(A, b)

print("Solución con Jacobi:", x_jacobi)
print("Solución con Gauss-Seidel:", x_gauss_seidel)

#15)
def gradiente(f, grad_f, x0, tol=1e-5, max_iter=1000):
    x = x0
    iteraciones = [x0]
    for _ in range(max_iter):
        grad = grad_f(x)
        # Usamos line_search para encontrar el t óptimo
        t_opt, _, _ = line_search(f, grad_f, x, -grad)[:3]
        if t_opt is None:  # Si line_search no encuentra t, tomamos un valor pequeño
            t_opt = 1e-4
        x_new = x - t_opt * grad
        iteraciones.append(x_new)
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    return np.array(iteraciones)

# Ejemplo de uso con una función cuadrática simple
def f(x):
    return x[0]**2 + x[1]**2

def grad_f(x):
    return np.array([2*x[0], 2*x[1]])

x0 = np.array([2.0, 2.0])
tol = 1e-5

iteraciones = gradiente(f, grad_f, x0, tol)
print("Secuencia de puntos generada:\n", iteraciones)
print("Número de iteraciones:", len(iteraciones))



