from abc import ABC, abstractmethod

# Cree la base PastorAlemán (animal) como una Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# Obligando a sus Subclases a definir el método hacer_sonido
class PastorAlemán(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Uso
mascota = PastorAlemán()
print(mascota.hacer_sonido())  # Guau!