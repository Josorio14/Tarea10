from datetime import date

def obtener_datos_personales():
    datos_personas = []
    print("Introduce los nombres y las fechas de nacimiento de las 4 personas:")
    for i in range(4):
        nombre = input(f"Escribe el nombre de la {i+1}a persona: ")
        Año_de_nacimiento = input(f"Escribe el año de nacimiento de {nombre}: ")
        edad = date.today().year - int(Año_de_nacimiento)
        datos_personas.append((nombre, Año_de_nacimiento, edad))
    return datos_personas

# Programa Principal
aactual = date.today().year
personas = obtener_datos_personales()

print(f"El año actual es: {aactual}")
print("{:<20} {:<20} {:<20}".format('Nombre', 'Data de nacimiento', 'Años que tendrá en la actualidad'))

for persona in personas:
    print("{:<20} {:<20} {:<20}".format(*persona))