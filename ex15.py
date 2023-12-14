def longitud_de_una_lista(a):
	long = 0
	for i in a:
		long +=1
	return long

#Ejemplo de la longitud de la cadena de carácteres
a = "El amor lo conquista todo"
print("La longitud de la cadena escrita és: ", longitud_de_una_lista(a))

#Ejemplo de una lista[]
b  = [24, 22, 23, "sistemas", "Mariano"]
print("La longitud de la llista escrita és: ", longitud_de_una_lista(b))

#Ejemplo de una tupla()
c  = (3, 5, 7, 9, 29)
print("La longitud de la tupla escrita és: ", longitud_de_una_lista(c))

#Ejemplo del conjunto{}
d = {3, 5, 7, 9, 10} 
print("La longitud del conjunto escrita és: ", longitud_de_una_lista(d))			
