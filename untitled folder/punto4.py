
def cmonedas(dinero: int)-> str:
    
    m500= str(int(dinero/500))
    
    """En m500 dividimos el valor ingresado entre 500 para saber 
    cuántas monedas de 500 se podrían devolver como cambio,
    este valor está dado por el cociente."""
    
    r500= dinero%500
    
    """En r500 sacamos el residuo de la operación para luego ser
    dividida por la siguiente cantidad."""
    
    m200= str(int(r500/200))
    r200= r500%200
    m100= str(int(r200/100))
    r100= r200%100
    m50= str(int(r100/50))
    
    """Las variables comenzadas con 'r' indican el residuo, y las que empiezan
    por 'm' indican la cantidad de monedas como cambio."""
    
    """El proceso se repite hasta que el residuo ya no sea divisible
    por la siguiente moneda."""
    
    return m500+","+m200+","+m100+","+m50
    
"""Luego se imprimen en el orden indicado"""

