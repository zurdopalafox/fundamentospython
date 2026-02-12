import oracledb

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

print("Id Departamento:")
id = input()
print("Nombre del departamento")
nombre = input()
print("localidad")
localidad= input()

# insert into DEPT values (55, 'NUEVO', 'MADRID')
sqlinsert = "insert into DEPT values (" + id + ", '" + nombre + "', '" + localidad + "')"
print(sqlinsert)
micursor.execute(sqlinsert)

# insert into DEPT values (55, 'NUEVO', 'MADRID')
sqlinsert = f"insert into DEPT values ({int(id) + 1}, '{nombre}', '{localidad}')"
print(sqlinsert)
micursor.execute(sqlinsert)

micursor.execute("commit")

sqlconsulta = "select * from DEPT"
micursor.execute(sqlconsulta)

for fila in micursor:
    print(fila[0], "-", fila[1], "-", fila[2])

micursor.close()
miconexion.close()
