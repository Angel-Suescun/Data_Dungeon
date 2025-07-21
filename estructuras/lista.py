class Lista:
    def __init__(self) -> None: # Inicializa una lista vacía
        self.capacidad = 10
        self.size = 0
        self.items = [None] * self.capacidad

    def _redimensionar(self) -> None: # Aumenta la capacidad de la lista
        self.capacidad *= 2
        nuevos_items = [None] * self.capacidad
        for i in range(self.size):
            nuevos_items[i] = self.items[i]
        self.items = nuevos_items

    def agregar(self, item) -> None: # Agrega un elemento al final de la lista
        if self.size == self.capacidad:
            self._redimensionar()
        self.items[self.size] = item
        self.size += 1

    def eliminar(self, item: any) -> None: # Elimina la primera ocurrencia de un elemento en la lista
        for i in range(self.size):
            if self.items[i] == item:
                for j in range(i, self.size - 1):
                    self.items[j] = self.items[j + 1]
                self.items[self.size - 1] = None
                self.size -= 1
                return
        raise ValueError("Item no encontrado en la lista")

    def obtener_tamano(self) -> int: # Devuelve el número de elementos en la lista
        return self.size

    def obtener_elemento(self, indice: int) -> any: # Devuelve el elemento en la posición indicada
        if 0 <= indice < self.size:
            return self.items[indice]
        raise IndexError("Índice fuera de rango")
    
    def __str__(self) -> str: # Representación en cadena de la lista
        return "[" + ", ".join(str(self.items[i]) for i in range(self.size)) + "]"
    
    def __repr__(self) -> str: # Representación para desarrolladores
        return "[" + ", ".join(str(self.items[i]) for i in range(self.size)) + "]"
    
    def __iter__(self): # Permite iterar sobre los elementos de la lista
        for i in range(self.size):
            yield self.items[i]

