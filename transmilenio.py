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
    G.add_edge("HE", "C100", weight=1.5) # Héroes a Calle 100
    G.add_edge("C72", "C26", weight=5.0) # Calle 72 a Calle 26
    G.add_edge("C26", "AJ", weight=2.0)  # Calle 26 a Av. Jiménez
    G.add_edge("AJ", "PS", weight=10.0)  # Av. Jiménez a Portal Sur
    G.add_edge("C100", "C72", weight=1.5) # Calle 100 a Calle 72
    G.add_edge("C72", "PN", weight=9.0)  # Calle 72 a Portal Norte
    G.add_edge("C26", "PN", weight=9.0)  # Calle 26 a Portal Norte
    G.add_edge("AJ", "PN", weight=10.0)  # Av. Jiménez a Portal Norte

    return G

# Encontrar la mejor ruta usando Dijkstra
def mejor_ruta(grafo, origen, destino):
    try:
        ruta_corta = nx.dijkstra_path(grafo, source=origen, target=destino, weight='weight')
        distancia = nx.dijkstra_path_length(grafo, source=origen, target=destino, weight='weight')
        return ruta_corta, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')

def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show(block=False) 

if __name__ == "__main__":
    grafo_transporte = crear_grafo()

    mostrar_grafo(grafo_transporte)

    print("---------------------------------------------- Bienvenido a Transmi Bogota ----------------------------------------------")
    print("")
    print("Con el fin de ayudarlo a encontrar la mejor ruta a su destino, ingrese sus estacion de origen y destino a continuación")
    print("")
    origen = input("Ingrese la estación de origen (PN, HE, C72, C100, C26, AJ, PS): ").upper()
    destino = input("Ingrese la estación de destino (PN, HE, C72, C100, C26, AJ, PS): ").upper()
    print("")

    # Buscar la mejor ruta
    ruta, distancia = mejor_ruta(grafo_transporte, origen, destino)

    if ruta:
        ruta_completa = [grafo_transporte.nodes[estacion]['nombre'] for estacion in ruta]
        print(f"La mejor ruta desde la estación {grafo_transporte.nodes[origen]['nombre']} hasta la estación {grafo_transporte.nodes[destino]['nombre']} es: {' -> '.join(ruta_completa)} con una distancia total de {distancia} km.")
        print("")
        print("----------------------------------------- Gracias Por Utilizar Transmi Bogota ----------------------------------------------")
    else:
        print(f"No existe una ruta entre {origen} y {destino}.")
    
    input("Presiona Enter para finalizar...")
    plt.close()  # Cierra la ventana del grafo después de la interacción