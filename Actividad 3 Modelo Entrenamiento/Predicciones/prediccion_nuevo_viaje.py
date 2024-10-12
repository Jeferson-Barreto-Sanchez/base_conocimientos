import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib
import os


# Carga el modelo entrenado y encoders
ruta_modelos = os.path.join(os.path.dirname(__file__), '../modelo/modelo_congestion.pkl')

modelo = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/modelo_congestion.pkl'))
le_dia = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/le_dia.pkl'))
le_estacion_origen = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/le_estacion_origen.pkl'))
le_estacion_destino = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/le_estacion_destino.pkl'))
le_nivel_congestion = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/le_nivel_congestion.pkl'))
le_clima = joblib.load(os.path.join(os.path.dirname(__file__), '../modelo/le_clima.pkl'))

# Lista de días de la semana en el orden correcto
dias_ordenados = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Reordena los días de acuerdo a la lista de días
dias_semana = sorted(list(le_dia.classes_), key=lambda x: dias_ordenados.index(x))

estaciones_origen = le_estacion_origen.classes_  
estaciones_destino = le_estacion_destino.classes_
clima = le_clima.classes_

# Crear lista de horas en formato HH:MM
horas = [f"{str(h).zfill(2)}:00" for h in range(24)]  # Desplegable de horas en formato HH:MM

# Función para predecir la congestión
def predecir_congestion():
    dia = dia_var.get()
    hora_inicio_str = hora_inicio_var.get()
    hora_fin_str = hora_fin_var.get()
    estacion_origen = estacion_origen_var.get()
    estacion_destino = estacion_destino_var.get()
    num_pasajeros = int(num_pasajeros_var.get())

    # Convertir las horas a formato numérico (solo la hora, ignorando los minutos)
    try:
        hora_inicio = int(hora_inicio_str.split(':')[0])
        hora_fin = int(hora_fin_str.split(':')[0])
    except ValueError:
        resultado_label.config(text="Error: Las horas deben estar en formato HH:MM.")
        return

    # Codificar las entradas usando los LabelEncoders previamente entrenados
    try:
        dia_codificado = le_dia.transform([dia])[0]  # Convertir día al formato que conoce el modelo
        estacion_origen_codificada = le_estacion_origen.transform([estacion_origen])[0]  # Codificar estación de origen
        estacion_destino_codificada = le_estacion_destino.transform([estacion_destino])[0]  # Codificar estación de destino
    except ValueError as e:
        resultado_label.config(text=f"Error en la codificación: {e}")
        return

    clima_codificado = le_clima.transform([clima_var.get()])[0]  # Codificar clima
    
    # Crear un DataFrame para las entradas
    entrada = pd.DataFrame([[dia_codificado, hora_inicio, hora_fin, estacion_origen_codificada, estacion_destino_codificada, clima_codificado, num_pasajeros]], 
                        columns=['Día de la semana', 'Hora de inicio', 'Hora de fin', 'Estación de origen', 'Estación de destino', 'Clima', 'Número de pasajeros'])
    
    # Realizar la predicción
    try:
        prediccion = modelo.predict(entrada)
        nivel_congestion = le_nivel_congestion.inverse_transform(prediccion)[0]
        resultado_label.config(text=f"Nivel de congestión predicho: {nivel_congestion}")
    except Exception as e:
        resultado_label.config(text=f"Error en la predicción: {e}")
        print(f"Error en la predicción: {e}")

# Crear la interfaz con tkinter
root = tk.Tk()
root.title("Predicción de Congestión")

# Variables de Tkinter para los campos
dia_var = tk.StringVar()
hora_inicio_var = tk.StringVar()
hora_fin_var = tk.StringVar()
estacion_origen_var = tk.StringVar()
estacion_destino_var = tk.StringVar()
clima_var = tk.StringVar()
num_pasajeros_var = tk.StringVar()

# Etiquetas y entradas (con valores extraídos automáticamente desde los LabelEncoders)
ttk.Label(root, text="Día de la semana:").grid(row=0, column=0)
ttk.Combobox(root, textvariable=dia_var, values=list(dias_semana)).grid(row=0, column=1)  # Usar clases originales

ttk.Label(root, text="Hora de inicio (HH:MM):").grid(row=1, column=0)
ttk.Combobox(root, textvariable=hora_inicio_var, values=horas).grid(row=1, column=1)  # Desplegable de horas

ttk.Label(root, text="Hora de fin (HH:MM):").grid(row=2, column=0)
ttk.Combobox(root, textvariable=hora_fin_var, values=horas).grid(row=2, column=1)  # Desplegable de horas

ttk.Label(root, text="Estación de origen:").grid(row=3, column=0)
ttk.Combobox(root, textvariable=estacion_origen_var, values=list(estaciones_origen)).grid(row=3, column=1)  # Usar clases originales

ttk.Label(root, text="Estación de destino:").grid(row=4, column=0)
ttk.Combobox(root, textvariable=estacion_destino_var, values=list(estaciones_destino)).grid(row=4, column=1)  # Usar clases originales

ttk.Label(root, text="Clima:").grid(row=5, column=0)
ttk.Combobox(root, textvariable=clima_var, values=list(clima)).grid(row=5, column=1)

ttk.Label(root, text="Número de pasajeros:").grid(row=6, column=0)
ttk.Entry(root, textvariable=num_pasajeros_var).grid(row=6, column=1)

# Botón de predicción
ttk.Button(root, text="Predecir Congestión", command=predecir_congestion).grid(row=7, column=0, columnspan=5)

# Etiqueta de resultado
resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=8, column=0, columnspan=2)  # Cambié el índice de la fila a 8 para que no se superponga

# Iniciar la interfaz
root.mainloop()
