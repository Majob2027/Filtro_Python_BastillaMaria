import Modulo_usuarios



while True :
    print ("***********************************")
    print ("*    Bienvenido administrador     *")
    print ("***********************************")

    print("  Que desea hacer ")
    print("")
    print("1. Modulo usuarios")
    print("")
    print("2. Módulo de Bonificaciones para Clientes Leales")
    print("")
    print("3. Modulo Gestion de servicios")
    print("")
    print("4. Modulo reportes")
    decision_principal=int(input("--->"))
    print("")
    print("")


    if decision_principal==1:
        print ("***********************************")
        print ("*          Modulo usuarios        *")
        print ("***********************************")
        print("1. Registro y Gestión de Usuarios")
        print("2. Seguimiento del Historial de Usuarios")
        print("3. Personalización de Servicios")
        print("4. Gestión de la Fidelización de Clientes")
        decision1=int(input("Elija un numero"))
        print("")

    if decision1==1 :
        print (" 1. Agregar usuario")
        print("")
        print (" 2. Actualizar usuario ")
        print("")
        print (" 3. Eliminar usuario ")
        print("")
        decision2=int(input("Elija un opcion "))
        print("")

    if decision2 == 1 :
        print("Vamos a agregar un nuevo usuario ")
        print(Modulo_usuarios.crearusuario())
        x=input("")
    if decision2 == 2 :
        print("Vamos a actualizar")
        print(Modulo_usuarios.actualizar_usuario())
        x=input("")
    if decision2 == 3 :
        print("Eliminar un usuario")
        print(Modulo_usuarios.elminarusuario())
        x=input("")
        

    elif decision_principal==2:
        print ("*************************************************")
        print ("* Módulo de Bonificaciones para Clientes Leales *")
        print ("*************************************************")

    elif decision_principal==2:
        print ("******************************")
        print ("* Modulo Gestion de servicios*")
        print ("******************************")


    elif decision_principal==2:
        print ("******************")
        print ("* Modulo reportes*")
        print ("******************")
    


        


