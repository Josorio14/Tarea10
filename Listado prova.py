

"""
a = [3,2,4,'a',[1,'b'],"Hola"]
print(a[0])
print(a[-1])
print(a[:])

print(a[-2:])
"""

b = [3,5,4,'a',(1 ,2 ,3), "Hola"]
b.append("Adios")
b.insert(1,5)
b.insert(5,'b')

b.extend([10,11,12])
b.pop(2)
print(b)