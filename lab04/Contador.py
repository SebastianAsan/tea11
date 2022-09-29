contador = 0
suma = 0
while True:
    número = input("Ingrese un número: ")
    if (número == "salir" ):
        break
    contador = contador + 1
    suma = suma + int(número)
    print("Contador:", contador)
    print("Suma:", suma)
    print("Promedios:", suma/contador)
    