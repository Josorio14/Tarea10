def gran_lista():
    a = 'l' # Inicia 'a' con un valor diferente de 'fin'
    l = [] # Inicializa una lista vacía 'l'
    # Utiliza un bucle 'while' para pedir que se introduzca números hasta que se añada 'fin'
    while a!= 'fin':
        a = input("Introduce un número en la lista, para terminarla añade un 'fin' : ")
        # Verifica si se añade 'fin', si no, agrega el número a la lista 'l'
        if a!= 'fin':
            l.append(int(a))
    # Verifica si la lista 'l' no está vacía
    if l: 
        return max(l)   # Retorna el número más grande de la lista utilizando la función 'max'
    else:
        return None    # Retorna 'None' si la lista está vacía

resultado = gran_lista()
print("El número más grande de la lista és: {}".format(resultado))