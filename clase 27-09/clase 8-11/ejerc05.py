"""Ejercicio 05
Escriba un programa que pruebe que una contraseña sea segura.
La contraseña debe tener al manos 8 caracteres y contener al menos una letra mayuscula
"""

print(len(cadena))
print("a". isupper())
print("A". islower())
print("a". isnumeric()) 

cadena = input("Introduzca una contraseña: ")
if len (cadena) < 8:
    print("La contrseña no es segura")
else:
    mayus = False
    minus = False
    num = False 
    for i in cadena:
        if i.supper():
            mayus = True
        elif i.islower():
            minus = True
        elif i.isnumeric():
            num = True
            if mayus and minus and num:
                print("La contraseña es segura")
            else:
                print("La contraseña no es segura")