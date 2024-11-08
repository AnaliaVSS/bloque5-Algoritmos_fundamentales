def buscar_calificacion(matriz, calificacion_buscada):
    for i, fila in enumerate(matriz):
        for j, calificacion in enumerate(fila):
            if calificacion == calificacion_buscada:
                return i, j
    return None

# Ejemplo de uso
# Matriz de calificaciones: cada fila es un estudiante y cada columna una materia
calificaciones = [
    [90, 85, 78],
    [88, 92, 80],
    [79, 95, 84]
]

calificacion_buscada = 92
resultado = buscar_calificacion(calificaciones, calificacion_buscada)

if resultado:
    estudiante, asignatura = resultado
    print(f"La calificación {calificacion_buscada} se encuentra en el estudiante {estudiante + 1}, asignatura {asignatura + 1}.")
else:
    print(f"La calificación {calificacion_buscada} no se ha encontrado en la matriz.")
