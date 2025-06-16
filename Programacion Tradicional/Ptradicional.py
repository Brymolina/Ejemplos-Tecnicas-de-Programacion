# Programa para calcular el promedio semanal del clima en Atacames usando programación tradicional

def obtener_temperaturas_atacames():
    # Temperaturas simuladas de una semana en Atacames (°C)
    return [28.5, 29.0, 28.8, 30.1, 29.5, 28.9, 29.2]

def calcular_promedio(temperaturas):
   # Se calcula el promedio de una lista de temperaturas
    return sum(temperaturas) / len(temperaturas)

# Programa principal
temperaturas_semana = obtener_temperaturas_atacames() # se obtienen las temperaturas simuladas
promedio = calcular_promedio(temperaturas_semana)
# se calcula el promedio

# se muestra el resultado obtenido
print("Temperaturas semanales en Atacames:", temperaturas_semana)
print(f"Promedio semanal: {promedio:.2f}°C")