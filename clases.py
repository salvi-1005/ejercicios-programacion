class Perro:
    # El constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza      # Atributo de instancia

    # Un método de la clase
    def ladrar(self):
        return f"{self.nombre} dice: Guau!"

# Instanciar (crear) un objeto a partir de la clase
mi_perro = Perro("Rex", "Golden Retriever")

# Acceder a los atributos y métodos
print(mi_perro.raza)      # Imprime: Golden Retriever
print(mi_perro.ladrar())  # Imprime: Rex dice: Guau!

class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho  
        self._alto = alto    
        
    def ancho(self):
        return f"ancho: {self._ancho}"
    
    def setAncho(self, valor):
        """Este es el SETTER de ancho (incluye validación de enteros positivos)"""
        if not isinstance(valor, (int, float)):
            raise TypeError("El ancho debe ser un número.")
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que cero.")
        self._ancho = valor
        
    def alto(self):
        return f"alto: {self._alto}"
    
    def setAlto(self, valor):
        """Este es el SETTER de alto"""
        if not isinstance(valor, (int, float)):
            raise TypeError("El alto debe ser un número.")
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que cero.")
        self._alto = valor
        
    def area(self):
        return f"area: {self._ancho * self._alto}"
        
    def perimetro(self):
        return f"perimetro: {(self._ancho * 2) + (self._alto * 2)}"


mi_rectangulo = Rectangulo(3, 7)
print(mi_rectangulo.ancho())       
print(mi_rectangulo.alto())        
print(mi_rectangulo.area())        
print(mi_rectangulo.perimetro())   

mi_rectangulo.setAncho(4)
mi_rectangulo.setAlto(8)

print(mi_rectangulo.ancho())       
print(mi_rectangulo.alto())        
print(mi_rectangulo.area())        
print(mi_rectangulo.perimetro()) 



