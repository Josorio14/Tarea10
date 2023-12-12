def función_grande_de_tres(a, b, c):
    if a > b > c:
        print("{} es mayor que {} que es mayor que {}".format(a, b, c))
    elif a < b < c:
        print("{} es menor que {} que es menor que {}".format(a, b, c))


    elif a > b == c:
        print("{} es mayor que {} y {} ambos son iguales".format(a, b, c))
    elif a < b == c:
        print("{} es menor que {} y {} ambos son iguales".format(a, b, c))
    

    elif a == b > c:
        print("{} y {} son iguales y mayor que {}".format(a, b, c))

    elif a == b < c:
        print("{} y {} son iguales y menor que {}".format(a, b, c))


    elif a == c < b:
        print("{} y {} son iguales y menor que {}".format(a, c, b))
    elif a == c > b:
        print("{} y {} son iguales y mayor que {}".format(a, c, b))

    elif a > c > b:
        print("{} es mayor que {} y es mayor que {}".format(a, c, b))   
         
    elif c > a > b:
        print("{} es mayor que {} y es mayor que {}".format(c, a, b))

    elif b > c > a:
        print("{} es mayor que {} y es mayor que {}".format(b, c, a))   

    elif a == b == c:
        print("Los tres números son iguales.")

    #Con el else me ha ayudado a comprobar que es posible hacer todas las combinaciones,
    # si me faltaba una combinación, daba el print
    else:
        print("Los números no siguen un patrón claro de mayor, menor o igual.")

# Programa principal
a = int(input("Introduce el 1er número: "))
b = int(input("Introduce el 2do número: "))
c = int(input("Introduce el 3er número: "))
función_grande_de_tres(a, b, c)