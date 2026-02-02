class Persona:

# Constructor
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.email = ""
        self.anyonacimiento = 0
        self.pais = "Francia"

    # Método para representar el objeto como cadena cuando se imprime con print()
    # por defecto llama al método __str__() e imprime su valor de retorno <class30persona.Persona object at 0x104fe86e0>

    def __str__(self):
            return f"Nombre: {self.nombre} {self.apellidos}, Email: {self.email}, Año de Nacimiento: {self.anyonacimiento}, País: {self.pais}"

    def getNombreCompleto(self):
            return self.nombre + " " + self.apellidos
        
    def getEdad(self):
            edad = 2026 - self.anyonacimiento
            return edad
    
    # Método para obtener una edad falsa restando años con un parámetro(anyosquitados)
    def getEdadFalsa(self,anyosquitados):
        edad = 2026 - self.anyonacimiento - anyosquitados
        return edad



