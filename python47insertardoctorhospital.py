import oracledb

miconexion = oracledb.connect(user="system", password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

miapellido = input("Dame un Apellido para el Doctor: ")
miespecialidad = input("Dame la especialidad para el Doctor: ")
misalario = input("Dame el salario para el Doctor: ")

print("Seleccione un hospital a asignar al Dr.: ")
misql= "select max(doctor_no) + 1 as MAXIMO from DOCTOR"
micursor.execute(misql)
miid = micursor.fetchone()

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

misql = "insert into DOCTOR values(:hospital_cod,:id_doctor,:apell,:espec,:sal)"
micursor.execute(misql,(idhospital,miid[0],miapellido,miespecialidad,misalario))

micursor.execute("commit")
micursor.close()
miconexion.close()