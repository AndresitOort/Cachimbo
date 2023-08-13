
def calcular_constante_K2(m1: float, m2: float)->float:
    g= 6.67e-11
    pi=3.14
    k1=4*pow((pi),2)
    k2= g*(m1+m2)
    kt= k1/k2
    return kt

def calcular_distancia_media_satelite(m1: float, m2: float, periodo: float)-> float:
    d1=pow(periodo,2)
    d2= calcular_constante_K2(m1, m2)
    d3= d1/d2
    df= pow(d3,1/3)
    return df

def reportar_distancia (cuerpo1: str, cuerpo2: str ,m1:float ,m2:float, periodo: float)->str:
    d= str(round(calcular_distancia_media_satelite(m1, m2, periodo)))
    
    return print("La órbita de", cuerpo2,"alrededor de", cuerpo1, "es de",d, "Kms usando la masa de ambos cuerpos." )
 
    
    
    