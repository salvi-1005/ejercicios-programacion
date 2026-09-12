import sys

#%%Con linea de comandos
print('Con línea de comandos:')
altura_pelota = 50
i = 0
if len(sys.argv) == 2:
    altura_pelota = float(sys.argv[1])
while i < 5:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 2))

print('--------')

#%%Importando el módulo "rebotes" del ejercicio 3.10)

import rebote3_10 as rb

print('Importando módulo rebotes:')
rb.rebotar(50, 5)