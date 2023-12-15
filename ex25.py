def palabra_mas_grande(lista_palabras):
    # Verifica si la lista de palabras está vacía
    if not lista_palabras:
        return None  # Devuelve "None" si la lista está vacía

    palabra_mas_larga = lista_palabras[0]  # Inicia con la primera palabra
    # Utiliza un bucle con 'for' para comparar cada palabra de la lista
    for palabra in lista_palabras:
        # Verifica si la longitud de la palabra actual es mayor que la longitud de la palabra más larga encontrada hasta ahora
        if len(palabra) > len(palabra_mas_larga):
            # Si es así, actualiza la "palabra_mas_larga" con la palabra actual
            palabra_mas_larga = palabra
    # Retorna la palabra más larga encontrada en la lista
    return palabra_mas_larga

#Programa principal

a = input("Introduce las palabras separadas por espacios: ")

palabra = a.split() #El split devuelve una lista de palabras como cadena de separación. 

resultado = palabra_mas_grande(palabra)

if resultado is not None:
    print("La palabra más larga es:", resultado)
else:
    print("La lista está vacía")


