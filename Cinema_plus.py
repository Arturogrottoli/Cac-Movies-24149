import json
import random
def añadir_pelicula(**kwargs): # asignacion de diccionario
    diccionario=kwargs
    return diccionario
def numerico(arg): # control numerico
    if arg.isdecimal()== True:
        control="ok"
    elif arg.isdecimal()== False:
        print("No ingreso una respuesta valida")
        control="no"
    return control
def espacios(arg): # control espacios
    if arg == "" or arg.isspace == True:
        control="no"
        print("No ingreso una respuesta valida")
    else:
        control="ok"
    return control
def grabar_pelicula(nombre_archivo,lista):
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista, archivo)
def buscar_pelicula(busqueda, peliculas):
    if busqueda == "id":
        for pelicula in peliculas:
            for clave, valor in pelicula.items():
                if clave == "Id":
                    print(f"{clave}. {valor}")
    elif busqueda == "titulo":
        for pelicula in peliculas:
            for clave, valor in pelicula.items():
                if clave == "Titulo":
                    print(f"{peliculas.index(pelicula) + 1}. {clave}. {valor}")
    else:
        print("No ingreso un valor valido")

with open("peliculas.json", "r") as archivo:
    peliculas = json.load(archivo)

lista_genero=["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
lista_clasificacion = ["ATP" , "PG" , "PG-13" , "R" , "NC-17"]

while True:
    opcion = (input("""
Bienvenida/o a CINEMA+.

1. ABM de peliculas
2. Calificación de títulos.
3. Reportes y estadísticas.
4. Salir 
Ingrese una opción: """))
    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        if int(opcion) == 1:
            while True:
                opcion_ABM = input("""
Sección ABM 

1. Alta de nueva película. 
2. Modificación de película existente 
3. Baja de película (eliminar) 
4. Volver. 
Ingrese una opción: """)
                if opcion_ABM == "1" or opcion_ABM == "2" or opcion_ABM == "3" or opcion_ABM == "4":
                    if int(opcion_ABM) == 1:
                        print("")
                        ids = []
                        for pelicula in peliculas:
                            for clave, valor in pelicula.items():
                                if clave == "Id":
                                    ids.append(valor)
                        ids.sort()
                        contador = 0
                        while True:
                            contador = contador + 1
                            if contador not in ids:
                                id = contador
                                break
                        while True:
                            titulo=input("Ingrese un titulo: ").capitalize()
                            if espacios(titulo) == "ok":
                                break
                        genero=[]
                        while True:
                            gen=input("""Ingrese el numero del generos.
1.Acción, 
2.Animación, 
3.Comedia, 
4.Drama, 
5.Ciencia ficción, 
6.Terror, 
7.Suspenso, 
8.Romántica
Opcion: """)
                            if numerico(gen) == "ok":
                                gen=int(gen)-1
                                if lista_genero[gen] not in genero:
                                    genero.append(lista_genero[gen])
                                else:
                                    print("El genero ya fue agregado anteriormente")
                                while True:
                                    res_genero =input("Quiere ingresar otro genero s/n: ").lower()
                                    if res_genero == "n" or res_genero == "s":
                                        break
                                    elif res_genero != "s":
                                        print("No ingreso una respuesta valida")
                                if res_genero == "n":
                                    break
                        while True:
                            duracion=input("Ingrese la duracion en minutos: ")
                            if numerico(duracion) == "ok":
                                duracion=int(duracion)
                                break
                        while True:
                            sinopsis=input("Ingrese la sinopsis: ").capitalize()
                            if espacios(sinopsis) == "ok":
                                break
                        while True:
                            pais_origen=input("Ingrese el pais de origen: ").capitalize()
                            if espacios(pais_origen) == "ok":
                                break
                        while True:
                            idioma=input("Ingrese el idioma: ").capitalize()
                            if espacios(idioma) == "ok":
                                break
                        while True:
                            clasificacion=input("Ingrese la clasificacion (ATP, PG, PG-13, R, NC-17): ").upper()
                            if clasificacion in lista_clasificacion:
                                break
                            else:
                                print("No ingreso una clasificación valida")
                        while True:
                            disponible=input("Indique disponibilidad s/n: ").lower()
                            if disponible == "s":
                                disponible=True
                                break
                            elif disponible == "n":
                                disponible=False
                                break
                            else:
                                print("No ingreso una respuesta valida")
                        pelicula=(añadir_pelicula(Id=id,
                        Titulo=titulo,
                        Genero=genero,
                        Duracion=duracion,
                        Sinopsis=sinopsis,
                        Pais_origen=pais_origen,
                        Idioma=idioma,
                        Clasificacion=clasificacion,
                        Calificacion=0.0,
                        Disponible=disponible))
                        while True:
                            cargar = input("Desea cargar la pelicula s/n: ").capitalize()
                            if cargar == "S":
                                peliculas.append(pelicula)
                                print("\nLa pelifula se cargo correctamente")
                                break
                            elif cargar == "N":
                                print("\nLa pelicula no fue cargada")
                                break
                            else:
                                print("No ingreso un valor valido")

                        peliculas.sort(key=lambda p: p["Id"])
                        grabar_pelicula("peliculas.json",peliculas)

                    elif int(opcion_ABM) == 2:
                        while True:
                            opcion_menu12 = input("""
Modificación de pelicula existente

1. Buscar por id.
2. Buscar por título
3. Volver
Ingrese una opción: """)
                            if opcion_menu12 == "1" or opcion_menu12 == "2" or opcion_menu12 == "3":
                                opcion_menu12 = int(opcion_menu12)
                                print("")
                                if opcion_menu12 == 1:
                                    busqueda = "id"
                                    buscar_pelicula(busqueda, peliculas)
                                    while True:    
                                        opcion_modificar = input("""
¿Que pelicula desea modificar?
ingrese un valor numerico: """)
                                        if numerico(opcion_modificar) == "ok":
                                            opcion_modificar=int(opcion_modificar)
                                            if len(peliculas) >= opcion_modificar and opcion_modificar > 0:
                                                break
                                    while True:    
                                        valor_modificar = input("""
¿Que desea modificar? 
1.Titulo
2.Genero
3.Duracion
4.Sinopsis
5.Pais de origen
6.Idioma
7.Clasificacion
8.Disponibilidad
Ingrese una opcion numerica: """)
                                        if numerico(valor_modificar) == "ok":
                                            valor_modificar=int(valor_modificar)
                                            break
                                    if valor_modificar == 1:
                                        valor_modificar = "Titulo"
                                        while True:
                                            modificar=input("Ingrese un nuevo titulo: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 2:
                                        valor_modificar = "Genero"
                                        modificar=[]
                                        while True:
                                            gen=input("""Ingrese el numero del generos.
1.Acción, 
2.Animación, 
3.Comedia, 
4.Drama, 
5.Ciencia ficción, 
6.Terror, 
7.Suspenso, 
8.Romántica
Opcion: """)
                                            if numerico(gen) == "ok":
                                                gen=int(gen)-1
                                                if lista_genero[gen] not in modificar:
                                                    modificar.append(lista_genero[gen])
                                                else:
                                                    print("El genero ya fue agregado anteriormente")
                                                while True:
                                                    res_genero =input("Quiere ingresar otro genero s/n: ").lower()
                                                    if res_genero == "n" or res_genero == "s":
                                                        break
                                                    elif res_genero != "s":
                                                        print("No ingreso una respuesta valida")
                                                if res_genero == "n":
                                                    break
                                    elif valor_modificar == 3:
                                        valor_modificar = "Duracion"
                                        modificar=input("Ingrese la nueva duracion en minutos: ")
                                        if numerico(modificar) == "ok":
                                            modificar=int(modificar)
                                            break
                                    elif valor_modificar == 4:
                                        valor_modificar = "Sinopsis"
                                        while True:
                                            modificar=input("Ingrese una nueva sinopcis: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 5:
                                        valor_modificar = "Pais_origen"
                                        while True:
                                            modificar=input("Ingrese un nuevo pais de origen: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 6:
                                        valor_modificar = "Idioma"
                                        while True:
                                            modificar=input("Ingrese un nuevo idioma: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 7:
                                        valor_modificar = "Clasificacion"
                                        while True:
                                            modificar=input("Ingrese la nueva clasificacion (ATP, PG, PG-13, R, NC-17): ").upper()
                                            if modificar in lista_clasificacion:
                                                break
                                            else:
                                                print("No ingreso una clasificación valida")
                                    elif valor_modificar == 8:
                                        valor_modificar = "Disponible"
                                        while True:
                                            modificar=input("Indique disponibilidad s/n: ").lower()
                                            if disponible == "s":
                                                modificar=True
                                                break
                                            elif disponible == "n":
                                                modificar=False
                                                break
                                            else:
                                                print("No ingreso una respuesta valida")
                                    while True:
                                        validar_modificar = input("¿Desea realizar la modificacion? (s/n): ").lower()
                                        if validar_modificar == "s":
                                            print("La pelicula fue modificada correctamente")
                                            peliculas[opcion_modificar - 1][valor_modificar] = modificar
                                            grabar_pelicula("peliculas.json",peliculas)
                                            break
                                        elif validar_modificar == "n":
                                            print("No se modifico la pelicula")
                                            break
                                        else:
                                            print("No ingreso una respuesta valida")
                                    break
                                elif opcion_menu12 == 2:
                                    busqueda = "titulo"
                                    buscar_pelicula(busqueda, peliculas)
                                    while True:    
                                        opcion_modificar = input("""
¿Que pelicula desea modificar?
ingrese un valor numerico: """)
                                        if numerico(opcion_modificar) == "ok":
                                            opcion_modificar=int(opcion_modificar)
                                            if len(peliculas) >= opcion_modificar and opcion_modificar > 0:
                                                break
                                    while True:    
                                        valor_modificar = input("""
¿Que desea modificar? 
1.Titulo
2.Genero
3.Duracion
4.Sinopsis
5.Pais de origen
6.Idioma
7.Clasificacion
8.Disponibilidad
Ingrese una opcion numerica: """)
                                        if numerico(valor_modificar) == "ok":
                                            valor_modificar=int(valor_modificar)
                                            break
                                    if valor_modificar == 1:
                                        valor_modificar = "Titulo"
                                        while True:
                                            modificar=input("Ingrese un nuevo titulo: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 2:
                                        valor_modificar = "Genero"
                                        modificar=[]
                                        while True:
                                            gen=input("""Ingrese el numero del generos.
1.Acción, 
2.Animación, 
3.Comedia, 
4.Drama, 
5.Ciencia ficción, 
6.Terror, 
7.Suspenso, 
8.Romántica
Opcion: """)
                                            if numerico(gen) == "ok":
                                                gen=int(gen)-1
                                                if lista_genero[gen] not in modificar:
                                                    modificar.append(lista_genero[gen])
                                                else:
                                                    print("El genero ya fue agregado anteriormente")
                                                while True:
                                                    res_genero =input("Quiere ingresar otro genero s/n: ").lower()
                                                    if res_genero == "n" or res_genero == "s":
                                                        break
                                                    elif res_genero != "s":
                                                        print("No ingreso una respuesta valida")
                                                if res_genero == "n":
                                                    break
                                    elif valor_modificar == 3:
                                        valor_modificar = "Duracion"
                                        modificar=input("Ingrese la nueva duracion en minutos: ")
                                        if numerico(modificar) == "ok":
                                            modificar=int(modificar)
                                            break
                                    elif valor_modificar == 4:
                                        valor_modificar = "Sinopsis"
                                        while True:
                                            modificar=input("Ingrese una nueva sinopcis: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 5:
                                        valor_modificar = "Pais_origen"
                                        while True:
                                            modificar=input("Ingrese un nuevo pais de origen: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 6:
                                        valor_modificar = "Idioma"
                                        while True:
                                            modificar=input("Ingrese un nuevo idioma: ").capitalize()
                                            if espacios(modificar) == "ok":
                                                break
                                    elif valor_modificar == 7:
                                        valor_modificar = "Clasificacion"
                                        while True:
                                            modificar=input("Ingrese la nueva clasificacion (ATP, PG, PG-13, R, NC-17): ").upper()
                                            if modificar in lista_clasificacion:
                                                break
                                            else:
                                                print("No ingreso una clasificación valida")
                                    elif valor_modificar == 8:
                                        valor_modificar = "Disponible"
                                        while True:
                                            modificar=input("Indique disponibilidad s/n: ").lower()
                                            if disponible == "s":
                                                modificar=True
                                                break
                                            elif disponible == "n":
                                                modificar=False
                                                break
                                            else:
                                                print("No ingreso una respuesta valida")
                                    while True:
                                        validar_modificar = input("¿Desea realizar la modificacion? (s/n): ").lower()
                                        if validar_modificar == "s":
                                            print("La pelicula fue modificada correctamente")
                                            peliculas[opcion_modificar - 1][valor_modificar] = modificar
                                            grabar_pelicula("peliculas.json",peliculas)
                                            break
                                        elif validar_modificar == "n":
                                            print("No se modifico la pelicula")
                                            break
                                        else:
                                            print("No ingreso una respuesta valida")
                                    break
                                elif opcion_menu12 == 3:
                                    break
                            else:
                                print("\nNo ingresaste un número válido\n")
                    elif int(opcion_ABM) == 3:
                        while True:
                            opcion_menu13 = input("""
Baja de pelicula existente

1. Buscar por id.
2. Buscar por título
3. Volver
Ingrese una opción: """)
                            if opcion_menu13 == "1" or opcion_menu13 == "2" or opcion_menu13 == "3":
                                opcion_menu13 = int(opcion_menu13)
                                print("")
                                if opcion_menu13 == 1:
                                    busqueda = "id"
                                    buscar_pelicula(busqueda, peliculas)
                                    while True:    
                                        opcion_borar = input("""
¿Que pelicula desea borar?
ingrese un valor numerico: """)
                                        if numerico(opcion_borar) == "ok":
                                            opcion_borar=int(opcion_borar)
                                            if len(peliculas) >= opcion_borar and opcion_borar > 0:
                                                break
                                    while True:
                                        validar_borar = input("¿Desea eliminar la pelicula? (s/n): ").lower()
                                        if validar_borar == "s":
                                            pelicula_borrar = peliculas.pop(opcion_borar - 1)["Titulo"]
                                            print(f"La pelicula {pelicula_borrar} fue eliminada correctamente")
                                            grabar_pelicula("peliculas.json",peliculas)
                                            break
                                        elif validar_borar == "n":
                                            print("La pelicula no se elimino")
                                            break
                                        else:
                                            print("No ingreso una respuesta valida")
                                    break
                                elif opcion_menu13 == 2:
                                    busqueda = "titulo"
                                    buscar_pelicula(busqueda, peliculas)
                                    while True:    
                                        opcion_borar = input("""
¿Que pelicula desea borar?
ingrese un valor numerico: """)
                                        if numerico(opcion_borar) == "ok":
                                            opcion_borar=int(opcion_borar)
                                            if len(peliculas) >= opcion_borar and opcion_borar > 0:
                                                break
                                    while True:
                                        validar_borar = input("¿Desea eliminar la pelicula? (s/n): ").lower()
                                        if validar_borar == "s":
                                            pelicula_borrar = peliculas.pop(opcion_borar - 1)["Titulo"]
                                            print(f"La pelicula {pelicula_borrar} fue eliminada correctamente")
                                            grabar_pelicula("peliculas.json",peliculas)
                                            break
                                        elif validar_borar == "n":
                                            print("La pelicula no se elimino")
                                            break
                                        else:
                                            print("No ingreso una respuesta valida")
                                    break
                                elif opcion_menu13 == 3:
                                    break
                            else:
                                print("\nNo ingresaste un número válido\n")    
                    elif int(opcion_ABM) == 4:
                        break
                else:
                    print("\nNo ingresaste un número válido\n")
        elif int(opcion) == 2:
            print("""
Calificacion de titulos:
Califique segun notas del 1 al 10""")
            listado_aleatorio = []
            contador_calificaciones = 0
            while True:
                numero_aleatorio = random.randint(1, len(peliculas))
                if numero_aleatorio not in listado_aleatorio:
                    contador_calificaciones = contador_calificaciones + 1
                    while True:
                        calificacion = input(f"""
{peliculas[numero_aleatorio - 1]["Titulo"]}
Ingrese una calificacion: """)
                        if numerico(calificacion) == "ok":
                            if int(calificacion) > 0 and int(calificacion) < 11:
                                break
                    calificaciones = peliculas[numero_aleatorio - 1]["Calificacion"]
                    promedio_cal= (calificaciones + int(calificacion)) / 2
                    peliculas[numero_aleatorio - 1]["Calificacion"] = promedio_cal
                    listado_aleatorio.append(numero_aleatorio)
                    if contador_calificaciones == 10:
                        break
            print("Muchas gracias por sus calificaciones:\n")
        elif int(opcion) == 3:
            while True:
                opcion_RyE = input("""
Reportes y estadísticas                

1. Listado de películas.
2. Películas de mayor puntaje.
3. Volver.
Ingrese una opción: """)
                if opcion_RyE == "1" or opcion_RyE == "2" or opcion_RyE == "3":
                    if int(opcion_RyE) == 1:
                        print("""
Listado de películas.
""")
                        for pelicula in peliculas:
                            for clave, valor in pelicula.items():
                                if clave == "Titulo":
                                    print(valor)
                    elif int(opcion_RyE) == 2:
                        peliculas.sort(key=lambda p: p["Calificacion"],reverse = True)
                        print("")
                        for i in range(0,10):
                            titulo_cal = peliculas[i]["Titulo"]
                            calificacion_cal = peliculas[i]["Calificacion"]
                            print(f"{(i + 1)}. {titulo_cal}. Calificacion:{calificacion_cal}")
                        peliculas.sort(key=lambda p: p["Id"])
                    elif int(opcion_RyE) == 3:
                        break
                else:
                    print("\nNo ingresaste una opción válida\n")
        elif int(opcion) == 4:
            salir = ""
            while salir != "s" and salir != "n":
                salir = input ("Segura/o que desea salir? (s/n): ").lower()
            if salir == "s":
                print("\"Muchas gracias por elejir CINEMA+\"")
                break
            elif salir == "n":
                continue
    else:
        print("\nNo ingresaste un número válido\n")
