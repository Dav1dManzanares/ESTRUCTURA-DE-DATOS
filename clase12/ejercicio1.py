#sin vectores
#primer_valor = int(input("ingre el primer numero: "));
#segundo_valor = int(input("ingre el segundo numero: "));
#tercer_valor = int(input("ingre el tercer numero: "));
#cuarto_valor = int(input("ingre el cuarto numero: "));
#cinto_valor = int(input("ingre el cinto numero: "));

#suma = primer_valor + segundo_valor + tercer_valor + cuarto_valor + cinto_valor

#print(f"la suma de los 5 numero ingresador es: {suma}");

suma = []


for i in range(5):

    sumas = float(input(f"por favor ingresar 5 numero {i + 1}:"))
    suma.append(sumas)


suma_total = sum(suma)

print(f"La suma de los números ingresados es: {suma_total}")
