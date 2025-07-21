# Asumo que tienes las clases importables desde estructuras
from estructuras.arreglo import Arreglo 
from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.arbol import Arbol
from estructuras.grafo import Grafo
from estructuras.lista import Lista
from estructuras.nodo import Nodo
from estructuras.vertice import Vertice
from game.objetos.objeto import Objeto
from game.objetos.buff import Buff
from game.objetos.mision import Mision
from game.objetos.habilidad import Habilidad

class Jugador:
    def __init__(self, nombre: str, ruta_imagen: str)->None: # Constructor del jugador
        self.nombre = nombre
        self.ruta_imagen = ruta_imagen
        self.inventario = Arreglo(12)           # Inventario del jugador
        self.vida = 100                        # Vida actual del jugador
        self.vida_maxima = 100                 # Vida máxima del jugador
        self.historial_acciones = Pila()        # Últimas acciones realizadas
        self.buff_activos = Cola()               # Buffs activos en orden
        self.arbol_habilidades = Arbol("Raíz")  # Árbol n-ario de habilidades
        self.posicion_actual = None              # Nodo vértice actual en el grafo del mapa
        self.misiones = Lista()                   # Lista de misiones activas

    # --- Inventario ---
    def agregar_item(self, objeto: 'Objeto') -> None:
    # Buscar si ya está en el inventario
        for i in range(self.inventario.tamano):
            nodo = self.inventario.get_nodo(i)
            if nodo and nodo.valor.nombre == objeto.nombre:
                print(f"Ya tienes el objeto: {objeto.nombre}")
                return

        # Verificar espacio disponible
        if self.inventario.tamano >= self.inventario.capacidad:
            print("Inventario lleno, no se puede agregar el objeto.")
            return

        # Agregar el nuevo objeto al primer espacio libre
        nuevo_nodo = Nodo(objeto)
        self.inventario.set_nodo(self.inventario.tamano, nuevo_nodo)
        print(f"Objeto agregado al inventario: {objeto.nombre}")

    def eliminar_item(self, nombre: str) -> None:
        for i in range(self.inventario.tamano):
            nodo = self.inventario.get_nodo(i)
            if nodo and nodo.valor.nombre == nombre:
                self.inventario.eliminar(i)
                print(f"Objeto eliminado del inventario: {nombre}")
                return
        print(f"No se encontró el objeto: {nombre}")
    
    def usar_item(self, indice: int) -> bool: # Usar un objeto del inventario
        actual = self.inventario.get_nodo(indice)
        if actual and actual > 0:
            self.inventario.eliminar(indice)
            self.historial_acciones.apilar(f"Usó {actual.valor.nombre}")
            return True
        return False

    def mostrar_inventario(self) -> None:
        print(f"Inventario: {repr(self.inventario)}")

    # --- Historial de acciones ---
    def registrar_accion(self, accion: str) -> None:
        self.historial_acciones.apilar(accion)

    def deshacer_ultima_accion(self) -> str:
        if not self.historial_acciones.esta_vacia():
            accion = self.historial_acciones.desapilar()
            print(f"Acción deshecha: {accion}")
            return accion
        else:
            print("No hay acciones para deshacer")
            return " "

    # --- Buffs ---
    def agregar_buff(self, buff: 'Buff') -> None:
        self.buff_activos.encolar(buff)
        print(f"Buff '{buff}' agregado")

    def aplicar_buff(self) -> 'Buff':
        if not self.buff_activos.esta_vacia():
            buff = self.buff_activos.desencolar()
            print(f"Buff '{buff}' aplicado")
            return buff
        else:
            print("No hay buffs activos")
            return None

    # --- Posición en el mapa ---
    def mover_a(self, vertice_destino: 'Vertice') -> None:
        if self.posicion_actual is None:
            print("No estás en ninguna posición, no puedes moverte.")
            return

        # Verificar si el destino es adyacente al actual
        if vertice_destino.valor not in self.posicion_actual.aristas:
            print(f"No puedes moverte a {vertice_destino.valor}, no está conectado.")
            return

        # Mover al nuevo vértice
        if vertice_destino in self.posicion_actual.aristas:
            self.posicion_actual = vertice_destino
            self.registrar_accion(f"Se movió a {vertice_destino.valor}")
        else:
            print(f"No puedes moverte a {vertice_destino.valor}, no está conectado.")

    # --- Misiones ---
    def agregar_mision(self, mision: 'Mision') -> None:
        self.misiones.agregar(mision)
        print(f"Misión '{mision}' agregada")

    def mostrar_misiones(self) -> None:
        print("Misiones activas:")
        for i, m in enumerate(self.misiones.items[:self.misiones.size]):
            print(f" {i+1}. {m}")

    # --- Árbol de habilidades ---
    def agregar_habilidad(self, padre_valor: any, habilidad: Habilidad) -> None:
        exito = self.arbol_habilidades.agregar_nodo(padre_valor, habilidad)
        if exito:
            print(f"Habilidad '{habilidad}' agregada bajo '{padre_valor}'")
        else:
            print(f"No se encontró la habilidad padre '{padre_valor}'")

    def activar_habilidad(self, habilidad: Habilidad) -> None:
        if habilidad in self.arbol_habilidades:
            habilidad.activar(self)
            print(f"Habilidad '{habilidad}' activada")
        else:
            print(f"Habilidad '{habilidad}' no encontrada en el árbol")