import oracledb

miconexion = oracledb.connect(user="system", password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

miapellido = input("Dame un Apellido para el Plantilla: ")
mifuncion = input("Dame la funcion para el Plantilla: ")
miturno = input("Dame el Turno para el Plantilla: ")
misalario = input("Dame el Salario para el Plantilla: ")
micodsala = input("Dame el codigo de sala para el Plantilla: ")


print("Seleccione un hospital a asignar al Dr.: ")
misql= "select max(empleado_no) + 1 as MAXIMO from PLANTILLA"
micursor.execute(misql)
miidempleado = micursor.fetchone()

misql = "select nombre, hospital_cod from HOSPITAL"
micursor.execute(misql)
listadeCodigos = []
contador = 1
for fila in micursor:
    print(f"{contador}.- {fila[0]}")
    listadeCodigos.append(fila[1])
    contador = contador + 1
opcion = int(input("Seleccione un hospital:"))
idhospital = listadeCodigos[opcion - 1]

misql = "insert into PLANTILLA values(:hospital_cod,:salacod,:empleadono,:apell,:funcion,:turno,:salario)"
micursor.execute(misql,(idhospital,micodsala,miidempleado[0],miapellido,mifuncion,miturno,misalario))

micursor.execute("commit")
micursor.close()
miconexion.close()