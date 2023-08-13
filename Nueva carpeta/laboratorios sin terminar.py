


def invertir_cadena(frase:str)->str:
    
    indexacion1=-2
    indexacion2=-1
    fraseNueva=""
    
    for invertir in frase:
        
        if fraseNueva=="":
            fraseNueva=frase[:-1]+invertir
                       
        else:
            
            fraseNueva=fraseNueva[:indexacion1]+invertir+fraseNueva[indexacion2:]
            indexacion1-=1
            indexacion2-=1
            
    return "Ahora tu frase es: {0}".format(fraseNueva)


def letra_mas_comun(cadena:str)->str:
        
    letraDic={}
    
    for i in cadena:
        
        if i in letraDic:
            letraDic[i]+=1
            
        else:
            letraDic[i]=1
            
    masRepetida= ""
    repeticiones=0
    
    for i in letraDic.keys():
            
        if letraDic[i]>repeticiones:
            masRepetida=i
            repeticiones=letraDic[i]
            
    return masRepetida
        
        
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
                