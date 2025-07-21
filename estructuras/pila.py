from estructuras.nodo import Nodo

class Pila:
    def __init__(self) -> None:  # Inicializa la pila vacía
        self.tope = None
        self.tamano = 0

    def esta_vacia(self) -> bool:  # Verifica si la pila está vacía
        return self.tope is None
    
    def apilar(self, valor: any) -> None:  # Agrega un nuevo elemento a la pila
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamano += 1

    def desapilar(self) -> any:  # Elimina y devuelve el último elemento agregado a la pila
        if self.esta_vacia():
            raise IndexError("Desapilando de una pila vacía")
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return valor

    def ver_tope(self) -> any:  # Devuelve el valor del último elemento sin eliminarlo
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.tope.valor

    def __str__(self) -> str:  # Representación en cadena de la pila
        elementos = []
        nodo_actual = self.tope
        while nodo_actual:
            elementos.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
        return "Pila: [" + ", ".join(elementos) + "]"