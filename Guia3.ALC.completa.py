import matplotlib.pyplot as plt
import numpy as np


def proyectarPts(T, wz):
    assert(T.shape == (2,2)) # chequeo de matriz 2x2
    assert(T.shape[1] == wz.shape[0]) # multiplicacion matricial valida   
    xy = np.dot(T, wz)
    return xy
wz = np.array([[1,2],[3,4]])

def pointsGrid(corners):
    # crear 10 lineas horizontales
    [w1, z1] = np.meshgrid(np.linspace(corners[0,0], corners[1,0], 46),
                        np.linspace(corners[0,1], corners[1,1], 10))

    [w2, z2] = np.meshgrid(np.linspace(corners[0,0], corners[1,0], 10),
                        np.linspace(corners[0,1], corners[1,1], 46))

    w = np.concatenate((w1.reshape(1,-1),w2.reshape(1,-1)),1)
    z = np.concatenate((z1.reshape(1,-1),z2.reshape(1,-1)),1)
    wz = np.concatenate((w,z))
                         
    return wz
          
def vistform(T, wz, titulo=''):
    # transformar los puntos de entrada usando T
    xy = proyectarPts(T, wz)
    if xy is None:
        print('No fue implementada correctamente la proyeccion de coordenadas')
        return
    # calcular los limites para ambos plots
    minlim = np.min(np.concatenate((wz, xy), 1), axis=1)
    maxlim = np.max(np.concatenate((wz, xy), 1), axis=1)

    bump = [np.max(((maxlim[0] - minlim[0]) * 0.05, 0.1)),
            np.max(((maxlim[1] - minlim[1]) * 0.05, 0.1))]
    limits = [[minlim[0]-bump[0], maxlim[0]+bump[0]],
               [minlim[1]-bump[1], maxlim[1]+bump[1]]]             

    fig, (ax1, ax2) = plt.subplots(1, 2)         
    fig.suptitle(titulo)
    grid_plot(ax1, wz, limits, 'w', 'z')    
    grid_plot(ax2, xy, limits, 'x', 'y')    
    
def grid_plot(ax, ab, limits, a_label, b_label):
    ax.plot(ab[0,:], ab[1,:], '.')
    ax.set(aspect='equal',
           xlim=limits[0], ylim=limits[1],
           xlabel=a_label, ylabel=b_label)


def main():
    print('Ejecutar el programa')
    # generar el tipo de transformacion dando valores a la matriz T
    T = np.array([[1., 0.4],[0,1.]])
    corners = np.array([[0,0],[100,100]])
    wz = pointsGrid(corners)
    vistform(T, wz, 'Deformar coordenadas')
theta = np.radians(45)
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
A = np.array([[cos_theta, (-sin_theta)],[sin_theta, cos_theta]])
R = np.array([[cos_theta, (-sin_theta),0],[sin_theta, cos_theta,0],[0,0,1]])
T = np.array([[1,0,2],[0,1,3],[0,0,1]])
E = np.array([[2,0,0],[0,2,0],[0,0,1]])
D = np.array([[2,0,0],[0,1,0],[0,0,1]])
coordenadas = np.array([[1,1,1]])

CE = np.dot(coordenadas, E)
CT = np.dot(coordenadas, T)
CR = np.dot(coordenadas, R)
CD = np.dot(coordenadas, D)

def rotation_matrix(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([[cos_theta, (-sin_theta)],[sin_theta, cos_theta]])
    
if __name__ == "__main__":
    main()

import sys
e = sys.float_info.epsilon
p =1e34
q = 1
p + q - p
p = 100
q =1e-15
(p + q) + q 
((p + q) + q) + q
0.1+0.2 == 0.3
0.1+0.3 == 0.4
1e-323
1e-324
e/2
1 + e/2 + e/2
1 + e/2 + e/2
1 + e/2 + e/2 - 1
1 + e/2 + e/2 - 1

def seno1():
    for j in range(1, 25):
        resp = np.sin(10*j*(np.pi))
    return resp

def seno2():
    for j in range(1, 25):    
        resp = np.sin((np.pi)/2 + (np.pi)*10*j)
    return resp
