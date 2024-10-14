import csv
import random
import os

# Posibles valores para las nuevas variables
climas = ['soleado', 'nublado', 'lluvioso']
dias_semana = ['laboral', 'fin de semana']
eventos_especiales = [0, 1]  # 0: No, 1: Sí
horas_pico = [0, 1]  # 0: No, 1: Sí
distancias = [round(random.uniform(0.5, 20.0), 2) for _ in range(1000)]  # Distancia entre 0.5 y 20 km

# Estaciones del TransMilenio con coordenadas (ejemplo)
estaciones = [
    ('Portal El Dorado', 4.681081, -74.121352),
    ('Calle 100', 4.685253, -74.057590),
    ('Gobernacion', 4.642477, -74.096455),
    ('Portal Sur', 4.596921, -74.169589),
    ('Portal Del Norte',4.754521, -74.046076),
    ('Avenida Chile', 4.665855, -74.074947),
    ('Calle 26', 4.615955, -74.072385)
]

# Crear la carpeta 'dataset' si no existe
ruta_dataset = os.path.join(os.path.dirname(__file__), '')
os.makedirs(ruta_dataset, exist_ok=True)  

# Generar el dataset con las nuevas variables
ruta_archivo = os.path.join(ruta_dataset, 'dataset_transmilenio.csv')  # Ruta completa del archivo CSV

# Generar el dataset con las nuevas variables
with open(ruta_archivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escribir los encabezados con las nuevas columnas
    writer.writerow(['estacion', 'latitud', 'longitud', 'capacidad', 'tiempo_permanencia', 'hora_dia', 'clima', 'dia_semana', 'evento_especial', 'distancia_estaciones', 'hora_pico'])
    
    for _ in range(1000):  # 1000 filas de datos
        # Seleccionar una estación aleatoria con sus coordenadas
        estacion, latitud, longitud = random.choice(estaciones)
        
        capacidad = random.randint(10, 100)  # Número de pasajeros
        tiempo_permanencia = round(random.uniform(5.0, 30.0), 2)  # Tiempo en minutos
        hora_dia = random.randint(0, 23)  # Hora del día
        clima = random.choice(climas)
        dia_semana = random.choice(dias_semana)
        evento_especial = random.choice(eventos_especiales)
        distancia = random.choice(distancias)
        hora_pico = random.choice(horas_pico)
        
        # Escribir la fila de datos con las coordenadas y la estación
        writer.writerow([estacion, latitud, longitud, capacidad, tiempo_permanencia, hora_dia, clima, dia_semana, evento_especial, distancia, hora_pico])

print(f"El dataset ha sido actualizado y guardado como 'dataset_transmilenio.csv'.")
