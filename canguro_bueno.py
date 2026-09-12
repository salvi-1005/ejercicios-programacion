#11.11)
class Canguro():
    def __init__(self, nombre, contenido=None):
        self.nombre = nombre
        if contenido is None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido
    def __str__(self):
        return f'({self.nombre}, {self.contenido_marsupio})'
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
    
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)
