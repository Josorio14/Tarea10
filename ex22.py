def crear_puntos(lista):
    for num in lista:
        print("." * num)

lista = input("Introduce los números separados por espacios: ")
números = []

for valor in lista.split():
    números.append(int(valor))
crear_puntos(números)

