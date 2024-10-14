import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Carga el dataset
ruta_dataset = os.path.join(os.path.dirname(__file__), '../dataset/dataset_transmilenio.csv')
df = pd.read_csv(ruta_dataset)

#Ruta para guardar el modelo y LabelEncoder
ruta_modelo = os.path.join(os.path.dirname(__file__), '')

# Mostrar las primeras filas del dataset
print(df.head(500))

# Codificar variables categóricas usando LabelEncoder
le_dia = LabelEncoder()
le_estacion_origen = LabelEncoder()
le_estacion_destino = LabelEncoder()
le_nivel_congestion = LabelEncoder()
le_clima = LabelEncoder()

# Codificar variables categóricas
df['Día de la semana'] = le_dia.fit_transform(df['Día de la semana'])
df['Estación de origen'] = le_estacion_origen.fit_transform(df['Estación de origen'])
df['Estación de destino'] = le_estacion_destino.fit_transform(df['Estación de destino'])
df['Clima'] = le_clima.fit_transform(df['Clima'])  # Agregar codificación para el clima
df['Nivel de congestión'] = le_nivel_congestion.fit_transform(df['Nivel de congestión'])  # Variable objetivo


# Separar características (X) y variable objetivo (y)
X = df[['Día de la semana', 'Hora de inicio', 'Hora de fin', 'Estación de origen', 'Estación de destino','Clima', 'Número de pasajeros']]
y = df['Nivel de congestión']

# Convertir horas en formato numérico usando .loc
X.loc[:, 'Hora de inicio'] = X['Hora de inicio'].apply(lambda x: int(x.split(':')[0]) if isinstance(x, str) else x)
X.loc[:, 'Hora de fin'] = X['Hora de fin'].apply(lambda x: int(x.split(':')[0]) if isinstance(x, str) else x)


# Dividir los datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Hacer predicciones
y_pred = clf.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Guardar los encoders
joblib.dump(le_dia, os.path.join(ruta_modelo, 'le_dia.pkl'))
joblib.dump(le_estacion_origen, os.path.join(ruta_modelo,'le_estacion_origen.pkl'))
joblib.dump(le_estacion_destino, os.path.join(ruta_modelo,'le_estacion_destino.pkl'))
joblib.dump(le_nivel_congestion, os.path.join(ruta_modelo,'le_nivel_congestion.pkl'))
joblib.dump(le_clima, os.path.join(ruta_modelo,'le_clima.pkl'))  # Guardar el encoder de clima

# Guardar el modelo entrenado
joblib.dump(clf, os.path.join(ruta_modelo,'modelo_congestion.pkl'))
