def narcisista(numeroentrada):
    suma = 0
    numero_str = str(numeroentrada)
    sumanumeros = 0
    for i in range(len(numeroentrada)):
        numeroexp = int(numeroentrada[i]) ** (len(numeroentrada))
        sumanumeros = sumanumeros + numeroexp  
    if sumanumeros == int(numeroentrada):   
       return True
    else:
       return False


numeroentrada = input("Introduce un número : ")
if narcisista(numeroentrada):
    print("El número es narcisista")
else:
    print("El número no es narcisista")

rangoinferior = int(input("Introduce el rango inferior : "))
rangosuperior = int(input("Introduce el rango superior : "))
print("Números narcisistas entre", rangoinferior, "y", rangosuperior, " son:")
for numero in range(rangoinferior, rangosuperior + 1):
    if narcisista(str(numero)):
        print(numero)   





