#Primera forma 
"""
a =[2,3,4]
print(a)
for i in a:
    b =i*i*i
    print(b)
"""
#Segunda forma 
"""
a =[2,3,4]
for i in range(len(a)):
    a[i]=a[i]*a[i]*a[i]
    print(a)
"""

#Tercera forma 
"""
a =[2,3,4]
for i, e in enumerate(a):
    a[i]=e*e*e
    print(a)
"""

#Busca y determina un elemento y si existen 2(ocurrencia) si no la hay da else"No més hi ha zero o una"
"""
l= (1, 4, 2,(1, 3, 3), 3, 4, 2, 1, 1)
def tercera_ocurrencia(l,e):
    #cUANTOS ELEMENTOS HAY EN LA TUPLA 
    a = l.count(e)
    if a==0:
        print("NO hay ocurrencias de este elemento")
    elif a==1:
        print("La primera ocurrencia del elementro está en la posición {}".format(l.index(e)))
    elif a==2:
        print("Hay más de una ocurrencia {}".format(l.index(e)))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e,(so+1))
        print(so)

    #Si es mayor que dos encontrara la tercera ocurrencia
    elif a>2:
        print("Hay más de dos ocurrencias {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e,(so+1))
        print(so)
    else:
        print("Valor no válido")



#Programa principal 
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1, 4, 2, 1)
e = int(input("Elegeixi l'element que vol cercar la 3a ocurrencia: "))
tercera_ocurrencia(l, e)
"""











