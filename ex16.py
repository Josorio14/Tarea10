def voc(c):
  	return c.lower() in ["a","e","i","o","u"]

#Programa principal     
letra = input("Introduce una letra para ver si es vocal o no: ")

if voc(letra):
  print("La letra es vocal.")
else:
  print("No es vocal.")




