def find_missing_number(cant_elementos, numeros):

    cont = 1 # Contador que sirve para comparar con el valor proveniente de la lista

    # Iteramos sobre la lista de los números
    for valor in numeros:
        
        # Verificamos la igualdad entre elemento iterado y el contador
        if(valor != cont):
            return cont
        
        cont += 1 # Sumamos uno al contador

    return cont

# Caso de Prueba
assert find_missing_number(5, [1,2,4,5]) == 3, "Error en el caso de prueba"

# Mensaje que sale un caso de que no haya errores de prueba
print("Todos los casos de prueba han pasado con éxito")

