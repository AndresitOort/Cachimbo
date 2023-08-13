import examen_calculos_estelares as ecs

def ejecutar_reportar_distancia ()->None: 
    cuerpo1=str(input("Digita el nombre del cuerpo mayor: "))
    cuerpo2=str(input("Digita el nombre del cuerpo menor: "))
    masa1=float(input("Digita la masa del cuerpo mayor (En Kg): "))
    masa2=float(input("Digita la masa del cuerpo menor (En Kg): "))
    periodo= float(input("Digita el periodo (En segundos): "))
    distancia= ecs.reportar_distancia(cuerpo1, cuerpo2, masa1, masa2, periodo)
    print(distancia)

    
ejecutar_reportar_distancia()