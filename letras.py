import sys

letras = r"C:\Users\SD\Downloads\letras.csv"

from collections import Counter

def N_letras_mas_repetidas(letras, N):
    with open(letras, "r", encoding="utf-8") as f:
        texto = f.read()
    letras = [c for c in texto if c.isalpha()]
    contador = Counter(letras)
    return contador.most_common(N)


class Texto:
    def __init__(self, letras, N):
        self.letras = letras
        self.N = N
    def leer_de_archivo(self):
        with open(self.letras, "r", encoding="utf-8") as f:
            texto = f.read()
        return texto
    def mas_frecuentes(self, N):
        with open(self.letras, "r", encoding="utf-8") as f:
            texto = f.read()
        letra = [c for c in texto if c.isalpha()]
        contador = Counter(letra)
        return contador.most_common(N)

a = Texto(letras, 4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python script.py archivo_letras N")
    letras = sys.argv[1]
    N = int(sys.argv[2])
    print(N_letras_mas_repetidas(letras, N))
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python script.py archivo_letras N")
    letras = sys.argv[1]
    N = int(sys.argv[2])
    print(Texto(letras, N).mas_frecuentes(N))
        
