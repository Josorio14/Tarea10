def nombres_que_comienzan_por(lista_nombres):
    contador = 0   #contador se usará para contar cuántos nombres comienzan con la letra 'a'.
    for nombre in lista_nombres: #Inicia un bucle que recorre cada elemento 
        if nombre.lower().startswith('a'): #Se utiliza el método startswith para verificar si el nombre comienza con la letra especificada.
            contador += 1
    return contador

print("Introduce nombres y sepáralos por espacios")
a = input("Lista: ")

lista_numeros = []
for elemento in a.split():
    lista_numeros.append(elemento)

resultado = nombres_que_comienzan_por(lista_numeros)
print("Hay {} nombres que comienzan por la letra 'a' ".format(resultado))