import numpy as np
import keyword
import math
keyword.kwlist

altura_obelisco = 102
dia = 1
pila_billetes = 1
while (pila_billetes < altura_obelisco):
    pila_billetes = pila_billetes*2
    dia = dia + 1
    print(dia, pila_billetes)
    
altura_pelota = 100
i = 0
while i < 10:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 1))
    
def saludo(nombre):
    print('hola', nombre)

a = 2.1 + 4.2

#1.8)
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

adelanto = 1000
mes = 0
 
while saldo > 0:
    mes = mes + 1
    if mes <= 12:
        pago = pago_mensual + adelanto
    else:
       pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago 
    total_pagado = total_pagado + pago 
    
print('Total pagado', round(total_pagado, 2), mes)

#1.9)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= 60) and (mes <= 108):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    mes = mes + 1
    
print('Total pagado', round(total_pagado, 2), mes)

#1.10)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= 61) and (mes <= 108):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    print(mes, round(total_pagado, 2), round(saldo, 2))
    mes = mes + 1
    
#1.11)
mes = 0   
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    if pago > saldo * (1+tasa/12):
        pago = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    print(mes, round(total_pagado, 2), round(saldo, 2))
    mes = mes + 1    
        
#1.13)
def esfera(r):
    return (4/3)*(math.pi)*(r**3)

a = 'basavareddy'
b = a [-1:]
a.strip()
c = a.replace('basavareddy','monfils')

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

cadena = "Ejemplo con for"
for c in cadena:
    print('caracter:', c)
# Mirá el output.

cadena = "Ejemplo con for"

def contar_letras(cadenas:str):
    contador = 0
    for c in cadenas:
        if c == "o":
            contador += 1 
    print(contador)
    
tenistas = ['alcaraz', 'sinner']

frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera,Banana'
lista_frutas = frutas.split(',')
compra = []

for s in lista_frutas:
    print('s =', s)