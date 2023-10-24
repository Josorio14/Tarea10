def menu_principal():
    print("""       
        menuprincipal:
        1.Calculadora enteros
        2.Calculadora reals
        3.Salir
        """)
    x = int(input("Elegir una opción"))
    if x>0 and x<4:
        return x
    else:
        return 0
    
#Programa principal
a = menu_principal()
print(a)

