# Importa la función randint desde el módulo random
from random import randint

# Genera y devuelve una lista de 20 elementos aleatorios entre 1 y 100
def lista_20_elementos():
    lista = [randint(1, 100) for _ in range(20)]
    return lista

#Verifica si una lista tiene elementos duplicados
def hay_duplicados(lista):
    # Utiliza un conjunto (set) llamado vistos para rastrear los elementos vistos
    vistos = set()
    # Utiliza una lista de comprensión para encontrar los elementos duplicados
    duplicados = [x for x in lista if x in vistos or vistos.add(x)]
    
    # Imprime un mensaje indicando si hay o no duplicados
    if len(duplicados) > 0:
        print("La lista {} tiene elementos duplicados: {}".format(lista, duplicados))
    else:
        print("La lista {} no tiene elementos duplicados".format(lista))

# Programa principal
# Llama a la función lista_20_elementos y almacena el resultado en la variable x
x = lista_20_elementos()
# Llama a la función hay_duplicados con x como argumento
hay_duplicados(x)