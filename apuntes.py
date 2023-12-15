def mostrar_mayores_que(t, n_referencia):
    print("Todos los números mayores que {} son: ".format(n_referencia))
    for e in t:
        if e > n_referencia:
            print("{} ".format(e))

def leer_lista():
    # Prec: Lee una lista de números
    # Post: Retorna la lista leída.
    b = []
    a = "a"
    while a != ".":
        a = input("Introduzca el siguiente número: ")
        if a != ".":
            b.append(int(a))
        else:
            return b

# Programa principal
i = input("Introduzca el número que desea comparar: ")
x = leer_lista()
a = tuple(x)
mostrar_mayores_que(a, int(i))  # Convertir 'i' a entero antes de llamar a la función

