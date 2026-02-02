from class32mes import Mes

listaMeses = []

enero = Mes()
enero.nombre = "Enero"
enero.temperaturaMinima = -3.5
enero.temperaturaMaxima = 10.2
enero.calcularTemperaturaMedia()
print("Mes:", enero.nombre)
print("Temperatura mínima:", enero.temperaturaMinima)
print("Temperatura máxima:", enero.temperaturaMaxima)
print("Temperatura media:", enero.temperaturaMedia)
#--------------------------------------------------------
febrero = Mes()
febrero.nombre = "Febrero"
febrero.temperaturaMinima = -1.0
febrero.temperaturaMaxima = 12.5
febrero.calcularTemperaturaMedia()
print("Mes:", febrero.nombre)
print("Temperatura mínima:", febrero.temperaturaMinima)
print("Temperatura máxima:", febrero.temperaturaMaxima)
print("Temperatura media:", febrero.temperaturaMedia)

#--------------------------------------------------------
# Ahora pediremos los datos de tres meses al usuario y los almacenaremos en una lista
print("-----------------------------")  
print("Introduce los datos de tres meses:")
for i in range(3):
    mes = Mes()
    mes.nombre = input("Introduce el nombre del mes: " + str(i+1) + ": " )
    mes.temperaturaMinima = float(input("Introduce la temperatura mínima del mes: "))
    mes.temperaturaMaxima = float(input("Introduce la temperatura máxima del mes: "))
    listaMeses.append(mes)
    
print("-----------------------------")  
for mes in listaMeses:
    mes.calcularTemperaturaMedia()
    print("Mes:", mes.nombre)
    print("Temperatura mínima:", mes.temperaturaMinima)
    print("Temperatura máxima:", mes.temperaturaMaxima)
    print("Temperatura media:", mes.temperaturaMedia)
    print("-----------------------------")
#--------------------------------------------------------
# Finalmente mostramos todos los meses introducidos
print("Lista de todos los meses introducidos:")
for mes in listaMeses:
    print("Mes:", mes.nombre, 
          " - Temp. Mínima:", mes.temperaturaMinima,
          " - Temp. Máxima:", mes.temperaturaMaxima,
          " - Temp. Media:", mes.temperaturaMedia)  
#--------------------------------------------------------
# Fin del programa



