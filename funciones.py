# FUnciones de intercambio de valores
"""
def intercambio(a, b):
    return b, a

x = "María"
y = "José"
print("EL valor de x es {} y el de y es {}".format(x, y)) #Los imprime tal cual el orden y su valor "María" y "José"

x, y = intercambio(x, y) #Coje los valores de retorno y los gira "José" y "María"
print("Después del intercambio, el valor de  es {} y el de y és {}".format(x, y))

"""
#Aqui imprime el nombre 
"""
def mayor(x,y):
    if x>y:
        return x
    else:
        return y
    
a = int(input("Intro el 1r número: "))
b = int(input("Intro el 2n número: "))
c = mayor(a, b)
print("El mayor de {} y {} és {}".format(a,b,c))
"""
#función que contiene una lista 
"""
def cambio(l): 
    #Te pide que introduzcas el valor de la posicion de la listal quieras cambiar
    x = int(input("Introduce la posición a modificar: ")) 
    #Te pide que introduzcas el valor por el cual quieres sustituir
    l[x]= input("Introduce el valor a inserir: ")   



#Programa principal
a = [3, 4, 5, 6, 7, 8, "a", (1, 2),[3, 4], 10]
print("EL valor de la lista antes de cambiar es {}".format(a)) #Imprime la lista "a"

cambio(a) #posiciona el valor que he añadido

#Lee la lista con el cambio
print("El valor de la lista después de cambiar es: {}".format(a))
"""
#DIccionario cambios
"""
def cambio(l): 
    x = input("Introduce la posición a modificar: ")
    l[x]= int(input("Introduce el valor a inserir: "))   

#Programa principal
a = {"a":3, "b":5, "c":7, "d":9, "e":10}
print("el valor del diccionario antes de cambiar es: {}".format(a))
cambio(a)
print("El valor del diccionario después de cambiar es: {}".format(a))
"""
def cambio(l,m,n): 
    print("1) {}{} \n {}".format(l, m, n))
    l = "Adiós, "
    m = "Sebas"
    n ="Qué te vaya bien"
    print("2){}{} \n {}".format(l, m, n))

#Programa principal
a = "Hola, "
b = "Ramis."
c ="¿Como estás?"
print("eL valor de la variable antes de cambiar es: {}{} \n {}".format(a, b, c))
cambio(a, b, c)
print("eL valor de la variable después de cambiar es: {}{} \n {}".format(a, b, c))


