import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

mioficio = input("Introduzco el oficio: ")
miincremento = input("Introduzca el incremento: ")
misql = "update EMP set salario = salario + :miincremento where oficio = :mioficio"
misql1 = "Select apellido, oficio, salario from emp where oficio = :mioficio"

# Hacemos la actualizacion de los salarios
micursor.execute(misql,(miincremento, mioficio,))
print("El numero de empleados a los que les hemos incrementado el salario son : ", micursor.rowcount)
micursor.execute("commit")

# Realizamos consulta de los registros afectados
micursor.execute(misql1,(mioficio,))
for apellido,oficio,salario in micursor:
    print(f"Apellido: {apellido} --- Oficio: {oficio} --- Salario: {salario}")

micursor.close()
miconexion.close()