def superposición(a, b):
	n = 0 # indica cuántos elementos hay en común
	for e in a:
		n += b.count(e)
	if n>0:
		return [n, True]
	else:
		return  [0, False]

# Programa Principal
a = input("Introduce la primera lista de elementos como una cadena, sin espacios: ")
b = input("Introduce la segunda lista de elementos como una cadena, sin espacios:  ")
c,d = superposición(a,b)
if (c==0):
	print("Las dos listas no tienen ningún elemento en común.")
else:
	print("Las listas tienen ", c, " elementos en común")
