import oracledb

print("Conectando a Oracle ....")
# Tenemos un objeto conexion que nos pedira (user,password,server)

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

print("Estamos conectados ..........")


misql1 = "select * from enfermo"

micursor = miconexion.cursor()
micursor.execute(misql1)
for fila in micursor:
    print(fila)

minuminscripcion = input("Introduce el numero de inscripcion del enfermo a eliminar: ")
misql = "delete enfermo where inscripcion = " + minuminscripcion
micursor.execute(misql)

if micursor.rowcount != 0:
    micursor.execute("commit")
    print("El enfermo con múero de inscripción ",minuminscripcion," ha sido eliminado ")
else:       
    print("Ese enfermo con numero de inscripción ", minuminscripcion, " no existe o ha muerto en otro lado !!")

micursor.close()
miconexion.close()