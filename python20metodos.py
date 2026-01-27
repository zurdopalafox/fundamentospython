def primerMetodo():
    print("Este es el primer método")

def segundoMetodo():
    print("Este es el segundo método")  

def metodoSaludar(nombre):
    print("Hola, " + nombre + "!")  

def metodoDespedir(nombre,dia): 
     print("Un gusto hoy ", dia, "Mr./Ms " + nombre + "!")

metodoSaludar("Ana")
metodoSaludar("Luis")
nombre = input("Ingresa tu nombre: ")
metodoSaludar(nombre)   
metodoDespedir("Ana","lunes")
metodoDespedir("Luis","viernes")
primerMetodo()
segundoMetodo()
primerMetodo()
segundoMetodo()

