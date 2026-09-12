import random
import numpy as np

random.seed(31415)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

print(random.choices(caras,k=5))

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

print(random.shuffle(naipes))
print(random.sample(naipes,k=40))

n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')
print(random.random())

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def estimar_pi():
    todos_los_puntos = [generar_punto() for i in range(100000)]
    dentro_del_circulo = []
    for punto in todos_los_puntos:
        if ((punto[0]**2) + (punto[1]**2)) < 1:
            dentro_del_circulo.append(punto)
    return (len(dentro_del_circulo)/len(todos_los_puntos))*4

print(estimar_pi())

for i in range(6):
        print(f'{random.normalvariate(0,1):.2f}', end=', ')
        
def medir_temp(n):
    temperaturas = []
    for i in range(n):
        temperaturas.append(random.normalvariate(37.5,0.2))
    return temperaturas

def resumen_temp(n):
    temp = medir_temp(n)
    promedio = sum(valor for valor in temp)//n
    if len(sorted(temp)) % 2 == 0:
        mediana = (sorted(temp)[len(sorted(temp))//2] + sorted(temp)[(len(sorted(temp))//2-1)])/2
    else:
        mediana = sorted(temp)[((len(sorted(temp))-1)//2)]
    return (max(temp), min(temp), promedio, mediana)  

def mediana(temp):
    d = sorted(temp)
    if len(d) % 2 == 0:
        mediana = (d[len(d)//2] + d[len(d)//2-1])/2
    else:
        mediana = d[((len(d)-1)//2)]      
    return mediana


