#17)

def sierpinski(n):
    if n == 0:
        return ["*"]

    anterior = sierpinski(n - 1)
    ancho = len(anterior[-1])

    arriba = [
        " " * ((ancho + 1) // 2) + fila +
        " " * ((ancho + 1) // 2)
        for fila in anterior
    ]

    abajo = [
        fila + " " + fila
        for fila in anterior
    ]

    return arriba + abajo


for linea in sierpinski(4):
    print(linea)
    
#18)
    
import turtle

#Curva de Koch

def curvas(longitud, nivel, t):
    if nivel == 0:
        t.forward(longitud)
    else:
        longitud_tercio = longitud / 3
        curvas(longitud_tercio, nivel - 1, t)
        t.left(60)
        curvas(longitud_tercio, nivel - 1, t)
        t.right(120)
        curvas(longitud_tercio, nivel - 1, t)
        t.left(60)
        curvas(longitud_tercio, nivel - 1, t)

#19) 
#Copo de nieve de Koch (usa la curva 3 veces)

def copos(longitud, nivel, t):
    for _ in range(3):
        curvas(longitud, nivel, t)
        t.right(120)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
# Dibujar el copo completo de 4 niveles
copos(300, 4, t)
turtle.done()

#20)

def haches(x, y, longitud, nivel, t):
    if nivel == 0:
        return
    
    # Calcular extremos de la H actual
    x_izq, x_der = x - longitud / 2, x + longitud / 2
    y_sup, y_inf = y + longitud / 2, y - longitud / 2
    
    # Dibujar la H
    t.penup()
    t.goto(x_izq, y)  # Línea central
    t.pendown()
    t.goto(x_der, y)
    
    t.penup()
    t.goto(x_izq, y_sup)  # Barra izquierda
    t.pendown()
    t.goto(x_izq, y_inf)
    
    t.penup()
    t.goto(x_der, y_sup)  # Barra derecha
    t.pendown()
    t.goto(x_der, y_inf)
    
    # Siguiente nivel en las 4 esquinas
    nueva_longitud = longitud / 2
    haches(x_izq, y_sup, nueva_longitud, nivel - 1, t)
    haches(x_izq, y_inf, nueva_longitud, nivel - 1, t)
    haches(x_der, y_sup, nueva_longitud, nivel - 1, t)
    haches(x_der, y_inf, nueva_longitud, nivel - 1, t)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
haches(0, 0, 150, 4, t)
turtle.done()

#21)

def dibujar_cuadrado(x, y, lado, t):
    t.penup()
    t.goto(x - lado/2, y - lado/2)
    t.pendown()
    for _ in range(4):
        t.forward(lado)
        t.left(90)

def cuadrados(x, y, lado, nivel, t):
    if nivel == 0:
        return
    
    # Dibujar el cuadrado del nivel actual
    dibujar_cuadrado(x, y, lado, t)
    
    # Esquinas para el próximo nivel recursivo
    desplazamiento = lado / 2
    nuevo_lado = lado * 0.4  # Proporción aproximada según la imagen de la guía
    
    cuadrados(x - desplazamiento, y - desplazamiento, nuevo_lado, nivel - 1, t)
    cuadrados(x + desplazamiento, y - desplazamiento, nuevo_lado, nivel - 1, t)
    cuadrados(x - desplazamiento, y + desplazamiento, nuevo_lado, nivel - 1, t)
    cuadrados(x + desplazamiento, y + desplazamiento, nuevo_lado, nivel - 1, t)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
cuadrados(0, 0, 120, 4, t)
turtle.done()

#22)

def dibujar_rombo(x, y, diagonal, t):
    t.penup()
    t.goto(x, y - diagonal / 2)
    t.pendown()
    t.setheading(45) # Rotar para dibujar el rombo
    for _ in range(4):
        # El lado de un rombo a partir de su diagonal
        t.forward((diagonal / 2) * (2 ** 0.5)) 
        t.left(90)
    t.setheading(0) # Restablecer orientación

def rombos(x, y, diagonal, nivel, t):
    if nivel == 0:
        return
    
    dibujar_rombo(x, y, diagonal, t)
    
    desplazamiento = diagonal / 2
    nueva_diagonal = diagonal * 0.4
    
    # Ramificación recursiva en los 4 vértices del rombo
    rombos(x, y - desplazamiento, nueva_diagonal, nivel - 1, t)
    rombos(x, y + desplazamiento, nueva_diagonal, nivel - 1, t)
    rombos(x - desplazamiento, y, nueva_diagonal, nivel - 1, t)
    rombos(x + desplazamiento, y, nueva_diagonal, nivel - 1, t)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
rombos(0, 0, 150, 4, t)
turtle.done()

#23)

def hilbert(nivel, angulo, longitud, t):
    if nivel == 0:
        return

    t.right(angulo)
    hilbert(nivel - 1, -angulo, longitud, t)
    
    t.forward(longitud)
    t.left(angulo)
    hilbert(nivel - 1, angulo, longitud, t)
    
    t.forward(longitud)
    hilbert(nivel - 1, angulo, longitud, t)
    
    t.left(angulo)
    t.forward(longitud)
    hilbert(nivel - 1, -angulo, longitud, t)
    t.right(angulo)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
# Nivel 4, ángulo de giro de 90° y distancia por tramo corta
hilbert(4, 90, 10, t)
turtle.done()

#24)

def medio_sierpinski(nivel, longitud, t):
    if nivel == 0:
        t.forward(longitud)
        return
    medio_sierpinski(nivel - 1, longitud, t)
    t.left(45)
    t.forward(longitud * (2 ** 0.5))
    t.left(45)
    medio_sierpinski(nivel - 1, longitud, t)

def curvasierpinski(nivel, longitud, t):
    # Enlaza cuatro segmentos recursivos idénticos para cerrar el diseño
    for _ in range(4):
        medio_sierpinski(nivel, longitud, t)
        t.right(90)

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
curvasierpinski(3, 5, t) # 3 niveles de recursión según indica la consigna
turtle.done()

