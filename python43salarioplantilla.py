import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

mihospitalcod = input("Introduzco el codigo de Hospital: ")
miincremento = input("Introduzca el incremento: ")
misql = "update PLANTILLA set salario = salario + :miincremento where hospital_cod = :mihospitalcod"
misql1 = "Select apellido, funcion, salario from plantilla where hospital_cod = :mihospitalcod"

# Hacemos la actualizacion de los salarios
micursor.execute(misql,(miincremento, mihospitalcod,))
print("El numero de empleados de la Plantilla a los que les hemos incrementado el salario son : ", micursor.rowcount)
micursor.execute("commit")

# Realizamos consulta de los registros afectados
micursor.execute(misql1,(mihospitalcod,))
for apellido,funcion,salario in micursor:
    print(f"Apellido: {apellido} --- Función: {funcion} --- Salario: {salario}")

micursor.close()
miconexion.close()