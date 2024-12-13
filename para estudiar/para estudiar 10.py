"""
Contador de palabras unicas
"""
def contar_palabras_unicas(oracion):
    palabras = oracion.lower().split()
    palabras_limpias = ''.join(char for char in palabras if char.isalnum() for palabra in palabras)
    palabras_unicas = set(palabras_limpias)
    palabras_ordenadas = sorted(palabras_unicas)
    return palabras_ordenadas, len(palabras_ordenadas)

oracion = input("Ingrese una oracion:")

palabras_ordenadas, total_unicas = contar_palabras_unicas(oracion)
print("\nResultado:")
print(f"total de palabras unicas {total_unicas}")
print("total de palabras ordenadas alfabeticamente")
print(''.join(palabras_ordenadas))