#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:30:58 2024

@author: Estudiante
"""
import numpy as np

np.finfo(float).max

eps = np.finfo(np.double).eps
print('1 + ε =', 1 + eps)
print('1 + ε/2 =', 1 + eps/2,'\n')
print('¿1 + ε = 1?', 1 + eps == 1)
print('¿1 + ε/2 = 1?', 1 + eps/2 == 1)

print(0.1)
print(f"{np.single(0.1):.17f}")

print(f"0.1 + 0.2 = {0.1:.17f} + {0.2:.17f} = {0.1+0.2:.17f}")
print(f"0.3 = {0.3:.17f}")

np.frexp(np.single(0.1))
np.allclose(0.3,0.2+0.1)

mantissa, exp = np.frexp(np.single(0.1))
mantissa * 2.**exp

mantissa_maquina = mantissa*(2**24)

f"{int(mantissa_maquina):b}" 
mantissa_guardada = 110011001100110011001101

np.float16 
np.nextafter(np.float16(1024),np.float16(2000))

x = np.float16(2048)
y = np.float16(1)
print(f'{x} + {y} = {x + y}')
print(x + y == x)

#1)

n = 7
s1 = np.float32(0)
for i in range(1, 10**n + 1):
    s1 += np.float32(1) / np.float32(i)
print("Suma 1 = ", s1)
    
s2 = np.float32(0)
for i in range(1, 2 * 10**n + 1):
    s2 += np.float32(1) / np.float32(i)
print("Suma 2 = ", s2)
 
#2)    

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(np.exp(1))
s = np.float32(0)
for i in range(11):
    s += np.float32(1) / factorial(i)
print('Suma:', s)
print('Valor real de e:', np.exp(1))

#3)

print(10**8)

c = np.float64(0)

for i in range(10**8):
    c += np.float64(1)

print(c)

