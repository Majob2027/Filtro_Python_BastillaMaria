def crearusuario ():
    import json
    print ("Vamos a añadir un usuario ")
    with  open ('Datos.json' , 'r') as file:
        mijson=json.load (file)

     
    lista_usuarios={}

    lista_usuarios["Identificacion"]= input("Escriba identificacion de usuario : ")
    lista_usuarios["Nombre"]= input("Escriba nombre del usuario : ")
    lista_usuarios["Apellido"]= input("Escriba Apelliido  de usuario : ")
    lista_usuarios["Direccion"]= input("Escriba Direccion de usuario : ")
    lista_usuarios["Telefono"]= input("Escriba telefono de usuario : ")
    lista_usuarios["Años con movistar"]= input("Escriba años con movistar:" )
    print (" Escriba : si 10 años o mas = Leales o entre 3 y 10 años o mas = Clientes regulares o si menos de tres años = Nuevos ") 
    lista_usuarios["Categoria"]=input ("  Escriba Leales o Clientes regulares o clientes nuevos dependienod a lo mecionado anteriormente :") 

    print ("Usuario creado correctamente ")
    mijson['Datos'].append (lista_usuarios)


    with  open ('Datos.json' , 'w') as file:
        json.dump (mijson , file , indent=2)





def actualizar_usuario ():
    import json
    print ("Vamos a actualizar un usuario ")
    with  open ('Datos.json' , 'r') as file:
        mijson=json.load (file)
        lista =mijson['Datos']

    
    lista = mijson['Datos']

    print("Por favor, escriba el número de identificación de la persona a actualizar:")
    documento = (input("---> "))


    Usuario_encontrado = None
    for Usuario in lista :
        if Usuario["Identificacion"] == documento:
            Usuario_encontrado = Usuario
            break

    if Usuario_encontrado is not None:
        print("Seleccione la información a actualizar:")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Direccion")
        print("4. Telefono")
        print("5. Años con movistar")
        print("6. Categoria")
        print (" Recuerde que si cambia años movistar debera cambiar categoria")

        decision = int(input("---> "))

        if decision == 1:
            Usuario_encontrado['Nombre'] = input("Escriba el nuevo nombre: ")
        elif decision == 2:
            Usuario_encontrado['Apellido'] = input("Escriba el nuevo Apellido: ")
        if decision == 3:
            Usuario_encontrado['Direccion'] = input("Escriba la nueva direccion: ")
        if decision == 4:
            Usuario_encontrado['Telefono'] = input("Escriba el nuevo Telefono: ")
        if decision == 5:
            Usuario_encontrado['Años con movistar'] = input("Escriba Años movistar: ")
        if decision == 6:
            Usuario_encontrado['Categoria'] = input("Escriba la nueva categoria: ")
        print ("Usuario actualizado correctamente ")

    with  open ('Datos.json' , 'w') as file:
        json.dump (mijson , file , indent=2)





def elminarusuario ():

    import json
    print ("Vamos a Eliminar  un usuario ")
    with  open ('Datos.json' , 'r') as file:
        mijson=json.load (file)
        lista =mijson['Datos']

    print("Por favor, escriba el número de identificación de la persona a Eliminar:")
    documento = (input("---> "))


    Usuario_encontrado = None
    for Usuario in lista :
        if Usuario["Identificacion"] == documento:
            Usuario_encontrado = Usuario
            break

    if Usuario_encontrado is not None:
        mijson['Datos'].remove(Usuario_encontrado)
    
    print ("Usuario eliminado correctamente ")

    with  open ('Datos.json' , 'w') as file:
        json.dump (mijson , file , indent=2)
    

    





            


    










