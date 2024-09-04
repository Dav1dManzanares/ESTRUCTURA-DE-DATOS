

matriz = []
suma_total = 0
print("\npor favor ingrese los valores de la matriz:")

for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"elemento [{i +1}][{j+1}]: "))
        fila.append(valor)
        suma_total += valor 
        matriz.append(fila)

print("\nla matriz ingresada es: ")
for fila in matriz:
    print(fila)

print(f"\nLa suma de todos los elementos de la matriz es: {suma_total}")