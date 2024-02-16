

def leales ():
    import json
    
    with open("Datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"] if camper["Categoria"] == "Leales"]
    print(" Por favor de enter para mostrar Campers que aprobaron el examen inicial")
    enter=input("")


    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('Datos.json', 'w', encoding="utf8") as x:
            json.dump(data, x, indent=4)

