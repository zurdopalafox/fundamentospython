import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()
oficios = dict()
misql = "select distinct OFICIO from EMP"

micursor.execute(misql)

i = 1
for oficio in micursor:
    print("OFICIO de Cursor:",oficio)
    oficios[i] = oficio
    i = i + 1
# Un diccionario es una colección desordenada de elementos que se almacenan en pares clave-valor.
# Cada clave es única dentro del diccionario y se utiliza para acceder a su valor asociado.
for numero,oficio in oficios.items():
    print(f"{numero}. {oficio}")

miseleccion = input("Elija una opcion: ")
oficioseleccionado = oficios[int(miseleccion)]
print("Haz elegido :", oficioseleccionado)
misql = "select * from EMP where oficio = :mioficio"
micursor.execute(misql,(oficioseleccionado))

for fila in micursor:
    print(fila)

micursor.close()
miconexion.close()
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
