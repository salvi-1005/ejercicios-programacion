import sys

def rebotar(altura_pelota, n):
    i = 0
    if len(sys.argv) == 2:
        altura_pelota = float(sys.argv[1])
    while i < n:
        rebote = 0.6*altura_pelota
        altura_pelota = altura_pelota*0.6
        i = i+1
        print(i,round(rebote, 2))