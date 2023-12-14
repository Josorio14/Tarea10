#Función que cuenta cuantas mayúsculas hay en una cadena de carácteres
def núm_mayúsculas(cadena):
    # Inicializamos un contador para las letras mayúsculas
    contador_mayúsculas = 0
    
    # Repetimos sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificamos si el caracter es una letra mayúscula
        if caracter.isupper():
            contador_mayúsculas += 1
    
    # Devolvemos la cantidad de letras mayúsculas encontradas
    return contador_mayúsculas

# Programa Principal
cadena_ejemplo = input("Introduce un texto añadiendo mayúsculas:")
resultado = núm_mayúsculas(cadena_ejemplo)
print(f"En la cadena '{cadena_ejemplo}' hay {resultado} letras mayúsculas.")
