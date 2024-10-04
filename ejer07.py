"""
Introduzca los datos de un rectangulo y calcula su perimetro y area
perimetro = lado mas ancho por 2
area = lado por ancho
"""

lado = int(int(input("introduce el valor del lado: ")))
ancho = int(input("introduce el valor del ancho: "))

perimetro = (lado + ancho) * 2
area = lado * ancho

print(f"El perimetro es: {perimetro}")
print(f"El area es: {area}")