"""
Crea un programa que implemente un cifrado césar.
Este metodod consiste en despalazar cada letra de un texto un número fijo de posiciones en el alfabeto.
por ejemplo, con un desplazamiento de 3, la letra 'A' se convierte en'D', 'B' en 'E' y asi sucesivamente.
las letras deben permanecer en su caso (mayusculas/minusculas) y los caracteres que no sean letras deben permanecer igual.
"""
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += nuevo_caracter
            return resultado
        # Solicitar al usuario una frase y el desplazamiento
        texto = input("Introduce un texto para cifrar: ")
        desplazamiento = int(input("Introduce el desplazamiento (número entero): "))
        # Aplicar el ciifrado césar
        texto_cifrado = cifrado_cesar(texto, desplazamiento)
        
        # Mostrar el resultado
        print(f"\nTexto cifrado: {texto_cifrado}")