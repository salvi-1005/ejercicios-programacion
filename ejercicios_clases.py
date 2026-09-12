def cant_digitos(n):
   if n < 10:
      return 1
   return 1 + cant_digitos(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Cantidad de dígitos de {n}: {cant_digitos(n)}")

def reversa_num(n):
    if n < 10:
        return n
    return (n % 10) * (10**(cant_digitos(n)-1)) + reversa_num(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Reversa de {n}: {reversa_num(n)}")

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print("------------------------------------------------------")
n = 543
print(f"Suma de dígitos de {n}: {suma_digitos(n)}")

def reversa_y_suma(n):
    if n < 10:
        return (n, n)
    return ((n % 10) * (10**(cant_digitos(n)-1)) + reversa_num(n // 10), (n % 10) + suma_digitos(n // 10))

print("------------------------------------------------------")
n = 543
print(f"Reversa y suma de dígitos de {n}: {reversa_y_suma(n)}")

def doble(n):
    num_s = str(n)
    if len(num_s) == 0:
        return '', 0
    reverso, suma = doble(num_s[1:])
    
    return reverso + num_s[0], int(num_s[0]) + suma

n = 543
print(f"Reversa y suma de dígitos de {n}: {doble(n)}")

def desde_hasta(a,b):
    if a > b:
        return []
    return [a] + desde_hasta(a+1, b)
print("------------------------------------------------------")
a = 1
b = 5
print(f"Números desde {a} hasta {b}: {desde_hasta(a,b)}")

def agregar(lista, e):
    return lista, lista + [e]

print(agregar([1,2,3], 4))

def partes(lista):
    if not lista:
        return [list()]
    primero = lista[0]
    nueva_lista = []
    for elem in partes(lista[1:]):
        nueva_lista.append([primero] + elem)
    return partes(lista[1:]) + nueva_lista

lista = ['A','B','C','D','E']
print(partes(lista))

def partes_iterativo(cadena):
  resultado = [list()]
  for elemento in cadena:
    nuevos = [sub + [elemento] for sub in resultado]
    resultado.extend(nuevos)
  return resultado

lista = ['A','B','C','D','E']
print(partes_iterativo(lista))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    