
def sucesion_fibonacci (cantidad_numeros:int)->str:
    
    primero=0
    segundo=1
    lista=[]
    reiteraciones=1
    
    while len(lista)<=cantidad_numeros:
        
        if reiteraciones%2!=0:
            lista.append(primero)
            primero+=segundo
        
        else:
            
            lista.append(segundo)
            segundo+=primero
       
        reiteraciones+=1
        
    return lista