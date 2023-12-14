def analizar_número():
    suma = 0
        # Introduce un número
    a = input("Introduce un número: ")
        # Imprimimos la cantidad de dígitos en el número
    print("{} tiene {} dígitos".format(a, len(a)))
        # Recorremos cada dígito en la cadena junto con su índice
    for i, e in enumerate(a):
        # Comprobamos si el índice es par
        if i % 2 == 0:
         # Imprimimos el dígito y su posición para los índices pares
            print("El dígito en la posición par {} es {}".format(i, e))

# Llamada a la función
analizar_número()