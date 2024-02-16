def crearservicio ():
    import json
    print ("Vamos a añadir un Servicio ")
    with  open ('servicio.json' , 'r') as file:
        mijson=json.load (file)

     
    lista_servicios={}

    lista_servicios["Identificacion"]= input("Escriba identificacion de servicio : ")
    lista_servicios["Nombre"]= input("Escriba nombre del servicio: ")
    lista_servicios["Duracion"]= input("Escriba duracion del servicio : ")
    lista_servicios["Caracteristica 1"]= input("Escriba caracteristica del servicio: ")
    lista_servicios["Caracteristica 2"]= input("Escriba caracteristica del servicio: ")
    lista_servicios["Caracteristica 3"]= input("Escriba caracteristica del servicio:" )
    lista_servicios["Precio"]=input ("  Escriba precio :") 

    print ("Servicio creado correctamente ")
    mijson['Servicios'].append (lista_servicios)


    with  open ('servicio.json' , 'w') as file:
        json.dump (mijson , file , indent=2)





def actualizar_servicio ():
    import json
    print ("Vamos a actualizar un servicio ")
    with  open ('servicio.json' , 'r') as file:
        mijson=json.load (file)

    
    lista = mijson['Servicios']

    print("Por favor, escriba el número de identificación de el servicio a actualizar:")
    documento = (input("---> "))


    Usuario_encontrado = None
    for Usuario in lista :
        if Usuario["Identificacion"] == documento:
            Usuario_encontrado = Usuario
            break

    if Usuario_encontrado is not None:
        print("Seleccione la información a actualizar:")
        print("1. Nombre")
        print("2. Duracion")
        print("3. Caracteristica 1")
        print("4. Caracteristica 2")
        print("5. Caracteristica 3")
        print("6. Precio")
 

        decision = int(input("---> "))

        if decision == 1:
            Usuario_encontrado['Nombre'] = input("Escriba el nuevo nombre: ")
        elif decision == 2:
            Usuario_encontrado['Duracion'] = input("Escriba el nuevo Apellido: ")
        if decision == 3:
            Usuario_encontrado['Caracteristica 1'] = input("Escriba la nueva direccion: ")
        if decision == 4:
            Usuario_encontrado['Caracteristica 2'] = input("Escriba el nuevo Telefono: ")
        if decision == 5:
            Usuario_encontrado['Caracteristica 3'] = input("Escriba Años movistar: ")
        if decision == 6:
            Usuario_encontrado['Precio'] = input("Escriba la nueva categoria: ")
        print ("Usuario actualizado correctamente ")

    with  open ('servicio.json' , 'w') as file:
        json.dump (mijson , file , indent=2)





def elminarservicio ():

    import json
    print ("Vamos a Eliminar  un usuario ")
    with  open ('servicio.json' , 'r') as file:
        mijson=json.load (file)
        lista =mijson['Servicios']

    print("Por favor, escriba el número de identificación de el servicio a Eliminar:")
    documento = (input("---> "))


    Usuario_encontrado = None
    for Usuario in lista :
        if Usuario["Identificacion"] == documento:
            Usuario_encontrado = Usuario
            break

    if Usuario_encontrado is not None:
        mijson['Servicios'].remove(Usuario_encontrado)
    
    print ("Servicio eliminado correctamente ")

    with  open ('servicio.json' , 'w') as file:
        json.dump (mijson , file , indent=2)
    

    