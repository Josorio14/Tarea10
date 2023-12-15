# Función que convierte un número binario a decimal.
def bintodec(binario):
    # Utiliza la función 'int' para convertir el número binario a decimal (base 2).
    return int(binario, 2)

# Función que convierte una lista de números binarios a decimales.
def listbintodec(llbin):
    # Inicia con una lista vacía para almacenar los resultados.
    listdec = []
    # Utiliza un bucle con 'for' para iterar sobre cada elemento de la lista de números binarios.
    for e in llbin:
        # Llama a la función 'bintodec' para convertir cada número binario a decimal.
        listdec.append(bintodec(e))
    # Retorna la lista completa de números decimales resultantes.
    return listdec


# Programa  que convierte los números  binarios de una lista en enteros

# Introducir la lista de números binarios separados por espacios
a = input("Introduce la lista de números binarios separados por espacios: ")

# Dividir la entrada del usuario en una lista de cadenas
lista_binarios = a.split()

# Convertir la lista de números binarios a decimal
lista_decimales = listbintodec(lista_binarios)

# Imprimir los resultados
for i, e in enumerate(lista_decimales):
    print(f"El número binario: {lista_binarios[i]} corresponde al número decimal: {e}")