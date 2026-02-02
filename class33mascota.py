from datetime import datetime
class Mascota:
    nombre = ""
    raza = ""
    anyonacimiento = 0
    anyoadopcion = 0
    anioactual = datetime.now().year

    def getAnyosAdoptada(self):
        return self.anioactual - self.anyoadopcion
    
    def getEdad(self):      
        return self.anioactual - self.anyonacimiento
    

        return self.anyoadopcion - self.anyonacimiento
    
