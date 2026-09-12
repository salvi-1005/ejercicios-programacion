import sys

altura_pelota = 100
i = 0
if len(sys.argv) == 2:
    altura_pelota = float(sys.argv[1])
while i < 10:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 1))