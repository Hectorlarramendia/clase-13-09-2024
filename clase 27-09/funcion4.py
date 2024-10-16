def varios(*var):
    for i in var:
        print(f"{i}")
        
varios(1)
varios(1,"dos")
varios(3,4,5)
varios("uno", "dos", "tres", "cuatro")

def fun_c_v(**cv):
    
    for c,v in cv.items():
        print(f"clave: {c}, valor: {v}")
        fun_c_v(clave1="valor1", clave2="valor2")
        fun_c_v(nombre="Ana", Apellido="Balbuena", edad=23)
        def login(**cred):
         for c,v in cred.items():
                if c == "celular":
                    print(f"login por celular: {v}")
                elif c == "email":
                    print(f"login por email: {v}")
                    login(celular="5959663322",passw="01234567899", fecha="11-10-2024")
                    login(email="micorreoijemail.com",passw="0123456789", fecha="11-10-2024")
                    