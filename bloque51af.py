from collections import deque

# Clase Nodo que representa cada grado y sus estudiantes
class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.izquierda = None
        self.derecha = None

# Función para realizar un recorrido por niveles en el árbol
def recorrido_por_niveles(raiz):
    if not raiz:
        return

    # Usamos una cola para realizar el recorrido por niveles
    cola = deque([raiz])
    while cola:
        nodo_actual = cola.popleft()  # Extraemos el nodo actual de la cola
        # Imprimimos el grado y la lista de estudiantes del nodo actual
        print(f"Grado: {nodo_actual.grado}, Estudiantes: {', '.join(nodo_actual.estudiantes)}")
        # Añadimos los hijos izquierdo y derecho a la cola si existen
        if nodo_actual.izquierda:
            cola.append(nodo_actual.izquierda)
        if nodo_actual.derecha:
            cola.append(nodo_actual.derecha)

# Ejemplo de uso
# Crear el árbol de grupos de estudiantes
raiz = Nodo("Primero", ["Alice", "Bob"])
raiz.izquierda = Nodo("Segundo", ["Carlos", "Diana"])
raiz.derecha = Nodo("Tercero", ["Eva", "Francisco"])
raiz.izquierda.izquierda = Nodo("Cuarto", ["George", "Hannah"])
raiz.izquierda.derecha = Nodo("Quinto", ["Irene", "Jack"])
raiz.derecha.izquierda = Nodo("Sexto", ["Kevin", "Laura"])
raiz.derecha.derecha = Nodo("Séptimo", ["Mike", "Nina"])

# Realizar el recorrido por niveles e imprimir los resultados
recorrido_por_niveles(raiz)



