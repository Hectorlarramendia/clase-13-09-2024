"""
Calcular el perimetro y area de un triangulo
"""
import math

def perimetro_triangulo(Lado1, Lado2, Lado3):
    return Lado1 + Lado2 + Lado3


def area_triangulo(Lado1, Lado2, Lado3):
    s = (Lado1 + Lado2 + Lado3) / 2
    return math.sqrt(s * (s - Lado1) * (s - Lado2) * (s - Lado3))

def es_triangulo(Lado1,Lado2,Lado3):
    return Lado1+Lado2>Lado3 and Lado1+Lado3>Lado2 and Lado2+Lado3>Lado1

def main():
    Lado1 = float(input("Lado1:"))
    Lado2 = float(input("Lado2:"))
    Lado3 = float(input("Lado3:"))
    if es_triangulo(Lado1, Lado2, Lado3):
     print(f"perimetro de un triangulo es: {perimetro_triangulo(Lado1,Lado2,Lado3):.2f}")
     print(f"Area de un triangulo es: {area_triangulo(Lado1,Lado2,Lado3):.2f}")
    else:
     print("No es un triangulo")
if __name__ == "__main__":
    main()
