import sys

def fibonacciNoRecursivo(n: int) -> int:
  # Implementar esta funcion
  i: int = 0
  if(n >= 2):
    i=2
    s: list() = [0, 1]
    while(i <= n):
      s.append(s[i-2] + s[i-1])
      i += 1
    return s[len(s)-1]
  else:
    if(n == 1):
      return 1
    else:
      return 0


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))