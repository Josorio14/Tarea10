# Aventura de los viajeros y los enigmas
import random
import time

# Función donde muestra la introducción a la historia. Utiliza triple comilla para definir un bloque de texto multilínea.
def intro():
    print("""
    En una tierra lejana donde viajeros buscan respuestas, tú y tus amigos deciden aventurarse,
    Siguen el camino indicado por las estrellas, pero se encuentran en un valle misterioso.
    Al final de cada sendero hay un templo antiguo, en uno viven sabios que los guiarán hacia el conocimiento,
    y en el otro, unos guardianes que los pondrán a prueba con enigmas complejos.
    """)

# Función donde nos preguntan a qué templo queremos ir "1" o "2"
def cambioTemplo():
    templo = ""
    while templo != "1" and templo != "2":
        templo = input("¿A qué Templo quieres entrar? Introduce 1 o 2: ")
    return templo

# Función que simula el encuentro con un enigma en uno de los templos.
#  Selecciona aleatoriamente si el jugador supera o no el enigma. 
# Actualiza los puntos del jugador y muestra un mensaje correspondiente.
def encuentro(cambioTemplo, puntos):

    # Imprimemensajes narrativos con pausas temporales usando 'time.sleep'
    print("Te estás acercando al templo...")
    time.sleep(2)
    print("Es un lugar mágico y lleno de misterio...")
    time.sleep(2)
    print("Una figura enigmática aparece, te mira y ...")
    print("")
    time.sleep(2)
    # Generar un número aleatorio (1 o 2) para representar al guardián del templo
    guardián = random.randint(1, 2)
    # Verifica si la elección del jugador (cambioTemplo) coincide con el guardián
    if cambioTemplo == str(guardián):
        puntos += 1
        print("Superas el enigma con éxito... Tienes {} puntos".format(puntos))
    else:
        print("Te has perdido en la confusión... ¡Ups! Tienes {} puntos".format(puntos))
        puntos -= 1

# Programa principal 
puntos = 0
nuevaAventura = "si"
while nuevaAventura == "s" or nuevaAventura == "si":
    intro()
    nTemplo = cambioTemplo()
    encuentro(nTemplo, puntos)
    nuevaAventura = input("¿Quieres vivir una nueva aventura? Introduce si o no: ")
    print("\n")
