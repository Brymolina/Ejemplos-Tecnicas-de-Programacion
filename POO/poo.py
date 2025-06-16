# Programa para calcular el promedio semanal del clima en Atacames usando Programación Orientada a Objetos

class ClimaSemana:
    def __init__(self):
        # Temperaturas de una semana en Atacames (°C)
        self.__temperaturas = [28.5, 29.0, 28.8, 30.1, 29.5, 28.9, 29.2]

    def calcular_promedio(self):
        # se retorna el promedio de las temperaturas que se ha almacenado
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultado(self):
        # se muestra las temperaturas y el promedio calculado en atacames
        print("Temperaturas semanales en Atacames:", self.__temperaturas)
        promedio = self.calcular_promedio()
        print(f"Promedio semanal: {promedio:.2f}°C")

# Programa principal
semana_atacames = ClimaSemana()
semana_atacames.mostrar_resultado()