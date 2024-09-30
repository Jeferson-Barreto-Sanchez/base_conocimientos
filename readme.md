Instrucciones para Ejecutar y Probar el Código

1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado Python y todas las bibliotecas necesarias para ejecutar el código.

Para facilitar la instalación de las dependencias, en la carpeta del proyecto encontrarás un archivo llamado requirements.txt. Este archivo contiene todas las bibliotecas que necesitas, por lo que podrás instalarlas todas de una vez.

Para instalar las dependencias, ejecuta en tu terminal:

pip install -r requirements.txt

Las principales bibliotecas utilizadas son:

-networkx: Para la manipulación de grafos y la ejecución del algoritmo de Dijkstra.
-tkinter: Para la creación de la interfaz gráfica donde podrás ingresar las estaciones.
-matplotlib: Para visualizar el grafo con las estaciones y sus conexiones.

2. Descripción del Código

Este código simula el sistema de transporte público de Bogotá, específicamente TransMilenio, utilizando un grafo en el que las estaciones están representadas como nodos, y las conexiones entre estaciones (con sus respectivas distancias en kilómetros) como aristas. El objetivo es encontrar la mejor ruta desde una estación de origen a una estación de destino utilizando el algoritmo de Dijkstra.

3. Estructura del Código

crear_grafo: Función que construye el grafo, añadiendo las estaciones (nodos) y las conexiones (aristas) entre ellas, asignando pesos (distancias en kilómetros) a cada conexión.

mejor_ruta: Implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos estaciones y calcular la distancia total del recorrido.

Interfaz gráfica (Tkinter): Permite al usuario ingresar las estaciones de origen y destino y muestra la mejor ruta disponible junto con la distancia total. Además, incluye un botón para visualizar el grafo con las estaciones y sus conexiones.

4. Ejecución del Código

Descarga o clona el repositorio donde se encuentra el código.

Instala las dependencias ejecutando en la terminal el siguiente comando desde la carpeta del proyecto:

pip install -r requirements.txt

Corre el programa ejecutando el siguiente comando en la terminal:

python transmilenio.py

Interfaz Gráfica:

Aparecerá una ventana en la que podrás ingresar las estaciones de origen y destino. Los códigos de las estaciones disponibles son:

PN: Portal Norte
HE: Héroes
C72: Calle 72
C100: Calle 100
C26: Calle 26
AJ: Av. Jiménez
PS: Portal Sur

Tras ingresar los datos, presiona el botón "Buscar mejor ruta" para obtener la mejor ruta y la distancia total del recorrido.

Visualizar el Grafo:

Si deseas ver un grafo visual que representa el sistema de estaciones y sus distancias, presiona el botón "Mostrar Grafo".

5. Ejemplo de Uso

Si ingresas la estación de origen como "PN" (Portal Norte) y la estación de destino como "PS" (Portal Sur), el programa calculará la ruta más corta entre estas estaciones y mostrará tanto las estaciones intermedias como la distancia total del recorrido.

6. Resultado Esperado

Después de ingresar las estaciones y ejecutar la búsqueda, deberías ver algo como lo siguiente en la interfaz:

La mejor ruta desde la estación Portal Norte hasta la estación Portal Sur es: 
Portal Norte -> Héroes -> Calle 72 -> Calle 26 -> Av. Jiménez -> Portal Sur

Distancia total del recorrido: 26.5 km

Además, si haces clic en el botón "Mostrar Grafo", se abrirá una ventana con una representación visual del sistema de TransMilenio.

Con estas instrucciones podrás ejecutar y probar el código sin problemas. ¡Buena suerte!