def contador_vocales(a):
        # Definir una tupla con las vocales y 'otras'
    b = ('a', 'e', 'i', 'o', 'u', 'otras')
        # Inicializar una lista para almacenar el conteo de cada vocal
    vocales = [0, 0, 0, 0, 0, 0]
        # Iterar sobre cada carácter en la palabra
    for i, e in enumerate(a):
        # Verificar si el carácter es una vocal y actualizar el conteo
        if e == 'a' or e == 'A' or e == 'à' or e == 'á' or e == 'À' or e == 'Á':
            vocales[0] += 1
        elif e == 'e' or e == 'E' or e == 'è' or e == 'é' or e == 'È' or e == 'É':
            vocales[1] += 1
        elif e == 'i' or e == 'I' or e == 'í' or e == 'Í':
            vocales[2] += 1
        elif e == 'o' or e == 'O' or e == 'ò' or e == 'ó' or e == 'Ò' or e == 'Ó':
            vocales[3] += 1
        elif e == 'u' or e == 'U' or e == 'ú' or e == 'Ú':
            vocales[4] += 1
        # Si no es una vocal, incrementar el conteo en 'otras'
        else:
            vocales[5] += 1
    # Imprimir el resultado del conteo de cada vocal
    for i, e in enumerate(vocales):
        print("La vocal '{}' aparece {} veces".format(b[i], vocales[i]))

# Programa principal
a = input("Introduce una palabra a analizar: ")
contador_vocales(a)