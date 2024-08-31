#el diccionario que define una relacion una a una edtre claves y valores
Datos_Basicos = {"Nombres": "juan carlos",
                 "apellido": "perez garcia",
                 "DUI": "023151556-6",
                 "fecha de nacimiento": "02/5/2356",
                 "lugar de nacimiento": "soya city",
                 "nacionalidad": "salvadoreño",
                 "estado civil": "complicado",
                 }

print("\n Detalle del dicciomario")
print("=====================================")

print("\nClaves del diccionario: ", Datos_Basicos.keys())
print("\nvalores del diccionario: ", Datos_Basicos.values())
print("\nElementos del diccionario: ", Datos_Basicos.items())

#ejemplos practico de los deccionario
print("\nInscripcion del curso")
print("=================================")

print("\nDatos del participante")
print("===============================")

print("DUI:", Datos_Basicos["DUI"])
print("Nombre completo: ",Datos_Basicos["Nombres"]+" "+Datos_Basicos["apellido"])
