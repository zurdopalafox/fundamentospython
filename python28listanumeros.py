totalimpares= 0
totalpares= 0
totalnumeros= 0
sumanumeros= 0
listanumeros= []
listaNumerospares= []
listaNumerosimpares= []
numero= 0

while numero != -1:
    numero = int(input("Introduce un número (-1 para terminar): "))
    if numero != -1:
        listanumeros.append(numero)
        totalnumeros= totalnumeros + 1
        sumanumeros= sumanumeros + numero
        if numero % 2 == 0:
            totalpares= totalpares + 1
            listaNumerospares.append(numero)
        else:
            totalimpares= totalimpares + 1
            listaNumerosimpares.append(numero)
print("Has introducido", totalnumeros, "números.")
print("Los números introducidos son:", listanumeros)
print("La suma de los números es:", sumanumeros)
print("Has introducido", totalpares, "números pares:", listaNumerospares)
print("Has introducido", totalimpares, "números impares:", listaNumerosimpares)