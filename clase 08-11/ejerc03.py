"""Ejercicio 03
Calcular el nuevo salario del empleado por el incremento en x%
"""

def calcular_nuevo_salario(salario , incremento):
    """
    Calcular el nuevo salario del empleado por el incremento en x%
    """
    return salario + (salario * (incremento/100))

salario = 530
incre = 3.5
print(f"salario anterior: ${salario:.2f}")
print(f"incremento: {incre}%")
print(f"El nuevo salario es : ${calcular_nuevo_salario(salario, 3.5):.2f}")