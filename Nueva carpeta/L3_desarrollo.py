
def buscar_elementos_iguales_seguidos(lista:list)->int:
    for i in range(len(lista)-1):
        if lista[i]==lista[i+1]:
            return i
    return -1


def contar_apariciones(lista1:list,lista2:list)->int:
    
    contador=0
    
    for i in range(0,len(lista1)):
        
        lista3=lista1[i:len(lista2)+i]
        
        if lista3==lista2:
            contador+=1
            
    return contador  


def sumaAcumulada (lista:list)->list:
    
    suma=[]
    
    for i in range(0,len(lista)):
        
        if i==0:
            suma.append(lista[i])
        
        else:
            suma.append(lista[i]+suma[i-1])
            
    return suma
        
        
            
    