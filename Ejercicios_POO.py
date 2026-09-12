#53)

class Lamparita:
    def __init__(self):
        self.prendida = False
    def __prender__(self):
        self.prendida = True
    def __apagar__(self):
        self.prendida = False
    def __estado__(self):
        if self.prendida == True:
            return "Prendida"
        if self.prendida == False:
            return "Apagada"

lamparita = Lamparita()
print(lamparita.__estado__())

lamparita.__prender__()
print(lamparita.__estado__())

lamparita.__apagar__()
print(lamparita.__estado__())

#56)

class Monedero:
    def __init__(self, s):
        self.saldo = s
    def meter_dinero(self, dinero):
        self.saldo += dinero
    def sacar_dinero(self, dinero):
        if self.saldo - dinero >= 0:
            self.saldo -= dinero
        else:
            raise ValueError("No hay suficiente dinero en el monedero.")
    def consultar_dinero_disponible(self):
        return self.saldo
        
print("--------------------------------------------")

monedero = Monedero(100)
print(f"Dinero disponible: {monedero.consultar_dinero_disponible()}")

monedero.meter_dinero(50)
print(f"Dinero disponible: {monedero.consultar_dinero_disponible()}")

monedero.sacar_dinero(70)
print(f"Dinero disponible: {monedero.consultar_dinero_disponible()}")
        
#59)

class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock
    def actualizar_stock(self, stock_nuevo):
        if self.stock >= stock_nuevo:
            self.stock -= stock_nuevo
        else:
            print("No hay stock suficiente")
    def get_nombre(self):
        return self.nombre
    def get_precio_unitario(self):
        return self.precio_unitario
    def get_stock(self):
        return self.stock
    def __str__(self):
        return (f"Producto: {self.nombre} - Precio: {self.precio_unitario} - Stock: {self.stock}")
    
class Pedido:
    def __init__(self, ID, productos):
        self.ID = ID
        self.productos = productos
        self.estado = 'Sin iniciar'
    def costo_total(self):
        costo = 0
        for producto in self.productos:
            costo += (producto.get_precio_unitario() * producto.get_stock())
        return costo - (costo * 0.1)
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    def get_id(self):
        return self.ID
    def get_productos(self):
        return self.productos
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print("el producto {producto.get_nombre()} no está en la lista")
    def __str__(self):
        return (f"ID: {self.ID} - Productos: {', '.join(producto.__str__() for producto in self.productos)}")
    
print("--------------------------------------------")  
  
banana = Producto('Banana', 500, 3)
queso = Producto('Queso', 700, 5)
pedido = Pedido(234, [banana, queso])

print(banana)
print(f"Costo total del pedido: {pedido.costo_total()}")
print(f"pedido: {pedido}")
    
#64)

class Restaurante:
    total_sucursales = 0
    def __init__(self, nombre, ciudad, cant_empleados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.cant_empleados = cant_empleados
        Restaurante.total_sucursales += 1
    @classmethod
    def obtener_numero_sucursales(cls):
        return cls.total_sucursales
    @staticmethod
    def calcular_costo_operativo(empleado_promedio):
        return empleado_promedio * 2000

print("--------------------------------------------")
    
restaurante1 = Restaurante("Las Delicias Del Mar", "Buenos Aires", 15)
restaurante2 = Restaurante("Las Delicias Del Mar", "Mar Del Plata", 13)
restaurante3 = Restaurante("Las Delicias Del Mar", "Rosario", 17)

print(f"cantidad de sucursales: {restaurante3.obtener_numero_sucursales()}")
print(f"costo operativo: {restaurante3.calcular_costo_operativo(restaurante3.cant_empleados)}")

#66)

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def asignar_x(self, nuevo_x):
        self.x = nuevo_x
    def asignar_y(self, nuevo_y):
        self.y = nuevo_y
    def obtener_x(self):
        return self.x
    def obtener_y(self):
        return self.y
    def sumar_puntos(self, otro):
        self.x += otro.x
        self.y += otro.y
        return (self.x,self.y)
    def __eq__(self, otro):
        return (
            isinstance(otro, Punto)
            and self.x == otro.x
            and self.y == otro.y
        )
    
print("--------------------------------------------")

punto1 = Punto(3,4)

print(f"x: {punto1.obtener_x()}")
print(f"y: {punto1.obtener_y()}")

punto2 = Punto(4,5)

print(f"suma: {punto1.sumar_puntos(punto2)}")

punto3 = Punto(4,5)

print(punto1 == punto2)
print(punto2 == punto3)

#69)

class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    def __gt__(self, otro):
        if isinstance(otro, Fecha):
            if self.dia > otro.dia and self.mes == otro.mes and self.año == otro.año:
                return True
            if self.mes > otro.mes and self.año == otro.año:
                return True
            if self.año > otro.año:
                return True
            else:
                return False
        else:
            return False
    def __str__(self):
        return (f"fecha: {self.dia}/{self.mes}/{self.año}")
    
print("--------------------------------------------")
fecha1 = Fecha(10,5,2003)
fecha2 = Fecha(5,5,2005)

print(fecha1)
print(fecha1 < fecha2)

#72)

class Vehiculo:
    def __init__(self, marca, modelo, precioBase):
        self.marca = marca
        self.modelo = modelo
        self.precioBase = precioBase
    def calcular_costo_alquiler(self, dias):
        return self.precioBase * dias
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precioBase):
        super().__init__(marca, modelo, precioBase)
    def calcular_costo_alquiler(self, dias):
        return self.precioBase * dias + (self.precioBase * dias * 0.2)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, precioBase):
        super().__init__(marca, modelo, precioBase)
    def calcular_costo_alquiler(self, dias):
        return self.precioBase * dias - (self.precioBase * dias * 0.15)
        
print("--------------------------------------------")
    
vehiculo = Vehiculo('Nissan', 'Murano', 100000.0)
auto = Auto('Volkswagen', 'Tcross', 200000.0)
moto = Moto('Renault', 'Jeep', 150000.0)

print(f"Costo del vehículo: {vehiculo.calcular_costo_alquiler(15)}")
print(f"Costo del auto: {auto.calcular_costo_alquiler(15)}")
print(f"Costo de la moto: {moto.calcular_costo_alquiler(15)}")

#75)

#a)

class Trayecto:
    def __init__(self, origen, destino, distancia, cant_estaciones):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.cant_estaciones = cant_estaciones
    def get_origen(self):
        return self.origen
    def get_destino(self):
        return self.destino
    def get_distancia(self):
        return self.distancia
    def get_cant_estaciones(self):
        return self.cant_estaciones

from abc import ABC, abstractmethod
    
class TipoDeViaje(ABC):
    def __init__(self, trayecto, cant_vagones, cap_maxima, cant_pasajeros):
        if cant_pasajeros > cap_maxima:
            raise ValueError("No hay más luar en el tren")
        self.trayecto = trayecto
        self.cant_vagones = cant_vagones
        self.cap_maxima = cap_maxima
        self.cant_pasajeros = cant_pasajeros
    @abstractmethod
    def tiempo_de_demora(self):
        pass
class Diesel(TipoDeViaje):
    def __init__(self, trayecto, cant_vagones, cap_maxima, cant_pasajeros):
        super().__init__(trayecto, cant_vagones, cap_maxima, cant_pasajeros)
    def tiempo_de_demora(self):
        return (self.trayecto.get_distancia() * (self.trayecto.get_cant_estaciones()/2)) + ((self.trayecto.get_cant_estaciones() + self.cant_pasajeros/10))
    
class Electrico(TipoDeViaje):
    def __init__(self, trayecto, cant_vagones, cap_maxima, cant_pasajeros):
        super().__init__(trayecto, cant_vagones, cap_maxima, cant_pasajeros)
    def tiempo_de_demora(self):
        return self.trayecto.get_distancia() * (self.trayecto.get_cant_estaciones()/2)

class AltaVelocidad(TipoDeViaje):
    def __init__(self, trayecto, cant_vagones, cap_maxima, cant_pasajeros):
        super().__init__(trayecto, cant_vagones, cap_maxima, cant_pasajeros)
    def tiempo_de_demora(self):
        return self.trayecto.get_distancia()/10
    
class Viaje:
    def __init__(self, tipo_de_viaje):
        self.tipo_de_viaje = tipo_de_viaje
    def tiempo_de_demora(self):
        return self.tipo_de_viaje.tiempo_de_demora()
    
print("--------------------------------------------")
    
trayecto1 = Trayecto('Buenos Aires', 'Mar Del Plata', 400, 4)
trayecto2 = Trayecto('Cusco', 'Aguas Calientes', 100, 2)
trayecto3 = Trayecto('Londres', 'Edimburgo', 500, 6)

diesel = Diesel(trayecto1, 10, 200, 180)
electrico = Electrico(trayecto2, 12, 300, 290)
altaVelocidad = AltaVelocidad(trayecto3, 15, 500, 470)

viaje1 = Viaje(diesel)
viaje2 = Viaje(electrico)
viaje3 = Viaje(altaVelocidad)

print(f"tiempo promedio del diesel: {viaje1.tiempo_de_demora()}")
print(f"tiempo promedio del eléctrico: {viaje2.tiempo_de_demora()}")
print(f"tiempo promedio del de alta velocidad: {viaje3.tiempo_de_demora()}")

#b)
print("--------------------------------------------")
print(f"tiempo promedio del diesel: {diesel.tiempo_de_demora()}")
print(f"tiempo promedio del eléctrico: {electrico.tiempo_de_demora()}")
print(f"tiempo promedio del de alta velocidad: {altaVelocidad.tiempo_de_demora()}")

#82)

class Publicacion:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio
    def __str__(self):
        return (f"Título: {self.titulo}, Precio: {self.precio}")
    
class Libro(Publicacion):
    def __init__(self, titulo, precio, nro_de_paginas, año):
        super().__init__(titulo, precio)
        self.nro_de_paginas = nro_de_paginas
        self.año = año
    def __str__(self):
        return (f"Título: {self.titulo}, Precio: {self.precio}, Número de páginas: {self.nro_de_paginas}, Año de publicación: {self.año}")
        
class Disco(Publicacion):
    def __init__(self, titulo, precio, duracion):
        super().__init__(titulo, precio)
        self.duracion = duracion
    def __str__(self):
        return (f"Título: {self.titulo}, Precio: {self.precio}, Duración en minutos: {self.duracion}")
        
print("--------------------------------------------")

publicacion = Publicacion("La Odisea", 30000)
libro = Libro("El Señor De Los Anillos", 50000, 150, 2006)
disco = Disco("Caracachumba", 1000, 80)

print(publicacion)
print(libro)
print(disco)

#85)

class Automovil(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    @abstractmethod
    def otorgar_permiso(self, fecha):
        pass
    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}")
class AutoMediano(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.fecha_permiso = None
    def otorgar_permiso(self, fecha):
        self.fecha_permiso = fecha
        self.habilitado = True
        print(f"Permiso adquirido para {self.marca} {self.modelo} el {fecha}")
        
class Camion(Automovil):
    def __init__(self, marca, modelo, concesionaria):
        super().__init__(marca, modelo)
        self.concesionaria = concesionaria
        self.fecha_permiso = None
    def otorgar_permiso(self, fecha):
        if self.concesionaria.autorizado(self):
            self.fecha_permiso = fecha
            self.habilitado = True
            print(f"Permiso de camión {self.marca} {self.modelo} autorizado el {fecha}")
        else:
            raise ValueError("El camión no está autorizado")
        
class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.camiones_registrados = []
    def registrar_camion(self, camion):
        self.camiones_registrados.append(camion)
    def autorizado(self, camion):
        return camion in self.camiones_registrados
    
print("--------------------------------------------")
    
concesionaria = Concesionaria("Mercedes-Benz")
camion = Camion("Mercedes", "Actros", concesionaria)

concesionaria.registrar_camion(camion)
camion.otorgar_permiso("19/08/2026")

print(camion)

#88)

class ExpresionAritmetica(ABC):
    def __init__(self, valor):
        self.valor = valor
    @abstractmethod
    def operacion(self):
        pass
    
class Suma(ExpresionAritmetica):
    def __init__(self, exp1, exp2):
        self._exp1 = exp1
        self._exp2 = exp2
    def operacion(self):
        return self._exp1 + self._exp2

    
class Producto(ExpresionAritmetica):
    def __init__(self, exp1, exp2):
        self._exp1 = exp1
        self._exp2 = exp2
    def operacion(self):
        return self._exp1 * self._exp2

class Negacion(ExpresionAritmetica):
    def __init__(self, valor):
        super().__init__(valor)
    def operacion(self):
        return -self.valor
    
class Incrementar(ExpresionAritmetica):
    def __init__(self, valor):
        super().__init__(valor)
    def operacion(self):
        return self.valor + 1
    
class Decrementar(ExpresionAritmetica):
    def __init__(self, valor):
        super().__init__(valor)
    def operacion(self):
        return self.valor - 1
    
print("--------------------------------------------")
    
suma = Suma(5, 10)
producto = Producto(5, 10)
negacion = Negacion(4)
incrementar = Incrementar(7)
decrementar = Decrementar(7)

print(f"Suma: {suma.operacion()}")
print(f"Producto: {producto.operacion()}")
print(f"Negación: {negacion.operacion()}")
print(f"Incremento: {incrementar.operacion()}")
print(f"Decremento: {decrementar.operacion()}")

#96)

class Hora:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    def ver_hora(self):
        return (f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")
    @staticmethod
    def sumar_horas(hora1, hora2):
        nueva_hora = hora1.horas + hora2.horas
        nuevo_minutos = hora1.minutos + hora2.minutos
        nuevo_segundos = hora1.segundos + hora2.segundos
        if nueva_hora >= 24:
            nueva_hora -= 24
        if nuevo_minutos >= 60:
            nuevo_minutos -= 60
            nueva_hora += 1
        if nuevo_segundos >= 60:
            nuevo_segundos -= 60
            nuevo_minutos += 1
        return Hora(nueva_hora, nuevo_minutos, nuevo_segundos)
    def sumar_horas_2(self, otro):
        self.horas += otro.horas
        self.minutos += otro.minutos
        self.segundos += otro.segundos
        if self.horas >= 24:
            self.horas -= 24
        if self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
        if self.segundos >= 60:
            self.segundos -= 60
            self.minutos += 1
        
print("--------------------------------------------")
        
hora1 = Hora(18,54,0)
hora2 = Hora(3,7,0)
suma = hora1.sumar_horas(hora1, hora2)
hora1.sumar_horas_2(hora2)

print(f"Hora 1: {hora1.ver_hora()}")
print(f"Hora 2: {hora2.ver_hora()}")
print(f"Suma de horas: {suma.ver_hora()}")
print(f"suma de horas: {hora1.ver_hora()}")
    