import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

micursor = miconexion.cursor()
misql = "select * from DEPT"
micursor.execute(misql)
for numdepto, nombre, loc in micursor:
    print("No. Departamento: ",numdepto, " ------ ", nombre," ------ ", loc)


midept_no = int(input("Introduzco el numero de departamento a consultar: "))
misql = "select apellido, oficio, dept_no from EMP where dept_no = :midept_no"

micursor.execute(misql,(midept_no,))

for apellido,oficio,nodept in micursor:
    print(f"Apellido: {apellido} --- Oficio : {oficio} --- No. Departamento: {nodept}")

micursor.close()
miconexion.close()