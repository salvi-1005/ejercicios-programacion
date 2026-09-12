#Matriz unidimensional vertical

for i in range(1, 7):
    print (i)

#Matriz unidimensional horizontal

for i in range(1, 7):
    print (i, end = ' ')

print ('/n')

#Matriz bidimensional (6x6)

for i in range(1, 7):
    for j in range(1, 7):
        print (0, end = ' ')
    print('')

for i in range(1, 7):
    for j in range(1, 7):
        print (f'({i},{j})', end = ' ')
    print('')

#Colocar 1 en la diagonal

for i in range(1, 7):
    for j in range(1, 7):
        if (i==j):
            print (1, end = ' ')
        else:
            print (0, end = ' ')
    print('')

import numpy as np
c = 1 + 3
a = 7
b = a + 1
print('b=',b)
