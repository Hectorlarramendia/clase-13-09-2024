lista = ["Ana","Eduardo", "Luis", "Juan", "Pedro", "Brian", "John" ]
tupla = tuple(lista)
sets = set(lista)
def saludar(x="Mundo"):
    print(f"Hola, {x}!")
    
    saludar()    
for i in lista:
        saludar(1)
for i in tupla:
        saludar(i)
        print("---------------------------")
def sal(x):
    return f"Hola, {x}!"


s = [sal(i) for i in lista]
# print(s)

for i in s:
    print(i)