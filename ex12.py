#Ejercicio 12

#Funciones

def menu_principal():
    print("""       
        Menú principal:  \n
        1.Calculadora enteros
        2.Calculadora reales
        3.Cambio de bases
        4.Salir
        """)
    a = int(input("Elegir una opción:"))
    return a

def calculadora_enteros():
    b = 1
    while b>0:
        print("""
        Menú calculadora enteros:\n
          1) Suma
          2) Resta
          3) Multiplicación
          4) División 
          5) Cambio de valores
          6) Salir
              """)
        b = int(input("Elegir una opción:"))
        match b:
            case 1: #Sumar
                x = int(input("Introduce el primer número a sumar: "))
                y = int(input("Introduce el segundo número a sumar: "))
                print("Resultado: {} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introduce el primer número a restar: "))
                y = int(input("Introduce el segundo número a restar: "))
                print("Resultado: {} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introduce el primer número a multiplicar: "))
                y = int(input("Introduce el segundo número a multiplicar: "))
                print("Resultado: {} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introduce el primer número a dividir: "))
                y = int(input("Introduce el segundo número a dividir: "))
                print("Resultado: {} / {} = {}".format(x, y, x/y))
            case 5: #Cambio de valores
                x = int(input("Introduce el primer número a cambiar: "))
                y = int(input("Introduce el segundo número a cambiar: "))
            case 6: #Salir
                print("Adiós, volveras al menú principal\n")
                b = -1
              

def calculadora_reales():
    b = 1
    while b>0:
        print("""
        Menú calculadora reales:\n
          1) Suma
          2) Resta
          3) Multiplicación
          4) División 
          5) Cambio de valores
          6) Salir
              """)
        b = int(input("Elegir una opción:"))
        match b:
            case 1: #Sumar
                x = float(input("Introduce el primer número a sumar:"))
                y = float(input("Introduce el segundo número a sumar:"))
                print("Resultado: {} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introduce el primer número a restar:"))
                y = float(input("Introduce el segundo número a restar:"))
                print("Resultado: {} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introduce el primer número a multiplicar:"))
                y = float(input("Introduce el segundo número a multiplicar:"))
                print("Resultado: {} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introduce el primer número a dividir:"))
                y = float(input("Introduce el segundo número a dividir:"))
                print("Resultado: {} / {} = {}".format(x, y, x/y))
            case 5: #Cambio de valores
                x = float(input("Introduce el primer número:"))
                y = float(input("Introduce el segundo número:"))
            case 6: #Salir
                print("Adiós, volveras al menú principal\n")
                b = -1

#Funciones de cambios de base

#De decimal a binario, octal y hexadecimal
def dectobin(numero):
    return bin(numero)

def dectooct(numero):
    return oct(numero)

def dectohex(numero):
    return hex(numero)


#Este de Binario a octal, decimal y hexadecimal
def bintooct(numero):
    a=int(numero,2)
    return dectooct(a) 
def bintodec(numero):
    a=int(numero,2)
    return a
def bintohex(numero):
    a=int(numero,2)
    return dectohex(a)

#Esta de Octal binario, decimal y hexadecimal
def octtobin(numero):
    a= int(numero,8)
    return dectobin(a)
def octtodec(numero):
    a= int(numero,8)
    return a
def octtohex(numero):
    a= int(numero,8)
    return dectohex(a) 

#Esta de Hexadecimal a binario, octal y decimal
def hextonum(hex):#Esta función pasa cualquier hexadecimal a un numero
    pnum ={
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }

    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
    
def hextodec2(hex):
    #Precondicion de entrada:hex es una cadena de carácteres que esta codificada en hexadecimal
    # Post condicion de salida: Lo devuelve en número decimal
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posición = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat= 16 ** posición
        pnum = elevat * valor
        decimal += pnum
        posición += 1
        return decimal
    
def hextobin(numero):
    #Precondicion de entrada:numero es una cadena de carácteres   codificada en hexadecimal
    # Post condicion de salida: Devuelve el valor en binario
    a =int(numero,16)
    return dectobin(a)
def hextooct(numero):
    #Precondicion de entrada:numero es una cadena de carácteres codificada en hexadecimal
    # Post condicion de salida: Devuelve el valor en octal
    a =int(numero,16)
    return dectooct(a)
def hextodec(numero):
    #Precondicion de entrada:numero es una cadena de carácteres codificada en hexadecimal
    # Post condicion de salida: Devuelve el valor en octal
        a =int(hextodec2(numero))
        return a


def calculadora_de_cambios_de_bases():
    e = 1
    while e>0:
        print("""
        Menú calculadora de cambio de bases:\n
            1) Dado un binario lo pasamos a todo el resto
            2) Dado un octal lo pasamos a todo el resto
            3) Dado un decimal lo pasamos a todo el resto
            4) Dado un hexadecimal lo pasamos a todo el resto
            5) Salir
              """)
        e = int(input("Elegir una opción:"))
        match e:
            case 1: #Binario to
                b = (input("Introduce el número en binario:"))
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binario {} es: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))

            case 2: #Octal to
                o = (input("Introduce el número en octal:"))
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El número octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))

            case 3: #Decimal to
                d = int(input("Introduce el número en decimal:"))
                o = dectooct(d)
                b = dectobin(d)
                h = dectohex(d)
                print("El número decimal {} es: \n oct -> {} \n bin -> {} \n hex -> {}".format(d,o,b,h))

            case 4: #Hexadecimal to
                h = (input("Introduce el número en hexádecimal:"))
                o = hextooct(h)
                d = hextodec(h)
                b = hextobin(h)
                print("El número hexadecimal {} es: \n oct -> {} \n dec -> {} \n bin -> {} ".format(h,o,d,b))

            case 5: #Salir
                print("Adiós, volveras al menú principal \n")
                e = -1

#Programa principal     
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enteros()
        case 2:
            calculadora_reales()
        case 3:
            calculadora_de_cambios_de_bases()
        case 4:
            a= -1
        case other:
            print("Opción no válida, vuelta al menú principal\n\n")

