import oracledb

miconexion= oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")

micursor = miconexion.cursor()

turno= input("Introduce el turno de la plantilla que quieres consultar (M/T/N) :")
misql = "select apellido, funcion from plantilla where turno = upper('" + (str(turno)) + "')"

micursor.execute(misql)

# micursor.fetchone()

for fila in micursor:
    print(fila)

micursor.close()
miconexion.close()


