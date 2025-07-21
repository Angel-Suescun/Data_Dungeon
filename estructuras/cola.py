from estructuras.nodo import Nodo

class Cola:
    def __init__(self) -> None: # Inicializa una cola vacía
        self.frente = None  # inicio de la cola
        self.final = None   # final de la cola
        self.tamano = 0

    def esta_vacia(self)-> bool: # Verifica si la cola está vacía
        return self.frente is None

    def encolar(self, valor: any)-> None: # Agrega un nuevo nodo al final de la cola
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar(self) -> any: # Elimina el nodo del frente de la cola y devuelve su valor
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None  # la cola queda vacía
        self.tamano -= 1
        return valor

    def ver_frente(self) -> any: # Devuelve el valor del nodo en el frente de la cola sin eliminarlo
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        return self.frente.valor

    def mostrar(self) -> None: # Muestra los valores de la cola
        actual = self.frente
        print("Cola:", end=" ")
        while actual:
            print(actual.valor, end=" <- ")
            actual = actual.siguiente
        print("None")

    def __str__(self) -> str: # Representación en cadena de la cola
        valores = []
        actual = self.frente
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return "Cola: [" + ", ".join(valores) + "]"
    
    def __repr__(self):
        return f"Cola({self.frente}, {self.final}, {self.tamano})"