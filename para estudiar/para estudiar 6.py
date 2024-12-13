class persona:
    """
    clase que representa a una persona
    """
def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad
    def saludar (self):
        print(f"Hola {self.nombre} tu edad es {self.edad}")
        
        #crear un objeto de la clase persona
        persona1 = persona("Hector", 18)
        persona1.saludar()