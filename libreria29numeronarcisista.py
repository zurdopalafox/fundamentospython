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