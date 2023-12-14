def crear_llista_fitxer(fitxer):
    with open(fitxer, 'r') as f:
        llista = f.readlines()
    
    lparaules = [linea.rstrip('\n') for linea in llista] 
    print(lparaules)

# Programa Principal
crear_llista_fitxer('/home/cicles/AO/Tarea10/prova.txt')