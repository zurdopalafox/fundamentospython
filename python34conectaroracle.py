import oracledb

print("Conectando a Oracle ....")
# Tenemos un objeto conexion que nos pedira (user,password,server)

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

print("Estamos conectados ..........")

micursor = miconexion.cursor()
micursor.execute("select * from EMP")
fila = micursor.fetchone()

# Tenemos un metodo fetchone() que se mueve una fila en la que estamos ubicados cada vez que lo ejecutamos
# asi lo reorremos de uno en uno 
# fila =  micursor.fetchone()
# print(fila)
# fila =  micursor.fetchone()
# print(fila)

# Lo recorremos con un bucle for
# for fila in micursor:
#    print(fila[0], end=' ') # EMP_NO
#    print(fila[1]) # APELLIDO
#    print(fila)    # LA FILA COMPLETA

# Lo recorremos con un bucle for dejando cada columna en una variable y solo imprimo las primeras 3
for numeroempleado, apellido, oficio,X1,X2,X3,X4,X5 in micursor:
   print(numeroempleado,apellido,oficio)


# Lo recorremos con un bucle while
# while fila != None:
#     fila =  micursor.fetchone()
#     print(fila)


micursor.close()
miconexion.close()



