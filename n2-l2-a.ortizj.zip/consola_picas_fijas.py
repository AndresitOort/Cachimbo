import picas_fijas as pf
import random as rdm

def ejecutar_picas_y_fijas(numero_secreto:int,turnos:int)->bool:
    print("Le quedan "+str(turnos)+" turnos.")
    numero_propuesto=int(input("Ingrese su número a jugar: "))
    fijas= pf.contar_fijas(numero_secreto, numero_propuesto)
    picas= pf.contar_picas(numero_secreto, numero_propuesto)
    
    if fijas==4:
        print("Obtuvo "+str(picas)+" picas")
        return True
    else:
        pc=picas-fijas
        print("Obtuvo "+str(pc)+" picas")
        print("Obtuvo "+str(fijas)+" fijas")
        return False

def iniciar_aplicacion()->None:
    numero_s= rdm.randint(1000,9999)
    print("Bienvenido a picas y fijas")
    print(numero_s)
    turnos=5
    
    while turnos >0:
        if ejecutar_picas_y_fijas(numero_s, turnos)==True:
           return print("Has ganado, felicitaciones") 
        else:
            turnos-=1
    print("Has perdido, intentalo de nuevo")
            
        
iniciar_aplicacion()

