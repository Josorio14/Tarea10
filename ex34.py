def es_bisiesto(año):
        # Condición para ser año bisiesto
        # Un año es bisiesto si es divisible por 4, pero no por 100 y también es divisible por 400.
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return True
    else:
        return False

# Ejemplo de uso
año_a_verificar = int(input("Introduce un año: "))

# Verificar si el año es bisiesto usando la función
if es_bisiesto(año_a_verificar):
    print("{} es un año bisiesto.".format(año_a_verificar))
else:
    print("{} no es un año bisiesto.".format(año_a_verificar))