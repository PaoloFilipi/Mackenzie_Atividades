def matriTransp(matriz):
    print('-='*30)
    for l in range (quantColuna):
        for c in range (quantLinha):
            print(f'[{matriz[c][l]:^5}]',end='')
        print()


quantLinha = int(input('Digite a quantidade de linhas da matriz: '))
quantColuna =  int(input('Digite a quantidade de colunas da matriz: '))

matriz = []

for l in range(quantLinha):
    linha = []
    for c in range(quantColuna):
        numero = int(input((f'Digite o valor da posição [{l}{c}]: ')))
        linha.append(numero)
    matriz.append(linha)
print('-='*30)

for l in range(quantLinha):
    for c in range(quantColuna):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

matriTransp(matriz)