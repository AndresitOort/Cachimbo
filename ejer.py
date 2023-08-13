#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:49:10 2022

@author: andresestebanortizjimenez


"""

catalogo = [
    {
    
    'nombre': 'perfume',
    'precio': 5000
    },
    {
    'nombre': 'shampoo',
    'precio': 100000
    },
    {
     'nombre': 'desodorante',
     'precio': 200
     }, 
    {
     'nombre': 'elver',
     'precio': 400000000
    }
    
    ]

masBarato = ''




def producto_barato(catalogo):
    
    for i in catalogo:
        for j in catalogo:
            
            if j['precio']<i['precio'] and i['nombre'] != j['nombre']:
                
                masBarato = j['nombre']
                
    return masBarato
        
                
    
            
    
    
    


print(producto_barato(catalogo))
    


            
            
            

    

