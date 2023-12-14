#Función que genera la tabla de multiplicar de un número dado
def tabla_multiplicar(a):
    # Bucle que itera 20 veces para generar la tabla
    for i in range(20):
    # Impresión de cada línea de la tabla
        print("{} x {} = {}".format(i + 1, a, (i + 1) * a))

# Programa principal
x = int(input("Introduce un número para calcular su tabla de multiplicar: "))
tabla_multiplicar(x)