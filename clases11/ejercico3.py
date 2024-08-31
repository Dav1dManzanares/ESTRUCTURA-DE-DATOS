filas = int(input("ingrese el numero de filas: "))
columna = int(input("ingrese el numero de columnas: "))

matriz = []
print("\npor favor ingrese los valores de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columna):
        valor = float(input(f"elemento [{i +1}][{j+1}]: "))
        fila.append(valor)
        matriz.append(fila)

print("\nla matriz ingresada es: ")
for fila in matriz:
    print(fila)