def bintodec(binario):
    return int(binario, 2)

def listbintodec(llbin):
    listdec = []
    for e in llbin:
        listdec.append(bintodec(e))
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