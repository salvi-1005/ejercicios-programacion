from datetime import date
from datetime import timedelta
from datetime import datetime

#10.1)
def vida_en_segundos(fecha_nac):
    hoy = date.today()
    delta_t = hoy - fecha_nac
    return delta_t.total_seconds()

print('viví',vida_en_segundos(date(year = 2003, month = 5, day = 10)),'segundos')

#10.2)
def cuanto_falta_para_la_primavera():
    hoy = date.today()
    primavera = date(year = 2026, month = 9, day = 21)
    delta_t = primavera - hoy 
    return delta_t.days

print('faltan',cuanto_falta_para_la_primavera(),'días para la primavera')

#10.3)
def fecha_de_reincorporacion():
    inicio = date(year = 2020, month = 9, day = 26)
    dias = timedelta(days = 200)
    return inicio + dias
    
dia = fecha_de_reincorporacion().day
mes = fecha_de_reincorporacion().month
año = fecha_de_reincorporacion().year

print('me reincorporo al trabajo el',dia,'/',mes,'/',año)

#10.4)
def dias_habiles(inicio, fin, feriados):
    inicio = datetime.strptime(inicio, '%d/%m/%Y').date()
    fin = datetime.strptime(fin, '%d/%m/%Y').date()
    feriados = [datetime.strptime(f, '%d/%m/%Y').date() for f in feriados]
    fechas = []
    días_de_la_semana = [0,1,2,3,4]
    fecha = inicio
    while fecha <= fin:
        if fecha.weekday() in días_de_la_semana and fecha not in feriados:
            fechas.append(fecha)
        fecha += timedelta(days=1)
    return fechas
           
inicio = '10/10/2020'
fin = '31/12/2020'
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

print(dias_habiles(inicio, fin, feriados))