# Programa que determina el mayor, el intermedio y el menor de tres números introducidos por el usuario
num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
num3=float(input("Introduce el tercer número: "))  
if num1>=num2 and num1>=num3:
    mayor=num1
    if num2>=num3:
        intermedio=num2
        menor=num3
    else:
        intermedio=num3
        menor=num2
elif num2>=num1 and num2>=num3:
    mayor=num2
    if num1>=num3:
        intermedio=num1
        menor=num3
    else:
        intermedio=num3
        menor=num1
elif num3>=num1 and num3>=num2:
    mayor=num3
    if num1>=num2:
        intermedio=num1
        menor=num2
    else:
        intermedio=num2
        menor=num1
print("El número mayor es: " + str(mayor))  
print("El número intermedio es: " + str(intermedio))
print("El número menor es: " + str(menor))
print("Fin del programa")

