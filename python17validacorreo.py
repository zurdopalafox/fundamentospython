correoelectronico = input("Ingrese una dirección de correo electrónico: ")
numeroarrobas = 0
arrobaalprincipio = False
nohaypuntojustodespuesarroba = False
eldominioesmayoradosotres = False
tienearroba = correoelectronico.find("@")
tienepunto = correoelectronico.rfind(".")
if correoelectronico[0] == "@" or correoelectronico[-1] == "@":
   arrobaalprincipiooalfinal = True
for i in range(len(correoelectronico)):
    if correoelectronico[i] == "@":
        numeroarrobas += 1
posicionarroba = correoelectronico.find("@",0)
if correoelectronico[posicionarroba + 1] != ".":
        nohaypuntojustodespuesarroba = True
posiciondelpuntodominio= correoelectronico.rfind(".")
if (len(correoelectronico) > posiciondelpuntodominio+3  or len(correoelectronico) > posiciondelpuntodominio+4) and posiciondelpuntodominio != -1:
    eldominioesmayoradosotres = True
if tienearroba != -1:
    tienearroba = True
else:
    tienearroba = False
if tienepunto != -1:
    tienepunto = True
else:
    tienepunto = False      
print("El correo contiene @ : ",tienearroba)
print("El correo contiene . : ",tienepunto)
print("El @ está al principio o al final: ", arrobaalprincipio)
if numeroarrobas == 1:
    numeroarrobas = True
else:
    numeroarrobas = False   
print("Hay solo una @: ", numeroarrobas)
print("No hay un punto justo después de la @: ", nohaypuntojustodespuesarroba)
print("El dominio tiene mas de dos o tres caracteres: ", eldominioesmayoradosotres)

