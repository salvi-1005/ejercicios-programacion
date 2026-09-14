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
    
    @property
    def ancho(self):
        return f"ancho: {self._ancho}"
    
    @ancho.setter
    def setAncho(self, valor):
        """Este es el SETTER de ancho (incluye validación de enteros positivos)"""
        if not isinstance(valor, (int, float)):
            raise TypeError("El ancho debe ser un número.")
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que cero.")
        self._ancho = valor
        
    @property
    def alto(self):
        return f"alto: {self._alto}"
    
    @alto.setter
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
    
    def __eq__(self, otro):
        return (
            isinstance(otro, Rectangulo)
            and self._ancho == otro._ancho
            and self._alto == otro._alto
        )
    def __hash__(self):
        return hash((self.ancho, self.alto))
    
    def __str__(self):
        return (f"Ancho: {self._ancho}, Alto: {self._alto}")
    def __repr__(self):
        return (f"Ancho: {self._ancho}, Alto: {self._alto}")


mi_rectangulo = Rectangulo(3, 7)
print(mi_rectangulo.ancho)       
print(mi_rectangulo.alto)       
print(mi_rectangulo.area())        
print(mi_rectangulo.perimetro())   

mi_rectangulo._ancho = 4
mi_rectangulo._alto = 8

print(mi_rectangulo.ancho)       
print(mi_rectangulo.alto)        
print(mi_rectangulo.area())        
print(mi_rectangulo.perimetro()) 

mi_rectangulo_2 = Rectangulo(4, 8)
print(mi_rectangulo == mi_rectangulo_2)

print(hash(mi_rectangulo))
print(hash(mi_rectangulo_2))

class Persona:
    cantidad = 0
    def __init__(self):
        Persona.cantidad += 1
    @classmethod
    def cantidad_personas(cls):
        return cls.cantidad
    
juan = Persona()
print(f"Cantidad de personas: {Persona.cantidad_personas()}")

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.actual < self.limite:
            self.actual += 1
            return self.actual
        else:
            raise StopIteration

contador = Contador(5)
for num in contador:
    print(num)
    
class Saludo:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def __call__(self, nombre):
        return f'{self.mensaje}, {nombre}!'

saludo = Saludo('Hola')

print(saludo('Juan'))  
print(saludo('Ana'))   


class CuentaBancaria:
    __slots__ = ['nombre', 'saldo'] 
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0
    def depositar(self, monto):
        self.saldo += monto
    def extraer(self, monto):
        if self.saldo - monto < 0:
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto
    def obtener_saldo(self):
        return self.saldo
    def __str__(self):
        return (f"Nombre: {self.nombre}, saldo: {self.saldo}")
    def __repr__(self):
        return f"CuentaBancaria(Nombre: {self.nombre!r}, saldo: {self.saldo!r})"
    
cuenta = CuentaBancaria("Balanz")
cuenta.depositar(100)
cuenta.extraer(10)
print(cuenta)
print(f"Saldo total: {cuenta.obtener_saldo()}")

class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas)/len(self.notas)
    def mejor_nota(self):
        maximo = self.notas[0]
        for elem in self.notas:
            if elem > maximo:
                maximo = elem
        return maximo
    def __len__(self):
        return len(self.notas)
    def __getitem__(self, index):
        return self.notas[index]
    def __setitem__(self, key, value):
        self.notas[key] = value
    def __str__(self):
        return (f"Nombre: {self.nombre} - Notas: {', '.join(str(nota) for nota in self.notas)}")
                
Salvador = Alumno('Salvador', [9.5,7,10,8.5,10])
print(f"Promedio de Salvador: {Salvador.promedio()}")
print(f"Mejor nota de Salvador: {Salvador.mejor_nota()}") 
print(f"Cantidad de notas de Salvador: {len(Salvador)}")

print(Salvador.notas[0])
Salvador.notas[2] = 6

print(f"Promedio de Salvador: {Salvador.promedio()}")

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):      
        self.nombre = nombre
    @abstractmethod
    def calcular_sueldo(self):
        pass
    
class Administrativo(Empleado):
    def __init__(self, nombre, horas_trabajadas):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
    def calcular_sueldo(self):
        return self.horas_trabajadas ** 2
    
class Vendedor(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad
    def calcular_sueldo(self):
        return self.edad * 10
    
class Gerente(Empleado):
    def __init__(self, nombre, años_de_aporte, carga_horaria_semanal):
        super().__init__(nombre)
        self.años_de_aporte = años_de_aporte
        self.carga_horaria_semanal = carga_horaria_semanal
    def calcular_sueldo(self):
        return self.años_de_aporte ** 2 + self.carga_horaria_semanal ** 2
   
administrativo = Administrativo('Alejandro', 1200)
vendedor = Vendedor('Carlos', 54)
gerente = Gerente('Emilio', 27, 30)

print(f"Sueldo de Alejandro: {administrativo.calcular_sueldo()}")
print(f"Sueldo de Carlos: {vendedor.calcular_sueldo()}")
print(f"Sueldo de Emilio: {gerente.calcular_sueldo()}")

import math

class Figura(ABC):
    def __init__(self, nombre):      
        self.nombre = nombre
    @abstractmethod
    def calcular_area(self):
        pass
    
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio**2
    
class Cuadrado(Figura):
    def __init__(self, nombre, alto):
        super().__init__(nombre)
        self.alto = alto
    def calcular_area(self):
        return self.alto ** 2
    
class Triangulo(Figura):
    def __init__(self, nombre, alto, ancho):
        super().__init__(nombre)
        self.alto = alto
        self.ancho = ancho
    def calcular_area(self):
        return (self.alto * self.ancho) / 2
   
circulo = Circulo('Circulo', 6)
cuadrado = Cuadrado('Cuadrado', 4)
triangulo = Triangulo('Triangulo', 5, 8)

print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Área del cuadrado: {cuadrado.calcular_area()}")
print(f"Área del triángulo: {triangulo.calcular_area()}")

class Operacion(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    @abstractmethod
    def evaluar(self):
        pass
class Suma(Operacion):
    def __init__(self, nombre, exp1, exp2):
        super().__init__(nombre)
        self._exp1 = exp1
        self._exp2 = exp2
    def evaluar(self):
        return self._exp1 + self._exp2

class Resta(Operacion):
    def __init__(self, nombre, exp1, exp2):
        super().__init__(nombre)
        self._exp1 = exp1
        self._exp2 = exp2
    def evaluar(self):
        return self._exp1 - self._exp2    

class Multiplicacion(Operacion):
    def __init__(self, nombre, exp1, exp2):
        super().__init__(nombre)
        self._exp1 = exp1
        self._exp2 = exp2
    def evaluar(self):
        return self._exp1 * self._exp2

class Division(Operacion):
    def __init__(self, nombre, exp1, exp2):
        super().__init__(nombre)
        self._exp1 = exp1
        self._exp2 = exp2
    def evaluar(self):
        return self._exp1 / self._exp2
    
suma = Suma('Suma', 5, 10)
resta = Resta('Resta', 16, 4)
multiplicacion = Multiplicacion('Multiplicación', 5, 10)
division = Division('Division', 16, 4)

print(f"Suma: {suma.evaluar()}")
print(f"Resta: {resta.evaluar()}")
print(f"Multiplicacion: {multiplicacion.evaluar()}")
print(f"División: {division.evaluar()}")

suma_1 = Suma('Suma 1', 5, 3).evaluar()
resta_1 = Resta('Resta 1', 8, 2).evaluar()
producto_1 = Multiplicacion('Producto 1', suma_1, resta_1)

print(f"(5+3)*(8-2) = {producto_1.evaluar()}")