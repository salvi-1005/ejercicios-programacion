"""

Ejercicio 5

#Ejemplo de lista vuelos = [["Buenos Aires","Rosario"] , ["Cordoba","San Luis"] , ["Rosario","Cordoba"],
#                           ["Corrientes","Posadas"] , ["Usuahia","Mendoza"]]

def soloParteUnVUeloDeCadaCiudad(vuelos: list) -> bool:
  #Retorna True las ciudades de origen de los vuelos son todas diferentes

def soloLlegaUnVueloAcadaCuidad(vuelos: list) -> bool:
  #Retorna True las ciudades de destino de los vuelos son todas diferentes

def sinRepetidos(vuelos: list) -> bool:
  #Retorna True si en la lista no hay ningun vuelo repetido, es decir con las mismas
  #ciudades de origen y de destino

def vuelosValidos(ruta: list, vuelos: list) -> bool:
  #Retorna True si la ruta no tiene vuelos repetidos y esta completamente incluida en la lista de vuelos

def hayRuta(vuelos: list, origen: str, destino: str) -> bool:
  #Retorna True si hay una ruta posible dentro de los vuelos disponibles desde la ciudad de origen
  #hasta la ciudad de destino

def caminoDeVuelos(ruta: list) -> bool:
  #Retorna True si para cada vuelo en la ruta (par de ciudades) la ciudad de origen en el vuelo actual
  #es la misma que la ciudad de destino del vuelo anterior

def largoDeRuta(ruta: list, origen: str, destino: str, ) -> :

def sePuedeLlegar(vuelos: list, origen: str, destino: str) -> int:

"""

def soloParteUnVUeloDeCadaCiudad(vuelos):
    orígenes_distintos = True
    i = 0
    while orígenes_distintos and i < len(vuelos) - 1:
        j = i + 1
        while j < len(vuelos) and orígenes_distintos:
            if vuelos[j][0] == vuelos[i][0]:
                orígenes_distintos = False
            else:
                j += 1
        i += 1
    return orígenes_distintos

def soloLlegaUnVueloAcadaCuidad(vuelos):
    destinos_distintos = True
    i = 0
    while destinos_distintos and i < len(vuelos) - 1:
        j = i + 1
        while j < len(vuelos) and destinos_distintos:
            if vuelos[j][1] == vuelos[i][1]:
                destinos_distintos = False
            else:
                j += 1
        i += 1
    return destinos_distintos

def sinRepetidos(vuelos):
    no_hay_vuelos_repetidos = True
    i = 0
    while no_hay_vuelos_repetidos and i < len(vuelos) - 1:
        j = i + 1
        while no_hay_vuelos_repetidos and j < len(vuelos):
            if vuelos[i] == vuelos[j]:
                no_hay_vuelos_repetidos = False
            else:
                j += 1
        i += 1
    return no_hay_vuelos_repetidos

def hayRuta(vuelos, origen, destino):
    hay_ruta = False
    i = 0
    while not hay_ruta and i < len(vuelos):
        if vuelos[i][0] == origen and vuelos[i][1] == destino:
            hay_ruta = True
        else:
            i += 1
    return hay_ruta

def vuelosValidos(ruta, vuelos):
    vuelos_válidos = False
    if sinRepetidos(ruta):
        vuelos_válidos = True
        i = 0
        while i < len(ruta) and vuelos_válidos:
            if not hayRuta(vuelos, ruta[i][0], ruta[i][1]):
                vuelos_válidos = False
            else:
                i += 1
    return vuelos_válidos

def caminoDeVuelos(ruta):
    es_un_camino = True
    i = 0
    while i < len(ruta) - 1 and es_un_camino:  # comentario
        if ruta[i][1] != ruta[i + 1][0]:
            es_un_camino = False
        else:
            i += 1
    return es_un_camino

def largoDeRuta(ruta, origen, destino, vuelos, longCamino):
    return vuelosValidos(ruta, vuelos) and len(ruta) >= 1 and ruta[0][0] == origen and ruta[len(ruta) - 1][1] == destino and caminoDeVuelos(ruta) and len(ruta) == longCamino

def traducir(v:str):
    l = v.split(" ")
    r=[]
    for s in l:
        r.append(s.split(","))
    return r

sss = "misiones,jujuy salta,chubut rosario,misiones"


#v = [["Buenos Aires","Rosario"] , ["Cordoba","San Luis"] , ["Rosario","Cordoba"], ["Corrientes","Posadas"] , ["San Luis","Corrientes"]]
v = "BuenosAires,Rosario Cordoba,SanLuis Rosario,Cordoba Corrientes,Posadas SanLuis,Corrientes"
o = "BuenosAires"
d = "SanLuis"

def sePuedeLlegar (origen: str, destino: str, vue):

    vuelos = traducir(vue)
    #validar lista de vuelos
    if origen == destino: return -1   # verifica que origen y destino sean diferentes
    if not soloParteUnVUeloDeCadaCiudad(vuelos): return -1
    if not soloLlegaUnVueloAcadaCuidad(vuelos): return -1
    if not sinRepetidos(vuelos): return -1

    r = []
    desde = origen
    j = 0
    ruta_completa = False
    while not ruta_completa and j < len(vuelos):
        origen_coincide = False
        i = 0
    
        while not origen_coincide and i < len(vuelos):
            if vuelos[i][0] == desde:
                origen_coincide = True
            else:
                i += 1
    
        if origen_coincide: 
                r.append(vuelos[i]) 
        else: 
            break
        
        if vuelos[i][1] == destino:
            ruta_completa = True
        else:
            j += 1
        
        desde = vuelos[i][1]
    
    if not ruta_completa: r=-1

    return len(r)


print (sePuedeLlegar(o,d,v))

"""
print("¿Solo parte 1 vuelo de cada ciudad?", end = " ")
if soloParteUnVUeloDeCadaCiudad(vuelos):
    print("sí")
else:
    print("no")
print("¿Solo llega 1 vuelo a cada ciudad?", end = " ")
if soloLlegaUnVueloAcadaCuidad(vuelos):
    print("sí")
else:
    print("no")
print("¿No hay vuelos repetidos?", end = " ")
if sinRepetidos(vuelos):
    print("sí")
else:
    print("no")
print("¿Hay una ruta de Rosario a Buenos Aires?", end = " ")
if hayRuta(vuelos, "Rosario", "Buenos Aires"):
    print("sí")
else:
    print("no")
print("¿Hay una ruta de Cordoba a San Luis?", end = " ")
if hayRuta(vuelos, "Cordoba", "San Luis"):
    print("sí")
else:
    print("no")
print("La ruta [[\"Cordoba\",\"San Luis\"] , [\"Rosario\",\"Mendoza\"],[\"Corrientes\",\"Posadas\"]] ¿está en los vuelos?", end = " ")
if vuelosValidos([["Cordoba","San Luis"] , ["Rosario","Mendoza"],["Corrientes","Posadas"]], vuelos):
    print("sí")
else:
    print("no")
print("La ruta [[\"Cordoba\",\"San Luis\"] , [\"San Luis\",\"Mendoza\"],[\"Corrientes\",\"Posadas\"]] ¿es un camino?", end = " ")
if caminoDeVuelos([["Cordoba","San Luis"] , ["San Luis","Mendoza"],["Corrientes","Posadas"]]):
    print("sí")
else:
    print("no")
print("La ruta [[\"Cordoba\",\"San Luis\"] , [\"San Luis\",\"Mendoza\"],[\"Mendoza\",\"Posadas\"]] ¿es un camino?", end = " ")
if caminoDeVuelos([["Cordoba","San Luis"] , ["San Luis","Mendoza"],["Mendoza","Posadas"]]):
    print("sí")
else:
    print("no")
print("La ruta [[\"Cordoba\",\"San Luis\"] , [\"San Luis\",\"Mendoza\"],[\"Mendoza\",\"Posadas\"]] ¿es válida para viajar de Córdoba a Posadas haciendo 3 vuelos?", end = " ")
if largoDeRuta([["Cordoba","San Luis"] , ["San Luis","Mendoza"],["Mendoza","Posadas"]], "Córdoba", "Posadas", vuelos, 3):
    print("sí")
else:
    print("no")
print("La ruta [[\"Buenos Aires\",\"Rosario\"], [\"Rosario\",\"Cordoba\"], [\"Cordoba\",\"San Luis\"]] ¿es válida para viajar de Buenos Aires a San Luis haciendo 3 vuelos?", end = " ")
if largoDeRuta([["Buenos Aires","Rosario"], ["Rosario","Cordoba"], ["Cordoba","San Luis"]], "Buenos Aires", "San Luis", vuelos, 3):
    print("sí")
else:
    print("no")
print("La ruta [[\"Buenos Aires\",\"Rosario\"], [\"Rosario\",\"Cordoba\"], [\"Cordoba\",\"San Luis\"]] ¿es válida para viajar de Buenos Aires a San Luis haciendo 2 vuelos?", end = " ")
if largoDeRuta([["Buenos Aires","Rosario"], ["Rosario","Cordoba"], ["Cordoba","San Luis"]], "Buenos Aires", "San Luis", vuelos, 2):
    print("sí")
else:
    print("no")
print("La ruta [] ¿es válida para viajar de Buenos Aires a San Luis haciendo 2 vuelos?", end = " ")
if largoDeRuta([], "Buenos Aires", "San Luis", vuelos, 2):
    print("sí")
else:
    print("no")

"""