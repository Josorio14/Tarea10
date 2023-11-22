#Número 1
"""
if 4 in x:
    print("4 esta dentro de la lista" .format(x))
""" 

#Número 2
#Te contara cuantos carácteres de 4 hay, el resultado es 2
"""
a =[3,27,4,'hola','b',27,4]
b = a.count(4)
print(b)
"""

#Número 3
#Te contara la lista entera no sé porque
"""
a =[3,27,4,'hola','b',27,4]
e = a[::-1]
print(e)
"""

#Número 4
#TSirve para unir los carácteres, lo leera como "234"
"""
a =["2","3","4"]
b = "".join(a)
print(b)
""" 

#Número 5
#Ordena la lista de menor a mayor
"""
a =[3, 5, 27, 30, 16, 4]
a.sort()
print(a)
"""

#Número 6
#Gira el sentido de la lista de derecha a izquierda
"""
a =[3, 5, 27, 30, 16, 4]
a.reverse()
print(a)
"""

#Número 7
#La primera orden lee la lista, la segunda la pasa a tupla 
# y la tercera la transforma de nuevo en una lista
"""
a =[1, 2, 3]
print(a)

b=tuple(a)
print(b)

c = list(b)
print(c)
"""


#Número 8-- FORMAS DE RECORRER UNA TUPLA --


#Número A
#Lee elemento a elemento
"""
a =[56, 42, 23]
for i in a:
    print(i)
"""

#Número B
#Lee añadiendo un índice y lo que tiene en orden
"""
a =[56, 42, 23]
for p in range(len(a)):
    print("Índice: {}, element: {}".format(p, a[p]))
"""
#Número C
#Es LO MISMO QUE EL NÚMERO B PERO DE OTRA MANERA ESCRITA
"""
a =[56, 42, 23]
for p, e in enumerate(a):
    print("Índice: {}, element: {}".format(p, e))
"""
#Número C

#Número 9-- DICCIONARIO -- al añadir asi el print detecta el valor nom y lee el contenido
"""
a = {"nombre": "joan", "Apellido": "Ramis", "edad":30,"teléfono:971360133}
print(a["nom"])
"""

#Número 10-- otro diccionario
"""
dic = {"nombre":"Joan", "apellido": "Ramis", "edad":30, "teléfono":"971360133"}

for element in dic:
    print("La clave {} tiene el valor {}".format(element,dic[element]))
"""
#dic.clear()
