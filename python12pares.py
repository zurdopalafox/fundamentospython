rangoinferior= float(input("Ingrese el rango inferior: "))
rangosuperior= float(input("Ingrese el rango superior: "))
while rangoinferior > rangosuperior:
    print("El rango inferior debe ser menor o igual que el rango superior. Intente de nuevo.")
    rangosuperior= float(input("Ingrese el rango superior: "))
for numero in range(int(rangoinferior), int(rangosuperior) + 1):
    if numero == 0 :
        print("El número 0 no es ni PAR ni IMPAR")
    elif numero % 2 == 0:
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")

