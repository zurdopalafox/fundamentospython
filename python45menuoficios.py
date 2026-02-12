import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
#Necesitamos una lista oficios []
listaOficios = []
sql = "select distinct OFICIO from EMP"
cursor.execute(sql)
#Recorremos los oficios
for row in cursor:
    #Agregamos cada oficio
    listaOficios.append(row[0])

#Recorremos la lista para nuestro menu
#Creamos un contador para el dibujo bonito
contador = 1
for ofi in listaOficios:
    print(f"{contador}.- {ofi}")
    contador = contador + 1
print("Seleccione una opción")
opcion = int(input())
oficioSeleccionado = listaOficios[opcion - 1]
print(f"Oficio seleccionado: {oficioSeleccionado}")
#Consultamos los empleados con el oficio seleccionado
sql = "select * from EMP where OFICIO=:oficio"
cursor.execute(sql, (oficioSeleccionado,))
print("-----Lista de empleados----")
for row in cursor:
    #print("- " + row[1] + ", Salario: " + str(row[5]))
    print(f"{row[2]}, - {row[1]}, - Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin de programa")