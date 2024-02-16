def clientesleales ():
    print ("presiona enter para visualizar las personas que son clientes leales ")
    x=input("")

    import json
    with  open ('Datos.json' , 'r') as file:
        mijson=json.load (file)
        lista =mijson['Datos']

    
    lista = mijson['Datos']

    documento = ("cliente leal")


    Usuario_encontrado = None
    for Usuario in lista :
        if Usuario["Identificacion"] == documento:
            Usuario_encontrado = Usuario
            break

    if Usuario_encontrado is not None:
        print(f"Nombre" , [])