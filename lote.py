class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    def costo(self):
        return self.cajones*self.precio 
    def vender(self, cant_cajones):
        self.cajones -= cant_cajones
        

a = Lote('Pera', 100, 490.10)

b = Lote('Manzana', 50, 122.34)
c = Lote('Naranja', 75, 91.75)
print(b.cajones * b.precio)
print(c.cajones * c.precio)

lotes = [a, b, c]

for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
     
import fileparse

camion_dicts = fileparse.parse_csv_tipos(r"C:\Users\SD\Downloads\camion.csv", select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]


print(sum([c.costo() for c in camion]))

import informe_final_final

camion_2 = informe_final_final.leer_camion(r"C:\Users\SD\Downloads\camion.csv")