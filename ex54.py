# Definición de la función sumar
def sumar(a, b):
    suma = 0
    # Comprueba si a es mayor que b
    if a > b:
        # Bucle que suma los números desde b hasta a (inclusive) con un paso de 1
        for i in range(b, a + 1, 1):
            suma += i
    # Comprueba si b es mayor que a
    elif b > a:
        # Bucle que suma los números desde a hasta b (inclusive) con un paso de 1
        for i in range(a, b + 1, 1):
            suma += i
    else:
        # En caso de que a y b sean iguales, la suma es 0
        suma = 0
    return suma

# Programa principal
# Solicita al usuario que introduzca el primer número y almacena el resultado en la variable a
a = int(input("Introduce el primer número: "))
# Solicita al usuario que introduzca el segundo número y almacena el resultado en la variable b
b = int(input("Introduce el segundo número: "))
# Llama a la función sumar con a y b como argumentos y almacena el resultado en la variable c
c = sumar(a, b)
# Muestra la suma de los números entre a y b
print("La suma de los números entre {} y {} es {}".format(a, b, c))