"""Ejercicio04
Escriba un prgrama que haga la tabla de multiplicar de cualquier entero numero dado por el usuario la tabla debe ser de 0 al 12.
"""

nro = int(input("Escriba un numero: "))

for i in range(0, 13):
    print(f"{nro} x {i} = {nro * i}")