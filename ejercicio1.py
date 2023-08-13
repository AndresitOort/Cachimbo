
def volumen_cilindro(radio: float, altura: float)->float:
    pi= 3.14
    area= pi*pow(radio,2)
    volumen= area*altura
    return round(volumen,1)