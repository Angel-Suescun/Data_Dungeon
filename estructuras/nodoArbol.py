class NodoArbol:
    def __init__(self, valor) -> None: #Constructor
        self.valor = valor
        self.hijos = [] #Lista de hijos

    def __str__(self) -> str: #Representación del nodo
        return str(self.valor)

    def agregar_hijo(self, hijo) -> None: #Método para agregar un hijo al nodo
        self.hijos.append(hijo)

    def __repr__(self) -> str: #Representación del nodo para debugging
        return f"NodoArbol({self.valor})"