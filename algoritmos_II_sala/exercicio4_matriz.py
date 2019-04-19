quantLinham1 = int(input('Digita a quandidade de linha da primeira matriz: '))
quantColunam1 = int(input('Digita a quantidade de coluna da primeira matriz: '))
quantLinham2 = int(input('Digite a quantidadede linha da segunda matriz: '))
quantColunam2 = int(input('Digite a quantidade de coluna da segunda matriz: '))

matriz1 = []
matriz2 = []


for l in range(quantLinham1):
    linha = []
    for c in range(quantColunam1):
        valores = int(input(f'Digite os valores das posições[{l}{c}]: '))
        linha.append(valores)
matriz1.append(linha)


for l  in range(quantLinham2):
    linha2 = []
    for c in range(quantColunam2):
        valores2 = int(input(f'Digite os valores das posições[{l}{c}]: '))
        linha2.append(valores2)
matriz2.append(linha2)
print('-='*30)

for l in range(quantLinham1):
    for c in range(quantColunam1):
        print(matriz1[l][c])
    print()
print()
for l in range(quantLinham2):
    for c in range(quantColunam2):
        print(matriz2[l][c])
    print()

