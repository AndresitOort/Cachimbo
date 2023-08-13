
def menor_digito(numero:int)->int:
    
    numero=abs(numero)
    menor=numero
    
    for i in str(numero//1):
        
        numint=int(i)
        
        if numint<menor:
            menor=numint
         
    return menor
        
            
            
def mayor_digito(numero:int)->int:
    
    numero=abs(numero)
    mayor=0
    
    for i in str(numero//1):
        
        numint=int(i)
        
        if numint>mayor:
            mayor=numint
         
    return mayor


def es_primo(numero:int)->bool:
        
    if numero==2:
        return True
    
    for i in range(2,numero):
        
        if numero%i==0:
            return False
        
    return True
            
        

def palindromos(cadena:str)->bool:
    
    cadena= cadena.lower()
    cadena= cadena.replace(",","")
    cadena= cadena.replace(" ","")
    cadena= cadena.replace("á","a")
    cadena= cadena.replace("é","e")
    cadena= cadena.replace("í","i")
    cadena= cadena.replace("ó","o")
    cadena= cadena.replace("ú","u")
    
    indexacion=0
    indexneg= len(cadena)-1
    
    for i in cadena:
        
        if cadena[indexacion] == cadena[indexneg]:
            indexacion+=1
            indexneg-=1
        
        else:
            return False
        
    return True
        
        
        
        
        
        
