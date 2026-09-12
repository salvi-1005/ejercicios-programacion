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
    
print('Total pagado', round(total_pagado, 2),'en', mes ,'meses')

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
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
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
    mes = mes + 1
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        pago = pago_mensual + pago_extra
    else:
        pago = pago_mensual
    if pago > saldo * (1+tasa/12):
        pago = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    print(mes, round(total_pagado, 2), round(saldo, 2))

#Total pagado: $878202.57 en 310 meses.