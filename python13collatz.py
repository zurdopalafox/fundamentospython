numerocollatz = int(input("Ingrese un número entero positivo: "))
while numerocollatz != 1:
    if numerocollatz % 2 == 0:
        numerocollatz = numerocollatz // 2
    else:
        numerocollatz = 3 * numerocollatz + 1
    print(numerocollatz)
print("¡La secuencia ha llegado a 1!")
