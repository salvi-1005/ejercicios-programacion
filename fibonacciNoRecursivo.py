import sys

def generaListaFibonacciIterativo(n: int) -> list[int]:
  listaFibonacci = []
  act = 0
  sig = 1
  for i in range(n+1):
    listaFibonacci.append(act)
    aux = act
    act = sig
    sig = act+aux
  return listaFibonacci

def esSecuenciaFibonacci(l: list[int]) -> bool:
  esFibo = True
  if (len(l) > 0 and l[0] != 0) or (len(l) > 1 and l[1] != 1):
      esFibo = False
  if len(l) > 2:
    i = 2
    esFibo = True
    while esFibo and i < len(l):
      if l[i] != l[i-1]+l[i-2]:
        esFibo = False
      i += 1
  return esFibo
  
def fibonacciNoRecursivo(n: int) -> int:
  numeroPosN = None
  if n >= 0:
    listaFibonacci = generaListaFibonacciIterativo(n)
  if len(listaFibonacci) == n+1 and esSecuenciaFibonacci(listaFibonacci):
    numeroPosN = listaFibonacci[len(listaFibonacci)-1]
  return numeroPosN

def fibonacciRecursivo(n: int) -> int:
  if n == 0:
      return 0
  if n == 1:
      return 1
  return n + fibonacciRecursivo(n-1)

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))