def sumar_lista(a):
		suma = 0
		for i in a:
			suma += i
		return suma

def multiplicar_lista(a):
		multiplicar = 1
		for i in a:
			multiplicar *=i
		return multiplicar
#Programa principal
x = [3, 6, 4, 5]
print("La suma de todos los elementos de la lista es: ", sumar_lista(x))
print("La multiplicación de todos los elementos de la lista es: ", multiplicar_lista(x))
