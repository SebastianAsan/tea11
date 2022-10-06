try:
    entrada = input("Ingrese el nombre del archuivo: ")
    archivo = open(entrada, "r", encoding="UTF-8")
    for linea in archivo:
      print(linea.upper())
except:
  print("Error, archivo no existe")
  