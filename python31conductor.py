from class31coche import Coche
from clase31deportivo import Deportivo

# Crear y probar un coche deportivo
print("Creando el coche deportivo...")
mi_deportivo = Deportivo()
mi_deportivo.marca = "Ferrari"
mi_deportivo.modelo = "488 GTB"
print(f"Coche deportivo creado: {mi_deportivo.marca} {mi_deportivo.modelo}")
print("Arrancando el coche deportivo...")
mi_deportivo.arrancar()
print("Acelerando el coche deportivo...")
mi_deportivo.acelerar()
mi_deportivo.acelerar()
print("Activando turbo del coche deportivo...")
mi_deportivo.turbo()
print("Frenando el coche deportivo...")
mi_deportivo.frenar()
print("Apagando el coche deportivo...")
mi_deportivo.apagar()
mi_deportivo.frenar()
print("Estado final del coche deportivo:")
print(f"Marca: {mi_deportivo.marca}, Modelo: {mi_deportivo.modelo}, Velocidad: {mi_deportivo.velocidad} km/h, Estado: {'Encendido'}" if mi_deportivo.estado else "Apagado") 
print("--------------------------------------------------"
      
      # Crear y probar un coche normal)

print("Creando el coche normal ...")
mi_coche = Coche()
mi_coche.marca = "Toyota"
mi_coche.modelo = "Corolla"
print(f"Coche creado: {mi_coche.marca} {mi_coche.modelo}")
print("Arrancando el coche...")
mi_coche.arrancar()
print("Acelerando el coche...")
mi_coche.acelerar()
mi_coche.acelerar()
print("Frenando el coche...")
mi_coche.frenar()
print("Apagando el coche...")
mi_coche.apagar()
mi_coche.frenar()
print("Estado final del coche:")
print(f"Marca: {mi_coche.marca}, Modelo: {mi_coche.modelo}, Velocidad: {mi_coche.velocidad} km/h, Estado: {'Encendido'}" if mi_coche.estado else "Apagado")

                                                                                                           