import random
# Generar un número aleatorio entre 1 y 10
num_aleatorio = random.randint(1, 10)
print(f"numero aleatorio: {num_aleatorio}")
# Generar un número aleatorio entre 1 y 10 con decimales
num_aleatorio_decimal = random.uniform(1, 10)
print(f"numero aleatorio decimal: {num_aleatorio_decimal}")
print(f"numero aleatorio decimal redondeado: {num_aleatorio_decimal:.2f}")
# Generar una lista de 10 números aleatorios entre 1 y 100 sin repetir usando la librería random 
num = random.sample(range(1, 101),10)
print("lista1:", num)
# Generar una lista de 10 números aleatorios entre 1 y 100 usando la librería random y list comprehension
nums = [random.randint(1,100) for i in range(10)]
print("lista2:", nums)
  # Generar una lista de 10 números aleatorios entre 1 y 100 sin repetir usando la librería random y while
nums_sin_repetir = []
while len(nums_sin_repetir) < 10:
    num = random.randint(1, 100)
    if num not in nums_sin_repetir:
        nums_sin_repetir.append(num)
        print("lista3:", nums_sin_repetir)
    # Generar una lista de 10 números aleatorios entre 1 y 100 sin repetir 
n_s = set()
while len(n_s) < 10:
    n_s.add(random.randint(1,100))
    print("lista4:", list(n_s))
    # ver si un numero no aparece en  una lista
if 9 not in nums_sin_repetir:
    print(" el numero 9 esta en la lista")
else:
    print("el numero 9 no esta en la lista")
# ver si un numero aparece en un set
if 8 in n_s:
    print("el numero 8 esta en la lista")
else:
    print("el numero 8 no esta en la lista")
