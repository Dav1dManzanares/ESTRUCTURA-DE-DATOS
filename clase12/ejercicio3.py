numero = []
for i in range(7):
    numeros = float(input(f"por favor ingresar 7 numero {i + 1}:"))
    numero.append(numeros)


suma_total = max(numero)

print(f"el mayor de los números ingresados es: {suma_total}")