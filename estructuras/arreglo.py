from estructuras.nodo import Nodo

class Arreglo: # Clase que representa un arreglo de nodos con punteros
    def __init__(self, capacidad: int) -> None: # Inicializa el arreglo con una capacidad dada
        self.capacidad = capacidad
        self.datos = [None] * capacidad  # arreglo de referencias a nodos
        self.tamano = 0  # Inicializa el tamaño del arreglo

    def set_nodo(self, indice: int, nodo: 'Nodo') -> None: # Asigna un nodo a una posición específica del arreglo
        if not isinstance(nodo, Nodo):
            raise TypeError("Se debe proporcionar un objeto de tipo Nodo")
        if 0 <= indice < self.capacidad:
            self.datos[indice] = nodo
            self.tamano += 1  # solo contar si estamos agregando nuevo
        else:
            raise IndexError("Índice fuera de rango")

    def get_nodo(self, indice: int) -> any: # Obtiene el nodo en una posición específica del arreglo
        if 0 <= indice < self.capacidad:
            return self.datos[indice]
        else:
            raise IndexError("Índice fuera de rango")

    def eliminar(self, indice: int) -> None:
        if 0 <= indice < self.tamano:
            # Mover los elementos una posición a la izquierda
            for i in range(indice, self.tamano - 1):
                self.datos[i] = self.datos[i + 1]

            # Vaciar el último elemento (que quedó duplicado)
            self.datos[self.tamano - 1] = None
            self.tamano -= 1
        else:
            raise IndexError("Índice fuera de rango")

    def __str__(self) -> str: # Representación en cadena del arreglo
        return "[" + ", ".join(str(self.datos[i]) 
                            if self.datos[i] else "None" 
                            for i in range(self.capacidad)) + "]"

    def __repr__(self) -> str: # Representación para desarrolladores
        elementos = []
        for i in range(self.tamano):
            if self.datos[i] is not None and hasattr(self.datos[i], 'valor'):
                elementos.append(str(self.datos[i].valor))
        return "[" + ", ".join(elementos) + "]"
