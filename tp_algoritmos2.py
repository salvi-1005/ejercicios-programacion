class Ruta:
    def __init__(self, distancia, riesgo):
        self.distancia = distancia
        self.riesgo = riesgo
    def costo(self):
        return self.distancia + 5 * self.riesgo
    def __repr__(self):
        return f"distancia: {self.distancia}, riesgo: {self.riesgo}"

Cusco_Anta = Ruta(20, 8)
Cusco_Chinchero = Ruta(15, 2)
Anta_Ollantaytambo = Ruta(25, 8)
Chinchero_Urubamba = Ruta(20, 1)
Urubamba_Pachar = Ruta(10, 1)
Pachar_Ollantaytambo = Ruta(8, 1)

class Grafo:
    def __init__(self, lista_de_adyacencia):
        self.lista_de_adyacencia = lista_de_adyacencia
    def __str__(self):
        return str(self.lista_de_adyacencia)

grafo = Grafo({
    "Cusco": {

        "Anta": {
            Cusco_Anta
        },

        "Chinchero": {
            Cusco_Chinchero
        }
    },

    "Anta": {

        "Ollantaytambo": {
            Anta_Ollantaytambo
        }
    },

    "Chinchero": {

        "Urubamba": {
            Chinchero_Urubamba
        }
    },

    "Urubamba": {

        "Pachar": {
            Urubamba_Pachar 
        }
    },

    "Pachar": {

        "Ollantaytambo": {
            Pachar_Ollantaytambo
        }
    },

    "Ollantaytambo": {}
})

print(grafo)


