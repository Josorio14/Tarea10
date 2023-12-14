#calcula la cantidad de dígitos de un número dado.
def contar_dígitos(número):
    dígitos = 0
    for n in str(número):
        dígitos += 1
    return dígitos

# Introduce un número
a = int(input("Introduce un número natural menor que 900000: "))
# Verificación si el número es mayor que 900,000
if a > 900000:
    print("El número es más grande que 900000. Introduce un número valido.")
else:
    print("{} tiene {} dígitos".format(a, contar_dígitos(a)))