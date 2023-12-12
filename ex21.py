def crear_repetidos(número,carácter):
	c = carácter*int(número)
	return c

#Programa principal
x = int(input("Introduce un número: "))
y = input("Introduce un carácter: ")
print("El carácter ", y, " repetido ",x,"-veces es: ", crear_repetidos(x,y))





