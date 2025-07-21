from estructuras.ElementoHash import ElementoHash 

class TablaHash:
    def __init__(self, capacidad: int = 10) -> None:  # Inicializa la tabla hash con una capacidad dada
        self.capacidad = capacidad
        self.tabla = [None] * capacidad  # Crea una lista de tamaño 'capacidad' llena de None
    
    def _hash(self, clave: any) -> int:  # Función hash simple usando suma de códigos ASCII
        # Función hash simple usando suma de códigos ASCII
        return sum(ord(c) for c in str(clave)) % self.capacidad #

    def insertar(self, clave: any, valor: any) -> None:  # Inserta un nuevo elemento en la tabla hash
        indice = self._hash(clave)
        nuevo_elemento = ElementoHash(clave, valor)

        if self.tabla[indice] is None:
            self.tabla[indice] = nuevo_elemento
        else:
            actual = self.tabla[indice]
            while actual:
                if actual.clave == clave:
                    actual.valor = valor  # actualizar si ya existe
                    return
                if actual.siguiente is None:
                    break
                actual = actual.siguiente
            actual.siguiente = nuevo_elemento  # agregar al final

    def obtener(self, clave: any) -> any:  # Obtiene el valor asociado a una clave
        indice = self._hash(clave)
        actual = self.tabla[indice]
        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        return None  # no encontrado

    def mostrar(self)-> None:  # Muestra el contenido de la tabla hash
        for i, elemento in enumerate(self.tabla):
            print(f"[{i}]", end=" → ")
            actual = elemento
            while actual:
                print(f"({actual.clave}: {actual.valor})", end=" → ")
                actual = actual.siguiente
            print("None")