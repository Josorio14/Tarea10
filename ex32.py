def nombres_que_comienzan_por(lista_nombres, letra):
    contador = 0
    for nombre in lista_nombres: #Se inicia un bucle que recorre cada nombre en la lista
        if nombre.lower().startswith(letra.lower()): #Se utiliza el método startswith para verificar si el nombre comienza con la letra especificada.
            contador += 1
    return contador

#Se imprime el mensaje que introduce con nombres separados por espacios.
print("Introduce nombres y sepáralos por espacios")
a = input("Lista: ")

letra_a_verificar = input("Introduce la letra para verificar el inicio de los nombres: ")

lista_nombres = a.split()
resultado = nombres_que_comienzan_por(lista_nombres, letra_a_verificar)

#Se imprime un mensaje indicando cuántos nombres comienzan con la letra especificada
print("Hay {} nombres que comienzan por la letra '{}' ".format(resultado, letra_a_verificar))