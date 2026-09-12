altura_pelota = 100
i = 0
while i < 10:
    rebote = 0.6*altura_pelota
    altura_pelota = altura_pelota*0.6
    i = i+1
    print(i,round(rebote, 1))

#1 60.0
#2 36.0
#3 21.6
#4 13.0
#5 7.8
#6 4.7
#7 2.8
#8 1.7
#9 1.0
#10 0.6