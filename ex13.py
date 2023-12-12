def funcióngrande(x,y):
    #Si x es mayor que y, retornamos a x
    if x>y:
        return x
    #Si x no  es mayor que y, retornamos y
    elif x<y: 
        return y
    #Si no, son iguales
    else:
        print("{} y {} son iguales".format(x,y))

    
#Programa principal

a = int(input("Intro el 1r número: "))
b = int(input("Intro el 2n número: "))
c = funcióngrande(a, b)
#Si "a" no es igual "b" se imprime la siguiente instrucción
if not a==b:
    print("El mayor de {} y {} es {}".format(a,b,c))

