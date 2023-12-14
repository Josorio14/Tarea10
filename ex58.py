def es_primo(num):
    # Verifica si el número es menor que 2, en cuyo caso no es primo
    if num < 2:
        return False
    # Bucle que itera desde 2 hasta el número -1 para verificar si tiene algún divisor
    for i in range(2, num):
    # Si el número es divisible por algún valor en el rango, no es primo
        if num % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True

# Programa principal
numeros_primos = 0
lista_primos = []

# Bucle para verificar los números primos del 1 al 100
for num in range(1, 101):
    if es_primo(num):
        lista_primos.append(num)
        numeros_primos += 1

# Imprime la cantidad de números primos y la lista de números primos
print("Hay {} números primos y son {}".format(numeros_primos, lista_primos))