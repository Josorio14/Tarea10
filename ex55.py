# Definición de la función dibujar
def dibujar(a):
    l = []
    
    # Bucle para dibujar patrón ascendente
    for j in range(a + 1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()
    
    # Bucle para dibujar patrón descendente
    for j in range(a + 1, 0, -1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()

# Programa principal
# Solicita al usuario que introduzca un número y almacena el resultado en la variable a
a = int(input("Introduce un número: "))
# Llama a la función dibujar con a como argumento
dibujar(a)