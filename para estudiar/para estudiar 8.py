# ver si una palabra contiene la letra i
palabra = input ("Ingrese una palabra:")
if "i" in palabra:
   print(f"la letra i esta en la palabra {palabra.count("i")} veces en la palabra {palabra}")
else:
   print(f"la letra i no esta en la palabra {palabra}")
    # ver si un nombre esta en una lista
nombres = ["pepe", "Juan", "Maria", "Luis", "Ana"]
if "pepe" in nombres:
   print("el nombre pepe esta en la lista")
else:
   print("el nombre pepe no esta en la lista")