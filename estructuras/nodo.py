class Nodo:
    def __init__(self, valor: any) -> None: # Inicializa un nodo con un valor y una referencia a otro nodo
        self.valor = valor
        self.siguiente = None  # referencia (puntero) a otro nodo

    def __repr__(self): # Representación en cadena del nodo
        return f"Nodo({self.valor})"