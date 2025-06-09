# Clase base
class Animal:
    def hacer_sonido(self):
        return "Algún sonido"

# Subclases con comportamiento diferente
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Función que demuestra polimorfismo
def reproducir_sonido(animal):
    print(animal.hacer_sonido())

# Pruebas
reproducir_sonido(Perro())
reproducir_sonido(Gato())