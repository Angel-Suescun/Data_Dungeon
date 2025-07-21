from estructuras.nodoArbol import NodoArbol

class Arbol:
    def __init__(self, valor_raiz: any) -> None: # Inicializa el árbol con un nodo raíz
        self.raiz = NodoArbol(valor_raiz)

    def buscar(self, nodo_actual: 'NodoArbol', valor_objetivo: any) -> 'NodoArbol': # Busca un nodo con el valor objetivo en el árbol
        if nodo_actual.valor == valor_objetivo:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self.buscar(hijo, valor_objetivo)
            if resultado:
                return resultado
        return None
    
    def agregar_nodo(self, valor_padre: any, valor_nuevo: any) -> bool: # Agrega un nuevo nodo como hijo de un nodo padre especificado
        nodo_padre = self.buscar(self.raiz, valor_padre)
        if nodo_padre:
            nuevo_nodo = NodoArbol(valor_nuevo)
            nodo_padre.agregar_hijo(nuevo_nodo)
            return True
        else:
            print(f"⚠️ Nodo padre '{valor_padre}' no encontrado.")
            return False

    def mostrar(self, nodo_actual: 'NodoArbol' =None, nivel: int =0): # Muestra el árbol de manera jerárquica
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + f"- {nodo_actual.valor}")
        for hijo in nodo_actual.hijos:
            self.mostrar(hijo, nivel + 1)