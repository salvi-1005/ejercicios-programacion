import random

def gana_punto(a, b):
    quien_gana = random.randint(a, b)
    return quien_gana

def game(a, b):
    puntos_a = 0
    puntos_b = 0
    while puntos_a < 4 | puntos_b < 4:
        if gana_punto(a, b) == a:
            puntos_a += 1
        if gana_punto(a, b) == b:
            puntos_b += 1
    if puntos_a > puntos_b:
        return a
    return b

def gana_set(a, b):
    games_a = 0
    games_b = 0
    while games_a < 6 | games_b < 6:
        if game(a, b) == a:
            games_a += 1
        if game(a, b) == b:
            games_b += 1
    if games_a > games_b:
        return a
    return b

def partido(a, b):
    sets_a = 0
    sets_b = 0
