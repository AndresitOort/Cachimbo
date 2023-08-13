"""
Ejercicio nivel 3: Avistamiento de Ovnis
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import ovnis as ov

def ejecutar_cargar_datos() -> dict:
    
    avistamientos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con los avistamientos: ")
    avistamientos = ov.cargar_datos(archivo)
    if len(avistamientos) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los bloques.")
    else:
        print("Se cargaron los siguientes países con sus avistamientos a partir del archivo.")
        for key in avistamientos.keys():
            print(key)
    return avistamientos

def ejecutar_avistamientos_en_fecha(avistamientos:dict) -> None:

    fecha = input("Ingrese la fecha a buscar en formato 'YYYY-MM--DD': ")
    print(ov.avistamientos_en_fecha(avistamientos, fecha))

def ejecutar_avistamientos_por_ciudad(avistamientos:dict) -> None:

    print(ov.avistamientos_por_ciudad(avistamientos))

def ejecutar_avistamientos_mas_de_x_segundos(avistamientos:dict) -> None:
    
    limite = float(input("Ingrese el límite inferior de la duración de un avistamiento en segundos: "))
    print(ov.avistamientos_mas_de_x_segundos(avistamientos, limite))

def ejecutar_avistamientos_por_rango_de_fechas(avistamientos:dict) -> None:

    fecha_in = input("Ingrese la fecha de inicio a buscar en formato 'YYYY-MM--DD': ")
    fecha_fin = input("Ingrese la fecha final a buscar en formato 'YYYY-MM--DD': ")
    
    print(ov.avistamientos_por_rango_de_fechas(avistamientos, fecha_in, fecha_fin))

def ejecutar_avistamientos_en_radio_determinado(avistamientos:dict) -> None:
 
    lat = float(input("Ingrese la latitud del centro del radio: "))
    long = float(input("Ingrese la longitud del centro del radio: "))
    radio = float(input("Inserte la distancia del radio: "))
    
    print(ov.avistamientos_en_radio_determinado(avistamientos, lat, long, radio))
    

def ejecutar_minimo_x_avistamientos_en_mes(avistamientos:dict) -> None:


    cantidad_minima = int(input("Ingrese la cantidad mínima de avistamientos a buscar: "))
    fecha = input("Ingrese el mes y año de interés, en el formato YYYY-MM:")
    
    cantidadMes= ov.minimo_x_avistamientos_en_mes(avistamientos, cantidad_minima, fecha)
    
    if cantidadMes==False:
        print("En el estado mes {0} no hubo al menos {1} avistamientos.".format(fecha, cantidad_minima))
    
    else:
        print("En el estado mes {0} sí hubo al menos {1} avistamientos.".format(fecha, cantidad_minima))
        

def ejecutar_dar_avistamiento_mas_corto_y_largo_por_pais(avistamientos:dict) -> None:
   
    pais = input("Ingrese el pais para la búsqueda: ")
    print(ov.dar_avistamiento_mas_corto_y_largo_por_pais(avistamientos, pais))

def ejecutar_contar_avistamientos_por_forma(avistamientos:dict) -> None:
    
    print(ov.contar_avistamientos_por_forma(avistamientos))

def ejecutar_pais_con_mas_avistamientos_de_x_segundos(avistamientos:dict) -> None:
    """Ejecuta la opción que determina cual es el país con el mayor número de avistamientos, entre los
    que tienen una duración de al menos un número de segundos ingresado por el usuario.
    El mensaje que se le muestra al usuario debe tener el siguiente formato: 
    'El país con más avistamientos que duran al menos (#segundos) segundos es (país), 
    con (#avistamientos) avistamientos.'
    """
    duracion=float(input("Ingresa la duración mínima del avistamiento: "))
    demanda= ov.pais_con_mas_avistamientos_de_x_segundos(avistamientos, duracion)
    print("El país con más avistamientos que duran al menos {0} segundos es {1}, con {2} avistamientos.".format(duracion, demanda["pais"],demanda["avistamientos"]))
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_avistamientos_que_contengan_cadena_en_comentarios(avistamientos:dict) -> None:
    
    cadena = input("Ingrese la cadena a buscar en los avistamientos: ")
    print(ov.avistamientos_que_contengan_cadena_en_comentarios(avistamientos, cadena))

def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de avistamientos.")
    print("2. Buscar avistamientos según una fecha.")
    print("3. Consultar los avistamientos por ciudad.")
    print("4. Consultar avistamientos con duración al menos de X segundos")
    print("5. Consultar los avistamientos en rango de fechas.")
    print("6. Consultar avistamientos dentro de un radio determinado.")
    print("7. Consultar si hubo cierta cantidad de avistamientos en un mes.")
    print("8. Consultar los avistamientos más largo y más corto de un país.")
    print("9. Consultar número de avistamientos por forma.")    
    print("10. Consultar país con mayor número de avistamientos que duran más de X segundos.")
    print("11. Consultar avistamientos que contengan una cadena.")
    print("12. Salir.") 

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    avistamientos = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            avistamientos = ejecutar_cargar_datos()
        elif opcion_seleccionada ==2:
            ejecutar_avistamientos_en_fecha(avistamientos)
        elif opcion_seleccionada ==3:
            ejecutar_avistamientos_por_ciudad(avistamientos)
        elif opcion_seleccionada ==4:
            ejecutar_avistamientos_mas_de_x_segundos(avistamientos)
        elif opcion_seleccionada ==5:
            ejecutar_avistamientos_por_rango_de_fechas(avistamientos)
        elif opcion_seleccionada ==6:
            ejecutar_avistamientos_en_radio_determinado(avistamientos)
        elif opcion_seleccionada ==7:
            ejecutar_minimo_x_avistamientos_en_mes(avistamientos)
        elif opcion_seleccionada ==8:
            ejecutar_dar_avistamiento_mas_corto_y_largo_por_pais(avistamientos)
        elif opcion_seleccionada ==9:
            ejecutar_contar_avistamientos_por_forma(avistamientos)
        elif opcion_seleccionada == 10:
            ejecutar_pais_con_mas_avistamientos_de_x_segundos (avistamientos)
        elif opcion_seleccionada == 11:
            ejecutar_avistamientos_que_contengan_cadena_en_comentarios(avistamientos)
        elif opcion_seleccionada == 12:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()