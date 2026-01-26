while (entrada := input("Ingrese un número (o 'salir' para terminar): ")) != 'salir':
    try:
        numero = float(entrada)
        cuadrado = numero ** 2
        print(f"El cuadrado de {numero} es {cuadrado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")


for i in range(5):
            print(f"Iteración del bucle for número {i + 1}")

