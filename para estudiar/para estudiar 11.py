"""
Crea un programa que cree dos listas aleatorias con 10 elementos cada una.
La primera lista solo tiene numeros pares
La segunda lista solo tiene numeros impares
Y crea una tercera lista con la suma de los elementos de la primera y la segunda
"""
import random
pares = [random.randrange(0,101,2) for _ in range(10)]

impares = [random.randrange(1,100,2) for _ in range(10)]

suma = [pares[i] + impares[i] for i in range(10)]

print("lista de pares:", pares)
print("lista de impares:", impares)
print("lista de suma:", suma)
