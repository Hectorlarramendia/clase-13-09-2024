# Funciones
# Definimos una función para sumar dos números
def suma(a, b):

# Función que toma dos números y devuelve su suma.
  return a + b
 
# Llamamos a la función y mostramos el resultado
resultado = suma(5, 5)
print("resultado:", resultado)
# Operaciones matemáticas básicas
# Suma
a = 5
b = 2
suma = a + b
print("suma de:",a , "+", b, "=", suma)
#resta
a = 5
b = 2
resta = a - b
print("resta de:", a, "-", b, "=", resta)
# multiplicacion 
a = 5
b = 2
multiplicacion = a * b
print("multiplicacion de:", a, "*", b, "=", multiplicacion)
#Division
a = 10
b = 2
division = a / b
print("division de:", a, "/", b, "=", division)

# Modulo
a = 5
b = 3
modulo = a % b
print("modulo de:", a, "%", b, "=", modulo)
# potencia
a = 4
b = 3
c = 1/2
potencia = a ** b
raiz = a ** c
print("potencia de:", a, "**", b, "=", potencia)
print("raiz de :",a, "**", c, "=", raiz)
#funcion de try para corregir errores
try:
  division = 10 / 0
except ZeroDivisionError:
  print("Error: no se puede dividir por cero")