import oracledb

class OracleEmpleados:
    def __init__(self):
    # Tenemos un objeto conexion que nos pedira (user,password,server)
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

    def eliminaEmpleado(self, paramnoempleado):
        #Creamos un cursor
        micursor = self.miconexion.cursor()
        misql = "delete from EMP where emp_no = :noempleado"
        micursor.execute(misql, (paramnoempleado,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros