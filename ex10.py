#Definición de la función
def mayor(a):
    if a>18:
        print("Es mayor de edad")
    elif a<18:
        print("Es menor de edad")
    else:
        print("Tiene 18 años")
#Programa principal
x = int(input(" Introduce tu edad: "))
mayor(x)