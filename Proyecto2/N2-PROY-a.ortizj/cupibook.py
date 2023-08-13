
def crear_amigo( nombre: str, fecha_de_nacimiento: int,
                 genero: str, genero_musical_favorito: str,
                 genero_literario_favorito: str,
                 numero_de_likes: int,
                 numero_de_publicaciones: int, cantidad_de_amigos: int,
                 bloqueado: bool) -> dict:
    
    signo=asignar_signo_zodiacal(fecha_de_nacimiento)
    
    amigue={"nombre":nombre, "fecha_de_nacimiento":fecha_de_nacimiento,"genero":genero,"signo_zodiacal":signo,
            "genero_musical_favorito":genero_musical_favorito,"genero_literario_favorito":genero_literario_favorito,
            "likes":numero_de_likes,"numero_de_publicaciones":numero_de_publicaciones,
            "cantidad_de_amigos":cantidad_de_amigos,"bloqueado":bloqueado}
    
    return amigue



def buscar_amigo_por_nombre( nombre:str, a1: dict, a2: dict, a3: dict, 
                            a4: dict ) -> dict:
    
    nombreA1= a1.get("nombre")
    nombreA2= a2.get("nombre")
    nombreA3= a3.get("nombre")
    nombreA4= a4.get("nombre")
        
    if nombre==nombreA1:
        return a1
    elif nombre==nombreA2:
        return a2
    elif nombre==nombreA3:
        return a3
    elif nombre==nombreA4:
        return a4
    else:
        return None
        
   

def buscar_amigo_con_mas_likes( a1: dict, a2: dict, a3: dict,
                               a4: dict ) -> dict:
    
    likesA1= a1["likes"]
    likesA2= a2["likes"]
    likesA3= a3["likes"]
    likesA4= a4["likes"]
    
    if likesA1>likesA2 and likesA1>likesA3 and likesA1>likesA4:
        return a1
    elif likesA2>likesA1 and likesA2>likesA3 and likesA2>likesA4:
        return a2
    elif likesA3>likesA1 and likesA3>likesA2 and likesA3>likesA4:
        return a3
    else:
        return a4
    

def buscar_amigo_con_menos_publicaciones( a1: dict, a2: dict, a3: dict,
                                         a4: dict ) -> dict:
    
    publicacionesA1= a1["numero_de_publicaciones"]
    publicacionesA2= a2["numero_de_publicaciones"]
    publicacionesA3= a3["numero_de_publicaciones"]
    publicacionesA4= a4["numero_de_publicaciones"]
    
    if publicacionesA1<publicacionesA2 and publicacionesA1<publicacionesA3 and publicacionesA1<publicacionesA4:
        return a1
    elif publicacionesA2<publicacionesA1 and publicacionesA2<publicacionesA3 and publicacionesA2<publicacionesA4:
        return a2
    elif publicacionesA3<publicacionesA1 and publicacionesA3<publicacionesA2 and publicacionesA3<publicacionesA4:
        return a3
    else: 
        return a4
    

def asignar_signo_zodiacal( fecha: int ) -> str:
    
    mmdd= fecha%10000
    diaz= mmdd%100
    mes= mmdd//100
    
    if (mes==12 and diaz>=22) or (mes==1 and diaz <=20):
        return "CAPRICORNIO"
    
    elif (mes==1 and diaz>=21) or (mes==2 and diaz <=19):
        return "ACUARIO"
    
    elif (mes==2 and diaz>=20) or (mes==3 and diaz <=20):
        return "PISCIS"
    
    elif (mes==3 and diaz>=21) or (mes==4 and diaz <=20):
        return "ARIES"

    elif (mes==4 and diaz>=21) or (mes==5 and diaz <=21):
        return "TAURO"
    
    elif (mes==5 and diaz>=22) or (mes==6 and diaz <=21):
        return "GEMINIS"
    
    elif (mes==6 and diaz>=22) or (mes==7 and diaz <=22):
        return "CANCER"
    
    elif (mes==7 and diaz>=23) or (mes==8 and diaz <=22):
        return "LEO"
    
    elif (mes==8 and diaz>=23) or (mes==9 and diaz <=22):
        return "VIRGO"
    
    elif (mes==9 and diaz>=23) or (mes==10 and diaz <=22):
        return "LIBRA"
    
    elif (mes==10 and diaz>=23) or (mes==11 and diaz <=22):
        return "ESCORPIO"
    
    else:
        return "SAGITARIO"
    
    
def es_cupiamigo( amigo1: dict , amigo2: dict) -> bool:
    
    amigoA1= amigo1["cantidad_de_amigos"]
    blockA1= amigo1["bloqueado"]
    musicaA1= amigo1["genero_musical_favorito"]
    literaturaA1= amigo1["genero_literario_favorito"]
    
    amigoA2= amigo2["cantidad_de_amigos"]
    blockA2= amigo2["bloqueado"]
    musicaA2= amigo2["genero_musical_favorito"]
    literaturaA2= amigo2["genero_literario_favorito"]
    
    signoCompatible= signo_es_compatible(amigo1, amigo2)
    
    cupiamigos=0
    
    if (amigoA1>=3) and (amigoA2>=3):
        cupiamigos=True
    else:
        return False
    
    if (blockA1==False) and (blockA2==False):
        cupiamigos=True
    else:
        return False
    
    if musicaA1==musicaA2:
        cupiamigos=True
    else:
        return False
    
    if literaturaA1==literaturaA2:
        cupiamigos=True
    else:
        return False
    
    if signoCompatible==True:
        cupiamigos=True
    else:
        return False
    
    return cupiamigos
    



def es_cupienemigo( amigo:dict ) -> bool:
    
    if amigo["bloqueado"]==True:
        return True
    
    elif (amigo["likes"]<5) and (amigo["cantidad_de_amigos"]==0):
        return True
    
    else:
        return False
    

def signo_es_compatible( amigo1: dict, amigo2: dict ) -> bool:
    
    
    signoA1= amigo1["signo_zodiacal"]  
    A2=amigo2["signo_zodiacal"]
    amigue= signosCompatibles(A2)
    
    if signoA1 in amigue:
        return True
    else:
        return False
    


def amigo_mas_compatibilidad( a1: dict, a2: dict,
                               a3: dict, a4: dict ) -> dict:
    
    amigue1=0
    amigue2=0
    amigue3=0
    amigue4=0
    
    
    if a1["cantidad_de_amigos"]>5:
        amigue1+=1
        
    if a2["cantidad_de_amigos"]>5:
        amigue2+=1
    
    if a3["cantidad_de_amigos"]>5:
        amigue3+=1
    
    if a4["cantidad_de_amigos"]>5:
        amigue4+=1
        
        
        
    if a1["bloqueado"]==True:
        amigue1-=10
    
    if a2["bloqueado"]==True:
        amigue2-=10
    
    if a3["bloqueado"]==True:
        amigue3-=10
     
    if a4["bloqueado"]==True:
        amigue4-=10
        
        
        
    if (a1["genero_musical_favorito"]=="pop") or  (a1["genero_musical_favorito"]=="rap") or  (a1["genero_musical_favorito"]=="salsa"):
        amigue1+=2
    else:
        amigue1+=1
        
    if (a2["genero_musical_favorito"]=="pop") or (a2["genero_musical_favorito"]=="rap") or (a2["genero_musical_favorito"]=="salsa"):
        amigue2+=2
    else:
        amigue2+=1
        
    if (a3["genero_musical_favorito"]=="pop") or  (a3["genero_musical_favorito"]=="rap") or  (a3["genero_musical_favorito"]=="salsa"):
        amigue3+=2
    else:
        amigue3+=1
        
    if (a4["genero_musical_favorito"]=="pop") or  (a4["genero_musical_favorito"]=="rap") or  (a4["genero_musical_favorito"]=="salsa"):
        amigue4+=2
    else:
        amigue4+=1
        
    
    if (a1["genero_literario_favorito"]=="drama") or (a1["genero_literario_favorito"]=="ciencia ficción"):
        amigue1+=1
    elif a1["genero_literario_favorito"]=="lírico":
        amigue1-=1
        
    if (a2["genero_literario_favorito"]=="drama") or (a2["genero_literario_favorito"]=="ciencia ficción"):
        amigue2+=1
    elif a2["genero_literario_favorito"]=="lírico":
        amigue2-=1
        
    if (a3["genero_literario_favorito"]=="drama") or (a3["genero_literario_favorito"]=="ciencia ficción"):
        amigue3+=1
    elif a3["genero_literario_favorito"]=="lírico":
        amigue3-=1
        
    if (a4["genero_literario_favorito"]=="drama") or (a4["genero_literario_favorito"]=="ciencia ficción"):
        amigue4+=1
    elif a4["genero_literario_favorito"]=="lírico":
        amigue4-=1
         
       
    if (amigue1>amigue2) and (amigue1>amigue3) and (amigue1>amigue4):
        return a1
    elif (amigue2>amigue1) and (amigue2>amigue3) and (amigue2>amigue4):
        return a2
    elif (amigue3>amigue1) and (amigue3>amigue2) and (amigue3>amigue4):
        return a3
    else:
        return a4
    

def contar_amigos_con_generos(a1: dict, a2: dict,
                                a3: dict, a4: dict, genero_musical:str,
                                genero_literario: str) -> int:
    
    coincidencias=0
    
    if (a1["genero_musical_favorito"]==genero_musical) and (a1["genero_literario_favorito"]==genero_literario):
        coincidencias+=1
        
    if (a2["genero_musical_favorito"]==genero_musical) and (a2["genero_literario_favorito"]==genero_literario):
        coincidencias+=1
        
    if (a3["genero_musical_favorito"]==genero_musical) and (a3["genero_literario_favorito"]==genero_literario):
        coincidencias+=1
    
    if (a4["genero_musical_favorito"]==genero_musical) and (a4["genero_literario_favorito"]==genero_literario):
        coincidencias+=1
        
    return coincidencias


def signosCompatibles(amigue:str)->dict:
    
    comp= amigue
    dictAmigue= {comp:{}}
    
    ari={"GEMINIS","LEO","LIBRA","SAGITARIO"}
    tau={"TAURO","CANCER","VIRGO","LIBRA","ESCORPIO","CAPRICORNIO","PISCIS"}
    gem={"ARIES","LEO","LIBRA","ACUARIO"}
    can={"TAURO","VIRGO","ESCORPIO","PISCIS"}
    leo={"ARIES","GEMINIS","LEO","VIRGO","LIBRA"}
    vir={"TAURO","CANCER","LEO","VIRGO","ESCORPIO","CAPRICORNIO","PISCIS"}
    lib={"ARIES","TAURO","GEMINIS","LEO","LIBRA","ACUARIO"}
    esc={"TAURO","CANCER","VIRGO","PISCIS"}
    sag={"ARIES","SAGITARIO","ACUARIO"}
    cap={"TAURO","VIRGO","PISCIS"}
    acu={"GEMINIS","LIBRA","SAGITARIO","ACUARIO"}
    pis={"TAURO","CANCER","VIRGO","ESCORPIO","CAPRICORNIO"}
    
    signoAmigue=0
    
    if comp=="ARIES":
        signoAmigue=dictAmigue[comp] = ari
        return signoAmigue
    
    elif comp=="TAURO":
        signoAmigue=dictAmigue[comp] = tau
        return signoAmigue
    
    elif comp=="GEMINIS":
        signoAmigue=dictAmigue[comp] = gem
        return signoAmigue
    
    elif comp=="CANCER":
        signoAmigue=dictAmigue[comp] = can
        return signoAmigue
    
    elif comp=="LEO":
        signoAmigue=dictAmigue[comp] = leo
        return signoAmigue
    
    elif comp=="VIRGO":
        signoAmigue=dictAmigue[comp] = vir
        return signoAmigue
    
    elif comp=="LIBRA":
        signoAmigue=dictAmigue[comp] = lib
        return signoAmigue
    
    elif comp=="ESCORPIO":
        signoAmigue=dictAmigue[comp] = esc
        return signoAmigue
    
    elif comp=="SAGITARIO":
        signoAmigue=dictAmigue[comp] = sag
        return signoAmigue
    
    elif comp=="CAPRICORINO":
        signoAmigue=dictAmigue[comp] = cap
        return signoAmigue
    
    elif comp=="ACUARIO":
        signoAmigue=dictAmigue[comp] = acu
        return signoAmigue
    
    else:
        signoAmigue=dictAmigue[comp] = pis
        return signoAmigue







