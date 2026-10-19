from functools import reduce

class ArbolN:
    def __init__(self, empleado, subordinados=None):
        self.empleado = empleado
        if subordinados is None:
            self.subordinados = []
        else:
            self.subordinados = subordinados

    @property 
    def dato(self): 
        return self.empleado 

    @dato.setter 
    def dato(self, valor): 
        self.empleado = valor 
    
    @property 
    def subarboles(self):
        return self.subordinados 
    
    @subarboles.setter 
    def subarboles(self, subarboles):
        self.subordinados = subarboles
        
    def es_hoja(self) -> bool:    
        return self.subordinados == []
    
    def _altura_funcional(self, nodo):
        if nodo.es_hoja():
            return 0
        return 1 + reduce(max, [self._altura_funcional(s) for s in nodo.subordinados])
    
    def altura_recursion_multiple(self) -> int: 
        if self.es_hoja(): 
            return 1 
        else: 
            return 1 + max([subarbol.altura() for subarbol in self.subordinados])
        
    def altura_bucle(self) -> int:        
        altura_actual = 0 
        for subarbol in self.subordinados:            
            altura_actual = max (altura_actual, subarbol.altura()) 
        return altura_actual + 1
    
    def altura(self) ->  int:
        def altura_n(bosque) -> int: 
            if not bosque: 
                return 0 
            else: 
                return max(bosque[0].altura(), altura_n(bosque[1:])) 
        return 1 + altura_n(self.subordinados)
    
    def altura_rec(self):
        return self._altura(self)

    def _altura(self, nodo):
        if nodo.es_hoja():
            return 0
        return 1 + self._max_altura(nodo.subordinados, 0)
    
    def cantidad_nodos(self):
        return self._cantidad_nodos(self)

    def _cantidad_nodos(self, nodo):
        if nodo.es_hoja():
            return 1
        return 1 + self._sumar_nodos(nodo.subordinados, 0)

    def _sumar_nodos(self, subarboles, i):
        if i == len(subarboles):
            return 0
        return (self._cantidad_nodos(subarboles[i]) + self._sumar_nodos(subarboles,i + 1))
    
    def _max_altura(self, lista_subarboles, i):
        if i == len(lista_subarboles) - 1:
            return self._altura(lista_subarboles[i])
        altura_actual = self._altura(lista_subarboles[i])
        altura_resto = self._max_altura(lista_subarboles, i + 1)
        return max(altura_actual, altura_resto)
    
    def preorder_funcional(self):
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.preorder(), \
                      self.subordinados, [self.empleado])
    
    def preorder_imperativo(self):    
        recorrido = [self.empleado] 
        for subarbol in self.subordinados:        
            recorrido += subarbol.preorder() 
        return recorrido
    
    def preorder(self): 
        def preorder_n(bosque): 
            if not bosque: 
                return [] 
            else: 
                return bosque[0].preorder() + preorder_n(bosque[1:])
        return [self.empleado] + preorder_n(self.subordinados)
        
    def inorder(self):
        if self.es_hoja():
            return [self.empleado]
        return (self.subordinados[0].inorder() + [self.empleado] + \
                self._inorder_resto(self.subordinados,1))

    def _inorder_resto(self, bosque, i):
        if i >= len(bosque):
            return []
        return (bosque[i].inorder() + self._inorder_resto(bosque, i + 1))
    
    def postorder_funcional(self):
        return reduce(lambda recorrido, subarbol: recorrido + \
                      subarbol.postorden(), self.subordinados, [self.empleado])
            
    def inorder_imperativo(self):
        recorrido = []
        if self.subordinados:
            recorrido += (self.subordinados[0].inorder_imperativo())
        recorrido.append(self.empleado)
        for subarbol in self.subordinados[1:]:
            recorrido += (subarbol.inorder_imperativo())
        return recorrido
    
    def inorder_funcional(self):
        if not self.subordinados:
            return [self.empleado]
        primero = (self.subordinados[0].inorder_funcional())
        resto = reduce(lambda rec, sub: rec + sub.inorder_funcional(), self.subordinados[1:], [])
        return (primero + [self.empleado] + resto)
    
    def postorder_imperativo(self):    
        recorrido = [self.empleado] 
        for subarbol in self.subordinados:        
            recorrido += subarbol.postorder() 
        return recorrido
    
    def postorder(self): 
        def postorder_n(bosque): 
            if not bosque: 
                return [] 
            else: 
                return bosque[0].postorder() + postorder_n(bosque[1:]) 
        return postorder_n(self.subordinados) + [self.empleado]
        
    def nivel(self, dato, niv=0):
        if self.empleado == dato:
            return niv
        for subarbol in self.subordinados:
            resultado = subarbol.nivel(dato, niv+1)
            if resultado is not None:
                return resultado
        return None  
    
    def copiar(self):
        copia = ArbolN(self.empleado)
        copia.subordinados = [subarbol.copiar() for subarbol in self.subordinados]
        return copia
    
    def __str__(self):
        return f"Preorden: {str(self.preorder())}, Postorden: {str(self.postorder())}, \
            Inorden: {str(self.inorder())}"
    
    def sin_hojas(self):
        if self.es_hoja():
            return None
        copia = ArbolN(self.empleado)
        copia.subordinados = [subarbol.sin_hojas() \
                    for subarbol in self.subordinados if not subarbol.es_hoja()]
        return copia
    
    def ramas(self):
        if self.es_hoja():
            return [[self.empleado]]
        resultado = []
        for subarbol in self.subordinados:
            for rama in subarbol.ramas():
                resultado.append([self.empleado] + rama)
        return resultado
    
    def contiene(self, valor):
        if self.empleado == valor:
            return True
        return any(subarbol.contiene(valor) for subarbol in self.subordinados)
    
    def antecesores(self, valor):
        if self.empleado == valor:
            return None
        copia = ArbolN(self.empleado)
        copia.subordinados = []
        for subarbol in self.subordinados:
            if subarbol.contiene(valor):
                resultado = subarbol.antecesores(valor)
                if resultado is not None:
                    copia.subordinados.append(resultado)
        return copia
    
    def recorrido_guiado(self, direcciones):
        if not direcciones:
            return self.empleado
        indice = direcciones[0]
        if indice >= len(self.subordinados):
            raise IndexError("Movimiento inválido")
        return self.subordinados[indice].recorrido_guiado(direcciones[1:])

from abc import ABC, abstractmethod

class Organigrama(ArbolN):
    def __init__(self, empleado, subordinados):
        super().__init__(empleado, subordinados)
    def es_valido(self, jefe=None):
        if jefe is None:
            if not isinstance(self.empleado, DirectorGeneral):
                return False
        if not self.empleado._es_valido():
            return False
        if isinstance(self.empleado, Pasante):
            if not isinstance(jefe, Senior):
                return False
        if isinstance(self.empleado, LiderTecnicx):
            if not isinstance(jefe, DirectorIT):
                return False
        if isinstance(self.empleado, Desarrollador):
            if not isinstance(jefe, LiderTecnicx):
                return False
        if isinstance(self.empleado,(DirectorIT, DirectorFinanzas, DirectorRecursosHumanos)):
            if not isinstance(jefe, DirectorGeneral):
                return False
        return self._validar_hijos(self.subordinados, self.empleado)
    def _validar_hijos(self, subordinados, jefe):
        if subordinados == []:
            return True
        return (subordinados[0].es_valido(jefe) and self._validar_hijos(subordinados[1:], jefe))
    def calcular_sueldo_total(self):
        return self._calcular_sueldo_total(self)
    def _calcular_sueldo_total(self, nodo):
        return (nodo.empleado.calcular_sueldo() + self._sumar_nodos(nodo.subordinados,0))
    def _sumar_nodos(self, subordinados, i):
        if i == len(subordinados):
            return 0
        return (subordinados[i].calcular_sueldo_total() + self._sumar_nodos(subordinados, i + 1))
    def calcular_sueldo_total2(self):
        return self._calcular_sueldo_total2(self)
    def _calcular_sueldo_total2(self, nodo, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        return lista[0].calcular_sueldo() + self._calcular_sueldo_total2(nodo, lista[1:])

class Empleado(ABC):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        self.nombre = nombre
        self.años_de_antiguedad = años_de_antiguedad
        self.cant_hijxs = cant_hijxs
    @abstractmethod
    def calcular_sueldo(self):
        pass
    @abstractmethod
    def _es_valido(self):
        pass
    def __repr__(self):
        return (f"({self.nombre}, "f"{self.años_de_antiguedad}, "f"{self.cant_hijxs}), "f"{self.calcular_sueldo()}")

class DirectorArea(Empleado):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        if self.cant_hijxs >= 1:
            return 2500000 + (5000 * self.años_de_antiguedad) + 100000
        return 2500000 + (5000 * self.años_de_antiguedad)
    def _es_valido(self):
        return True

class DirectorGeneral(DirectorArea):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        return 0

class DirectorIT(DirectorArea):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    
class DirectorFinanzas(DirectorArea):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
        
class DirectorRecursosHumanos(DirectorArea):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    
class LiderTecnicx(Empleado):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        if self.cant_hijxs >= 1:
            return 100000 + (3000 * self.años_de_antiguedad) + 100000
        return 100000 + (3000 * self.años_de_antiguedad)
    def _es_valido(self):
        return True
    
class Desarrollador(Empleado):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    @abstractmethod
    def _es_valido(self):
        pass
    
class Senior(Desarrollador):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        if self.cant_hijxs >= 1:
            return 700000 + (2000 * self.años_de_antiguedad) + 100000
        return 700000 + (2000 * self.años_de_antiguedad)
    def _es_valido(self):
        return self.años_de_antiguedad > 5
    
class Junior(Desarrollador):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        if self.cant_hijxs >= 1:
            return 500000 + (1500 * self.años_de_antiguedad) + 100000
        return 500000 + (1500 * self.años_de_antiguedad)
    def _es_valido(self):
        return self.años_de_antiguedad >= 1 and self.años_de_antiguedad <= 5
    
class Trainee(Desarrollador):
    def __init__(self, nombre, años_de_antiguedad, cant_hijxs):
        super().__init__(nombre, años_de_antiguedad, cant_hijxs)
    def calcular_sueldo(self):
        if self.cant_hijxs >= 1:
            return 300000 + 100000
        return 300000
    def _es_valido(self):
        return self.años_de_antiguedad < 1
    
class Pasante(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, 0, 0)
    def calcular_sueldo(self):
        return 0 
    def _es_valido(self):
        return True
    
organigrama = Organigrama(DirectorGeneral("Juan", 20, 2),
    [Organigrama(DirectorIT("Ana", 10, 1),
        [Organigrama(LiderTecnicx("Pedro", 7, 0),
            [Organigrama(Senior("Lucia", 8, 1),
                [Organigrama(Pasante("Martin"),[])]),
                     Organigrama(Junior("Carlos",3,0),[]),
                        Organigrama(Trainee("Jose",0.5,0),[])])]),
                            Organigrama(DirectorFinanzas("Laura",12,2),[]),
                                Organigrama(DirectorRecursosHumanos("Marta", 6, 0), [])])


print(organigrama.es_valido())
print(organigrama.calcular_sueldo_total2())
#print(organigrama)

class Hospital:
    def __init__(self, empleado, subordinados):
        self.empleado = empleado
        self.subordinados = subordinados
    def es_valido(self, jefe=None):
        if jefe is None:
            if not isinstance(self.empleado, DirectorDelHospital):
                return False
        if not self.empleado._es_valido():
            return False
        if isinstance(self.empleado, Cirujano):
            if not isinstance(jefe, JefeDeCirujia):
                return False
        if isinstance(self.empleado, Medico):
            if not isinstance(jefe, JefeDeClinicaMedica):
                return False
        if isinstance(self.empleado, Residente):
            if not isinstance(jefe, JefeDeCirujia) and not isinstance(jefe, JefeDeClinicaMedica):
                return False
        if isinstance(self.empleado,(JefeDeCirujia, JefeDeClinicaMedica, JefeDePediatria)):
            if not isinstance(jefe, DirectorDelHospital):
                return False
        if isinstance(jefe, Residente): #Un residente no puede tener subordinados
            return False
        return self._validar_hijos(self.subordinados, self.empleado)
    def _validar_hijos(self, subordinados, jefe):
        if subordinados == []:
            return True
        return (subordinados[0].es_valido(jefe) and self._validar_hijos(subordinados[1:], jefe)) 
    def calcular_sueldo_total(self):
        return self._calcular_sueldo_total(self)
    def _calcular_sueldo_total(self, nodo):
        return (nodo.empleado.calcular_sueldo() + self._sumar_nodos(nodo.subordinados,0))
    def _sumar_nodos(self, subordinados, i):
        if i == len(subordinados):
            return 0
        return (subordinados[i].calcular_sueldo_total() + self._sumar_nodos(subordinados, i + 1))

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def _es_valido(self):
        pass
    @abstractmethod 
    def calcular_sueldo(self):
        pass

class DirectorDelHospital(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
    def calcular_sueldo(self):
        return self.edad*100000

class JefeDeCirujia(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo(self):
        return len(self.nombre)*100000
        
class Cirujano(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
    def calcular_sueldo(self):
        return (len(self.nombre) + self.edad)*50000
    
class Residente(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
    def calcular_sueldo(self):
        return self.edad ** 2
        
class JefeDeClinicaMedica(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo(self):
        return len(self.nombre) * 20000
        
class Medico(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo(self):
        return self.edad ** 3
        
class JefeDePediatria(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo(self):
        return len(self.nombre) * 40000
        
hospital = Hospital(DirectorDelHospital("Juan", 58), \
    [Hospital(JefeDeCirujia("Monica", 51), \
        [Hospital(Cirujano("Roberto", 62),[]), Hospital(Residente("Pedro", 42), [])]), \
            Hospital(JefeDeClinicaMedica("Hernán", 54), [Hospital(Medico("Jose", 40), []), \
                Hospital(Residente("Gabriel", 35), [])]), Hospital(JefeDePediatria("Ernesto", 50), [])])
            
            

print(hospital.es_valido())
print(hospital.calcular_sueldo_total())

class Universidad(ArbolN):
    def __init__(self, empleado, subordinados):
        self.empleado = empleado
        self.subordinados = subordinados
    def es_valido(self, jefe=None):
        if jefe is None:
            if not isinstance(self.empleado, Rector):
                return False
            if self.cantidad_rectores() != 1:
                return False
        if not self.empleado._es_valido():
            return False
        if isinstance(self.empleado, Ayudante):
            if not isinstance(jefe, Profesor):
                return False
        if isinstance(self.empleado,(DecanoExactas, DecanoIngenieria, DecanoEconomicas)):
            if not isinstance(jefe, Rector):
                return False
        return self._validar_hijos(self.subordinados, self.empleado)
    def _validar_hijos(self, subordinados, jefe):
        if subordinados == []:
            return True
        return (subordinados[0].es_valido(jefe) and self._validar_hijos(subordinados[1:], jefe)) 
    def cantidad_rectores(self, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        if isinstance(lista[0], Rector):
            return 1 + self.cantidad_rectores(lista[1:])
        return self.cantidad_rectores(lista[1:])
    def cantidad_profesores(self, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        if isinstance(lista[0], Profesor):
            return 1 + self.cantidad_profesores(lista[1:])
        return self.cantidad_profesores(lista[1:])
    def cantidad_ayudantes(self, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        if isinstance(lista[0], Ayudante):
            return 1 + self.cantidad_ayudantes(lista[1:])
        return self.cantidad_ayudantes(lista[1:])

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def _es_valido(self):
        pass    

class Rector(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 

class DecanoExactas(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
        
class Profesor(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
    
class Ayudante(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
        
class DecanoIngenieria(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
        
class DecanoEconomicas(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    
universidad = Universidad(Rector("Fernando", 48), [Universidad(DecanoExactas("Facundo", 51), \
    [Universidad(Profesor("Rolando", 53), [Universidad(Ayudante("Octavio", 42), [])])]) , \
        Universidad(DecanoIngenieria("Gervasio", 49), []),   
            Universidad(DecanoIngenieria("Gervasio", 49), [])]) 
    
print(universidad.es_valido())
print(f"Cantidad de profesores: {universidad.cantidad_profesores()}")
print(f"Cantidad de ayudantes: {universidad.cantidad_ayudantes()}")

class EmpresaVideojuegos(ArbolN):
    def __init__(self, empleado, subordinados):
        self.empleado = empleado
        self.subordinados = subordinados
    def es_valido(self, jefe=None):
        if jefe is None:
            if not isinstance(self.empleado, CEO):
                return False
        if not self.empleado._es_valido():
            return False
        if isinstance(self.empleado, (DiseñadorSenior, DiseñadorJunior)):
            if not isinstance(jefe, DirectorDiseño):
                return False
        if isinstance(self.empleado,(ProgramadorSenior, ProgramadorJunior)):
            if not isinstance(jefe, DirectorProgramacion):
                return False
        if isinstance(self.empleado,(DirectorDiseño, DirectorProgramacion, DirectorArte)):
            if not isinstance(jefe, CEO):
                return False
        if isinstance(self.empleado, Pasante):
            if not isinstance(jefe, ProgramadorSenior):
                return False
        return self._validar_hijos(self.subordinados, self.empleado)
    def _validar_hijos(self, subordinados, jefe):
        if subordinados == []:
            return True
        return (subordinados[0].es_valido(jefe) and self._validar_hijos(subordinados[1:], jefe)) 
    def costo_mensual(self, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        return lista[0].calcular_sueldo_mensual() + self.costo_mensual(lista[1:])
    def cantidad_pasantes(self, lista=None):
        if lista is None:
            lista = self.preorder()
        if not lista:
            return 0
        if isinstance(lista[0], Pasante):
            return 1 + self.cantidad_pasantes(lista[1:])
        return self.cantidad_pasantes(lista[1:])
    

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def _es_valido(self):
        pass
    @abstractmethod 
    def calcular_sueldo_mensual(self):
        pass  
    def __repr__(self):
        return (f"({self.nombre}, "f"{self.edad})")

class CEO(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True 
    def calcular_sueldo_mensual(self):
        return 0

class DirectorDiseño(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return self.edad**3
        
        
class DirectorProgramacion(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return len(self.nombre)**7
        
class DirectorArte(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return self.edad ** len(self.nombre)

class Diseñador(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    @abstractmethod
    def _es_valido(self):
        return True
    @abstractmethod
    def calcular_sueldo_mensual(self):
        pass

class DiseñadorSenior(Diseñador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return len(self.nombre) * 500000

class DiseñadorJunior(Diseñador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return len(self.nombre) * 250000
    
class Programador(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    @abstractmethod
    def _es_valido(self):
        return True
    @abstractmethod
    def calcular_sueldo_mensual(self):
        pass
    
class ProgramadorSenior(Programador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return self.edad * 500000
        
class ProgramadorJunior(Programador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return self.edad * 250000
        
class Pasante(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def _es_valido(self):
        return True
    def calcular_sueldo_mensual(self):
        return 0
    
empresa = EmpresaVideojuegos(CEO("Norberto", 60), [EmpresaVideojuegos(DirectorDiseño("Santiago", 45),
    [EmpresaVideojuegos(DiseñadorSenior("Agustin", 31), []), 
         EmpresaVideojuegos(DiseñadorJunior("Franco", 24), [])]) ,
              EmpresaVideojuegos(DirectorProgramacion("Emilio", 51), 
                    [EmpresaVideojuegos(ProgramadorSenior("Nicolas", 29), 
                          [EmpresaVideojuegos(Pasante("Joaquin", 20), [])]),
                              EmpresaVideojuegos(ProgramadorJunior("Pedro", 25), [])]), 
                                  EmpresaVideojuegos(DirectorArte("Fabio", 57), [])])

print(empresa.es_valido())
print(f"Costo mensual: {empresa.costo_mensual()}")
print(f"Cantidad de pasantes: {empresa.cantidad_pasantes()}")

