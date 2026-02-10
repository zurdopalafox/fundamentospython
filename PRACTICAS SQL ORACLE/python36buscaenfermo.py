import oracledb

print("Conectando a Oracle ....")
# Tenemos un objeto conexion que nos pedira (user,password,server)

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

print("Estamos conectados ..........")

minuminscripcion = input("Introduce el numero de inscripcion del enfermo: ")

misql = "select apellido, direccion, fecha_nac from enfermo where inscripcion = " + minuminscripcion

micursor = miconexion.cursor()
micursor.execute(misql)
fila = micursor.fetchone()

if fila != None:
    print("Los datos del enfermo con múero de inscripción ",minuminscripcion," son: ", fila)
else:       
    print("Ese enfermo con numero de inscripción ", minuminscripcion, " no existe o ha muerto en otro lado !!")

micursor.close()
miconexion.close()