import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

micursor = miconexion.cursor()


midept_no = input("Introduzco el numero de departamento: ")
misql = f"select apellido, oficio, dept_no from EMP where dept_no = {midept_no}"

micursor.execute(misql)

for apellido,oficio,nodept in micursor:
    print(f"Apellido: {apellido} --- Oficio : {oficio} --- No. Departamento: {nodept}")

# IMPORTANTE : Si al ejecutar el programa introducimos 0 or 1=1 y damos enter nos regresa todas las filas de la tabla
#              Es una manera de hacer SQL INJECTION !!!! Tambien si capturamos : true hace lo mismo, esto es por concatenar la entrada del usuario.
#              Para evitar esto utilizaremos parámetros.

# Solucion 2 forzar a int() la entrada del usuario.

midept_no = int(input("Introduzco el numero de departamento: "))
misql = "select apellido, oficio, dept_no from EMP where dept_no = " + str(midept_no)

micursor.execute(misql)

for apellido,oficio,nodept in micursor:
    print(f"Apellido: {apellido} --- Oficio : {oficio} --- No. Departamento: {nodept}")

# Solucion 3 con Parámetros
# En oracle los parametros se definen como ":nombredelparámetro" o en SQLSERVER "@nombredelparámetro"

midept_no = int(input("Introduzco el numero de departamento: "))
misql = "select apellido, oficio, dept_no from EMP where dept_no = :midept_no"

micursor.execute(misql,(midept_no,))

for apellido,oficio,nodept in micursor:
    print(f"Apellido: {apellido} --- Oficio : {oficio} --- No. Departamento: {nodept}")

micursor.close()
miconexion.close()