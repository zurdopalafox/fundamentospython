import oracledb

print("Conectando a Oracle ....")
# Tenemos un objeto conexion que nos pedira (user,password,server)

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

print("Estamos conectados ..........")

micursor = miconexion.cursor()

micursor.execute("select * from EMP")

# Tenemos un metodo fetchone() que se mueve una fila en la que estamos ubicados cada vez que lo ejecutamos
fila =  micursor.fetchone()
print(fila)
fila =  micursor.fetchone()
print(fila)

for fila in micursor:
    print(fila)

micursor.close()
miconexion.close()



