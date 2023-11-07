#Ejercicio 11
#Funciones
def menu_principal():
    print("""       
        Menú principal:
        1.Calculadora enteros
        2.Calculadora reals
        3.Salir
        """)
    a = int(input("Elegir una opción:"))
    return a

def calculadora_enteros():
    b = 1
    while b>0:
        print("""
        Menú calculadora enteros:
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
                x = int(input("Introduce el primer número a sumar"))
                y = int(input("Introduce el segundo número a sumar"))
                print("Resultado: {} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introduce el primer número a restar"))
                y = int(input("Introduce el segundo número a restar"))
                print("Resultado: {} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introduce el primer número a restar"))
                y = int(input("Introduce el segundo número a restar"))
                print("Resultado: {} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introduce el primer número a restar"))
                y = int(input("Introduce el segundo número a restar"))
                print("Resultado: {} / {} = {}".format(x, y, x/y))
            case 5: #Cambio de valores
                x = int(input("Introduce el primer número"))
                y = int(input("Introduce el segundo número"))
            case 6: #Salir
                print("Adiós, volveras al menú principal")
                b = -1
              

def calculadora_reales():
    b = 1
    while b>0:
        print("""
        Menú calculadora reales:
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
                x = float(input("Introduce el primer número a sumar"))
                y = float(input("Introduce el segundo número a sumar"))
                print("Resultado: {} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introduce el primer número a restar"))
                y = float(input("Introduce el segundo número a restar"))
                print("Resultado: {} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introduce el primer número a restar"))
                y = float(input("Introduce el segundo número a restar"))
                print("Resultado: {} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introduce el primer número a restar"))
                y = float(input("Introduce el segundo número a restar"))
                print("Resultado: {} / {} = {}".format(x, y, x/y))
            case 5: #Cambio de valores
                x = float(input("Introduce el primer número"))
                y = float(input("Introduce el segundo número"))
            case 6: #Salir
                print("Adiós, volveras al menú principal")
                b = -1


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
            a= -1
        case other:
            print("Opción no válida, vuelve al menú principal")