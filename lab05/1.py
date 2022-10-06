cadena = "X-dspam-Confidence:0.4321"

post1 = cadena.find(":")
print("Inicia en el indice: "+ str(post1))

post2 = cadena.find("5")
print("Termina en: "+ str(post2))

final = len(cadena)
substring = cadena[post1+1:final]
numerico = float (substring)

print(numerico)
print(type(numerico))
