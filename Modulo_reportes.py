def mostrarservicios ():
  import json
  with open('servicio.json' ,'r' ) as file :
    mijson= json.load (file )
  lista= mijson['Servicios']

  print("Presione enter para mostrar servicios")
  enter= input("")


  for i in lista :
    print (["Nombre :" , i ['Nombre']])






     
    