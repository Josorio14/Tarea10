def invertir(a):
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r

def es_palíndromo(a):
	c = invertir(a)
	x = 0
	for i in range(len(a)):
		if a[i]!=c[i]:
			x+=1
	if x==0:
		return True
	else:
		return False
   	 
# Programa Principal
x = input("Introduce una palabra para ver si es palíndromo o no: ")
if es_palíndromo(x):
	print("La palabra ''", x, "'' al revés es ''", invertir(x), "'' por lo tanto si es un palíndromo.")
else:
	print("La palabra ''", x, "'' al revés es ''", invertir(x), "'' por lo tanto no es un palíndromo.")
