def contar_fijas(numero_secreto:int, numero_propuesto:int)->int:
    
    """Variables número secreto"""
    
    ns4= (numero_secreto//1)%10
    ns3= (numero_secreto//10)%10
    ns2= (numero_secreto//100)%10
    ns1= (numero_secreto//1000)%10
    
    """Variables número propuesto"""
    
    np4= (numero_propuesto//1)%10
    np3= (numero_propuesto//10)%10
    np2= (numero_propuesto//100)%10
    np1= (numero_propuesto//1000)%10
    
    """Variable de conteo"""
    
    fijitas=0

    if ns4==np4:
        fijitas+=1
    if ns3==np3:
        fijitas+=1
    if ns2==np2:
        fijitas+=1
    if ns1==np1:
        fijitas+=1
        
    return fijitas

def contar_picas(numero_secreto:int,numero_propuesto:int)->int:
    
    """Variables número secreto"""

    ns4= (numero_secreto//1)%10
    ns3= (numero_secreto//10)%10
    ns2= (numero_secreto//100)%10
    ns1= (numero_secreto//1000)%10

    """Variables número secreto"""

    np4= (numero_propuesto//1)%10
    np3= (numero_propuesto//10)%10
    np2= (numero_propuesto//100)%10
    np1= (numero_propuesto//1000)%10
    
    picas=0

    if np4==ns4 or np4==ns3 or np4==ns2 or np4==ns1:
        picas+=1
    if np3==ns4 or np3==ns3 or np3==ns2 or np3==ns1:
        picas+=1
    if np2==ns4 or np2==ns3 or np2==ns2 or np2==ns1:
        picas+=1
    if np1==ns4 or np1==ns3 or np1==ns2 or np1==ns1:
        picas+=1    
        
    return picas



