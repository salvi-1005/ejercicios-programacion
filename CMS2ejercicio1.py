def quienGana(j1: str, j2: str) ->str:
    if piedraGanaAtijera(j1, j2):
	   return j1
	if tijeraGanaAPapel(j1, j2):
	   return j1
	if papelGanaAPiedra(j1, j2):
	   return j1
	if piedraGanaAtijera(j2, j1):
	   return j2
	if tijeraGanaAPapel(j2, j1):
	   return j2
	if papelGanaAPiedra(j2 j1):
	   return j2
	else:
	    return empate

