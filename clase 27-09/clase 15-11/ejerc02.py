try:
    with open("archivo.txt", "r") as file:
        contenido = file.read()
        print("contrnido del archivo:")
        print(contenido)
        
except FileNotFoundError:
    
    print("Error: El archivo no fue encontrado.")
    
except PermissionError:
    
    print("Error: no tiene permisos para leer el archivo.")
    
except Exception as e:
    
    print(f"Ocurrio un error inesperado: {e}")
    
finally:
    # Este bloque se ejecuta siempre, haya o no una  ecepcion
    print("Finalizando la operacion de lectura.")