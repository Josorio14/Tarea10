#función para filtrar palabras
def filtrar_palabras(lista_de_palabras, a):
    for palabras in lista_de_palabras:
        if len(palabras) > a:
            print(palabras)
            

#Programa principal
b = input("Introduce las palabras separadas por espacios: ")

palabras = b.split()

c = int(input("Introduce el nombre mínimo de carácteres: "))
print("Palabras con más de {} carácteres:".format(c))
filtrar_palabras(palabras, c)




