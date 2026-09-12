from datetime import datetime

#10.1)
def vida_en_segundos(fecha_nac):
    hoy = datetime.now()
    delta_t = hoy - fecha_nac
    return delta_t.total_seconds()

print('viví',vida_en_segundos(datetime(2003, 5, 10, 17, 55)),'segundos')

