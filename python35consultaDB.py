import oracledb

print("Conectando a Oracle ....")
# Tenemos un objeto conexion que nos pedira (user,password,server)

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

print("Estamos conectados ..........")

minumdepto = input("Introduce el numero de departamento: ")

misql = "select dnombre from dept where dept_no = " + minumdepto

micursor = miconexion.cursor()
micursor.execute(misql)
fila = micursor.fetchone()

if fila != None:
    print("El nombre del departamento ",minumdepto," es: ", fila)
else:       
    print("Ese departamento no existe !!")

micursor.close()
miconexion.close()