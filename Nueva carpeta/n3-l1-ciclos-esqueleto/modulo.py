# -*- coding: utf-8 -*-

def maximo_comun_divisor(n1: int, n2: int)-> int:
    
    menor=min(n1,n2)
    mayor=max(n1,n2)
    divisor=menor
    
    while mayor%divisor!=0 or menor%divisor!=0:
        
        divisor-=1
        
    return "El Máximo común divisor entre {0} y {1} es {2}.".format(n1,n2,divisor)


def jugar_PUM(jugadores: int, numero: int)-> None:
    
    rango=1
    turnos=1
    
    while rango<=500:
        
        if turnos>jugadores:
            turnos=1
            
        if rango%numero==0:
            print(turnos,"PUM")
        
        else:
            print(turnos, rango)
            
        turnos+=1
        rango+=1
        
            