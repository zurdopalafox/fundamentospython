from class33mascota import Mascota

# Solicitamos capturar tres mascotas
listaMascotas = []
for i in range(3):
    mascota = Mascota()
    mascota.nombre = input("Introduce el nombre de la mascota " + str(i+1) + ": ")
    mascota.raza = input("Introduce la raza de la mascota " + str(i+1) + ": ")
    mascota.anyonacimiento = int(input("Introduce el año de nacimiento de la mascota " + str(i+1) + ": "))
    mascota.anyoadopcion = int(input("Introduce el año de adopción de la mascota " + str(i+1) + ": "))
    listaMascotas.append(mascota)   
# Mostramos los datos de las mascotas capturadas
print("\nDatos de las mascotas capturadas:")
for mascota in listaMascotas:
    print("Nombre:", mascota.nombre)
    print("Raza:", mascota.raza)
    print("Año de nacimiento:", mascota.anyonacimiento)
    print("Año de adopción:", mascota.anyoadopcion)
    print("Edad:", mascota.getEdad())
    print("Años desde la adopción:", mascota.getAnyosAdoptada())
    print("-----------------------------")
# Fin del programa

