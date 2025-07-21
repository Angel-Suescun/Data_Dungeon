class Vertice:
    def __init__(self, valor: any, ruta: str) -> None:  # Inicializa un vértice con un valor y una lista de adyacencia
        self.valor = valor
        self.aristas = []  # lista de nodos adyacentes al vértice
        self.ruta = ruta

    def agregar_arista(self, vertice: 'Vertice') -> None:  # Agrega un vértice adyacente a la lista de adyacentes
        self.aristas.append(vertice)

    def __repr__(self) -> str:  # Representación del vértice
        return f"Vertice(valor={self.valor}, aristas={len(self.aristas)})"