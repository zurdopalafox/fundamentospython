from oracle49enfermos import OracleEnfermos

miinscripcion = int(input("Introduce el numero de inscripción del Enfermo a eliminar: "))
oracle = OracleEnfermos()
registros = oracle.eliminaEnfermo(miinscripcion)
print(f"Enfermos eliminados : {registros}")
      

