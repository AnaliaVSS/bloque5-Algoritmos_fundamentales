def busqueda_binaria(lista, estudiante):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == estudiante:
            return medio
        elif lista[medio] < estudiante:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None

# Ejemplo de uso
estudiantes = ["Alice", "Bob", "Carlos", "Diana", "Eva", "Francisco"]
estudiante_buscado = "Carlos"

# Realizar la búsqueda binaria
resultado = busqueda_binaria(estudiantes, estudiante_buscado)

if resultado is not None:
    print(f"El estudiante {estudiante_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El estudiante {estudiante_buscado} no se ha encontrado en la lista.")
