suma = 0
a = input("Introduce un número: ")
# Bucle que suma cada dígito en la cadena
for i in a:
    suma = suma + int(i)

# Imprime la suma de los dígitos del número
print("La suma de los dígitos del número {} es {}".format(a, suma))

# Comprueba si la suma de los dígitos es par o impar
if suma % 2 == 0:
    print("La suma de los dígitos del número {} es par".format(a))
else:
    print("La suma de los dígitos del número {} es impar".format(a))