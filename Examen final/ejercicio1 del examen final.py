"""
Escriba un programa que llene una lista de forma aleatoria con 13 elementos entre 1 y 99

crea otra lista con los numeros pares de la primra lista
crea otra lista con los numeros impares de la primera lista
crea otra lista con los numeros multiplos de 3 de la primera lista
mostrar:
el tamaño de las listas 
el contenido de las listas 
el contenido de las listas ordenado
el promedio de las listas
"""

import random

# Llenar una lista de forma aleatoria con 13 elemento entre 1 y 99
lista = [random.randrange(1, 99) for _ in range(13)]

# crear listas para numeros pares, impares y múltiplos de 3
pares = [ num for num in lista if num % 2 == 0 ]
impares = [num for num in lista if num % 2 != 0]
multiplos_de_3 = [num for num in lista if num % 3 == 0]

# Funcion para calcular el promedio de una lista
def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# Mostrar el tamaño de las listas
print(f"Tamaño de la lista original: {len(lista)}")
print(f"Tamaño de la lista de pares: {len(pares)}")
print(f"Tamaño de la lista de impares: {len(impares)}")
print(f"Tamaño de la lista de múltiplos de 3: {len(multiplos_de_3)}")

# Mostrar el contenido de las listas
print(f"\nContenido de la lista original: {lista}")
print(f"Contenido de la lista de pares: {pares}")
print(f"Contenido de la lista de impares: {impares}")
print(f"Contenido de la lista de múltiplos de 3: {multiplos_de_3}")

# Mostrar el contenido de las listas ordenado
print(f"\nContenido de la lista original ordenado: {sorted(lista)}")
print(f"Contenido de la lista de pares ordenado: {sorted(pares)}")
print(f"Contenido de la lista de impares ordenado: {sorted(impares)}")
print(f"Contenido de la lista de múltiplos de 3 ordenado: {sorted(multiplos_de_3)}")

# Mostrar el promedio de las listas
print(f"\nPromedio de la lista original: {calcular_promedio(lista)}")
print(f"Promedio de la lista de pares: {calcular_promedio(pares)}")
print(f"Promedio de la lista de impares: {calcular_promedio(impares)}")
print(f"Promedio de la lista de múltiplos de 3: {calcular_promedio(multiplos_de_3)}")