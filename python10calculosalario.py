horassemanales=int(input("Ingrese las horas trabajadas a la semana: "))   
tarifahoraria=int(input("Ingrese la tarifa por hora: "))
kilometros=int(input("Ingrese los kilómetros recorridos en el mes: "))
if horassemanales>36:
   horasextras=horassemanales-36
else:
   horasextras=0
salariobase=((horassemanales-horasextras)*tarifahoraria)
salariohorasextras=(horasextras*(tarifahoraria*1.5))
salariobruto=salariobase+salariohorasextras

if kilometros>100 and kilometros<=900:
    destino="NACIONAL"
elif kilometros>900:
    destino="INTERNACIONAL"
if kilometros<100:
    destino="PROVINCIAL"
if salariobruto<=250:
    retencion=0
elif (salariobruto>250 and salariobruto<=500):
    retencion=.20
else:
    retencion=.50
iva=salariobruto*.16
salariototal=salariobruto-iva
print("--------------------------------------")
print("HORAS TRABAJADAS A LA SEMANA: " + str(horassemanales))
print("HORAS EXTRAS TRABAJADAS: " + str(horasextras))
print("TARIFA POR HORA: " + str(tarifahoraria))
print("DISTANCIA EN KMS: " + str(kilometros))
print("DESTINO: " + destino)
print("RETENCIÓN: " + str(retencion*100) + "%")
print("SALARIO BASE: " + str(salariobase))
print("SALARIO POR HORAS EXTRAS: " + str(salariohorasextras))
print("SALARIO BRUTO: " + str(salariobruto))
print("IVA 16%: " + str(iva))
print("--------------------------------------")
print("SALARIO TOTAL A RECIBIR: " + str(salariototal))
print("--------------------------------------")



     

