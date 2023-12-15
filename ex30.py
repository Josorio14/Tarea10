# Definición de una función llamada 'mostrar_mayores_que'
# que toma una tupla 'tupla' y un valor 'valor' como parámetros.
def mostrar_mayores_que(tupla, valor):
    # Itera a través de cada número en la tupla.    
    for número in tupla:
        # Compara cada número con el valor proporcionado.
        if número > valor:
            # Imprime el número si es mayor que el valor.
            print(número)


#Introduce números separados por espacios  y luego convertirlos en una tupla de números enteros.
tupla = input("Introduce números en la tupla separando por espacios: ")
números = tuple(map(int, tupla.split()))
# Definir un valor límite.
valor_límite = 18
# Mostrar los números mayores que el valor límite.
print("Números mayores que {}:".format(valor_límite))
mostrar_mayores_que(números, valor_límite)

