

import punto4 as p4 

def ejecutar_cmonedas()->None:
    dinero= int(input("Ingrese la cantidad a devolver: "))
    cambio= p4.cmonedas(dinero)
    print("Tu cambio en cantidad de monedas de: 500, 200, 100 y 50 corresponde a: ", cambio)
ejecutar_cmonedas()