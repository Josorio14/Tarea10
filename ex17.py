#Sebas, la función toma una lista como parámetro y con "sum" suma todos los elementos y luego devuelve la suma
def sumar_lista(lista):
    suma = sum(lista)
    return suma

# La función toma una lista como parámetro y inicia una variable multiplicar en 1.
# Utiliza un bucle "for" para iterar a través de los elementos de la lista y multiplicarlos entre sí.
# Devuelve el resultado de la multiplicación.

def multiplicar_lista(lista):
    multiplicar = 1
    for i in lista:
        multiplicar *= i
    return multiplicar

# Programa principal    
print("Introduce una lista de números separados por espacios")
entrada_usuario = input("Lista: ")

# Procesar y construir la lista
lista_numeros = []
for elemento in entrada_usuario.split():
    lista_numeros.append(int(elemento))

# Imprimir resultados
if lista_numeros:
    print("La suma de todos los elementos de la lista es:", sumar_lista(lista_numeros))
    print("La multiplicación de todos los elementos de la lista es:", multiplicar_lista(lista_numeros))
#Verifica si la lista lista_numeros no está vacía.
else:
    print("La lista está vacía.")
