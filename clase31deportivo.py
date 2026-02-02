from class31coche import Coche

class Deportivo(Coche):
    # Constructor
    def __init__(self):
        super().__init__()
        self.tipo_deportivo = ""  # Ejemplo: "Coupe", "Convertible", etc.

    def acelerar(self):
        if self.estado:
            self.velocidad += 20  # Acelera más rápido que un coche normal
            print(f"El coche deportivo ha acelerado. Velocidad actual: {self.velocidad} km/h")
        else:
            print("El coche deportivo está apagado. No se puede acelerar.")

    def frenar(self):
        if self.estado and self.velocidad > 0:
            self.velocidad -= 20  # Frena más rápido que un coche normal
            print(f"El coche deportivo ha frenado. Velocidad actual: {self.velocidad} km/h")
        elif not self.estado:
            print("El coche deportivo está apagado. No se puede frenar.")
        else:
            print("El coche deportivo ya está detenido.")

    def turbo(self):
        if self.estado:
            self.velocidad += 100
            print(f"¡Turbo activado! Velocidad actual: {self.velocidad} km/h")
        else:
            print("El coche deportivo está apagado. No se puede activar el turbo.")

# quiero que el Deportivo siempre tenga 100 km/h más de velocidad máxima que un coche normal
            def getVelocidadMaxima(self):
                velocidadCoche = super().getVelocidadMaxima()
                return velocidadCoche+ 100 
            