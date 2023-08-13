
def unSoloRecorrido(vuelos:dict)->str:
    
    aerolineaLider=None
    mayor=0
    masVuelos={}
    
    for i in vuelos:
        
        llave= vuelos[i]["aerolinea"]
        
        if llave in masVuelos:
            masVuelos[llave]+=1
        
        else:
            masVuelos[llave]=1
      
    for i in masVuelos.keys():
        
        if masVuelos[i]>mayor:
            mayor=masVuelos[i]
            aerolineaLider=i
            
    return aerolineaLider
        
print(unSoloRecorrido(vuelos={"XRT456":{"aerolinea":"XE","tiempo":1},"XRT486":{"aerolinea":"XE","tiempo":1},"XRY456":{"aerolinea":"ME","tiempo":1},"XJT456":{"aerolinea":"XE","tiempo":1},"XRT459":{"aerolinea":"XE","tiempo":1},"XRT436":{"aerolinea":"ME","tiempo":1}}))