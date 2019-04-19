def somaMatriz(matriz, matriz2):
    matrizResultado = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            matrizResultado[i][j] = matrizA[i][j] + matrizB[i][j]
    print('-='*30)
    for i in range(2):
        for j in range(2):
            print(f'[{matrizResultado[i][j]:^5}]', end='')
        print()

matrizA = [[0,0],[0,0]]
matrizB = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        matrizA[i][j] = int(input('Digite os valores da matrizA: '))

for l in range(2):
    for c in range(2):
        print(f'[{matrizA[l][c]:^5}]',end='')
    print()

for i in range(2):
    for j in range(2):
        matrizB[i][j] = int(input('Digite os valores da matrizB: '))


for l in range(2):
    for c in range(2):
        print(f'[{matrizB[l][c]:^5}]',end='')
    print()
somaMatriz(matrizA,matrizB)