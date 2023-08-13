"""
Ejercicio nivel 2: Cupibook: La nueva red social
Modulo de interacción por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""

import cupibook as cb

def mostrar_amigo( amigo:dict ) -> None:
    
    nombre = amigo["nombre"]
    fecha_de_nacimiento = amigo["fecha_de_nacimiento"]
    signo_zodiacal = amigo["signo_zodiacal"]
    genero = amigo["genero"]
    genero_musical_favorito = amigo["genero_musical_favorito"]
    genero_literario_favorito = amigo["genero_literario_favorito"]
    numero_de_likes = amigo["likes"]
    numero_de_publicaciones = amigo["numero_de_publicaciones"]
    cantidad_de_amigos = amigo["cantidad_de_amigos"]
    bloqueado = amigo["bloqueado"]

    print("Nombre: " + nombre +
          "\n\nFecha de nacimiento: " + str(fecha_de_nacimiento) +
          "\n\nSigno zodiacal: " + signo_zodiacal +
          "\n\nGénero: " + genero +
          "\n\nGénero musical favorito: " + genero_musical_favorito +
          "\n\nGénero literario favorito: " + genero_literario_favorito +
          "\n\nNúmero de likes: " + str(numero_de_likes) +
          "\n\nNúmero de publicaciones: " + str(numero_de_publicaciones) +
          "\n\nNúmero de amigos: " + str(cantidad_de_amigos) +
          "\n\nBloqueado: " + str(bloqueado)
    )

def ejecutar_buscar_amigo_con_mas_likes( a1:dict, a2:dict, 
                                           a3:dict, a4:dict ) -> None:
    
    if cb.buscar_amigo_con_mas_likes(a1, a2, a3, a4)==a1:
        print("El amigo {0} es el amigo más famoso con {1} likes.".format(a1["nombre"], a1["likes"]))
    
    elif cb.buscar_amigo_con_mas_likes(a1, a2, a3, a4)==a2:
        print("El amigo {0} es el amigo más famoso con {1} likes.".format(a2["nombre"], a2["likes"]))
    
    elif cb.buscar_amigo_con_mas_likes(a1, a2, a3, a4)==a3:
        print("El amigo {0} es el amigo más famoso con {1} likes.".format(a3["nombre"], a3["likes"]))
    
    else:
        print("El amigo {0} es el amigo más famoso con {1} likes.".format(a4["nombre"], a4["likes"]))
    
 

def ejecutar_buscar_amigo_con_menos_publicaciones( a1:dict, a2:dict, 
                                                    a3:dict, a4:dict ) -> None:
    
    if cb.buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)==a1:
        print("El amigo {0} es el amigo con el menor número de publicaciones".format(a1["nombre"]))
    
    elif cb.buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)==a2:
        print("El amigo {0} es el amigo con el menor número de publicaciones".format(a2["nombre"]))
    
    elif cb.buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)==a3:
        print("El amigo {0} es el amigo con el menor número de publicaciones".format(a3["nombre"]))
    
    else: 
        print("El amigo {0} es el amigo con el menor número de publicaciones".format(a4["nombre"]))
    
    
    

def ejecutar_compatibilidad_segun_signo( a1:dict, a2:dict, 
                                         a3:dict, a4:dict ) -> None:
    
    nombre_amigo1 = input("Ingrese el nombre del primer amigo que \
                          desea buscar: ")
    nombre_amigo2 = input("Ingrese el nombre del segundo amigo que \
                          desea buscar: ")
    
    amigos1=0
    amigos2=0
                          
    if nombre_amigo1==a1["nombre"]:
        amigos1=a1
        
    elif nombre_amigo1==a2["nombre"]:
        amigos1=a2
        
    elif nombre_amigo1==a3["nombre"]:
        amigos1=a3
        
    elif nombre_amigo1==a4["nombre"]:
        amigos1=a4
        
    else:
        return print("El amigo llamado {0} no existe en Cupibook.".format(nombre_amigo1))
        
        
    if nombre_amigo2==a1["nombre"]:
        amigos2=a1
        
    elif nombre_amigo2==a2["nombre"]:
        amigos2=a2
        
    elif nombre_amigo2==a3["nombre"]:
        amigos2=a3
        
    elif nombre_amigo2==a4["nombre"]:
        amigos2=a4
    
    else:
        return print("El amigo llamado {0} no existe en Cupibook.".format(nombre_amigo2))
        
    
    if cb.signo_es_compatible(amigos1,amigos2)==True:
        return print("El amigo {0} y el amigo {1} son compatibles según su signo.".format(nombre_amigo1, nombre_amigo2))
    
    else: 
        return print("El amigo {0} y el amigo {1} no son compatibles según su signo.".format(nombre_amigo1, nombre_amigo2))
    
   

def ejecutar_determinar_cupiamigo( a1:dict, a2:dict, 
                                  a3:dict, a4:dict ) -> None:
    
    nombre_amigo1 = input("Ingrese el nombre del primer amigo que \
                          desea buscar: ")
    nombre_amigo2 = input("Ingrese el nombre del segundo amigo que \
                          desea buscar: ")
                          
    amigos1=0
    amigos2=0
                          
    if nombre_amigo1==a1["nombre"]:
        amigos1=a1
        
    elif nombre_amigo1==a2["nombre"]:
        amigos1=a2
        
    elif nombre_amigo1==a3["nombre"]:
        amigos1=a3
        
    elif nombre_amigo1==a4["nombre"]:
        amigos1=a4
        
    else:
         return print("El amigo {0} no existe en CupiBook.".format(nombre_amigo1))
        
        
    if nombre_amigo2==a1["nombre"]:
        amigos2=a1
        
    elif nombre_amigo2==a2["nombre"]:
        amigos2=a2
        
    elif nombre_amigo2==a3["nombre"]:
        amigos2=a3
        
    elif nombre_amigo2==a4["nombre"]:
        amigos2=a4
    
    else:
        return print("El amigo {0} no existe en CupiBook.".format(nombre_amigo2))

    
    if cb.es_cupiamigo(amigos1, amigos2)==True:
        print("El amigo {0} y el amigo {1} son Cupiamigos.".format(nombre_amigo1,nombre_amigo2))
    
    else:
        return print("El amigo {0} y el amigo {1} no son Cupiamigos.".format(nombre_amigo1, nombre_amigo2))
                          
    
   

def ejecutar_determinar_cupienemigo( a1:dict, a2:dict, 
                                     a3:dict, a4:dict ) -> None:
    
    nombre = input("Ingrese el nombre del amigo que desea buscar: ")
    amigo=0
    
    if nombre == a1["nombre"]:
        amigo=a1
        
    elif nombre == a2["nombre"]:
        amigo=a2
        
    elif nombre == a3["nombre"]:
        amigo=a3
        
    elif nombre == a4["nombre"]:
        amigo=a4
        
    else: 
         return print ("El amigo {0} no existe en Cupibook".format(nombre))
    
    
    if cb.es_cupienemigo(amigo)==True:
        print("El amigo {0} es un Cupienemigo.".format(amigo["nombre"]))
    
    else:
        print("El amigo {0} no es Cupienemigo.".format(amigo["nombre"]))
    
    

def ejecutar_amigo_mayor_compatibilidad( a1:dict, a2:dict, 
                                           a3:dict, a4:dict ) -> None:
    
    compatibilidad= cb.amigo_mas_compatibilidad(a1, a2, a3, a4)
    
    print(compatibilidad)



def ejecutar_amigos_genero_musical_y_literario( a1:dict, a2:dict, 
                                                  a3:dict, a4:dict ) -> None:
    
    genero_musical = input("Ingrese el género musical que desea consultar: ")
    genero_literario = input("Ingrese el género literario que desea \
                             consultar: ")
    
    coincidencias=cb.contar_amigos_con_generos(a1, a2, a3, a4, genero_musical, genero_literario)
    
    print("El número de amigos que tienen como género musical y como género literario favoritos {0} y {1} son {2}.".format(genero_musical,genero_literario,coincidencias))       

    

def iniciar_aplicacion() -> None:
    fecha_nacimiento_a1 = 19960117
    fecha_nacimiento_a2 = 20030510
    fecha_nacimiento_a3 = 20011108
    fecha_nacimiento_a4 = 19990327
    
    amigo1 = cb.crear_amigo("Pedro Sánchez", fecha_nacimiento_a1, "M", "pop", "drama", 100,
    20, 5, False) 
    amigo2 = cb.crear_amigo("Luna Ariza", fecha_nacimiento_a2, "O", "pop",
    "drama", 80, 10, 3, False)
    amigo3 = cb.crear_amigo("Paula Hernández", fecha_nacimiento_a3, "F", "salsa",
    "ciencia ficción", 1, 50, 2, False) 
    amigo4 = cb.crear_amigo("Tobías Fuentes", fecha_nacimiento_a4, "M", "rap", "lírico", 20, 1,
    0, True) 

    ejecutando = True
    while ejecutando:
        print("\nAmigos de Cupibook" + ("-"*50))
        print("Amigo 1\n")
        mostrar_amigo(amigo1)
        print("-"*50)

        print("Amigo 2\n")
        mostrar_amigo(amigo2)
        print("-"*50)

        print("Amigo 3\n")
        mostrar_amigo(amigo3)
        print("-"*50)

        print("Amigo 4\n")
        mostrar_amigo(amigo4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            amigo1, amigo2, amigo3, amigo4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion( a1: dict, a2: dict, a3: dict, a4: dict ) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar amigo con más likes")
    print(" 2 - Buscar amigo con menos publicaciones")
    print(" 3 - Calcular la compatibilidad de dos amigos según signo \
          zodiacal")
    print(" 4 - Determinar amigo Cupiamigo")
    print(" 5 - Determinar amigo Cupienemigo")
    print(" 6 - Recomendar amigo con mayor compatibilidad")
    print(" 7 - Contar amigos con género musical y literario favorito")
    print(" 8 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_amigo_con_mas_likes(a1, a2, a3, a4)
    elif opcion_elegida == "2":
        ejecutar_buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)
    elif opcion_elegida == "3":
        ejecutar_compatibilidad_segun_signo(a1, a2, a3, a4)
    elif opcion_elegida == "4":
        ejecutar_determinar_cupiamigo(a1, a2, a3, a4)
    elif opcion_elegida == "5":
        ejecutar_determinar_cupienemigo(a1, a2, a3, a4)
    elif opcion_elegida == "6":
        ejecutar_amigo_mayor_compatibilidad(a1, a2, a3, a4)
    elif opcion_elegida == "7":
        ejecutar_amigos_genero_musical_y_literario(a1, a2, a3, a4)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    return continuar_ejecutando



iniciar_aplicacion()

