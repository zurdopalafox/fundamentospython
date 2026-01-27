numerodeentrada = str(input("Ingresa el ISBN : "))
suma = 0
#Validar que el valor ingresado sea un número entero positivo
if not numerodeentrada.isdigit() or int(numerodeentrada) <= 0:  
    print("Error: Debes ingresar un número entero positivo")
else:   
    for i in range(len(numerodeentrada)):
        suma = suma + (int(numerodeentrada[i]) * (i+1))
if suma % 11 == 0:
    print("El ISBN ingresado es válido.")
else:
    print("El ISBN ingresado no es válido.")
    