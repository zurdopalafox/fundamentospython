print("Ejemplo mayor de dos números en Python")
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero2 > numero1:
    print(f"El número {numero2} es mayor que {numero1}.")
else:
    print(f"Los números {numero1} y {numero2} son iguales.")