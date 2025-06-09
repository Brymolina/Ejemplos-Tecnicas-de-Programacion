# Clase base con atributos comunes
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"{self.marca} {self.modelo}"

# Subclase que hereda de Vehiculo y añade nuevos atributos
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas,):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.puertas = puertas

    def mostrar_info(self):
        return f"{super().mostrar_info()} con {self.puertas} puertas"

# Crear objeto y mostrar información
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.mostrar_info())