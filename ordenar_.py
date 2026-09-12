import time

lista = [6,3,2,7,9,8,1,0,4,5]

def bubble_sort(lista): #Complejidad: O(n^2)
    i = 0
    ordenado = False
    while not ordenado:
        ordenado = True
        i = 0
        while i <= len(lista)-2:
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
                i += 1
            else:
                i += 1
    return lista

print(f"bubble sort: {bubble_sort(lista)}")

def bubble_sort_for(lista): #Complejidad: O(n^2)
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#print(f"bubble sort con for: {bubble_sort_for(lista)}")

def insertion_sort(lista):
    
    for i in range(1, len(lista)):
        clave = lista[i]  
        j = i - 1         
        
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
            
        lista[j + 1] = clave
        
    return lista

print(f"insertion sort: {insertion_sort(lista)}")

lista = [6,3,2,7,9,8,1,0,4,5,11,10]

def counting_sort(lista, lugar):
    
    output = [0] * len(lista)
    count = [0] * 10
    
    for i in range(0, len(lista)):
        count[(lista[i] // lugar) % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    i = len(lista)-1
    while i >= 0:
        output[count[(lista[i] // lugar) % 10] - 1] = lista[i]
        count[(lista[i] // lugar) % 10] -= 1
        i -= 1
    
    for i in range(0, len(lista)):
        lista[i] = output[i]
        
    return lista
        
def radix_sort(lista):
    
    maximo = max(lista)
    lugar = 1
    while maximo // lugar > 0:
        counting_sort(lista, lugar)
        lugar *= 10
    return lista
        
print(f"radix sort: {radix_sort(lista)}")   
        
lista = [6,3,2,7,9,8,1,0,4,5,11,10]

def rs(lista):
    #print("lista:",lista)
    res = []
    buckets = [0] * len(lista)
    
    for num in lista:
        buckets[num] += 1
    #print ("cats:",buckets)
        
    for i in range(len(lista)):
        for _ in range(buckets[i]):
            res.append(i)
    #print ("res:",res)
    return res

print(f"radix sort 2: {rs(lista)}") 

l = []

start = time.time()

#for _ in range(10000):
    
    #insertion_sort(lista)
    
end = time.time()

lista = [8,3,5,1]

def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Se divide recursivamente cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Proceso de mezcla (Merge)
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Si quedaron elementos sueltos en la izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedaron elementos sueltos en la derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            
    return lista
 
print(f"merge sort: {merge_sort(lista)}")