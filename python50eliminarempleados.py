from oracle50empleados import OracleEmpleados

minoempleado = int(input("Introduce el numero de Empleado a eliminar: "))
oracle = OracleEmpleados()
registros = oracle.eliminaEmpleado(minoempleado)
print(f"Empleados eliminados : {registros}")