def mostrar(i):
    # Inicia una lista vacía 'b'
    b = []
    # Bucle para construir la lista con números descendentes desde 'i' hasta 1
    for e in range(i, 0, -1):
        b.append(e)
    # Imprime la lista como una cadena, separando los elementos por espacios
    print(' '.join(map(str, b)))

# Programa principal
# Introduce un número pequeño y almacena el resultado en la variable 'x'
x = int(input("Introduce un número pequeño: "))
# Bucle para llamar a la función 'mostrar' con valores decrecientes desde 'x' hasta 1
for i in range(x, 0, -1):
    mostrar(i)