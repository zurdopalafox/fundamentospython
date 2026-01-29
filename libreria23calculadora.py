def sumadosnumeros(a, b):
    return a + b    
def restadosnumeros(a, b):
    return a - b    
def multiplicaciondenumeros(a, b):
    return a * b    
def divisiondenumeros(a, b):
    return a / b

def menu():
    print("Seleccione la operacion.")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Introducir nuevos números")
    print("6.Salir")

 #Creamos método para validar la entrada de datos numericos

def obtener_numero():
     numero = input("Por favor, ingrese un número válido: ")   
     while (numero.isdigit() == False):
         print("Entrada inválida. Intente de nuevo.")
         numero = input("Por favor, ingrese un número válido: ")
     numero = int(numero)
     return numero