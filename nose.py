def cantidad_digitos(num:int)->int:
    
    numerito= abs(num)
    digitos=0
    finalizado=False
    ceros=0
    
    while finalizado==False:
        
        if numerito==0:
            finalizado=True
        
        elif numerito%10==0:    
            numerito=numerito//10
            ceros+=1
        
        else:
            numerito=numerito//10
            digitos+=1
            
    print("La cantidad de dígitos en el número que ingresaste es de: {0}".format(digitos+ceros))
    
    

def cantidadDigitos(num:int)->int:
    
    numerito= abs(num)
    cincoYcero=0
    
    while numerito>0:
        
        if numerito%10==0:
            cincoYcero+=1
            numerito=numerito//10
            
        elif numerito%10==5:
            cincoYcero+=1
            numerito=numerito//10
        
        else:
            numerito=numerito//10
            
    print("La cantidad de cincos o ceros en el número que ingresaste es de: {0}".format(cincoYcero))
