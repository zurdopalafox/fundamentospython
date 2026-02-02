from class30persona import Persona
print("Manejando clases personal")

#creamos un objeto de la clase Persona
persona1 = Persona()
persona1.nombre = "Roger"
persona1.apellidos = "Federer"
persona1.email = "roger.federer@tennis.com"
persona1.anyonacimiento = 1981
persona1.pais = "Suiza"
print("Nombre completo:", persona1.getNombreCompleto())
print("Edad:", persona1.getEdad())
print(persona1)



