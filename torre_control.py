#11.12)
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

