#Algoritmo para calcular el día de la semana
dia=int(input("Introduce un día del mes: "))
mes=int(input("Introduce un mes del año: "))
anio=int(input("Introduce un año: "))
if mes==1:
    mes=13
    anio=anio-1
elif mes==2:
    mes=14
    anio=anio-1
calculo2=int(((mes+1)*3)/5)
calculo3=int(anio/4)
calculo4=int(anio/100)
calculo5=int(anio/400)
calculo6=dia+(mes*2)+anio+calculo2+calculo3-calculo4+calculo5+2
calculo7=int(calculo6/7)
calculo8=calculo6-(calculo7*7)
if calculo8==0:
    print("El día es Sabado")
elif calculo8==1:
    print("El día es Domingo")
elif calculo8==2:                   
    print("El día es Lunes")
elif calculo8==3:
    print("El día es Martes")
elif calculo8==4:
    print("El día es Miércoles")
elif calculo8==5:
    print("El día es Jueves")
elif calculo8==6:
    print("El día es Viernes")      
print("Fin del programa")

