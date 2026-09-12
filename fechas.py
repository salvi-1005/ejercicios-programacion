import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)

fecha = datetime.date.today()
print(fecha)

d = datetime.date(2019, 4, 13)
print(d)

from datetime import date

timestamp = date.fromtimestamp(1760844364)
print('Fecha =', timestamp)

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes

from datetime import time

a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)

b = time(11, 34, 56)
print('b =', b)

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

d = time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
print('d =', d)

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)

from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)

from datetime import timedelta

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print('t3 =', t3)

t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())

now = datetime.now()

t = now.strftime('%H:%M:%S')
print('hora:', t)

s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
# en formato mm/dd/YY H:M:S
print('s1:', s1)

s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
# en formato dd/mm/YY H:M:S
print('s2:', s2)

from datetime import datetime

cadena_con_fecha= '21 September, 2021'
date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object =', date_object)


ahora = datetime.now()
print(ahora.year)   # Año
print(ahora.month)  # Mes
print(ahora.day)    # Día
print(ahora.hour)   # Hora
print(ahora.minute) # Minuto
print(ahora.second) # Segundo