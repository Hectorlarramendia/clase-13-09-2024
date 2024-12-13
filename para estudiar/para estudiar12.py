"""
Escriba un programa que llene una lista de forma aleatoria con 10 elementos entre 1 y 100.
Crea otra lista con los numeros pares de la primera lista
Crea otra lista con los numeros impares de la primera lista
Mostrar:
El tamaño de la primera lista
El tamaño de la segunda lista
El tamaño de la tercera lista
El contenido de la primera lista
El contenido de la segunda lista
El contenido de la tercera lista
El promedio de la primera lista
El promedio de la segunda lista
El promedio de la tercera lista
"""
import random
aleatorios = [random.randrange(1,101)for _ in range(10)]

pares = [num for num in aleatorios if num % 2 == 0 ]

impares = [num for num in aleatorios if num % 2 != 0 ]


print("el tamaño de la primera lista:", aleatorios)
print("el tamaño de la segunda lista:", pares)
print("el tamaño de la tercera lista:", impares)
print("el contenido de la primera lista:",aleatorios)
print("el contenido de la segunda lista:", pares)
print("el contenido de la tercera lista:", impares)
print("el promedio de la primera lita:", sum(aleatorios)/len(aleatorios))
print("el promedio de la segunda lista:", sum(pares)/len(pares) if len(pares) > 0 else 0)
print("el promedio de la tercera lista:", sum(impares)/len(impares) if len(impares) > 0 else 0)