# -*- coding: utf-8 -*-
def crear_libro(nom: str, cod: str,autor: int, adp: int, cant: int, pdv: float, cpu: float)->dict:
    dic_libro = { "nombre": nom, 
                       "codigo": cod,  
                       "autor": autor, 
                       "añoPublicacion": adp,
                       "cantidad": cant,
                       "precio": pdv, 
                       "costoProduccion": cpu}
    return dic_libro

#PROGRAMA PRINCIPAL
libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200 , 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100 , 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien",1937, 50 , 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20 , 26000, 13000)


def mayor_ganancia(libro1: dict, libro2: dict, libro3: dict, libro4: dict)->dict:
    
    gananciaL1= libro1["precio"]-libro1["costoProduccion"]
    gananciaL2= libro2["precio"]-libro2["costoProduccion"]
    gananciaL3= libro3["precio"]-libro3["costoProduccion"]
    gananciaL4= libro4["precio"]-libro4["costoProduccion"]
    
    if gananciaL1>gananciaL2 and gananciaL1>gananciaL3 and gananciaL1>gananciaL4:
        print(libro1)
    elif gananciaL2>gananciaL1 and gananciaL2>gananciaL3 and gananciaL2>gananciaL4:
        print(libro2)
    elif gananciaL3>gananciaL1 and gananciaL3>gananciaL2 and gananciaL3>gananciaL4:
        print(libro3)
    else:
        return libro4