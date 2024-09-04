numero = []
for i in range(8):
    numeros = float(input(f"por favor ingresar 7 numero {i + 1}:"))
    numero.append(numeros)


suma_total = (1 for num in numero if num > 0)

print(f"el mayor de los números ingresados es: {suma_total}")