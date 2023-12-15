# Importar la clase 'date' desde el módulo 'datetime'
from datetime import date

def obtener_datos_personales():
    # Inicia con una lista vacía para almacenar los datos de las personas.
    datos_personas = []
    # Introduce nombres y fechas de nacimiento para 4 personas.
    print("Introduce los nombres y las fechas de nacimiento de las 4 personas:")
    # Utiliza un bucle con 'for' para repetir la entrada de datos 4 veces.
    for i in range(4):
        # Solicita el nombre de la persona.
        nombre = input(f"Escribe el nombre de la {i+1}a persona: ")
        # Solicita el año de nacimiento de la persona.
        Año_de_nacimiento = input(f"Escribe el año de nacimiento de {nombre}: ")
        # Calcula la edad de la persona utilizando el año actual y el año de nacimiento.
        edad = date.today().year - int(Año_de_nacimiento)
        # Agrega los datos de la persona como una tupla a la lista 'datos_personas'.
        datos_personas.append((nombre, Año_de_nacimiento, edad))
    # Retorna la lista completa de datos de las personas.
    return datos_personas

# Programa Principal
aactual = date.today().year
personas = obtener_datos_personales()

print(f"El año actual es: {aactual}")
print("{:<20} {:<20} {:<20}".format('Nombre', 'Data de nacimiento', 'Años que tendrá en la actualidad'))

for persona in personas:
    print("{:<20} {:<20} {:<20}".format(*persona))