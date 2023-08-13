# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz (M,N,3) con la imagen cargada.
    """

    imagen = mpimg.imread(ruta_imagen).tolist()
    return imagen


def visualizar_imagen(imagen: list)->None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()


def convertir_negativo(imagen: list)->list:
    """  Convierte la imagen en negativo.
    El negativo se calcula cambiando cada componente RGB, tomando el valor absoluto de restarle al componente 1.0.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convertir a negativo.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            for k in range(3):
                nuevo = abs(imagen[i][j][k] - 1)
                imagen[i][j][k] = nuevo
    return imagen


def reflejar_imagen(imagen: list)->list:
    
    alto = len(imagen)
    
    for i in range(alto):
        fila= imagen[i]
        imagen[i]= fila[::-1]
    
    return imagen


def binarizar_imagen(imagen: list, umbral: float)->list:
    
    alto= len(imagen)
    ancho= len(imagen[0])
    
    for i in range(0,alto):
        for j in range(0,ancho):
            promedio=0
            for k in range(0,3):
                
                promedio+=imagen[i][j][k]
            
            promedioF= promedio/3
            
            if promedioF >= umbral:
                imagen[i][j]= [1.0]*3
                
            else:
                imagen[i][j]=[0]*3
            
    return imagen


def convertir_a_grises(imagen: list)->list:
    
    alto= len(imagen)
    ancho= len(imagen[0])
    
    for i in range(0,alto):
        for j in range(0,ancho):
            promedio=0
            for k in range(0,3):
                promedio+=imagen[i][j][k]
            
            promedioF=promedio/3
            imagen[i][j]=[promedioF]*3
            
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada pixel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convertir a grises.
    """
    return imagen







