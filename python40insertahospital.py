import oracledb

miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()

print("Codigo del Hospital:")
id = input()
print("Nombre del hospital")
nombre = input()
print("Dirección")
direccion= input()
print("Teléfono")
telefono= input()
print("Numero de camas")
nocamas= input()

# insert into DEPT values (55, 'NUEVO', 'MADRID')
sqlinsert = "insert into hospital values (" + id + ", '" + nombre + "', '" + direccion + "', '" + telefono + "', '" + nocamas + "')"
print(sqlinsert)
micursor.execute(sqlinsert)

# insert into DEPT values (55, 'NUEVO', 'MADRID')
sqlinsert = f"insert into hospital values ({int(id) + 1}, '{nombre}', '{direccion}', '{telefono}', '{nocamas}')"
print(sqlinsert)
micursor.execute(sqlinsert)

micursor.execute("commit")

sqlconsulta = "select * from hospital"
micursor.execute(sqlconsulta)

for fila in micursor:
    print(fila[0], "-", fila[1], "-", fila[2], "-", fila[3], "-", fila[4])

micursor.close()
miconexion.close()
