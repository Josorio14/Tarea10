# Define una función para leer una lista de palabras
def leer_lista_palabras():
    lista = [] # Inicia con una lista vacía
    palabra = "a"  # Inicia con una palabra con un valor inicial que no es el punto
    while palabra != ".":
        palabra = input("Introduce la siguiente palabra: ")
        if palabra != ".":
            lista.append(palabra) # Agrega la palabra a la lista si no es el punto
    lista.sort() # Ordena la lista alfabéticamente
    return lista # Retorna la lista resultante
 
def indice_palabra(lista, palabra):
    return [i for i, e in enumerate(lista) if palabra == e]

# Programa principal
# Llama a la función leer_lista_palabras y almacena el resultado en la variable a
a = leer_lista_palabras()
# Solicita al usuario que introduzca la palabra a buscar y almacena el resultado en la variable p
p = input("Introduce la palabra para buscar su índice: ")
# Llama a la función indice_palabra con a y p como argumentos y almacena el resultado en la variable b
b = indice_palabra(a, p)

# Comprueba si la lista es vacía
if len(b) == 0:
    print("Dentro de la lista {} no se encuentra el elemento {}".format(a, p))
else:
    print("Dentro de la lista {} la palabra {} aparece {} veces en las siguientes posiciones {}".format(a, p, len(b), b))