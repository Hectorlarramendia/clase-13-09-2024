# Este script introduce las partes básicas de Python con ejemplos prácticos.

# Declaración de variables
# En Python no necesitas especificar el tipo de la variable, se asigna automáticamente.
nombre = "Hector"     #cadena de texto
edad = 18             #Entero
estatura = 1.75       # Flotante
es_estudiante = True  #booleano

# imprimir en consola
print("Hola", nombre, "tu edad es", edad)
# Estructuras de control
#condicionales
if edad > 18: 
    print("eres mayor de edad")
elif edad == 18:
    print("tu edad es 18")
else:
    print("eres menor de edad")