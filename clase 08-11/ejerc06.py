"""Ejercicio 06
Escribir un programa que vslide si un numero es primo o no
"""
import time


def medir_tiempo(func):
    
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio:.6f} segundos.")
        return resultado
    return envoltura 


@medir_tiempo
def es_primo(n):
    if n <= 1 :
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % 1 == 0:
            return False 
        return True 
    
numero = int(input("Introduce un numero:"))
if es_primo(numero):
    print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo")