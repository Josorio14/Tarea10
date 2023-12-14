# Importa la función random desde el módulo random
from random import random
import random

# Genera y devuelve una lista de 20 elementos aleatorios entre 1 y 100
def lista_20_elementos():
    l = []
    for i in range(20):
        l.append(random.randint(1, 100))
    return l

# Verifica si una lista tiene elementos duplicados
def hay_duplicados(a):
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]     
    if len(dupes) > 0:
        print("La lista {} tiene elementos duplicados {} \n".format(a, dupes))
    else:
        print("La lista {} no tiene elementos duplicados {}".format(a, dupes))

# Elimina los elementos duplicados de una lista
def elimina_duplicats(a):
    b = list(set(a))
    return b


# Programa principal
# Llama a la función y almacena el resultado en la variable x
x = lista_20_elementos()

# Llama a la función con x como argumento
hay_duplicados(x)
# Llama a la función con x como argumento y almacena el resultado en la variable y
y = elimina_duplicats(x)
# Ordena la lista y
y.sort()
# Imprime la lista sin elementos duplicados
print("Entonces, la lista sin elementos duplicados es {}".format(y))
