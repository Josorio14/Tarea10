# Definición de la función elementos_pares
def elementos_pares(a):
        # Itera sobre la lista 'a' utilizando la función 'enumerate', 
        # que proporciona tanto el índice como el elemento en cada iteración
    for i, e in enumerate(a):
        # Verifica si el índice es impar (posiciones pares) y, en ese caso, imprime el elemento
        if i % 2 == 1:
            print(e)

# Definición de la función leer_lista
def leer_lista():
    # Inicializa una lista vacía 'l'
    l = []
     # Inicializa 'a' con un valor arbitrario ('a') para iniciar el bucle
    a = 'a'     
    # Bucle que continúa hasta que se introduce un punto ('.')
    while a != '.':
            # Introduce una nueva palabra y la almacena en 'a'
        a = input("Introduce una nueva palabra y punto (.) para terminar: ")
            # Si la entrada no es un punto, agrega la palabra a la lista 'l'
        if a != '.':
            l.append(a)
    # Retorna la lista final
    return l

# Programa principal
# Llama a la función leer_lista y almacena el resultado en la variable b
b = leer_lista()
# Llama a la función elementos_pares con b como argumento
elementos_pares(b)