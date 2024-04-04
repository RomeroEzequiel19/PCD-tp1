def is_palindromo(cadena):
    # Se convierte la cadena a minúsculas y se elimina los espacios en blanco
    cadena = cadena.lower().replace(" ", "")

    # Se invierte la cadena y se unen los elementos en una nueva
    cadena_reversa = "".join(reversed(cadena))

    # Verifica la longitud de la cadena de caracteres
    if len(cadena) < 1 or len(cadena) > 1000000 :
        return "La longitud de la cadena no está dentro del rango especificado"

    # Compara la cadena y su opuesto
    if cadena == cadena_reversa:

        return cadena_reversa

    else:

        # Se almacenan los valores pares
        valores_pares = []

        # Se almacenan los valores impares
        valores_impares = []

        # Se verifica la repetición de cada caracter en la cadena
        for valor in cadena:
            # Se busca si el valor está en la lista de impares
            if valor in valores_impares:
                # Se elimina de la lista y se agrega al de valores pares
                valores_impares.remove(valor)
                valores_pares.append(valor)
            else:
                # Se agrega a la lista de impares
                valores_impares.append(valor)

        # Si hay más de dos valores impares, no se puede realizar el palíndromo
        if len(valores_impares) > 1:
            return "NO SOLUTION"
        
        # Si hay un caracter impar lo ponemos en el centro del palíndromo
        if len(valores_impares) == "":
            central = ""
        else:
            central = valores_impares[0]

        # Se realiza la parte izquierda del palíndromo
        palindromo_izquierda = "".join(valores_pares)

        # Se realiza la parte izquierda invirtiendo los valores pares
        palindromo_derecha = "".join(reversed(palindromo_izquierda))

        # Se realiza el resultado final del palíndromo
        palindromo = palindromo_izquierda + central + palindromo_derecha

        return palindromo
    
# Caso de Prueba
assert is_palindromo("aabbc") == "abcba", "Error en el caso de prueba"

# Mensaje que sale un caso de que no haya errores de prueba
print("Todos los casos de prueba han pasado con éxito")

