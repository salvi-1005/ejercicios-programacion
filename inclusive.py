frase = 'todos somos programadores'
palabras = frase.split()
frase_t = []
for palabra in palabras:
    if palabra[-2] == "o":
        x = palabra.replace("o","e")
        y = x.replace("e","o",1)
        frase_t.append(y)
    if palabra[-2] != "o":
        frase_t.append(palabra)
print(' '.join(frase_t))
#'todes somes programadores'




    

    
