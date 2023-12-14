def rimar_palabras(x, y):
    #Comparación de las últimas tres letras:
    if x[-3:] == y[-3:]:
        return "Las palabras '{}' y '{}' riman las últimas tres letras '{}'".format(x, y, x[-3:])
    #Comparación de las últimas dos letras:
    elif x[-2:] == y[-2:]:
        return "Las palabras '{}' y '{}' riman las últimas dos letras '{}'".format(x, y, x[-2:])
    #Caso en el que no riman:
    else:
        return "Las palabras '{}' y '{}' no riman".format(x, y)

# Programa principal
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

resultado = rimar_palabras(palabra1, palabra2)
print(resultado)