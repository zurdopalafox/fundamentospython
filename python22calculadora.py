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
    print("5.Salir")

# Programa principal
opcion = '1'
while opcion in ['1','2','3','4','5']:   
    menu()
    opcion = input("Ingrese la opcion (1/2/3/4/5): ")
    if opcion == "5":
       print("Saliendo de la calculadora.")
       break
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if opcion == '1':
        print(num1,"+",num2,"=", sumadosnumeros(num1,num2))
    elif opcion == '2':
        print(num1,"-",num2,"=", restadosnumeros(num1,num2))
    elif opcion == '3':
        print(num1,"*",num2,"=", multiplicaciondenumeros(num1,num2))                
    elif opcion == '4':
        print(num1,"/",num2,"=", divisiondenumeros(num1,num2))



    