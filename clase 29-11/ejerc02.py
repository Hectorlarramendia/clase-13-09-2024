"""
Calcular el area de un cuadrado
"""
import math

def perimetro_cuadrado(Lado):
    return 4 * Lado

def area_cuadrado(Lado):
    return Lado * Lado

def main():
    Lado = float(input("Lado del cuadrad:"))
    ancho = float(input("Ancho del cuadrado: "))
    perimetro = perimetro_cuadrado(Lado)
    area = area_cuadrado(Lado)
    print(f"El perimetro del cuadrado es {perimetro:.2f}")
    print(f"El area de cuadrado es {area:.2f}")
    
    if __name__ == "__main__":
     main()
    