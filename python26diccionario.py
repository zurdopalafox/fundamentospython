print("Diccionarios")
# Un diccionario es una colección desordenada de elementos que se almacenan en pares clave-valor.
# Cada clave es única dentro del diccionario y se utiliza para acceder a su valor asociado.
provincias = dict()
provincias = {
              924: "Cádiz",
                5: "Sevilla",
              952: "Málaga",
              950: "Almería",
              955: "Huelva",
              956: "Córdoba",
              957: "Jaén",
              958: "Granada",
              959: "Cádiz"
              } 
print(provincias)
print(provincias.get(952))  # Acceder al valor asociado a la clave 952

# Acceder a un valor mediante su clave
print("Provincia con código 952:", provincias[952])
# Agregar un nuevo par clave-valor
provincias[941] = "Prueba"
print("Después de agregar una nueva provincia:", provincias)
# Modificar un valor existente
provincias[941] = "Nueva Prueba"
print("Después de modificar la provincia con código 941:", provincias)
# Eliminar un par clave-valor
del provincias[941]
print("Después de eliminar la provincia con código 941:", provincias)   

# Recorrer un diccionario
print("Recorriendo el diccionario de provincias:")
for codigo, nombre in provincias.items():
    print(f"Código: {codigo}, Provincia: {nombre}") 
# Verificar si una clave existe en el diccionario
codigo_a_buscar = 950
if codigo_a_buscar in provincias:
    print(f"La provincia con código {codigo_a_buscar} es {provincias[codigo_a_buscar]}")
else:
    print(f"No existe una provincia con código {codigo_a_buscar}")

for clave in provincias.keys():
    print("Clave:", clave)
for valor in provincias.values():
    print("Valor:", valor)

provincias_sorted = sorted(provincias.items())
print("Diccionario ordenado por claves:")
for codigo, nombre in provincias_sorted:
    print(f"Código: {codigo}, Provincia: {nombre}")

provincias.pop(955)  # Eliminar la provincia con código 955
print("Después de eliminar la provincia con código 955:", provincias)

# Obtener todas las claves y valores
claves = provincias.keys()
valores = provincias.values()
print("Claves del diccionario:", list(claves))
print("Valores del diccionario:", list(valores))
# Longitud del diccionario
print("Número de provincias en el diccionario:", len(provincias))
# Limpiar el diccionario
provincias.clear()
print("Después de limpiar el diccionario:", provincias)
# Verificar si el diccionario está vacío
if not provincias:
    print("El diccionario está vacío.")
else:
    print("El diccionario no está vacío.")


