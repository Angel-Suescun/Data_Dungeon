from estructuras.grafo import Grafo

class Mapa:
    def __init__(self) -> None:  # Constructor del mapa
        self.grafo = Grafo()
        self.nombre_ubicacion_actual = None

    def agregar_ubicacion(self, nombre: str, ruta: str) -> None:  # Agregar una nueva ubicación al mapa
        self.grafo.agregar_vertice(nombre, ruta)

    def conectar_ubicaciones(self, origen: str, destino: str) -> None:  # Conectar dos ubicaciones en el mapa
        self.grafo.agregar_arista(origen, destino)

    def establecer_ubicacion_inicial(self, nombre: str) -> None:  # Establecer la ubicación inicial del mapa
        if nombre in self.grafo.vertices:
            self.nombre_ubicacion_actual = nombre
        else:
            raise ValueError(f"La ubicación '{nombre}' no existe en el mapa.")

    def mover_a(self, destino: str) -> bool:  # Mover al jugador a una ubicación adyacente
        actual = self.grafo.vertices.get(self.nombre_ubicacion_actual)
        if not actual:
            raise ValueError("Ubicación actual no está definida.")

        for adyacente in actual.aristas:
            if adyacente.valor == destino:
                self.nombre_ubicacion_actual = destino
                return True  # Movimiento exitoso
        return False  # No se puede mover a ese destino

    def obtener_ubicacion_actual(self) -> str:  # Obtener el nombre de la ubicación actual
        return self.nombre_ubicacion_actual

    def mostrar_mapa(self) -> None: # Mostrar el mapa completo
        self.grafo.mostrar()

    def obtener_adyacentes(self, nombre: str) -> list[str]:  # Obtener ubicaciones adyacentes a una ubicación dada
        if nombre in self.grafo.vertices:
            return [v.valor for v in self.grafo.vertices[nombre].aristas]
        else:
            return []
