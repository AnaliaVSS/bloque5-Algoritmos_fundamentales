class Nodo:
    def __init__(self, promedio, estudiante):
        self.promedio = promedio
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, promedio, estudiante):
        if self.raiz is None:
            self.raiz = Nodo(promedio, estudiante)
        else:
            self._insertar_recursivo(self.raiz, promedio, estudiante)
    
    def _insertar_recursivo(self, nodo, promedio, estudiante):
        if promedio < nodo.promedio:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.izquierda, promedio, estudiante)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.derecha, promedio, estudiante)

    def inorden(self, nodo, resultado):
        if nodo is not None:
            self.inorden(nodo.izquierda, resultado)
            resultado.append((nodo.estudiante, nodo.promedio))
            self.inorden(nodo.derecha, resultado)

# Ejemplo de uso
# Lista de estudiantes y sus promedios de calificaciones
estudiantes = [
    ("Analía", 85.5),
    ("Maximiliano", 90.0),
    ("Egenia", 88.0),
    ("German", 92.5),
    ("Facundo", 87.0),
    ("Josefina", 89.0)
]

# Crear el ABB e insertar los estudiantes
arbol = ABB()
for estudiante, promedio in estudiantes:
    arbol.insertar(promedio, estudiante)

# Realizar el recorrido inorden y mostrar los resultados
resultado = []
arbol.inorden(arbol.raiz, resultado)

print("Estudiantes ordenados por promedio (de menor a mayor):")
for estudiante, promedio in resultado:
    print(f"{estudiante}: {promedio}")
