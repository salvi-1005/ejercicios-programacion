
#%%Cola
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl:
      def __init__(self):
          '''Abre la pista'''
          self.arribos = Cola()
          self.partidas = Cola()
     
      def nuevo_arribo(self, avion):
          self.arribos.encolar(avion)

      def nueva_partida(self, avion):
          self.partidas.encolar(avion)
          
      def ver_estado(self):
        """Muestra el estado actual de las colas."""
        texto = "Vuelos esperando para aterrizar: "
        if self.arribos.esta_vacia():
            texto += "ninguno"
        else:
            texto += ', '.join(self.arribos.items)

        texto += "  Vuelos esperando para despegar: "
        if self.partidas.esta_vacia():
            texto += "ninguno"
        else:
            texto += ', '.join(self.partidas.items)
        return texto
      
      def asignar_pista(self):
        """Asigna la pista: prioridad a los arribos."""
        if not self.arribos.esta_vacia():
            avion = self.arribos.desencolar()
            return f"El vuelo {avion} aterrizó con éxito."
        elif not self.partidas.esta_vacia():
            avion = self.partidas.desencolar()
            return f"El vuelo {avion} despegó con éxito."
        else:
            return "No hay vuelos en espera."
      
torre = TorreDeControl()

#%%Pila

def f():
    x = 50
    a = 20
    print("En f, x vale", x)

def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)


class Pila:
    '''Representa a una pila, con operaciones de apilar y desapilar.
    El primero en ser apilado es el último en ser desapilado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def apilar(self, x):
        '''Apila el elemento x.'''
        self.items.append(x)

    def desapilar(self):
        '''Elimina el último elemento de la pila 
        y devuelve su valor. 
        Si la pila esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La pila esta vacia')
        return self.items.pop(-1)

    def esta_vacia(self):
        '''Devuelve 
        True si la pila esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")


pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)