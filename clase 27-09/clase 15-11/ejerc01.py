try:

    num1 = int(input("Ingrese un numero:"))
    num2 = int(input("Ingrese otro numero:"))
    resultado = num1 / num2
    print(f"El resultado de la division es : {resultado}")

except ZeroDivisionError:

    print("Error: no se puede divididr por cero.")

except ValueError:
    
    print("Error: por favor, ingrese solo numeros.")
    
except Exception as e:
    
    print(f"Ocurrio un error inesperado: {e}")
finally:
    
    print("Fin del mensaje de excepciones.")