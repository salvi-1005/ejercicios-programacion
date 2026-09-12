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

#6.1)
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

#6.2)
def prob_generala_comun(N):
    contador = 0
    for i in range(N):
        tiro = tirar()
        if es_generala_no_necesariamente_servida(tiro):
            contador = contador + 1
    return contador/N