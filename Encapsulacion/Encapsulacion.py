# Clase que encapsula atributos privados y usa métodos para acceder o modificar datos
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Método getter
    def obtener_edad(self):
        return self.__edad

    # Método setter
    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

# Crear objeto
p = Persona("Bryan", 30)
p.establecer_edad(40)
print(p.obtener_edad())
