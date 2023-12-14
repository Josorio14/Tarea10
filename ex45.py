def leer_lista():
    # Inicia con una lista vacía
    a = []
    # Inicia con una cadena de caracteres con el valor "a"
    c = "a"
    # Bucle que continúa hasta que se introduzca un punto
    while c != ".":
        c = input("Introduce un elemento de la lista y después un punto para finalizar '.' para terminar: ")
     # Si la entrada no es un punto, agrega el elemento a la lista
        if c != ".":
            a.append(c)
    # Devuelve la lista completa
    return a

# Función eliminar_capicua
def eliminar_capicua(a):
    # Inicializa una lista vacía
    b = []
    # Comprueba si la longitud de la lista es mayor que 2
    if len(a) > 2:
    # Asigna a la lista "b" todos los elementos de "a" excepto el primero y el último
        b = a[1:-1]
    # Devuelve la lista b
    return b

# Programa principal
x = leer_lista()
y = eliminar_capicua(x)
print("La lista original {} se ha transformado en la lista {}".format(x, y))