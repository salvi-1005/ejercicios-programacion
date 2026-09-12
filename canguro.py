

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

class Rectangulo():
    def __init__(self, p1, p2):
        self.p1 = p1 
        self.p2 = p2 
    def base(self):
        return abs(self.p2.x - self.p1.x)
    def altura(self):
        return abs(self.p2.y - self.p1.y)
    def area(self):
        return self.base() * self.altura()
    def __str__(self):
        return f'({self.p1}, {self.p2})'
    def __repr__(self):
        return f'Rectangulo({self.p1}, {self.p2})'
    def desplazar(self, desplazamiento):
        self.p1 = self.p1 + desplazamiento
        self.p2 = self.p2 + desplazamiento
    def rotar(self):
        # Tomamos como pivote la esquina inferior derecha
        # Primero identificamos cuál es la esquina inferior derecha
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y

        # Coordenadas mínimas y máximas
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)

        # Esquina inferior derecha (pivote)
        pivote = Punto(xmax, ymin)
        base = self.base()
        altura = self.altura()

        # Al rotar 90° a la derecha: el ancho pasa a ser alto, y el alto pasa a ser ancho
        nuevo_p1 = pivote
        nuevo_p2 = Punto(pivote.x + altura, pivote.y + base)

        self.p1, self.p2 = nuevo_p1, nuevo_p2
    
#%%11.11)
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