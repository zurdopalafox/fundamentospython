numerousuario = 0
suma = 0
flag=True
while numerousuario != 0 or flag==True:
    numerousuario = int(input("Ingrese un número entero (0 para salir): "))
    suma = suma + numerousuario
    flag=False
print("La suma total es: " + str(suma))

