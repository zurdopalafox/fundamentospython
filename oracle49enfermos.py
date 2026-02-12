import oracledb

class OracleEnfermos:
    def __init__(self):
    # Tenemos un objeto conexion que nos pedira (user,password,server)
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle", dsn="localhost/FREEPDB1")

    def eliminaEnfermo(self, paraminscripcion):
        #Creamos un cursor
        micursor = self.miconexion.cursor()
        misql = "delete from ENFERMO where INSCRIPCION = :inscrip"
        micursor.execute(misql, (paraminscripcion,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
