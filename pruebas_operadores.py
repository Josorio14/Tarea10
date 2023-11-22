#OPerador matemático de suma, si cambias el simbolo + puede se resta o multiplicación.

"""
a = 9
b = 10
c = a + b
print("La suma de {} más {} és {}".format(a, b, c))
"""

#Operador matemático que ahora los nombres de las variables no estan fijos
"""
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
c = a + b
print("La suma de {} más {} és {}".format(a, b, c))
"""

# Te dice si es impar
"""
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
c = a % b
if a % 2==0:
    print("El nombre de {} es par".format(a))
else:
      print("El nombre de {} es impar".format(a))
if b % 2==0:
    print("El nombre de {} es par".format(b))
else:
      print("El nombre de {} es impar".format(b))
"""

#División
"""
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
c = a / b
print("La operación de {} y {} és {}".format(a, b, c))
"""

#COmpara a y b si son iguales o no 
"""
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
if a == b:
    print("El nombre de {} y {} son iguales".format(a,b))
else:
      print("El nombre de {} y {} no son iguales".format(a,b))
"""

#Programa que compara y dice si es mayor o igual que
"""
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
if a >= b:
    print("{} es mayor o igual que {}".format(a,b))
else:
      print("{} no es mayor o igual que {}".format(a,b))
      """
#UTilizar un bucle/interación/repetición
#Que lea 3 valores del teclado y que lo guarden dentro e una lista. fInalmente imprimir la lista 
"""
a =[]
for i in range(3):
    a.append(int(input("Introduce un número: ")))
    print(a)
"""
#Ahora determino que tamaño tendra la lista y numer ode valores que yo indico en el teclado
"""
a =[]
f = int(input("Introduce el tramaño de la lista: "))
for i in range(f):
    a.append(int(input("Introduce un número: ")))
    print(a)
"""
#Lectura de listas donde a coge el valor de b y luego la asignación la cambia.
"""
a = [2, 3, 4]
b = [5, 6, 10]
a = b
print(a)
a[2] = 15
print(b)
"""
#a =a unión de b las listas 
"""
a = [2, 3, 4]
b = [5, 6, 10]
a += b
print(a)
"""

#Aqui dice si a y b miran el mismo objeto, si b = [2, 3, 4] 
#no apuntaria al mismo objeto, aunque se parezcan son individuales a y b serian
# distintas cosas con el mismo valor de listas.
"""
a = [2, 3, 4]
b = a
if b is a:
    print("Apuntan al mismo objeto")
else: 
    print("No apuntan al mismo objeto")

#a = [2, 3, 4]
#b = [2, 3, 4]
#if b == a:  esta instrucción saldria que apuntan al mismo objeto ya que "==" compara el valor 
"""

"""
a = [3, (1,3), [4, 5, 6],7, "hola", "0",0,1]
if "a" in a:
    print("a es dentro de la lista {}".format(a))
elif "hola" in a:
    print("hola esta dentro de la lista {}".format(a))
elif "0" in a:
    print("Eso se ejecuta si es cierta la condición")
elif "b" in a:
    print("b estra dentro {}".format(a))
else:
    print("Dentro esta {}".format(a))
"""



#Aqui se mira si a es igual que algun caracter con condicionales
"""

a= "c"
if "a" == "b":
    print("a es b")

elif a == "c":
    print("a es c")

elif a == "d":
    print("a es d")

elif a == "e":
    print("a es e")
else:
    print("a no vale nada")

"""

#Aqui se mira si a es igual que algun caracter con match

"""
a = input("Introduce el segundo valor: ")

match a:
    case "b":
        print("a es b")
    case "c":
        print("a es c")
    case "d":
        print("a es d")
    case "e":
        print("a es e")
    case other:
        print("Opción no válida \n\n")
"""

#BUCLES
"""
i = 0
while i < 10:
    if i ==5:
        break
    i+=i
    """