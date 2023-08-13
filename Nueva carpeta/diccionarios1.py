
def mayor_promedio(estudiante1:dict, estudiante2:dict, estudiante3:dict, estudiante4:dict)->dict:
    
    estMejor={}
    
    prom1= estudiante1["promedio"]
    prom2= estudiante2["promedio"]
    prom3= estudiante3["promedio"]
    prom4= estudiante4["promedio"]
    
    if prom1>prom2 and prom1>prom3 and prom1>prom4:
        estMejor = estudiante1
        print(estudiante1['promedio'])
        
    elif prom2>prom1 and prom2>prom3 and prom2>prom4:
        estMejor = estudiante2
        print(estudiante2['promedio'])
        
    elif prom3>prom2 and prom3>prom1 and prom3>prom4:
        estMejor = estudiante3
        print(estudiante3['promedio'])
        
    else:
        estMejor = estudiante4
        print(estudiante4['promedio'])
        
    
    return estMejor
        
    
        