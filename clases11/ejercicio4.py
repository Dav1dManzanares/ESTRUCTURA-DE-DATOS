filas = int(input("ingresa el numero de la filas: "))
columnas = int(input("ingresa el numero de comlumnas: "))

martriz = [["A" for _ in range(columnas)] for _ in range(filas)]

print("\nla matriz resultante es: ")
for fila in martriz:
    print(fila)