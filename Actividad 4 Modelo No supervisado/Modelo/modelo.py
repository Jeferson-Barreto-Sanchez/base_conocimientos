import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import folium
import os

# Cargar el dataset
ruta_dataset = os.path.join(os.path.dirname(__file__), '../dataset/dataset_transmilenio.csv')
data = pd.read_csv(ruta_dataset)

# Preprocesamiento de los datos: Convertir las variables categóricas en numéricas
label_encoder = LabelEncoder()

# Codificar variables categóricas
data['clima'] = label_encoder.fit_transform(data['clima'])
data['dia_semana'] = label_encoder.fit_transform(data['dia_semana'])
data['evento_especial'] = label_encoder.fit_transform(data['evento_especial'])

# Preparar los datos de entrenamiento (sin incluir 'hora_pico')
features = data[['capacidad', 'tiempo_permanencia', 'clima', 'dia_semana', 'evento_especial', 'distancia_estaciones']]

# Entrenar el modelo KMeans
kmeans = KMeans(n_clusters=5, random_state=42)  # Ajusta el número de clústeres según los resultados
kmeans.fit(features)

# Añadir los clústeres al dataset
data['cluster'] = kmeans.labels_

ruta_resultados = os.path.join(os.path.dirname(__file__), 'resultados_cluster/')
os.makedirs(ruta_resultados, exist_ok=True)  # Crear la carpeta si no existe
data.to_csv(os.path.join(ruta_resultados, 'dataset_transmilenio_con_clusters.csv'), index=False)

print("El modelo ha sido entrenado y los clusters guardados en 'dataset_transmilenio_con_clusters.csv'.")

ruta_mapas = os.path.join(os.path.dirname(__file__), 'mapas/')
os.makedirs(ruta_mapas, exist_ok=True)  # Crear la carpeta si no existe
# Mostrar los clusters en un mapa utilizando folium
def mostrar_mapa_cluster(data):
    # Crear un mapa centrado en Bogotá (ajusta las coordenadas según la ubicación de TransMilenio)
    mapa = folium.Map(location=[4.7110, -74.0721], zoom_start=12)
    
    # Añadir puntos al mapa por cada estación
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['latitud'], row['longitud']],
            radius=5 + row['capacidad'] / 10,  # El radio depende de la capacidad de la estación
            popup=f"Estación: {row['estacion']}\nCapacidad: {row['capacidad']}\nCluster: {row['cluster']}",
            color='blue' if row['cluster'] == 0 else 'green' if row['cluster'] == 1 else 'red',
            fill=True,
            fill_opacity=0.6
        ).add_to(mapa)
    
    # Guardar el mapa en un archivo HTML
    mapa.save(os.path.join(ruta_mapas,'mapa_transmilenio.html'))
    print("El mapa con los clústeres ha sido guardado como 'mapa_transmilenio.html'.")

# Llamada a la función para mostrar el mapa
mostrar_mapa_cluster(data)

# Función para mostrar la congestión en horas pico sobre el mapa
def mostrar_mapa_clusters(data):
    # Filtrar las horas pico
    horas_pico_data = data[data['hora_pico'] == 1]

    # Crear el mapa centrado en Bogotá
    mapa = folium.Map(location=[4.7110, -74.0721], zoom_start=12)

    # Definir los colores según el nivel de congestión (puedes ajustar el esquema de colores)
    def obtener_color_congestion(cluster):
        if cluster == 0:
            return 'green'
        elif cluster == 1:
            return 'yellow'
        elif cluster == 2:
            return 'orange'
        elif cluster == 3:
            return 'red'
        else:
            return 'purple'

    # Añadir los puntos de congestión al mapa
    for _, row in horas_pico_data.iterrows():
        folium.CircleMarker(
            location=[row['latitud'], row['longitud']],
            radius=10,
            popup=f"Estación: {row['estacion']}\nCapacidad: {row['capacidad']}\nCluster: {row['cluster']}",
            color=obtener_color_congestion(row['cluster']),
            fill=True,
            fill_color=obtener_color_congestion(row['cluster']),
            fill_opacity=0.7
        ).add_to(mapa)

    # Guardar el mapa como archivo HTML
    mapa.save(os.path.join(ruta_mapas,'mapa_congestion_horas_pico.html'))
    print("El mapa de congestión en horas pico ha sido guardado como 'mapa_congestion_horas_pico.html'.")

# Llamada a la función para mostrar el mapa de congestión
mostrar_mapa_clusters(data)