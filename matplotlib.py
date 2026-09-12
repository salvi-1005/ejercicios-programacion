import numpy as np
import matplotlib.pyplot as plt
import random

# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(10, 6), dpi=80)

# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="seno")

plt.legend(loc='upper left')

# Rango del eje x
plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Ponemos marcas (ticks) en el eje x
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Rango del eje y
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Ponemos marcas (ticks) en el eje y
plt.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)

# Mostramos el resultado en pantalla
plt.show()

def cm2inch(value):
    return value/2.54

fig = plt.figure(figsize=(cm2inch(12.8), cm2inch(9.6)))

#9.1)
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

#9.2)
def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

M = 12
N = 100000

caminatas = [randomwalk(N) for _ in range(M)]

distancias_finales = [abs(c[-1]) for c in caminatas]

idx_mas_cerca = np.argmin(distancias_finales)
idx_mas_lejos = np.argmax(distancias_finales)

plt.subplot(2, 1, 1) 
plt.plot(randomwalk(N), color="blue", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="red", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="yellow", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="green", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="orange", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="violet", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="pink", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="brown", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="purple", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="grey", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="white", linewidth=2.5, linestyle="-")
plt.plot(randomwalk(N), color="black", linewidth=2.5, linestyle="-")
plt.xticks([]), plt.yticks([])
plt.xlabel("tiempo")
plt.ylabel("distancia al origen")
plt.xticks([]) 
plt.yticks([-500, 0, 500],
          [r'$-500$', r'$0$', r'$500$'])
plt.title("12 caminatas al azar")

plt.subplot(2, 2, 3)
plt.plot(caminatas[idx_mas_lejos], color="blue", linewidth=2.5, linestyle="-")
plt.xticks([]) 
plt.yticks([-500, 0, 500],
          [r'$-500$', r'$0$', r'$500$'])
plt.title("La caminata que más se aleja")

plt.subplot(2, 2, 4)
plt.plot(caminatas[idx_mas_cerca], color="blue", linewidth=2.5, linestyle="-")
plt.xticks([])   
plt.yticks([])
plt.title("La caminata que más se aleja")
plt.title("La caminata que menos se aleja")

plt.show()

#9.3)
n = 12 
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='right', va='top')
plt.ylim(-1.25, +1.25)
plt.xticks([])   
plt.yticks([])

plt.show()

#9.4)
plt.axes([0, 0, 1, 1], polar = True)

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
    
plt.xticks([])   
plt.yticks([])    
plt.show()

#9.5)
n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
color = np.arctan2(y, x)

plt.scatter(x, y, s=75, c=color, alpha=0.5, cmap='viridis')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xticks([])   
plt.yticks([])   

plt.show()