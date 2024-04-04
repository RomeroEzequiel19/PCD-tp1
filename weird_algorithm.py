def find_sequence(num):

    # Verifica si el número es entero positivo y entre los valores aceptados
    while ( num < 1 or num > 10^6  ):
        print("Error. Debe ingresar un número entero positivo")
        num = int(input("Ingrese un número entero positivo: "))

    lista = [] # Para almacenar la lista de números

    lista.append(num) # Se agrega el primer elemento a la lista

    # Iteramos para hallar la secuencia
    while num > 1:

        if(num % 2 == 0):

            num = num // 2 # Acción cuando el valor es par

            lista.append(num) # Agregamos el nuevo valor a la lista
              
        else:

            num = (num * 3) + 1 # Acción a realzar cuando el valor en impar

            lista.append(num) # Agregamos el nuevo valor a la lista
        
    return lista

# Caso de Prueba
assert find_sequence(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en la secuencia"

# Mensaje que sale un caso de que no haya errores de prueba
print("Todos los casos de prueba han pasado con éxito")

