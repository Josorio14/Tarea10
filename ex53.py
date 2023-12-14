def pares():
    a = []  #Lista para almacenar los números pares
    for i in range(2, 101, 2): #Bucle que itera desde 2 hasta 100 (inclusive) con paso 2
        a.append(i)          # Agrega el número par a la lista
    # Muestra la lista de números pares
    print("Los pares de 1 a 100 son {} \n".format(a))

def impares():
    a = []     # Lista para almacenar los números impares
    for i in range(1, 100, 2):     # Bucle que itera desde 1 hasta 99 (inclusive) con paso 2
        a.append(i)           # Agrega el número impar a la lista
        # Muestra la lista de números impares
    print("Los impares de 1 a 100 son {}".format(a))

# Programa principal
# Llama a la función pares para mostrar los números pares
pares()
# Llama a la función impares para mostrar los números impares
impares()