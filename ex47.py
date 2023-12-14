# Definición de la función hay_duplicados
def hay_duplicados(a):
    visto = set()
    duplicados = [x for x in a if x in visto or visto.add(x)]
    
    if len(duplicados) > 0:
        print("La lista {} tiene elementos duplicados: {}".format(a, duplicados))
    else:
        print("La lista {} no tiene elementos duplicados".format(a))

# Definición de la función leer_lista
def leer_lista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introduce un elemento de la lista y un punto (.) para finalizar: ")
        if c != ".":
            a.append(c)
    return a

# Programa principal
# Llama a la función leer_lista y almacena el resultado en la variable a
a = leer_lista()
# Llama a la función hay_duplicados con a como argumento
hay_duplicados(a)