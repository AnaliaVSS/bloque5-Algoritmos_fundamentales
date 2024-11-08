def ordenar_por_seleccion(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        # Encontrar el índice del máximo elemento restante
        max_idx = i
        for j in range(i + 1, n):
            if estudiantes[j][1] > estudiantes[max_idx][1]:
                max_idx = j
        # Intercambiar el máximo elemento encontrado con el primer elemento
        estudiantes[i], estudiantes[max_idx] = estudiantes[max_idx], estudiantes[i]

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

# Ordenar los estudiantes por su promedio de calificaciones
ordenar_por_seleccion(estudiantes)

# Imprimir la lista ordenada
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante in estudiantes:
    print(f"{estudiante[0]}: {estudiante[1]}")
