import math

def perimetro_rectangulo(Lado, ancho):
    return 4 * Lado * ancho

def area_rectangulo(Lado, ancho):
    return Lado * ancho
def main():
    Lado = float(input("Lado del rectangulo:"))
    ancho = float(input("Ancho del rectangulo: "))
    perimetro = perimetro_rectangulo(Lado, ancho)
    area = area_rectangulo(Lado,ancho)
    print(f"El perimetro del rectangulo es {perimetro:.2f}")
    print(f"El area de un rectangulo es {area:.2f}")
    
    if __name__ == "__main__":
     main()
    