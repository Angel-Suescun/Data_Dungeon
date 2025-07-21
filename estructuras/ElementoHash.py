class ElementoHash:
    def __init__(self, clave, valor)-> None: # Inicializa un elemento de la tabla hash con una clave y un valor
        self.clave = clave
        self.valor = valor
        self.siguiente = None

    def __str__(self) -> str: # Representación en cadena del elemento hash
        return f"Clave: {self.clave}, Valor: {self.valor}"