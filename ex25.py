def palabra_mas_grande(lista_palabras):
    if not lista_palabras:
        return None  # Devuelve "None" si la lista está vacía

    palabra_mas_larga = lista_palabras[0]  # Inicia con la primera palabra
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga

#Programa principal

a = input("Introduce las palabras separadas por espacios: ")

palabra = a.split() #El split devuelve una lista de palabras como cadena de separación. 

resultado = palabra_mas_grande(palabra)

if resultado is not None:
    print("La palabra más larga es:", resultado)
else:
    print("La lista está vacía")


