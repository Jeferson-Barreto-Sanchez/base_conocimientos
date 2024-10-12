import pandas as pd
import random

# Definir estaciones de TransMilenio
estaciones = ['Portal Norte', 'Héroes', 'Calle 72', 'Calle 100', 'Calle 26', 'Av. Jiménez', 'Portal Sur']

# Definir días de la semana y rangos horarios
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
rango_horas = [(6, 9), (9, 12), (12, 15), (15, 18), (18, 21), (21, 24)]  # Dividido en periodos de 3 horas

# Definir rangos de número de pasajeros y niveles de congestión
rangos_pasajeros = {'bajo': (0, 20), 'medio': (21, 40), 'alto': (41, 60), 'super':(61,80), 'mega':(81,100)}
niveles_congestion = ['Baja', 'Moderada', 'Alta']
climas = ['Soleado', 'Lluvioso', 'Nublado']  # Climas posibles

# Función para generar un número aleatorio de pasajeros según el rango de congestión
def generar_pasajeros(nivel_congestion,clima):
    if nivel_congestion == 'Baja' and clima== "Soleado":
        return random.randint(rangos_pasajeros['bajo'][0], rangos_pasajeros['medio'][1])
    elif nivel_congestion == 'Baja' and clima== "Nublado":
        return random.randint(rangos_pasajeros['bajo'][0], rangos_pasajeros['medio'][0])
    elif nivel_congestion == 'Baja' and clima== "Lluvioso":
        return random.randint(rangos_pasajeros['bajo'][0], rangos_pasajeros['medio'][0])
    elif nivel_congestion == 'Moderada' and clima== "Soleado":
        return random.randint(rangos_pasajeros['medio'][0], rangos_pasajeros['medio'][1])
    elif nivel_congestion == 'Moderada' and clima== "Nublado":
        return random.randint(rangos_pasajeros['medio'][1], rangos_pasajeros['alto'][0])
    elif nivel_congestion == 'Moderada' and clima== "Lluvioso" :
        return random.randint(rangos_pasajeros['medio'][1], rangos_pasajeros['alto'][1])
    elif nivel_congestion == 'Alta' and clima== "Soleado" :
        return random.randint(rangos_pasajeros['super'][0], rangos_pasajeros['super'][1])
    elif nivel_congestion == 'Alta' and clima== "Nublado" :
        return random.randint(rangos_pasajeros['super'][1], rangos_pasajeros['mega'][0])
    elif nivel_congestion == 'Alta' and clima== "Lluvioso" :
        return random.randint(rangos_pasajeros['alto'][1], rangos_pasajeros['mega'][1])
    else:
        return random.randint(rangos_pasajeros['alto'][1], rangos_pasajeros['mega'][1])

# Generar el dataset simulado
def generar_dataset_transmilenio(num_registros=1000):
    dataset = []
    for _ in range(num_registros):
        dia = random.choice(dias_semana)
        hora_inicio, hora_fin = random.choice(rango_horas)
        estacion_origen = random.choice(estaciones)
        estacion_destino = random.choice([est for est in estaciones if est != estacion_origen])
        nivel_congestion = random.choice(niveles_congestion)
        clima = random.choice(climas)  # Seleccionar clima aleatoriamente
        pasajeros = generar_pasajeros(nivel_congestion,clima)
        
        registro = {
            'Día de la semana': dia,
            'Hora de inicio': f'{hora_inicio}:00',
            'Hora de fin': f'{hora_fin}:00',  # Ajustar hora de fin según el tiempo de viaje
            'Estación de origen': estacion_origen,
            'Estación de destino': estacion_destino,
            'Número de pasajeros': pasajeros,
            'Nivel de congestión': nivel_congestion,
            'Clima': clima  # Agregar clima al registro
        }
        dataset.append(registro)

    df = pd.DataFrame(dataset)
    df.to_csv('dataset_transmilenio.csv', index=False)
    return df

# Generar el dataset y guardarlo en un archivo CSV
df = generar_dataset_transmilenio(50000) 
print("Dataset generado y guardado en 'dataset_transmilenio.csv'")
