"""
n=int(input("Ingrese la dimensión de la matriz: "))

m=[]
i=0

while i<n:
    filaNueva=[0]*n
    filaNueva[i]=1
    m.append(filaNueva)
    i+=1
    
for fila in m:
    print(fila)
    
def calcular_suma_diagonal(diagonal_mayor: bool, matriz: list)->int:
    
    diagSum=0
    indexador=-1
    
    if diagonal_mayor==True:
        
        for i in range(len(matriz)):
            
            diagSum= diagSum+matriz[i][i]
        
        return diagSum
    
    else:
        
        for i in range(len(matriz)):
            
            diagSum= diagSum+matriz[i][indexador]
            indexador=indexador-1
        
        return diagSum
    

def calcular_multiplicacion_en_columna(matriz: list, columna: int)->int:
    
    mult=1
    
    for i in matriz:
        
        mult=mult*i[columna]
        
    return mult
        
"""

def hacer_la_vaca(salon: list, vaca: str)->tuple:
    
    mayorCantidad=0
    recolectado=0
    fila=0
    columna=0
    
    if vaca=="botella":
        
        for i in salon:
            for j in i:            
                recolectado+=j
                
                if j>mayorCantidad:
                    mayorCantidad=j
                    fila=salon.index(i)
                    columna=i.index(j)
                    
        if recolectado>=120000:
            return ('Hay Vaca',fila,columna)
        
        else:
            return ('No Alcanza',fila,columna)
        
        
    elif vaca=="pastel":
        
        for i in salon:
            for j in i:  
            
                recolectado+=j
                
                if j>mayorCantidad:
                    mayorCantidad=j
                    fila=salon.index(i)
                    columna=i.index(j)
                    
        if recolectado>=35000:
            return ('Hay Vaca',fila,columna)
        
        else:
            return ('No Alcanza',fila,columna)
        








