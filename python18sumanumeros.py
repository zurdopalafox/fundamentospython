numerodeentrada = str(input("Ingresa una cifra de números a sumar: "))
suma = 0
#Validar que el valor ingresado sea un número entero positivo   
if not numerodeentrada.isdigit() or int(numerodeentrada) <= 0:
    print("Error: Debes ingresar un número entero positivo.")
else:   
    #sumar cada elemento ingresado  
    for i in range(len(numerodeentrada)):
        suma = suma +int(numerodeentrada[i])
        if i < len(numerodeentrada) - 1:
            print(numerodeentrada[i] + " + ", end="")
        else:   
            print(numerodeentrada[i] + " = " + str(suma))