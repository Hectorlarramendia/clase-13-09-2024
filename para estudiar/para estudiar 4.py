# Manejo de listas
# Agregar elementos a una lista
frutas = ["Manzana", "Banana", "Naranja"]
frutas.append("pera")   #para agregar una fruta al final
   
print("la lista de frutas:", frutas)
 
# Cortar listas (slicing)
print("las primeras dos frutas son:", frutas[:2])
# Acceder a elementos
print("la primera fruta es:", frutas[0])
#diccionarios (estructuras clave - valor)
persona = {
    "Nombre" : "Hector",
    "Apellido" : "Lopez",
    "edad" : 18
}
print("informacion personal:", persona)
# Accediendo por clave
print("Nombre:", persona["Nombre"])