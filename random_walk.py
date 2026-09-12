import numpy as np
import matplotlib.pyplot as plt

#9.2)
def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)    
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

