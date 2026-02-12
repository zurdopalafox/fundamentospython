import oracledb

miconexion= oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")
micursor = miconexion.cursor()
oficios = dict()
misql = "select distinct OFICIO from EMP"

micursor.execute(misql)

i = 1
for oficio in micursor:
    print("OFICIO de Cursor:",oficio)
    oficios[i] = oficio
    i = i + 1
# Un diccionario es una colección desordenada de elementos que se almacenan en pares clave-valor.
# Cada clave es única dentro del diccionario y se utiliza para acceder a su valor asociado.
for numero,oficio in oficios.items():
    print(f"{numero}. {oficio}")

miseleccion = input("Elija una opcion: ")
oficioseleccionado = oficios[int(miseleccion)]
print("Haz elegido :", oficioseleccionado)
misql = "select * from EMP where oficio = :mioficio"
micursor.execute(misql,(oficioseleccionado))

for fila in micursor:
    print(fila)

micursor.close()
miconexion.close()