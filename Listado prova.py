
#Eercicios de listas
"""
a = [3,2,4,'a',[1,'b'],"Hola"]
print(a[0])
print(a[-1])
print(a[:])

print(a[-2:])
"""
#Aqui es otro ejercicio de listas
"""
b = [3,5,4,'a',(1 ,2 ,3), "Hola"]
b.append("Adios")
b.insert(1,5)
b.insert(5,'b')

b.extend([10,11,12])
b.pop(2)
print(b)
"""
#EJercicio de par y impar

"""
x = int(input("Introduce un número:"))
if x % 2==0:
    print("Es par")
else:
    print("es impar")
    """

#Programa principal     
a = 1
while a>0:
    print("""
    Menú:
    1. Mirar si un número és impar o par
    2.Salir
        """)
    a = int(input("Seleciona una opción:"))
    match a:
        case 1: #SI queremos ver si un número es o no par
            x = int(input("Escribe un número:"))
            if x % 2==0:
                print("Es par")
            else:
                print("Es impar")
        case 2:
            a = 0
 
