import math

def perimetro_circulo(radio):
    return 2 * math.pi * radio



def area_circulo(radio):
    return math.pi * radio ** 2
def main():
    radio = float(input("radio del circulo"))
    ancho = float(input("ancho del circulo"))
    perimetro = perimetro_circulo(radio)
    area = area_circulo(radio)
    print("El perimetro del circulo es {perimetro:.2f} ")
    print("El area de un circulo es {area:.2f}")
    
    if __name__ == "__main__":
     main()