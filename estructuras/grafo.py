from estructuras.vertice import Vertice

class Grafo:
    def __init__(self) -> None: # Inicialisa un grafo vacío
        self.vertices = {}  # nombre → Vertice

    def agregar_vertice(self, valor: any, ruta: str) -> None: # agrega un vértice al grafo
        if valor not in self.vertices:
            self.vertices[valor] = Vertice(valor, ruta)

    def agregar_arista(self, origen: str , destino: str) -> None: # agrega una arista entre dos vértices
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].agregar_arista(self.vertices[destino])
            self.vertices[destino].agregar_arista(self.vertices[origen])  # grafo no dirigido

    def mostrar(self) -> None:  # muestra los vértices y sus adyacentes
        for valor, vertice in self.vertices.items():
            conexiones = [v.valor for v in vertice.aristas]
            print(f"{valor} → {conexiones}")
    
    def __str__(self) -> str:  # representación del grafo
        return "\n".join(f"{valor}: {vertice}" for valor, vertice in self.vertices.items())