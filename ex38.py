def calcular_capital_final(cantidad, interés, años):
    # Calcula el capital final utilizando la fórmula del interés compuesto
    capital_final = cantidad * (1 + interés / 100) ** años
    return capital_final


#Programa principal
# Pide al usuario ingresar la cantidad solicitada (entre 50000 y 80000 euros)
x = float(input("Introduce la cantidad solicitada (entre 50000 y 80000 euros): "))

# Introduce el interés (entre 0.5 y 13 por ciento)
y = float(input("Introduce el interés (entre 0.5 y 13 por ciento): "))

#Introduce el número de años
z = int(input("Introduce el número de años: "))

# Llama a la función y obtiene el resultado
resultado = calcular_capital_final(x, y, z)

# Muestra el resultado
print("El capital {}€ a un interés del {}% a {} años resulta que pagaremos {:.2f}€".format(x, y, z, resultado))
