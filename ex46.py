# Definición de la función esta_ordenada
def esta_ordenada(a):
    # Copia la lista original para realizar comparaciones
    b = a.copy()
    c = a.copy()
    # Ordena la copia en orden ascendente
    b.sort()
    # Ordena la copia en orden descendente
    c.sort(reverse=True)
    # Compara la lista original con la copia ordenada ascendente
    if a == b:
        print("La lista {} está ordenada ascendentemente {}".format(a, b))
    # Compara la lista original con la copia ordenada descendente
    elif a == c:
        print("La lista {} está ordenada descendentemente {}".format(a, c))
    else:
        print("La lista {} no está ordenada {}".format(a, b))

# Definición de la función leer_lista
def leer_lista():
    # Prec: Lee una lista de números
    # Post: Retorna la lista leída.
    b = []
    a = "a"
    # Bucle que continúa hasta que se introduce un punto
    while a != ".":
        # Solicita al usuario que introduzca el siguiente número
        a = input("Introduce el siguiente número: ")
        # Si la entrada no es un punto, convierte el valor a entero y agrega a la lista
        if a != ".":
            b.append(int(a))
        else:
            return b

# Programa principal
# Llama a la función leer_lista y almacena el resultado en la variable a
a = leer_lista()
# Llama a la función esta_ordenada con a como argumento
esta_ordenada(a)
