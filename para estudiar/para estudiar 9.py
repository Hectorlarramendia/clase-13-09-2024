# Generar una palabra aleatoria de 3 a 15 letras
import random
import string
letras = string.ascii_lowercase
palabras = ''.join(random.choice(letras) for i in range(random.randint(3, 15)))
print(palabras)

nombres = ["pepe", "Juan", "Maria", "Luis", "Ana"]
# Unir una lista de nombres con guiones
cad = '-'.join(nombres)
print(cad)
# Unir una lista de nombres con comoa 
cad = ','.join(nombres)
print(cad)
# ordenar una lista
cad = nombres.sort()
print(cad)
# invertir una lista
cad = nombres.reverse()
print(cad)

# copiar una lista
lista = nombres.copy()
print(lista)
# concatenar dos listas 
lista1 = ["pepe","juan","Maria", "Luis","Ana"]
lista2 = ["Luis","Maria","pepe", "Juan"]
lista3 = lista1 + lista2
print(lista3)
# contar el numero de veces que aparece un elemento en una lista
print(f"hay {lista3.count("pepe")} pepes en la lista")
# eliminar un elemento de una lista
lista = ["pepe", "juan", "maria", "luis", "ana"]
lista.remove("pepe")
print(lista)