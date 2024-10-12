
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Definir el sistema de transporte de TransMilenio como un grafo


def crear_grafo():
    G = nx.Graph()

    # Nodos (estaciones)
    G.add_node("PN", nombre="Portal Norte")
    G.add_node("HE", nombre="Héroes")
    G.add_node("C72", nombre="Calle 72")
    G.add_node("C100", nombre="Calle 100")
    G.add_node("C26", nombre="Calle 26")
    G.add_node("AJ", nombre="Av. Jiménez")
    G.add_node("PS", nombre="Portal Sur")

    # Conexiones entre estaciones (Aristas) con sus respectivos distancias en Km(pesos)
    G.add_edge("PN", "HE", weight=7.0)   # Portal Norte a Héroes
    G.add_edge("HE", "C72", weight=2.5)  # Héroes a Calle 72
    G.add_edge("HE", "C100", weight=1.5)  # Héroes a Calle 100
    G.add_edge("C72", "C26", weight=5.0)  # Calle 72 a Calle 26
    G.add_edge("C26", "AJ", weight=2.0)  # Calle 26 a Av. Jiménez
    G.add_edge("AJ", "PS", weight=10.0)  # Av. Jiménez a Portal Sur
    G.add_edge("C100", "C72", weight=1.5)  # Calle 100 a Calle 72
    G.add_edge("C72", "PN", weight=9.0)  # Calle 72 a Portal Norte
    G.add_edge("C26", "PN", weight=9.0)  # Calle 26 a Portal Norte
    G.add_edge("AJ", "PN", weight=10.0)  # Av. Jiménez a Portal Norte

    return G

# Encontrar la mejor ruta usando Dijkstra


def mejor_ruta(grafo, origen, destino):
    try:
        ruta_corta = nx.dijkstra_path(
            grafo, source=origen, target=destino, weight='weight')
        distancia = nx.dijkstra_path_length(
            grafo, source=origen, target=destino, weight='weight')
        return ruta_corta, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')


def buscar_ruta():
    origen = entrada_origen.get().upper()
    destino = entrada_destino.get().upper()

    # Verificar si las estaciones existen en el grafo
    if origen not in grafo_transporte.nodes or destino not in grafo_transporte.nodes:
        messagebox.showerror(
            "Error", "Las estaciones ingresadas no existen. Intenta de nuevo.")
        return

    # Buscar la mejor ruta
    ruta, distancia = mejor_ruta(grafo_transporte, origen, destino)

    if ruta:
        # Obtener los nombres completos de las estaciones
        ruta_completa = [grafo_transporte.nodes[estacion]['nombre']
                         for estacion in ruta]
        resultado.config(text=f"La mejor ruta desde la estación {grafo_transporte.nodes[origen]['nombre']} \n hasta la estación {
                         grafo_transporte.nodes[destino]['nombre']} es: \n\n{' -> '.join(ruta_completa)}\n\nDistancia total del recorrido : {distancia} km")
    else:
        messagebox.showinfo(
            "Sin ruta", "No existe una ruta entre las estaciones seleccionadas.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mejor Ruta - TransMilenio")

# Crear el grafo del sistema de transporte
grafo_transporte = crear_grafo()

# Etiquetas y entradas de texto para origen y destino
tk.Label(ventana, text="----------- Bienvenido a Transmi Bogota -------------").pack(pady=8)
tk.Label(ventana, text="Con el fin de ayudarlo a encontrar la mejor ruta a su destino,").pack(pady=1)
tk.Label(ventana, text="ingrese su estacion de origen y destino a continuación").pack(pady=5)
tk.Label(ventana, text="Estación de origen (PN, HE, C72, C100, C26, AJ, PS):").pack(pady=5)
entrada_origen = tk.Entry(ventana)
entrada_origen.pack(pady=5)

tk.Label(ventana, text="Estación de destino (PN, HE, C72, C100, C26, AJ, PS):").pack(pady=5)
entrada_destino = tk.Entry(ventana)
entrada_destino.pack(pady=5)

# Botón para buscar la ruta
boton_buscar = tk.Button(
    ventana, text="Buscar mejor ruta", command=buscar_ruta)
boton_buscar.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
resultado.pack(pady=10)


def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue',
            node_size=3000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show(block=False)


# Botón para mostrar el grafo
boton_grafo = tk.Button(ventana, text="Mostrar Grafo",
                        command=lambda: mostrar_grafo(grafo_transporte))
boton_grafo.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()