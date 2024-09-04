vector = []
for i in range(6):
    vectors = float(input(f"por favor ingresar 7 numero {i + 1}:"))
    vector.append(vectors)


vector_invertido = vector[::-1]

print("Vector original:", vector)
print("Vector invertido:", vector_invertido)