# Generar una lista de 10 números aleatorios entre 1 y 100 usando la librería random y list comprehension
import random
nums = [random.randint(1,100) for i in range(10)]
print("lista2:", nums)