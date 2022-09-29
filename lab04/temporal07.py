contador = 0
suma = 0
minimo = 0
maximo = 0
primerNumero = True
while True:
    número = input("Ingrese un número: ")
    if (número == "salir" ):
        break
    else:
        contador = contador + 1
        suma = suma + int(número)
        if (primerNumero):
            minimo = int(número)
            maximo = minimo
            primerNumero = False
        else:
            if (int(número) > maximo):
                maximo = int(número)
            if (int(número) < minimo):
                minimo = int(número)
    print("Contador:", contador)
    print("Suma:", suma)
    print("Promedios:", suma/contador)
    print("Minimo:", minimo)