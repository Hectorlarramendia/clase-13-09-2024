"""Existen dos variables, una con un nombre y otra con un apellido. primero se ha de comprobar
el nombre, si es igual a Ramos, se imprime por pantalla el texto nombre y apellido correctos. En caso de que el nombre de Daniel, pero el apellido no sea Ramos, se imprime por pantalla el texto apellido incorrecto, en caso que el nombre no sea Daniel, se imrime por pantalla el texto usuario desconocido
"""
nombre = "Daniel"
apellido = "Ramos"
if nombre=="Daniel" and apellido=="Ramos":
    print("Nombre y apellido correctos")
elif nombre=="Daniel" and apellido!="Ramos":
    print("Apellido incorrecto")
elif nombre!="Daniel" and apellido!="Ramos":
    print("Usuario incorrecto")