# -*- coding: utf-8 -*-

import modulo as mod

def ejecutar_maximo_comun_divisor()->None:
    print("\nBuscando el máximo común divisor entre dos números")
    numero1 = int(input("Por favor digite el primer número: "))
    numero2 = int(input("Por favor digite el segundo número: "))
    mcd = mod.maximo_comun_divisor(numero1, numero2)
    print("\nEl máximo común divisor de ", numero1, " y ",numero2, "es: ", mcd)

def ejecutar_PUM()->None:
    print("Vamos a jugar al PUM")
    n = int(input("Por favor digite la cantidad de jugadores: "))
    x = int(input("Por favor digite el número escogido para el PUM: "))
    mod.jugar_PUM(n, x)

def mostrar_menu()->None:
    print("1. Encontrar máximo común divisor")
    print("2. Jugar PUM")
    print("3. Salir")

def iniciar_aplicacion()->None:
    
    mostrar_menu()
    opcion=int(input("Bienvenid@ al programa!.\n\nSeleccione una de las opciones: "))
    
    while opcion!=3:
        
        if opcion==1:
            ejecutar_maximo_comun_divisor()
            print("\n")
            mostrar_menu()
            opcion=int(input("Deseas probar otra función?, Ingresa una opción: "))
            
        elif opcion==2:
            ejecutar_PUM()
            opcion=int(input("Ingresa una opción: "))

            
        else:
            opcion=int(input("Ingrese una opción válida: "))
    
    print("\nMuchas gracias, vuelva pronto!")


iniciar_aplicacion()
