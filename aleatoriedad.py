import random
from collections import Counter

random.seed(31415)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    primero = tirada[0]
    for dado in tirada:
        if dado != primero:
            return False
    return True
        
N = 100000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

def prob_generala_servida(N):
    contador = 0
    for i in range(N):
        tiro = tirar()
        if es_generala(tiro):
            contador = contador + 1
    return contador/N

def maxima_cara(tirada):
    return Counter(tirada).most_common()[0]

def todos_distintos(tirada):
    for i in range(5):
        for j in range(i + 1, 5):  
            if tirada[i] == tirada[j]:
                return False
    return True

def es_generala_no_necesariamente_servida(tirada):
    primer_tirada = tirada(5)
    if es_generala(primer_tirada):
        return True
    maxima_cara_primer_tirada, maxima_cantidad_primer_tirada = maxima_cara(primer_tirada)
    segunda_tirada = tirada(5 - maxima_cantidad_primer_tirada)
    segunda_tirada += [maxima_cara_primer_tirada] * maxima_cantidad_primer_tirada
    if es_generala(segunda_tirada):
        return True
    maxima_cara_segunda_tirada, maxima_cantidad_segunda_tirada = maxima_cara(segunda_tirada)
    tercer_tirada = tirada(5 - maxima_cantidad_segunda_tirada)
    tercer_tirada += [maxima_cara_segunda_tirada] * maxima_cantidad_segunda_tirada
    if es_generala(tercer_tirada):
        return True
    return False

def prob_generala_comun(N):
    contador = 0
    for i in range(N):
        tiro = tirar()
        if es_generala_no_necesariamente_servida(tiro):
            contador = contador + 1
    return contador/N

#%%Con reposición
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

print(random.choices(caras,k=5))

#%%Sin reposición
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

def repartir():
    mano = random.sample(naipes, 3)
    return mano

def es_envido(mano):
    for i in range(len(mano)):
        for j in range(len(mano)):
            if mano[i][1] == mano[j][1] and mano[i][0] > 4 and mano[j][0] > 4 and mano[i][0] < 8 and mano[j][0] < 8 and mano[i] != mano[j] and i != j:
                return True
    return False
        
exito = 0
n_manos = 13
for i in range(n_manos):
    mano = repartir()
    if es_envido(mano):
        exito += 1
    
prob_envido = exito/n_manos
print('probabilidad', prob_envido)

#%%Continuas
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
    promedio = sum(valor for valor in temp)/n
    ordenado = sorted(temp)
    if len(ordenado) % 2 == 0:
        mediana = (ordenado[len(ordenado)//2] + ordenado[len(ordenado)//2-1])/2
    else:
        mediana = ordenado[((len(ordenado)-1)//2)]
    return (max(temp), min(temp), promedio, mediana)  

def mediana(temp):
    d = sorted(temp)
    if len(d) % 2 == 0:
        mediana = (d[len(d)//2] + d[len(d)//2-1])/2
    else: 
        mediana = d[((len(d)-1)//2)]      
    return mediana

personas = ['Jorge']*30

#%%Cocumpleaños
def fechas_de_cumpleaños(personas):
    fechas_de_cumpleaños = []
    for persona in personas:
        cumpleaños = random.randint(1,365)
        fechas_de_cumpleaños.append(cumpleaños)
    return fechas_de_cumpleaños

fechas = fechas_de_cumpleaños(personas)

def hay_repetidos(fechas):
    for i in range(len(fechas)):
        for j in range(len(fechas)):
            if fechas[i] == fechas[j] and j!= i:
                return True
    return False
    
n = 1000

exitos = 0
for _ in range(n):
    fechas = fechas_de_cumpleaños(personas)
    if hay_repetidos(fechas):
        exitos += 1

prob_cump = exitos / n
print("Probabilidad:", prob_cump)

def generala_2(tirada):
    return max(tirada) == min(tirada)