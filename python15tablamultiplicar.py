numeroamultiplicar = int(input("Ingrese un número para ver su tabla de multiplicar: "))
listaderesultados = []
for i in range(1, 11):
    resultado = numeroamultiplicar * i
    print(f"{numeroamultiplicar} x {i} = {resultado}")
    listaderesultados.append(resultado)
print("La lista de resultados es: " + str(listaderesultados))

