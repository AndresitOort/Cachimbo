
def cantidad_digitos(numero:int)->int:
    
    digitos=0
    
    while numero>0:
        
            digitos+=1
            numero=numero//10
        
    return "El número que ingresaste tiene {0} dígitos.".format(digitos)

def cantidad2(numero:int)->int:
    
    ceros=0
    cincos=0
    
    while numero>0:
        
        if numero%10==0:
            ceros+=1
            numero=numero//10
        
        elif numero%10==5:
            cincos+=1
            numero=numero//10
        
        else:
            numero=numero//10
            
    return "El número que ingresaste tiene {0} ceros y {1} cincos.".format(ceros, cincos)