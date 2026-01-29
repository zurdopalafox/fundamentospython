import libreria23calculadora

# Programa principal
opcion = '1'
while opcion in ['1','2','3','4','5','6']:   
    libreria23calculadora.menu()
    opcion = input("Ingrese la opcion (1/2/3/4/5): ")
    if opcion == "6":
       print("Saliendo de la calculadora.")
       break
    num1 = libreria23calculadora.obtener_numero() 
    num2 = libreria23calculadora.obtener_numero()
    if opcion == '1':
        print(num1,"+",num2,"=", libreria23calculadora.sumadosnumeros(num1,num2))
    elif opcion == '2':
        print(num1,"-",num2,"=", libreria23calculadora.restadosnumeros(num1,num2))
    elif opcion == '3':
        print(num1,"*",num2,"=", libreria23calculadora.multiplicaciondenumeros(num1,num2))                
    elif opcion == '4':
        print(num1,"/",num2,"=", libreria23calculadora.divisiondenumeros(num1,num2))
    elif opcion == '5':
        print("Introduzca nuevos números para la operación.")