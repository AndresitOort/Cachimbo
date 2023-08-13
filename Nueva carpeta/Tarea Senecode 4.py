


def encontrar_mayor(entrada:list)->int:
    
    mayor=0
    
    if len(entrada)==0:
        return -1
    
    for i in entrada:
        
        if i>mayor:
            mayor=i
            
    return mayor


def buscar_elemento(entrada:list,buscado:int)->int:
    
    
    for i in entrada:
        
        if i==buscado:
            return entrada.index(i)
    
    return -1

def conteo_min_y_max(num_min:int,num_max:int,numeros:list)->str:
    
    numerosMax=0
    numerosMin=0
    numerosEntre=0
    
    for i in numeros:
        
        if i>num_max:
            numerosMax+=1
            
        elif i<num_min:
            numerosMin+=1
            
        elif i>num_min and i<num_max:
            numerosEntre+=1
    
    return "Hay {0} menores, {1} mayores y {2} dentro del intervalo".format(numerosMin,numerosMax,numerosEntre)
        

def producto_mas_barato(catalogo:dict)->str:
    
    masBarato=10000000000000
    articulo=""
    
    if catalogo=={}:
        return "No hay productos para escoger"
    
    for i in catalogo.keys():
        
        if catalogo[i]<masBarato:
            masBarato=catalogo[i]
            articulo=i
            
        elif catalogo[i]==masBarato:
            articulo=min(i,articulo)
            
    if masBarato>10000:
        return None
        
    return articulo
    

def comprar_jugador(jugadores: list, monedas: int)->str:
    
    valor=0
    nombre=None
    puntaje=0
    
    for i in jugadores:
        
        if i['media']>puntaje:
                
            if i['precio']<monedas:
                    
                valor= i['precio']
                nombre= i['nombre']
                puntaje= i['media']
                
        elif i['media']==puntaje:
                
            if i["precio"]<valor:
                valor=i["precio"]
                nombre=i["nombre"]
            
    else:
        return (nombre)
            
def contar_caracteres_repetidos(cadena:str)->int:
    
    repeticiones=0
    letras={}
    
    for i in cadena:
        
        if i in letras:
            letras[i]+=1
        
        else:
            letras[i]=1
    
    for i in letras:
        
        if letras[i]>=2:
            
            repeticiones+=1
        
    return repeticiones        
        
    
    
    

    
    
    
    
    
    