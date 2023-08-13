from math import radians, cos, sin, asin, sqrt

def distancia_entre_dos_puntos(lat1: float, lon1: float, lat2: float, lon2: float)-> float:
    
 lon1 = radians(lon1)
 lon2 = radians(lon2)
 lat1 = radians(lat1)
 lat2 = radians(lat2)
 dif_lon = lon2 - lon1
 dif_lat = lat2 - lat1
 a = sin(dif_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2)**2
 c = 2 * asin(sqrt(a))
 return c * 6371

def cargar_datos(ubicacion:str)->dict:
    
    avistamientosOvnis={}
    archivo= open(ubicacion, encoding='utf-8')
    encabezados= archivo.readline().split(",")
    lectura= archivo.readline()
    
    while len(lectura)>0:
        
        datos= lectura.split(",")
        paisAvistamiento=datos[3]
        caso={}
        
        if paisAvistamiento not in avistamientosOvnis:
            avistamientosOvnis[paisAvistamiento]=[]
        
        caso["datatime"]= datos[0]
        caso["city"]= datos[1]
        caso["state"]= datos[2]
        caso["shape"]= datos[4]
        caso["duration"]= datos[5]
        caso["comments"]= datos[6]
        caso["date posted"]= datos[7]
        caso["latitude"]= datos[8]
        caso["longitude"]= datos[9]
        avistamientosOvnis[paisAvistamiento].append(caso)
        
        lectura= archivo.readline()
        
    archivo.close()
    return avistamientosOvnis

def avistamientos_en_fecha(avistamientos:dict, fecha:str)->list:
    
    ovniVisto=[]
    
    for pais in avistamientos.values():
        
        for caso in pais:
            
            if caso["datatime"][:10]==fecha:
                
                ovniVisto.append(caso)
            
    return ovniVisto
            
            
def avistamientos_por_ciudad(avistamientos:dict)->dict:
    
    avistamientoCiudad={}
    
    for ovniVisto in avistamientos.values():
        
        for caso in ovniVisto:
            ciudad=caso["city"]
            del caso["city"]
            avistamientoCiudad[ciudad]=caso
        
    return avistamientoCiudad

    
def avistamientos_mas_de_x_segundos(avistamientos:dict,segundos:float)->dict:
    
    ovnisProlongados={}
    
    for ovniD in avistamientos:
        
        if ovniD not in ovnisProlongados:
            ovnisProlongados[ovniD]=[]
            ovni= avistamientos[ovniD]
            for caso in ovni:
                
                duracion=float(caso["duration"])
                
                if duracion>segundos:
                    ovnisProlongados[ovniD].append(caso)
                
            if ovnisProlongados[ovniD]==[]:
                del ovnisProlongados[ovniD]
                
    return ovnisProlongados



def avistamientos_por_rango_de_fechas(avistamientos:dict,fechaIn:str,fechaFin:str)->list:
    
    ovnisRango=[]
    
    for ovniR in avistamientos.values():
        
        for caso in ovniR:
            
            if caso["datatime"][:10]>fechaIn and caso["datatime"][:10]<fechaFin:
                ovnisRango.append(caso)
                
    return ovnisRango



def avistamientos_en_radio_determinado(avistamientos:dict,latitud:float,longitud:float,radio:float)->list:
    
    ovnisEnRadio=[]
    
    for ovniDistancia in avistamientos.values():
        
        for caso in ovniDistancia:
            
            lati=float(caso["latitude"])
            longi=float(caso["longitude"][:-1])
            
            if distancia_entre_dos_puntos(latitud, longitud, lati, longi) < radio:
                ovnisEnRadio.append(caso)
        
        return ovnisEnRadio
        


    
def minimo_x_avistamientos_en_mes(avistamientos:dict,cantidad:int,fecha:str)->bool:
    
    contadorAvistamientos=0
    
    for ovnisMes in avistamientos.values():
        
        for caso in ovnisMes:
            
            date=caso["datatime"][:7]
            
            if date==fecha:
               contadorAvistamientos+=1 
    
    if contadorAvistamientos>=cantidad:
        return True
    
    else: 
        return False
    


def dar_avistamiento_mas_corto_y_largo_por_pais(avistamientos:dict,pais:str)->dict:
    
    cortoLargo={}
    corto=100000000000
    largo=0
    
    for ovniPais in avistamientos:
        
        nacion= str(ovniPais)
        ufo=avistamientos[ovniPais]
        
        if pais==nacion:
            
            for caso in ufo:
                
                if float(caso["duration"])<corto:
                    corto=float(caso["duration"])
                    cortoLargo["corto"]=caso

                if float(caso["duration"])>largo:
                    largo=float(caso["duration"])
                    cortoLargo["largo"]=caso               
    
    return cortoLargo


def contar_avistamientos_por_forma(avistamientos:dict)->dict:
    
    conteoFormas={}
    
    for ovniShape in avistamientos.values():
        
        for caso in ovniShape:
            forma=caso["shape"]
            
            if forma in conteoFormas:
                conteoFormas[forma]+=1
            
            else:
                conteoFormas[forma]=1
    
    return conteoFormas

def pais_con_mas_avistamientos_de_x_segundos(avistamientos:dict,duracion:float)->dict:
    
    filtro=avistamientos_mas_de_x_segundos(avistamientos, duracion)
    masFrecuente={}
    repeticion=0
    
    for ovniS in filtro:
        casos=filtro[ovniS]
        
        if repeticion<len(casos):
            repeticion=len(casos)
            masFrecuente["pais"]=ovniS
            masFrecuente["avistamientos"]=len(casos)
        
    return masFrecuente



def avistamientos_que_contengan_cadena_en_comentarios(avistamientos:dict, cadena:str)->list:
    
    buscador=[]
    
    for ovniA in avistamientos.values():
        
        for caso in ovniA:
        
            if cadena in caso["comments"]:
                buscador.append(caso)
                
    return buscador 
    
a=cargar_datos("ovnis_limpio.csv")
print(pais_con_mas_avistamientos_de_x_segundos(a, 900000))
    

    


    
    