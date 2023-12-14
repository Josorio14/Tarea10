# Juego del MasterMind versión reducida

import random

# Elegimos un código de 4 dígitos entre 0 y 9
codigo = "".join(list(map(lambda x: str(x), random.sample(range(0, 9), 4))))
print("""
Este es tu primer Mastermind
Debes adivinar un número de 4 dígitos diferentes.
""")

tu_propuesta = input("Introduce un código de 4 dígitos: ")
# Hasta que no lo adivines, no sales del programa
intentos = 0
while tu_propuesta != codigo:
    intentos += 1
    aciertos = 0
    coincidencias = 0
    # Verificamos cuántos aciertos ha habido y cuántas coincidencias.
    for i in range(4):
        if tu_propuesta[i] == codigo[i]:
            aciertos += 1
        elif tu_propuesta[i] in codigo:
            coincidencias += 1
    print("Tu propuesta (", tu_propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")
    # Solicitamos otra propuesta
    tu_propuesta = input("Vuelve a introducir un código de 4 dígitos: ")
print("¡Felicidades! Has adivinado el código en", intentos, "intentos.")


