#Calcula la suma de los cuadrados de 4 posiciones menos que x. Número natural menor que 100.
def suma_cuadrados_menos_cuatro(x):
    # Verificación si x es mayor que 100
    if x > 100:
        print("El número es mayor que 100. Introduce un número válido.")
        #En el caso que no, se realiza la suma
    else:
        suma = 0
        # Bucle for para calcular la suma de cuadrados
        for i in range(x, 1, -4):
            suma += i**2
        print("La suma de los cuadrados de 4 posiciones menos de {} es: {} ".format(x, suma))

#Programa Principal
# Introduce un número natural:
número = int(input("Introduce un número natural menor que 100: "))

# Llama a la función con el valor introducido
suma_cuadrados_menos_cuatro(número)