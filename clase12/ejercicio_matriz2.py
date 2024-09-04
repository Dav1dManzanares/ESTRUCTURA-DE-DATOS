
tamaño = 4

martriz = [[0 for _ in range(tamaño)] for _ in range(tamaño)]

for i in range(tamaño):
    martriz[i][i] = 1


print("\nla matriz resultante es: ")
for fila in martriz:
    print(fila)
