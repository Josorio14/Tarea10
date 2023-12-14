def mostrar_mayores_que(tupla, valor):
    for número in tupla:
        if número > valor:
            print(número)

tupla = input("Introduce números en la tupla separando por espacios: ")
números = tuple(map(int, tupla.split()))
valor_límite = 18

print("Números mayores que{}:".format(valor_límite))
mostrar_mayores_que(números, valor_límite)

