

def calcular_constante_k2(masa1: float, masa2: float)-> float:
    pi= 3.14
    g= 6.67e-11
    elipse= 4*pow(pi,2)
    fuerzag= g*(masa1+masa2)
    kepler= elipse/fuerzag
    return kepler

def calcular_distancia_media_satelite(masa1:float,masa2:float,periodo:float)->float:
    k=calcular_constante_k2(masa1, masa2)
    interna= pow(periodo,2)/k
    raiz= pow(interna,1/3)
    return raiz 

def reportar_distancia(cuerpo1:str,cuerpo2:str,masa1:float,masa2:float,periodo:float)-> str:
    orbita= round(calcular_distancia_media_satelite(masa1, masa2, periodo))
    orbitaf= str(orbita/1000)
    return "La órbita de"+" "+cuerpo2+" "+"alrededor de"+" "+cuerpo1+" "+"es de"+" "+orbitaf+" kms usando la masa de ambos cuerpos." 