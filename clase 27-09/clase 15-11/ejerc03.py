
try:
    with open("ejemplo.txt", "w") as archivo:
        archivo.write("Esta es una llave de texto.\h")
        archivo.write("ESta es otra linea de texto.\h")
        print("se escribio correctamente en el archivo.")
except Exception as e:
    print(f"Error al escribir en el archivo: {e}") 
    
    
try:
        with open("ejemplo.txt", "r") as archivo:
            contenido = archivo.read()
            print("contenido del archivo:")
            print(contenido)
            
            
except FileNotFoundError:
        print("Error: el archivo no fue encontrado.")
        
except Exception as e: 
    print(f"Ocurrio un error al leer el archicvo {e}")