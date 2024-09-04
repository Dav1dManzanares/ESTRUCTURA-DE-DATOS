promedio = []

for i in range(10):
    promedios = float(input(f"ingrese 10 numero {i + 1}:"))
    promedio.append(promedios)

suma_total = sum(promedio)


promedio_total = suma_total / len(promedio)

print(f"el promdio de los números ingresados es: {promedio_total}")


