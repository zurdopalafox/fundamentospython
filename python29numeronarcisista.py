#Función para comprobar si un número es narcisista
def narcisista(numeroentrada):
    sumanumeros = 0
    for i in range(len(numeroentrada)):
        numeroexp = int(numeroentrada[i]) ** (len(numeroentrada))
        sumanumeros = sumanumeros + numeroexp  
    if sumanumeros == int(numeroentrada):   
       return True
    else:
       return False

#Comprobar si un número es narcisista
numeroentrada = input("Introduce un número : ")
if narcisista(numeroentrada):
    print("El número es narcisista")
else:
    print("El número no es narcisista")

#Buscar números narcisistas en un rango
rangoinferior = int(input("Introduce el rango inferior : "))
rangosuperior = int(input("Introduce el rango superior : "))
print("Números narcisistas entre", rangoinferior, "y", rangosuperior, " son:")
for numero in range(rangoinferior, rangosuperior + 1):
    if narcisista(str(numero)):
        print(numero)   





