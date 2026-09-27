def invertir_secuencia(s):
    if len(s) <= 1:
        return s
    return s[-1] + invertir_secuencia(s[1:-1]) + s[0]

s = "dangelo salvador"
#print(invertir_secuencia(s))

def suma_resta_alterna(l):
    if not l:
        return 0
    return resta_suma_alterna(l[:-1]) + l[-1] 
    
    
def resta_suma_alterna(l):
    if not l:
        return 0
    return suma_resta_alterna(l[:-1]) - l[-1]

s = [1,2,3,4,5,6]
print(suma_resta_alterna(s))
print(resta_suma_alterna(s))

n = 10
lista = [i for i in range(n, 0, -1)]

lista.pop(0)

print(lista)

class Yyy ():
    def __init__(self, x):
        self._x = x
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, v):
        self._x = v
        
zzz = Yyy(1)
print(zzz.x)
zzz.x = 2
print(zzz.x)

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
def quitar_personas(personas = list[Persona]):
    for persona in personas:
        personas.pop()
        print(persona.nombre)
        
claudia = Persona('Claudia')
jose = Persona('Jose')
personas = [claudia, jose]
quitar_personas(personas)
      