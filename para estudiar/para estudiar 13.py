"""
Encontrar la palabra mas larga
"""

def palabra_mas_larga(texto):
    palabras = texto.split()
    longitud_maxima = max(len(palabras) for palabra in palabras)
    palabras_largas = [palabra for palabra in palabras if len(palabra) == longitud_maxima]
    return palabras_largas, longitud_maxima
    
    
oracion = input("Ingrese una oracion:")

palabras_largas, longitud = palabra_mas_larga(oracion)
print("\nResultado:")
print(f"palabra mas largas: {', '.join(palabras_largas)}")
print(f"longitud de las palabras mas largas: {longitud}")