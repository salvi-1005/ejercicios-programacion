def fibonacciNoRecursivo(n: int) ->int:
    if n < 0:
       return undefined
    if n == 0:
       return 0
    if n == 1:
       return 1
    else:
       return:  esSecuenciaFibonacci(n-1) + esSecuenciaFibonacci(n-2) 