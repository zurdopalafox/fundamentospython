class Mes:  
    nombre = ""
    temperaturaMinima = 0.0
    temperaturaMaxima = 0.0
    temperaturaMedia = 0.0


    def calcularTemperaturaMedia(self):
        self.temperaturaMedia = (self.temperaturaMinima + self.temperaturaMaxima) / 2
        return self.temperaturaMedia
    