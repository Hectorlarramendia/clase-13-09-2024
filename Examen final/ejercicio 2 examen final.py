"""
Escribe un programa en que analice una cadena ingresada por el usuario.
determine:
cantidad de vocales, consonantes y otros caracteres(como espacios,numeros o simbolos) contiene.
cantidad de palabras y si existe la palabra "que"
cantidad de Mayusculas y minusculas
cantidad de la letra a y la letra f
"""

def analizar_cadena(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    cantidad_vocales = 0
    cantidad_consonantes = 0
    cantidad_otros = 0
    cantidad_mayusculas = 0
    cantidad_minusculas = 0
    cantidad_a = 0
    cantidad_f = 0

    for caracter in cadena:
        if caracter in vocales:
            cantidad_vocales += 1
        elif caracter in consonantes:
            cantidad_consonantes += 1
        else:
            cantidad_otros += 1

        if caracter.isupper():
            cantidad_mayusculas += 1
        elif caracter.islower():
            cantidad_minusculas += 1

        if caracter.lower() == 'a':
            cantidad_a += 1
        if caracter.lower() == 'f':
            cantidad_f += 1

    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    existe_palabra_que = "que" in palabras

    print(f"Cantidad de vocales: {cantidad_vocales}")
    print(f"Cantidad de consonantes: {cantidad_consonantes}")
    print(f"Cantidad de otros caracteres: {cantidad_otros}")
    print(f"Cantidad de palabras: {cantidad_palabras}")
    print(f"Existe la palabra 'que': {existe_palabra_que}")
    print(f"Cantidad de mayúsculas: {cantidad_mayusculas}")
    print(f"Cantidad de minúsculas: {cantidad_minusculas}")
    print(f"Cantidad de la letra 'a': {cantidad_a}")
    print(f"Cantidad de la letra 'f': {cantidad_f}")

# Ejemplo de uso
cadena = input("Ingresa una cadena:")
analizar_cadena(cadena)