class Coche:
    # Constructor
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado =  False  # False = apagado, True = encendido

    def arrancar(self):
        self.estado = True
        print("El coche ha arrancado.")

    def apagar(self):
        self.estado = False
        print("El coche se ha apagado.")

    def acelerar(self):
        if self.estado:
            self.velocidad += 10
            print(f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h")
        else:
            print("El coche está apagado. No se puede acelerar.")
            
    def frenar(self):
        if self.estado and self.velocidad > 0:
            self.velocidad -= 10
            print(f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h")
        elif not self.estado:
            print("El coche está apagado. No se puede frenar.")
        else:
            print("El coche ya está detenido.") 

