def find_number(fila, columna):

    # Almaceno un mensaje de error de posición
    msg = "La posición colocadas están fuera de la matriz"

    # Matriz de Ejemplo
    matriz = [
    [1, 2, 9, 10, 25],
    [4, 3, 8, 11, 24],
    [5, 3, 8, 11, 24],
    [16, 15, 14, 13, 22],
    [17, 18, 19, 20, 21]
    ]

    # Se verifica que los valores de la fila y la columna estén dentro del tamaño de la matriz
    if ( (fila < 1) or (fila >= int(len(matriz)) + 1) ) or ( (columna < 1) or (columna >= int(len(matriz[0])) + 1) ):
        return msg
    
    # Devuelve el valor dentro de esa posición
    return matriz[fila - 1][columna - 1]

# Caso de Prueba
assert find_number(2, 2) == 3, "Error en el caso de Prueba"

# Mensaje que sale un caso de que no haya errores de prueba
print("Todos los casos de prueba han pasado con éxito")

