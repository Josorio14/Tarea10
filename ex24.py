def gran_lista():
    a = 'l'
    l = []
    while a!= 'fin':
        a = input("Introduce un número en la lista, para terminarla añade un 'fin' : ")
        if a!= 'fin':
            l.append(int(a))
            
    if l: 
        return max(l)
    else:
        return None 

resultado = gran_lista()
print("El número más grande de la lista és: {}".format(resultado))